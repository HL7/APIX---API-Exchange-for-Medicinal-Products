APIX uses the **Task** resource as the primary envelope and workflow coordinator for all regulatory exchanges, fully replacing traditional eCTD folders and gateway submissions with an API-driven, structured, auditable, and real-time process.

This workflow is inspired by and reuses elements from:
- Uppsala Monitoring Centre's (UMC) [IDMP Request & Publish API Implementation Guide](https://build.fhir.org/ig/Uppsala-Monitoring-Centre/WHO-UMC-IDMP-Service/index.html)
- [Da Vinci Prior Authorization Support (PAS) workflows](https://build.fhir.org/ig/HL7/davinci-pas/specification.html)
- FHIR R5 [Subscriptions](https://hl7.org/fhir/R5/subscriptions.html)

### Task Identifiers
Each regulatory message (initial submission, response to questions, approval letter) is a separate **Task** instance. 

Each Task is connected by three identifiers: 
1. `Task.groupIdentifier` is a common UUID used to group all Tasks within a regulatory activity.
2. `Task.RegulatoryProcedureIdentifier` is the procedure number or application number assigned by the regulator. 
3. `partOf` relates a child Task to its parent Task.

### Task Status
In addition to the identifiers mentioned above, APIX uses **Task Status** ([see here for the Task Status Valueset](http://hl7.org/fhir/ValueSet/task-status)) to drive the the regulatory workflow.

The following table lists each status and its purpose throughout the workflow.

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
The following table demonstrates how the Status on a given Task changes throughout a regulatory activity.

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

The following step-by-step example demonstrates a complete Type IB variation procedure to extend the shelf-life of a product.

#### 1. Initial Submission (Company → Regulator)
**Action:** The applicant initiates the procedure by submitting the dossier.
*   **View Task:** <a href="example-workflow-1-initial-submission.html" target="_blank">HTML View</a> | <a href="../examples/example-workflow-1-initial-submission.json" target="_blank">JSON Resource</a>
*   **Key Data:**
    *   `code` = `initial-submission`
    *   `status` = `requested`
    *   `input` = Cover Letter, Application Form, and Quality Overall Summary (QOS)

#### 2. Regulatory Questions (Regulator → Company)
**Action:** The regulator validates the submission and raises questions (Information Request), causing a clock-stop.
*   **View Task:** <a href="example-workflow-2-questions.html" target="_blank">HTML View</a> | <a href="../examples/example-workflow-2-questions.json" target="_blank">JSON Resource</a>
*   **Key Data:**
    *   `code` = `information-request`
    *   `status` = `requested`
    *   `output` = List of Questions document
    *   `partOf` = Link to Initial Submission Task

#### 3. Company Response (Company → Regulator)
**Action:** The applicant performs the necessary tests and submits a response package, restarting the clock.
*   **View Task:** <a href="example-workflow-3-response.html" target="_blank">HTML View</a> | <a href="../examples/example-workflow-3-response.json" target="_blank">JSON Resource</a>
*   **Key Data:**
    *   `code` = `response-to-questions`
    *   `status` = `requested`
    *   `input` = Response document and raw stability data
    *   `partOf` = Link to Questions Task

#### 4. Final Decision (Regulator → Company)
**Action:** The regulator assesses the response and issues a final positive decision (Approval).
*   **View Task:** <a href="example-workflow-4-decision.html" target="_blank">HTML View</a> | <a href="../examples/example-workflow-4-decision.json" target="_blank">JSON Resource</a>
*   **Key Data:**
    *   `code` = `approval`
    *   `status` = `completed`
    *   `output` = Approval Letter and Final Assessment Report

### Subscriptions for Real-Time Notification
APIX includes support for the R5 Subscription framework.
- Companies create a Subscription (during onboarding) with criteria such as:
  - `Task?groupIdentifier={ProcedureID}`
  - or broader: `Task?requester={CompanyOrgID}`
- Channel: `rest-hook` (preferred) or `websocket`
- Every meaningful status change triggers an immediate notification (id-only or full-resource payload)
