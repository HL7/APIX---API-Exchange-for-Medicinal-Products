The **Task** resource is the universal envelope and workflow engine in APIX.  
Every regulatory interaction — from an initial marketing authorisation application (MAA) to a single validation question, response, or final decision letter — is represented as a separate **Task** instance.

### Key Elements on Every Regulatory Task

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
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Task.identifier</code></td>
<td>1..*</td>
<td>At minimum contains the Task UUID and the Procedure-scoped message identifier (e.g., <code>MSG-2025-0047-001</code>)</td>
<td>Business identifiers; the first identifier with <code>system = "https://api.apix.example.org/identifier/task"</code> is the canonical</td>
</tr>
<tr>
<td><code>Task.status</code></td>
<td>1..1</td>
<td><code>draft | requested | received | accepted | rejected | in-progress | on-hold | completed | cancelled | entered-in-error</code></td>
<td>Follows standard FHIR R5 Task lifecycle; drives APIX state machine</td>
</tr>
<tr>
<td><code>Task.statusReason</code></td>
<td>0..1</td>
<td>Used for rejection/withdrawal reasons (bound to APIX ValueSet)</td>
<td>Mandatory when <code>status = rejected</code> or <code>cancelled</code></td>
</tr>
<tr>
<td><code>Task.intent</code></td>
<td>1..1</td>
<td><code>proposal</code> (fixed for all regulatory Tasks)</td>
<td>Mandatory fixed value per profile</td>
</tr>
<tr>
<td><code>Task.priority</code></td>
<td>0..1</td>
<td><code>routine | urgent | asap | stat</code></td>
<td>Used for accelerated procedures</td>
</tr>
<tr>
<td><code>Task.code</code></td>
<td>1..1</td>
<td>From APIX TaskCode ValueSet (e.g., <code>initial-maa</code>, <code>validation-question</code>, <code>response-to-question</code>, <code>approval-letter</code>)</td>
<td>Defines the regulatory message type; drives downstream processing rules</td>
</tr>
<tr>
<td><code>Task.focus</code></td>
<td>0..1</td>
<td>Reference to the primary payload resource (typically a <code>Bundle</code> of type <code>document</code> or <code>collection</code>)</td>
<td>Used primarily for very large submissions (> ~50 MB) or when payload is stored externally</td>
</tr>
<tr>
<td><code>Task.for</code></td>
<td>1..1</td>
<td>Reference to the <code>MedicinalProductDefinition</code> or <code>RegulatedAuthorization</code> that is the subject of the procedure</td>
<td>Links the Task to the medicinal product under review</td>
</tr>
<tr>
<td><code>Task.input</code></td>
<td>0..*</td>
<td>type = APIX-defined codes (<code>payload</code>, <code>supporting-document</code>, <code>questionnaire-response</code>, etc.)<br>value[x] = DocumentReference | Bundle | QuestionnaireResponse | other</td>
<td>Primary mechanism for attaching content in most cases</td>
</tr>
<tr>
<td><code>Task.output</code></td>
<td>0..*</td>
<td>Used by regulator to return assessments, consolidated comments, approval letters, etc.</td>
<td>Only populated on regulator-originated or completed Tasks</td>
</tr>
<tr>
<td><code>Task.groupIdentifier</code></td>
<td>1..1</td>
<td>Procedure identifier (e.g., <code>PROC-2025-00047</code>)</td>
<td>Identical on every Task belonging to the same regulatory procedure</td>
</tr>
<tr>
<td><code>Task.partOf</code></td>
<td>0..*</td>
<td>Reference to parent Task (e.g., a response Task points to the original question Task)</td>
<td>Builds explicit thread/hierarchy within a procedure</td>
</tr>
<tr>
<td><code><code>Task.restriction</code></td>
<td>0..1</td>
<td><code>restriction.period</code> may contain regulatory clock-stop or deadline information</td>
<td>Used for formal clock-stop management</td>
</tr>
<tr>
<td><code>Task.owner</code></td>
<td>1..1</td>
<td>Reference to Organization (regulatory authority) when action is required from regulator<br>Reference to applicant Organization when action is required from company</td>
<td>Indicates current responsibility; changes with status transitions</td>
</tr>
<tr>
<td><code>Task.requester</code></td>
<td>1..1</td>
<td>Reference to the applicant Organization that initiated the overall procedure</td>
<td>Fixed for the entire procedure lifecycle</td>
</tr>
<tr>
<td><code>Task.authoredOn</code></td>
<td>1..1</td>
<td>Date/time the Task was created by the sender</td>
<td>Used for regulatory cycle-time calculation</td>
</tr>
<tr>
<td><code>Task.lastModified</code></td>
<td>1..1</td>
<td>Automatically updated on every status transition or content change</td>
<td>Essential for audit and performance metrics</td>
</tr>
<tr>
<td><code>Task.relevantHistory</code></td>
<td>0..*</td>
<td>Provenance resources recording submission, validation, status changes, etc.</td>
<td>Provides full audit trail</td>
</tr>
</tbody>
</table>

### Simple Task Examples

**Figure 1:** Initial MAA submission Task (company → regulator)  
**Figure 2:** Question Task (regulator → company)  
**Figure 3:** Response to question (company → regulator) with <code>Task.partOf</code> linking back to Figure 2  
**Figure 4:** Final approval letter Task (regulator → company) with <code>status = completed</code>

(Insert updated graphic diagrams here once available)