## SubscriptionNotification Bundle and SubscriptionStatus

When a Subscription is triggered in APIX, the FHIR server sends a **SubscriptionNotification Bundle** to the subscriber’s configured endpoint. This Bundle contains two essential components:

1. A **SubscriptionStatus** resource that explains *why* the notification was sent — including which Subscription fired, which SubscriptionTopic was matched, and how many times the Subscription has triggered.
2. A set of **event payload resources** (e.g., the updated Task) determined by the SubscriptionTopic and Subscription configuration.

Together, the SubscriptionNotification Bundle and SubscriptionStatus provide a complete picture of both the triggering event and the associated metadata, enabling APIX clients to react immediately and reliably to regulatory workflow changes.

---

### SubscriptionNotification Bundle

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
<td><code>Bundle.type</code></td>
<td>1..1</td>
<td><code>subscription-notification</code></td>
<td>Indicates that this Bundle was generated as the result of a triggered Subscription</td>
</tr>

<tr>
<td><code>Bundle.entry[0]</code></td>
<td>1..1</td>
<td><code>SubscriptionStatus</code> resource</td>
<td>The first entry always contains the <code>SubscriptionStatus</code>, which describes the triggering event and the Subscription involved</td>
</tr>

<tr>
<td><code>Bundle.entry[1..*]</code></td>
<td>0..*</td>
<td>Resources determined by the SubscriptionTopic and Subscription<br>e.g. <code>Task</code>, <code>DocumentReference</code></td>
<td>Contains the event payload; the specific resources included depend on the topic’s notification shape and the Subscription’s configuration</td>
</tr>

<tr>
<td>FHIR Definition</td>
<td>—</td>
<td><a href="https://hl7.org/fhir/R5/subscription-notification-bundle.html">SubscriptionNotificationBundle</a></td>
<td>Formal definition of the notification Bundle structure in FHIR R5</td>
</tr>

</tbody>
</table>

---

### SubscriptionStatus

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
<td><code>SubscriptionStatus.type</code></td>
<td>1..1</td>
<td><code>event-notification</code></td>
<td>Indicates the type of notification; <code>event-notification</code> is used when a Subscription is triggered. Other types exist for different phases of the FHIR R5 Subscription lifecycle.</td>
</tr>

<tr>
<td><code>SubscriptionStatus.eventsSinceSubscriptionStart</code></td>
<td>0..1</td>
<td>Integer count</td>
<td>Number of times this Subscription has been triggered since it was created; useful for monitoring and debugging</td>
</tr>

<tr>
<td><code>SubscriptionStatus.subscription</code></td>
<td>1..1</td>
<td>Reference to <code>Subscription</code></td>
<td>Identifies the Subscription instance that fired and caused this notification</td>
</tr>

<tr>
<td><code>SubscriptionStatus.topic</code></td>
<td>1..1</td>
<td>Canonical URL of the SubscriptionTopic</td>
<td>Indicates which SubscriptionTopic defined the trigger that produced this notification</td>
</tr>

</tbody>
</table>