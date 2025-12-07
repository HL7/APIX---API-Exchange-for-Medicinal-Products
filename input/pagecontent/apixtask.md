In APIX, the Task resource is the universal envelope and workflow engine for all biopharmaceutical regulatory interactions. Whether it is a clinical trial application, marketing authorization application, post-approval variation, response to questions,  decision letter, or review report, it is all represented as an individual **Task** resource.

The following are examples of Tasks with synthetic content: <a href="html-example-apix-shelf-life-original.html">Sample Task (Shelf Life)</a>, <a href="example-workflow-1-initial-submission.html">Initial Submission</a>, <a href="example-workflow-2-questions.html">Questions</a>, <a href="example-workflow-3-response.html">Response</a>, and <a href="example-workflow-4-decision.html">Decision</a>.

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
<td>1..2</td>
<td>• Canonical Task UUID (mandatory)<br>• Procedure-scoped number (optional), e.g. <code>EMEA/H/C/001234/II/0045</code></td>
<td>Technical ID + Official Procedure Number</td>
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
<td>Reference to <code>MedicinalProductDefinition</code> or <code>RegulatedAuthorization</code></td>
<td>Identifies the medicinal product that is the subject of the procedure</td>
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
<td>Primary mechanism to attach submission content</td>
</tr>
<tr>
<td><code>Task.output</code></td>
<td>0..*</td>
<td>type = <code>regulatory-document</code><br>valueReference = Reference(DocumentReference)</td>
<td>Used by the regulator to return assessment reports, decisions, etc.</td>
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
<td><code>Task.requester</code></td>
<td>1..1</td>
<td>Applicant Organization that initiated the procedure</td>
<td>Fixed for the entire procedure lifecycle</td>
</tr>
<tr>
<td><code>Task.requesterPerformer</code></td>
<td>1..1</td>
<td>Organization producing/performing the task</td>
<td>Designated performer (e.g. Applicant or Regulator)</td>
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
</tbody>
</table>
