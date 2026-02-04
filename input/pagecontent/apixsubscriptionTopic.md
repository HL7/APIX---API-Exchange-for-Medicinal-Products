## SubscriptionTopic

A **SubscriptionTopic** defines the event types that a FHIR server is capable of monitoring and notifying subscribers about. While a **Subscription** represents an individual client’s request to receive notifications, the **SubscriptionTopic** describes the *server‑side triggers* that determine when those notifications occur.

Clients use SubscriptionTopics to understand:

- What kinds of events the server supports (e.g., Task creation, Task status change)  
- What filters may be applied (e.g., by Task.identifier or Task.owner)  
- How the server evaluates whether an event matches a trigger  

A Subscription must reference a SubscriptionTopic by its canonical URL. For example, a Subscription that notifies on **Task.status** changes will reference the SubscriptionTopic that defines the status‑change trigger and its associated FHIRPath criteria.

---

### Key Elements of the APIX SubscriptionTopic Resource

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
<td><code>SubscriptionTopic.url</code></td>
<td>1..1</td>
<td>Canonical URL<br>e.g. <code>http://myfhir/fhir/SubscriptionTopic/TaskStatusChangeWithIdentifierFilter</code></td>
<td>Unique identifier used by Subscriptions to reference this topic; must be stable and globally resolvable</td>
</tr>

<tr>
<td><code>SubscriptionTopic.resourceTrigger</code></td>
<td>1..*</td>
<td>• <code>resource</code> = <code>Task</code><br>• <code>supportedInteraction</code> = <code>create</code> or <code>update</code><br>• <code>fhirPathCriteria</code> = e.g. <code>%previous.status != %current.status</code></td>
<td>Defines the events the server monitors and the conditions under which a notification is generated</td>
</tr>

<tr>
<td><code>SubscriptionTopic.canFilterBy</code></td>
<td>0..*</td>
<td>• <code>filterParameter</code> = <code>identifier</code> or <code>owner</code><br>• <code>filterDefinition</code> = FHIR SearchParameter URL</td>
<td>Specifies which filters clients may use when creating Subscriptions for this topic</td>
</tr>

<tr>
<td><code>SubscriptionTopic.name</code>, <code>.title</code>, <code>.description</code></td>
<td>1..1 (name)<br>0..1 (others)</td>
<td>Human‑readable metadata<br>e.g. “Task Status Change With Identifier Filter”</td>
<td>Provides descriptive context for implementers and UI presentation</td>
</tr>

</tbody>
</table>