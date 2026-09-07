<!-- SUBSCRIPTIONS PAGE -->
<div style="margin-bottom:32px;">
  <h2 style="font-size:1.7em; font-weight:800; color:#111827; margin-bottom:10px;">Real-Time Subscriptions</h2>
  <p style="font-size:.95em; color:#6b7280; line-height:1.6; max-width:640px;">APIX creates transparency in regulatory submissions by leveraging the <a href="https://hl7.org/fhir/subscriptions.html#overview-workflow">HL7 FHIR R5 Subscription Framework</a>. Instead of manually checking portals or waiting for emails, systems subscribe to specific events and receive immediate, machine-readable notifications.</p>
</div>

<div style="background:linear-gradient(135deg,#ecfdf5,#eff6ff); border:1px solid #a7f3d0; border-radius:12px; padding:20px 24px; margin-bottom:32px; display:flex; align-items:center; gap:16px; flex-wrap:wrap;">
  <div style="font-size:1.8em; flex-shrink:0;">📊</div>
  <div style="flex:1; min-width:200px;">
    <div style="font-weight:700; color:#065f46; font-size:.92em; margin-bottom:4px;">Unified Status Tracking</div>
    <p style="font-size:.85em; color:#064e3b; line-height:1.5; margin:0;">This capability underpins the "FedEx-style" visibility into the regulatory lifecycle — enabling portfolio-wide performance dashboards automatically.</p>
  </div>
</div>

<hr style="border:none; border-top:1px solid #e5e7eb; margin:0 0 32px;"/>

<div class="markdown-alert markdown-alert-note">
  <p class="markdown-alert-title">Note</p>
  <p>This capability underpins the <strong>Unified Status Tracking</strong> use case, providing a "FedEx-style" visibility into the regulatory lifecycle.</p>
</div>

### Key Points about FHIR Task and its use 
1. **Task.owner:** In FHIR, the Task.owner data element is defined as the entity responsible for managing task execution, having the "Performer; Executer" role. In this IG, it is the Organization which controls the Task.status and which indicates Task completion. e.g. A Regulator is the Task.owner of an initial application Task to review an application. The Regulator determines if the application Task is complete, noting the outcome with Task.output. 

### How It Works (Conceptual)

1. **SubscriptionTopic:** The Regulator server hosts SubscriptionTopics which allow a client system to 'subscribe' to certain events. In our case, there should be a SubscriptionTopic that allows Subscriptions to status changes of a specific Task. Additionally, the Regulator system will need a SubscriptionTopic that allows the Regulator to subscribe applicant systems to receive notification when Tasks are created with the Applicant system as the Task owner. 

Applicant System
2a.  **Subscribe:** The Applicant's system (e.g., RIM) sends a `Subscription` resource to the Regulator's APIX server that registers for the 
3b.  **Trigger:** A change occurs (e.g., an assessor changes a Task status from `received` to `in-progress`).
4b.  **Notify:** The Regulator's server matches the change to the Subscription criteria and immediately sends a notification to the Applicant's endpoint.

Regulator System
2a.  **Subscribe:** The Regulator system sends a `Subscription` resource to the Regulator's APIX server that registers a subcription for the Task creation SubscriptionTopic, filtered to respond only to specific Tasks where the Applicant is the Task.owner. 
3b.  **Trigger:** A change occurs (e.g., an assessor changes a Task status from `received` to `in-progress`).
4b.  **Notify:** The Regulator's server matches the change to the Subscription criteria and immediately sends a notification to the Applicant's endpoint.


### The Topic-Based Subscription Model

APIX uses the R5 Topic-Based Subscription model (`SubscriptionTopic`) to define standard events.

#### Standard Subscription Topics

<table style="border-collapse: collapse; width: 100%; border: 1px solid #d3d3d3;">
  <thead>
    <tr style="background-color: #f0f0f0;">
      <th style="border: 1px solid #d3d3d3; padding: 8px;">Topic Canonical</th>
      <th style="border: 1px solid #d3d3d3; padding: 8px;">Description</th>
      <th style="border: 1px solid #d3d3d3; padding: 8px;">Trigger Event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #d3d3d3; padding: 8px;"><code>http://hl7.org/fhir/uv/apix/SubscriptionTopic/task-update</code></td>
      <td style="border: 1px solid #d3d3d3; padding: 8px;"><strong>Task Status Change</strong></td>
      <td style="border: 1px solid #d3d3d3; padding: 8px;">Any update to <code>Task.status</code> (e.g., <code>accepted</code>, <code>rejected</code>, <code>on-hold</code>)</td>
    </tr>
    <tr>
      <td style="border: 1px solid #d3d3d3; padding: 8px;"><code>http://hl7.org/fhir/uv/apix/SubscriptionTopic/new-message</code></td>
      <td style="border: 1px solid #d3d3d3; padding: 8px;"><strong>New Inbound Task</strong></td>
      <td style="border: 1px solid #d3d3d3; padding: 8px;">Creation of a new Task assigned to the subscriber (e.g., a new Question or Decision)</td>
    </tr>
  </tbody>
</table>

### Creating a Subscription

To start receiving notifications, an Applicant POSTs a `Subscription` resource.

**Example: Subscribe to all updates for a specific Procedure**

```json
{
  "resourceType": "Subscription",
  "status": "active",
  "topic": "http://hl7.org/fhir/uv/apix/SubscriptionTopic/task-update",
  "filterBy": [
    {
      "filterParameter": "group-identifier",
      "value": "Procedure-2025-00123"
    }
  ],
  "channelType": {
    "system": "http://terminology.hl7.org/CodeSystem/subscription-channel-type",
    "code": "rest-hook"
  },
  "endpoint": "https://rim-system.pharma-corp.com/apix-webhook"
}
```

### Notification Channels

APIX supports two primary channel types for different architectural needs:

1.  **REST Hook (Server-to-Server):**
    *   **Best for:** Production RIM systems, cloud integrations.
    *   **Mechanism:** The regulator sends a POST request to a URL registered by the applicant.
    *   **Payload:** Can be `id-only` (ping) or `full-resource` (contains the updated Task).

2.  **WebSocket (Client-Side):**
    *   **Best for:** UI dashboards, lightweight apps, or firewalled environments where inbound webhooks are difficult.
    *   **Mechanism:** The client maintains an open socket connection to receive stream updates.

### Process Analytics & Cycle Time
Because every regulatory milestone is a timestamped event, the subscription feed doubles as a **real-time analytics stream**.

By storing the notification history, an organization can automatically reconstruct the full timeline of any procedure and calculate performance metrics without manual data entry:
*   **Time-to-Submission:** `Task.authoredOn` (Draft) vs `Task.lastModified` (Requested)
*   **Regulatory Cycle Time:** `Task.authoredOn` (Received) vs `Task.lastModified` (Completed)
*   **Clock-Stop Duration:** Time elapsed while `status = on-hold`
*   **Process Bottlenecks:** Visualizing which step (Validation vs Assessment vs Response) consumes the most time.

<div class="markdown-alert markdown-alert-tip">
  <p class="markdown-alert-title">Tip</p>
  <p>This raw data enables the "Free Performance Dashboards" mentioned in the <a href="index.html">IG Home</a>.</p>
</div>

### From Event Stream to Dashboards

For worked examples of what this analytics stream produces — a full single-procedure lifecycle timeline reconstructed from Task versions, a regulator's live activity board, and auto-generated annual performance reports — see the <a href="usecases.html#scenario-examples">Scenario Examples on the Use Cases page</a>.
