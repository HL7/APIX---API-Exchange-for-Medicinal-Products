<!-- SUBSCRIPTION TOPIC PAGE -->
<div style="margin-bottom:16px;">
  <h2 style="font-size:1.7em; font-weight:800; color:#111827; margin-bottom:10px;">SubscriptionTopic</h2>
  <p style="font-size:.95em; color:#6b7280; line-height:1.6; max-width:640px;">Defines the event types a FHIR server monitors and notifies subscribers about — the server-side trigger definitions that power real-time regulatory notifications.</p>
</div>

<div style="background:linear-gradient(135deg,#faf5ff,#eff6ff); border:1px solid #e9d5ff; border-radius:12px; padding:20px 24px; margin-bottom:24px;">
  <div style="font-weight:700; color:#003087; font-size:.92em; margin-bottom:6px;">For Business Readers</div>
  <p style="font-size:.85em; color:#374151; line-height:1.6; margin:0;">A SubscriptionTopic is the <strong>event catalogue</strong> published by the regulator's server. It tells implementers: "These are the events you can subscribe to" — such as "Task status changed" or "New Task created for your organization." Clients then create Subscriptions that reference these topics.</p>
</div>

A **SubscriptionTopic** defines the event types that a FHIR server is capable of monitoring and notifying subscribers about. While a **Subscription** represents an individual client’s request to receive notifications, the **SubscriptionTopic** describes the *server‑side triggers* that determine when those notifications occur.

Clients use SubscriptionTopics to understand:

- What kinds of events the server supports (e.g., Task creation, Task status change)  
- What filters may be applied (e.g., by Task.identifier or Task.owner)  
- How the server evaluates whether an event matches a trigger  

A Subscription must reference a SubscriptionTopic by its canonical URL. For example, a Subscription that notifies on **Task.status** changes will reference the SubscriptionTopic that defines the status‑change trigger and its associated FHIRPath criteria.

[Example SubscriptionTopic Task status update](SubscriptionTopic-TaskStatusChangeWithIdentifierFilter.html)

[Example SubscriptionTopic Task creation, filtered by owner](SubscriptionTopic-TaskCreationWithOrganizationAssignedFilter.html)

For more information on how this ties into Subscriptions see: [Real-time Subscriptions](subscriptions.html)

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