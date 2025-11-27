### Overview
APIX uses the **Task** resource as the primary envelope and workflow coordinator for all regulatory exchanges, fully replacing traditional eCTD folders and gateway submissions with an API-driven, structured, auditable, and real-time process.

A single regulatory procedure (e.g., initial MAA, Type II variation, shelf-life extension, PSUR) is represented by a set of related Tasks linked by a common `Task.groupIdentifier` (called **ProcedureID** or **TaskSetID** in APIX) and the partOf.
Each individual message (initial submission, response to questions, approval letter, etc.) is a separate **Task** instance.

This approach is directly inspired by and reuses elements from:
- Uppsala Monitoring Centre's (UMC) [IDMP Request & Publish API Implementation Guide](https://build.fhir.org/ig/Uppsala-Monitoring-Centre/WHO-UMC-IDMP-Service/index.html)
- [Da Vinci Prior Authorization Support (PAS) workflows](https://build.fhir.org/ig/HL7/davinci-pas/specification.html)
- FHIR R5 [Subscriptions](https://hl7.org/fhir/R5/subscriptions.html)

### Task Status
APIX uses the standard FHIR R5 **Task Status** value set:  
[http://hl7.org/fhir/ValueSet/task-status](http://hl7.org/fhir/ValueSet/task-status)

<style>
  .apix-table { border-collapse: collapse; width: 100%; margin: 1.5em 0; }
  .apix-table th, .apix-table td { border: 1px solid #d3d3d3; padding: 10px; text-align: left; vertical-align: top; }
  .apix-table th { background-color: #f0f0f0; font-weight: bold; }
  .apix-table tr:nth-child(even) { background-color: #f9f9f9; }
</style>

<table class="apix-table">
  <thead>
    <tr>
      <th>Code</th>
      <th>Display</th>
      <th>Meaning in APIX Regulatory Context</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>draft</strong></td><td>Draft</td><td>Task created locally by company, not yet submitted</td></tr>
    <tr><td><strong>requested</strong></td><td>Requested</td><td>Company has POSTed the Task to the regulator</td></tr>
    <tr><td><strong>received</strong></td><td>Received</td><td>Regulator server has received the Task (auto-transition)</td></tr>
    <tr><td><strong>accepted</strong></td><td>Accepted</td><td>Gateway/technical validation passed</td></tr>
    <tr><td><strong>rejected</strong></td><td>Rejected</td><td>Fatal validation failure → procedure terminated</td></tr>
    <tr><td><strong>in-progress</strong></td><td>In Progress</td><td>Scientific/regulatory assessment ongoing</td></tr>
    <tr><td><strong>on-hold</strong></td><td>On Hold</td><td>Clock stopped – regulator has raised questions</td></tr>
    <tr><td><strong>completed</strong></td><td>Completed</td><td>Procedure complete and regulatory decision delivered</td></tr>
    <tr><td><strong>cancelled</strong></td><td>Cancelled</td><td>Company withdraws the procedure</td></tr>
    <tr><td><strong>entered-in-error</strong></td><td>Entered in Error</td><td>Task created by mistake</td></tr>
  </tbody>
</table>

> **ready** and **failed** are not used in the core APIX workflow.

#### Typical State Transitions in a Regulatory Procedure

<table class="apix-table">
  <thead>
    <tr>
      <th>Status Change From → To</th>
      <th>Trigger / Example</th>
      <th>Who updates</th>
      <th>Subscription notification sent?</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>draft → requested</td><td>Company finalises and POSTs the Task</td><td>Company</td><td>Yes</td></tr>
    <tr><td>requested → received</td><td>Auto-receipt on regulator server</td><td>Regulator</td><td>Yes</td></tr>
    <tr><td>received → accepted</td><td>Gateway validation successful</td><td>Regulator</td><td>Yes (validation passed)</td></tr>
    <tr><td>received → rejected</td><td>Gateway validation fails</td><td>Regulator</td><td>Yes (rejection)</td></tr>
    <tr><td>accepted → in-progress</td><td>Assessment team begins review</td><td>Regulator</td><td>Yes</td></tr>
    <tr><td>in-progress → on-hold</td><td>Regulator creates child Task with questions</td><td>Regulator</td><td>Yes (clock-stop)</td></tr>
    <tr><td>on-hold → in-progress</td><td>Company responds → regulator restarts clock</td><td>Regulator</td><td>Yes (clock-restart)</td></tr>
    <tr><td>in-progress → completed</td><td>Decision letter issued</td><td>Regulator</td><td>Yes (final decisoin)</td></tr>
    <tr><td>any → rejected</td><td>Scientific rejection</td><td>Regulator</td><td>Yes</td></tr>
    <tr><td>any → cancelled</td><td>Company withdraws</td><td>Company</td><td>Yes</td></tr>
  </tbody>
</table>

### Full Workflow Example – Shelf-Life Update Variation
1. **Company → Regulator: Initial Submission**
   - Authenticates via SMART Backend Services
   - POSTs a Task with:
     - `code` = `initial-submission` (or national submission-type code)
     - `groupIdentifier` = new ProcedureID (e.g., `PROC-2025-12345`)
     - `input` contains revised ePI Bundle, CMC documents, cover letter (all contained)
     - `status` → **requested**
2. **Regulator Gateway Processing**
   - Auto-transition → **received** → validation → **accepted** (or **rejected**)
   - Notification sent via Subscription
3. **Regulator raises Questions**
   - Creates a **child Task** (`partOf` → original)
   - `code` = `information-request`
   - `output` contains Questionnaire / list of questions
   - Original Task → **on-hold** (`businessStatus` = `clock-stop`)
4. **Company Response**
   - Creates new Task (`partOf` → original)
   - `code` = `response-to-questions`
   - `input` contains answers and supporting documents
   - Regulator validates → original Task back to **in-progress** (`businessStatus` = `clock-restart`)
5. **Regulator Decision**
   - Updates Task (or creates final Task)
   - `output` = approval letter (contained DocumentReference) or rejection
   - `status` = **completed** or **rejected**

### Subscriptions for Real-Time Notification
APIX **requires** support for the R5 Subscription framework (or R5 backport).
- Companies create a Subscription (during onboarding) with criteria such as:
  - `Task?groupIdentifier={ProcedureID}`
  - or broader: `Task?requester={CompanyOrgID}`
- Channel: `rest-hook` (preferred) or `websocket`
- Every meaningful status change triggers an immediate notification (id-only or full-resource payload)

### Architecture Components (Example)
The following architecture components are a suggestion. Implementers and developers can use different solutions that acheive the same results.

<table class="apix-table">
  <thead>
    <tr>
      <th>Component</th>
      <th>Minimum Requirement</th>
      <th>Recommendation</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>FHIR Server (Regulator)</td><td>R5 (or R4 + backports), conditional create/update, Subscriptions, SMART Backend Services</td><td>HAPI FHIR, Smile CDR, Azure API for FHIR</td></tr>
    <tr><td>Authentication</td><td>SMART Backend Services (system/* scopes, JWT)</td><td>Mandatory</td></tr>
    <tr><td>Subscriptions</td><td>R5 Backport / R5 native, rest-hook + signed webhook</td><td>Mandatory for production</td></tr>
    <tr><td>Validation Engine</td><td>`$validate` + custom regulatory rules Operation</td><td>Integrated gateway</td></tr>
    <tr><td>Audit</td><td>Provenance resource on every Task update</td><td>Mandatory</td></tr>
    <tr><td>Search / Grouping</td><td>Support for `groupIdentifier`, `partOf`, chaining</td><td>Essential</td></tr>
  </tbody>
</table>
