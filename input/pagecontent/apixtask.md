In APIX, the Task resource is the universal envelope and workflow engine for all biopharmaceutical regulatory interactions. Whether it is a clinical trial application, marketing authorization application, post-approval variation, response to questions,  decision letter, or review report, it is all represented as an individual **Task** resource.

<!-- a href="html-example-apix-shelf-life-original.html">Sample Task (Shelf Life)</a -->

The following are examples of Tasks with synthetic content: <a href="Task-scenario1-01-initial-submission.html">Initial Submission</a>, <a href="Task-scenario1-05-technical-question.html">Questions</a>, <a href="Task-scenario1-06-technical-response.json">Response</a>, and <a href="Task-scenario1-07-final-decision.html">Decision</a>.

The following table provides an overview of the key elements of the APIX Task resource. For a technical description of the Task resource, see the <a href="https://build.fhir.org/ig/HL7/APIX---API-Exchange-for-Medicinal-Products/branches/main/StructureDefinition-apix-task.html">APIX Task profile</a>.

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
<td><code>Task.meta</code></td>
<td>1..1</td>
<td>• <code>versionId</code> (Mandatory)<br>• <code>lastUpdated</code> (Mandatory)<br>• <code>profile</code> (Fixed)</td>
<td>Technical metadata for versioning and conformance</td>
</tr>
<tr>
<td><code>Task.text</code></td>
<td>1..1</td>
<td>Narrative description</td>
<td>Free text description of the task for human readers</td>
</tr>
<tr>
<td><code>Task.identifier</code></td>
<td>1..*</td>
<td>• Canonical Task UUID (mandatory)<br>• Procedure-scoped number (optional), e.g. <code>EMEA/H/C/001234/II/0045</code></td>
<td>Technical ID + Official Procedure Number, useful in precise filtering of status‑change notifications</td>
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
<td><code>proposal</code></td>
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
<td><code>Task.for</code></td>
<td>0..1</td>
<td>Reference to <code>MedicinalProductDefinition</code> or <code>RegulatedAuthorization</code> or <code>Group</code> or <code>List</code></td>
<td>Identifies the medicinal product(s) that is/are the subject of the process. Use Group or List FHIR Resource for multiple products.</td>
</tr>
<tr>
<td><code>Task.requestedPeriod</code></td>
<td>0..1</td>
<td><code>start</code> = Clock Start<br><code>end</code> = Deadline</td>
<td>Regulatory clock management</td>
</tr>
<tr>
<td><code>Task.input</code></td>
<td>0..*</td>
<td>type = <code>regulatory-document</code><br>valueReference = Reference(DocumentReference)</td>
<td>Primary mechanism to attach submission content, or for a Regulator to ask questions or make requests. Can reference DocumentReferences.</td>
</tr>
<tr>
<td><code>Task.output</code></td>
<td>0..*</td>
<td>type = <code>regulatory-document</code><br>valueReference = Reference(DocumentReference)</td>
<td>Used by the regulator to return assessment reports, decisions, etc. Or, used by Applicant to provide responses to Regulator questions or requests. Can reference DocumentReferences.</td>
</tr>
<tr>
<td><code>Task.groupIdentifier</code></td>
<td>1..1</td>
<td>Procedure identifier, e.g. <code>PROC-2025-00047</code></td>
<td>Identical across every Task in the same regulatory procedure</td>
</tr>
<tr>
<td><code>Task.basedOn</code></td>
<td>0..*</td>
<td>Reference to the parent Task (e.g. a response points to the question Task), ordered lineage of Tasks (oldest → newest).</td>
<td>The element is an ordered array with the most distant ancestor Task as the first Task of the array (e.g. an initial request for review). The parent Task will be in the last position of the array.</td> 
</tr>
<tr>
<td><code>Task.partOf</code></td>
<td>0..*</td>
<td>Reference to a set of Tasks </td>
<td>Explicitly can build threads and hierarchies of Task to be performed as one set.</td> 
</tr>
<tr>
<td><code>Task.requester</code></td>
<td>1..1</td>
<td>Organization that initiated the task</td>
<td>Fixed for the entire procedure lifecycle</td>
</tr>
<tr>
<td><code>Task.owner</code></td>
<td>0..1</td>
<td>Organization responsible for fulfilling the Task</td>
<td>Designated performer Organization (e.g. Applicant or Regulator). In FHIR, the Task.owner data element is defined as the entity responsible for managing task execution and status, having the "Performer; Executer" role. In this IG, it is  additionally the Organization which controls the Task.status and which indicates Task completion. e.g. A Regulator is the Task.owner of an initial application Task to review an application. The Regulator determines if the application Task is complete, noting the outcome with Task.output. An Applicant would be the the Organization in Task.owner for a Task assigned to the Applicant by the Regulator. Upon the Applicant's completion of the Task, and the Applicant providing a response in Task.output and changing status to 'complete,' the Regulator determines if an additional Task or child Task is necessary for further clarification.</td> 
</tr>
<tr>
<td><code>Task.performer</code></td>
<td>0..1</td>
<td>Organization or individual producing/performing the task</td>
<td>Organization or individual who performed the task. Can be different from the Task.owner.</td>
</tr>
<tr>
<td><code>Task.businessStatus</code></td>
<td>0..1</td>
<td>Detailed regulatory status (e.g. clock-short, validated)</td>
<td>Enables detailed process analytics and clock-stop tracking</td>
</tr>
<tr>
<td><code>Task.authoredOn</code></td>
<td>1..1</td>
<td>Date/time the sender created the Task</td>
<td>Starting point for regulatory cycle-time metrics</td>
</tr>
<tr>
<td><code>Task.lastUpdated</code></td>
<td>1..1</td>
<td>Automatically updated on every change</td>
<td>Critical for audit and performance reporting</td>
</tr>
</tbody>
</table>

### Task Identifiers
Each regulatory message (initial submission, response to questions, approval letter) is a separate **Task** instance. 

Each Task is connected by four identifiers: 
1. `Task.groupIdentifier` is a common UUID used to group all Tasks within a regulatory activity.
2. `Task.RegulatoryProcedureIdentifier` is the procedure number or application number assigned by the regulator.
3. `basedOn` relates a child Task to its parent Task. 
3. `partOf` indicates a set of Tasks performed together.

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

<div class="markdown-alert markdown-alert-note">
  <p class="markdown-alert-title">Note</p>
  <p>The FHIR Task statuses <strong>ready</strong> and <strong>failed</strong> are not used in the core APIX workflow.</p>
</div>

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
