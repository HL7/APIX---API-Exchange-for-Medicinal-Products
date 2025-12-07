APIX creates transparency in regulatory submissions by leveraging the **HL7 FHIR R5 Subscription Framework**. Instead of manually checking portals or waiting for emails, systems can subscribe to specific events and receive immediate, machine-readable notifications.

This capability underpins the **Unified Status Tracking** use case, providing a "FedEx-style" visibility into the regulatory lifecycle.

### How It Works (Conceptual)

1.  **Subscribe:** The Applicant's system (e.g., RIM) sends a `Subscription` resource to the Regulator's APIX server.
2.  **Trigger:** A change occurs (e.g., an assessor changes a Task status from `received` to `in-progress`).
3.  **Notify:** The Regulator's server matches the change to the Subscription criteria and immediately sends a notification to the Applicant's endpoint.

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

This raw data enables the "Free Performance Dashboards" mentioned in the [IG Home](index.html).

### Conceptual Visualization
The following charts illustrate how raw subscription data can be transformed into executive insights.

#### 1. Unified Pipeline View (Global Portfolio)

<pre class="mermaid">
pie title Submission Status (Global)
    "In Progress (Clock On)" : 45
    "On Hold (Clock Stop)" : 15
    "Approved" : 30
    "Validation" : 10
</pre>

#### 2. Cycle Time Analysis (Reconstructed from Timestamped Tasks)

<pre class="mermaid">
gantt
    title Regulatory Procedure Timeline
    dateFormat  YYYY-MM-DD
    section Procedure A (Fast)
    Submission      :active,    p1, 2025-01-01, 3d
    Validation      :           p2, after p1, 5d
    Assessment      :           p3, after p2, 45d
    Decision        :crit,      p4, after p3, 5d
    section Procedure B (Delayed)
    Submission      :active,    p5, 2025-01-15, 3d
    Validation      :           p6, after p5, 5d
    Assessment      :           p7, after p6, 20d
    Clock Stop (Q&A):crit,      p8, after p7, 30d
    Response Review :           p9, after p8, 25d
    Decision        :           p10, after p9, 5d
</pre>

#### 3. Bottleneck Detection (Time Distribution)

<pre class="mermaid">
pie title Avg. Duration by Phase (Days)
    "Validation" : 12
    "Assessment (Phase I)" : 75
    "Clock Stop (Company Time)" : 45
    "Final Decision" : 10
</pre>
