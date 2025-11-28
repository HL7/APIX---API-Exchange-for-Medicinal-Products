# APIX Task – The Universal Regulatory Workflow Envelope

In APIX, every regulatory message or action — from the very first marketing authorisation application (MAA) to a single validation question, a response, or a final approval letter — is represented as an individual **Task** resource.

The Task acts as the universal envelope and workflow engine for all biopharmaceutical regulatory interactions.

### Key Elements – APIX Regulatory Task Profile (November 2025)

<style>
.apix-table { border-collapse: collapse; width: 100%; margin: 1.5em 0; }
.apix-table th, .apix-table td { border: 1px solid #d3d3d3; padding: 10px; text-align: left; vertical-align: top; }
.apix-table th { background-color: #f0f0f0; font-weight: bold; }
.apix-table tr:nth-child(even) { background-color: #f9f9f9; }
</style>

<table class="apix-table">
<thead>
<tr>
<th>Element</th>
<th>Cardinality (APIX)</th>
<th>Value / Example</th>
<th>Purpose / Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Task.identifier</code></td>
<td>1..*</td>
<td>• Canonical Task ID (system = https://api.apix.example.org/identifier/task)<br>• Procedure-scoped message ID, e.g. <code>MSG-2025-0047-012</code></td>
<td>Primary business identifiers; first identifier is the persistent Task UUID</td>
</tr>
<tr>
<td><code>Task.status</code></td>
<td>1..1</td>
<td><code>draft | requested | received | accepted | rejected | in-progress | on-hold | completed | cancelled | entered-in-error</code></td>
<td>Drives the APIX state machine and UI</td>
</tr>
<tr>
<td><code>Task.statusReason</code></td>
<td>0..1</td>
<td>CodeableConcept from APIX RejectionReason ValueSet</td>
<td>Mandatory when <code>status = rejected</code> or <code>cancelled</code></td>
</tr>
<tr>
<td><code>Task.intent</code></td>
<td>1..1</td>
<td><code>order</code></td>
<td>Fixed value for all regulatory Tasks</td>
</tr>
<tr>
<td><code>Task.priority</code></td>
<td>0..1</td>
<td><code>routine | urgent | asap | stat</code></td>
<td>Used for accelerated/conditional procedures</td>
</tr>
<tr>
<td><code>Task.code</code></td>
<td>1..1</td>
<td>From APIX TaskCode ValueSet, e.g.<br>• <code>initial-maa</code><br>• <code>variation-type-ia</code><br>• <code>validation-question</code><br>• <code>response-to-question</code><br>• <code>approval-letter</code></td>
<td>Defines the regulatory message type and triggers specific business rules</td>
</tr>
<tr>
<td><code>Task.focus</code></td>
<td>0..1</td>
<td>Reference to a <code>Bundle</code> (type = document or collection)</td>
<td>Used only for very large payloads (> ~50 MB) or externally stored submissions</td>
</tr>
<tr>
<td><code>Task.for</code></td>
<td>1..1</td>
<td>Reference to <code>MedicinalProductDefinition</code> or <code>RegulatedAuthorization</code></td>
<td>Identifies the medicinal product that is the subject of the procedure</td>
</tr>
<tr>
<td><code>Task.input</code></td>
<td>0..*</td>
<td>type = APIX codes (<code>payload</code>, <code>supporting-document</code>, <code>questionnaire-response</code>, etc.)<br>value[x] = DocumentReference | Bundle | QuestionnaireResponse | etc.</td>
<td>Primary and preferred way to attach submission content</td>
</tr>
<tr>
<td><code>Task.output</code></td>
<td>0..*</td>
<td>Used by the regulator to return assessment reports, consolidated comments, decisions, etc.</td>
<td>Populated only on regulator-initiated or completed Tasks</td>
</tr>
<tr>
<td><code>Task.groupIdentifier</code></td>
<td>1..1</td>
<td>Procedure identifier, e.g. <code>PROC-2025-00047</code></td>
<td>Identical across every Task in the same regulatory procedure</td>
</tr>
<tr>
<td><code>Task.partOf</code></td>
<td>0..*</td>
<td>Reference to the parent Task (e.g. a response points to the question Task)</td>
<td>Explicitly builds threads and hierarchies</td>
</tr>
<tr>
<td><code>Task.restriction</code></td>
<td>0..1</td>
<td><code>restriction.period</code> contains response deadline / clock-stop information</td>
<td>Formal regulatory clock management</td>
</tr>
<tr>
<td><code>Task.owner</code></td>
<td>1..1</td>
<td>• Regulatory authority when action required from agency<br>• Applicant organization when action required from company</td>
<td>Indicates current responsibility; flips with status changes</td>
</tr>
<tr>
<td><code>Task.requester</code></td>
<td>1..1</td>
<td>Applicant Organization that initiated the procedure</td>
<td>Fixed for the entire procedure lifecycle</td>
</tr>
<tr>
<td><code>Task.authoredOn</code></td>
<td>1..1</td>
<td>Date/time the sender created the Task</td>
<td>Starting point for regulatory cycle-time metrics</td>
</tr>
<tr>
<td><code>Task.lastModified</code></td>
<td>1..1</td>
<td>Automatically updated on every change</td>
<td>Critical for audit and performance reporting</td>
</tr>
<tr>
<td><code>Task.relevantHistory</code></td>
<td>0..*</td>
<td>References to <code>Provenance</code> resources recording submission, validation, status changes, etc.</td>
<td>Complete audit trail</td>
</tr>
</tbody>
</table>

### Common Task Examples

Figure 1 – Initial MAA Submission Task (company → regulator)  
Figure 2 – Validation Question Task (regulator → company)  
Figure 3 – Response to Validation Question (company → regulator)  
Figure 4 – Day-80 Assessment Report Task (regulator → company)  
Figure 5 – Final Approval Letter Task (regulator → company, status = completed)

*(Insert updated graphic diagrams here when available)*

This profile is published in the official APIX Implementation Guide:  
https://github.com/HL7/rtq-ig/tree/main/input/resources/task