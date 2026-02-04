## Subscription

In APIX, the **Subscription** resource is the mechanism that delivers real‑time notifications when regulatory events occur. A Subscription becomes active when:

1. The event matches the trigger defined in the **SubscriptionTopic**, and  
2. The resource involved satisfies the **Subscription.filterBy** constraints.

When both conditions are met, the server sends a notification bundle to the subscriber’s configured **Subscription.endpoint**.

APIX uses Subscriptions for two primary regulatory event types:

- **Task Status Change** — filtered by **Task.identifier**  
  Notifies the requester when the regulator updates the status of a Task (e.g., *received → accepted*, *in‑progress → on‑hold*, *completed*).

- **Task Creation** — filtered by **Task.owner**  
  Notifies an Organization when the regulator creates a new Task for them (e.g., questions, decision letters, follow‑up actions).

These two patterns allow APIX participants to receive immediate, event‑driven updates without polling.

---

### Key Elements of the APIX Subscription Resource

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
<td><code>Subscription.filterBy</code></td>
<td>0..*</td>
<td>• <code>filterParameter</code> = <code>identifier</code> or <code>owner</code><br>• <code>value</code> = e.g. <code>Organization/1001</code></td>
<td>Defines the subset of events the subscriber is interested in (e.g., Tasks for a specific organization or Tasks with a specific identifier)</td>
</tr>

<tr>
<td><code>Subscription.topic</code></td>
<td>1..1</td>
<td>Canonical URL of the SubscriptionTopic<br>e.g. <code>http://myfhir/fhir/SubscriptionTopic/TaskStatusChangeWithIdentifierFilter</code></td>
<td>Must exactly match the <code>SubscriptionTopic.url</code> that governs the event type and trigger logic</td>
</tr>

<tr>
<td><code>Subscription.endpoint</code></td>
<td>1..1</td>
<td>REST‑hook endpoint URL<br>e.g. <code>https://hapi.requestcatcher.com/</code></td>
<td>Destination where event notifications are delivered</td>
</tr>

<tr>
<td><code>Subscription.reason</code></td>
<td>1..1</td>
<td>Human‑readable explanation<br>e.g. “Notify Organization when a new Task is assigned”</td>
<td>Describes the business purpose for auditability and transparency</td>
</tr>

<tr>
<td><code>Subscription.managingEntity</code></td>
<td>0..1</td>
<td>Reference(Organization)<br>e.g. <code>Organization/1001</code></td>
<td>Identifies the organization responsible for maintaining the subscription</td>
</tr>

</tbody>
</table>