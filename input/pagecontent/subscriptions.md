APIX creates transparency in regulatory submissions by leveraging the **HL7 FHIR R5 Subscription Framework**. Instead of manually checking portals or waiting for emails, systems can subscribe to specific events and receive immediate, machine-readable notifications.

<div class="markdown-alert markdown-alert-note">
  <p class="markdown-alert-title">Note</p>
  <p>This capability underpins the <strong>Unified Status Tracking</strong> use case, providing a "FedEx-style" visibility into the regulatory lifecycle.</p>
</div>

### Key Points about FHIR Task and its use 
1. **Task.owner:** In FHIR, the Task.owner data element is defined as the entity responsible for managing task execution, having the "Performer; Executer" role. In this IG, it is the Organization which controls the Task.status and which indicates Task completion. e.g. A Regulator is the Task.owner of an initial application Task to review an application. The Regulator determines if the application Task is complete, noting the outcome with Task.output. 

### How It Works (Conceptual)

1.  **SubscriptionTopic:** The Regulator server hosts SubscriptionTopics which allow a client system to 'subscribe' to certain events. In our case, there should be a SubscriptionTopic that allows Subscriptions to status changes of a specific Task. Additionally, the Regulator system will need a SubscriptionTopic that allows the Regulator to subscribe applicant systems to receive notification when Tasks are created with the Applicant system as the Task owner. 

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

### Conceptual Visualization
The following charts illustrate how raw subscription data can be transformed into executive insights.

**1. Unified Pipeline View (Global Portfolio)**

<pre class="mermaid">
pie title Submission Status (Global)
    "In Progress (Clock On)" : 45
    "On Hold (Clock Stop)" : 15
    "Approved" : 30
    "Validation" : 10
</pre>

**2. Cycle Time Analysis (Reconstructed from Timestamped Tasks)**

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

**3. Bottleneck Detection (Time Distribution)**

<pre class="mermaid">
pie title Avg. Duration by Phase (Days)
    "Validation" : 12
    "Assessment (Phase I)" : 75
    "Clock Stop (Company Time)" : 45
    "Final Decision" : 10
</pre>

**4. Regulator View: Annual Statutory Compliance**

Automated generation of performance metrics for annual reports (e.g., Outcome of Initial Evaluations).

<div style="font-family: sans-serif; border: 1px solid #ddd; padding: 20px; max-width: 600px; background: #fff;">
  <h4 style="margin-top:0;">Outcome of Initial Evaluations (2025)</h4>
  
  <div style="margin-bottom: 15px;">
    <div style="font-weight: bold; font-size: 14px; margin-bottom: 5px;">Positive Opinion (114)</div>
    <div style="background-color: #f0f0f0; width: 100%; border-radius: 4px;">
       <div style="background-color: #2da44e; width: 90%; height: 24px; border-radius: 4px; text-align: right; color: white; padding-right: 10px; font-size: 12px; line-height: 24px;">90%</div>
    </div>
  </div>

  <div style="margin-bottom: 15px;">
    <div style="font-weight: bold; font-size: 14px; margin-bottom: 5px;">Withdrawn (8)</div>
    <div style="background-color: #f0f0f0; width: 100%; border-radius: 4px;">
       <div style="background-color: #6e7781; width: 6%; height: 24px; border-radius: 4px;"></div>
    </div>
  </div>

  <div style="margin-bottom: 15px;">
    <div style="font-weight: bold; font-size: 14px; margin-bottom: 5px;">Negative Opinion (5)</div>
    <div style="background-color: #f0f0f0; width: 100%; border-radius: 4px;">
       <div style="background-color: #cf222e; width: 4%; height: 24px; border-radius: 4px;"></div>
    </div>
  </div>
</div>

**5. Procedure Duration Analysis**

Breakdown of average review time by procedure type.

<div style="font-family: sans-serif; border: 1px solid #ddd; padding: 20px; max-width: 600px; background: #fff;">
  <h4 style="margin-top:0; text-align: center;">Avg. Days in Review (2025)</h4>  
  <div style="display: flex; align-items: flex-end; height: 200px; border-bottom: 2px solid #333; gap: 20px; padding-bottom: 10px;">
    <div style="flex: 1; display: flex; flex-direction: column; align-items: center;">
      <div style="width: 100%; background-color: #0969da; height: 180px; border-radius: 4px 4px 0 0; position: relative;">
        <span style="position: absolute; top: -20px; width: 100%; text-align: center; font-size: 12px; font-weight: bold;">210d</span>
      </div>
      <div style="margin-top: 10px; font-size: 11px; text-align: center;">Initial MAA</div>
    </div>
    <div style="flex: 1; display: flex; flex-direction: column; align-items: center;">
      <div style="width: 100%; background-color: #0969da; height: 77px; border-radius: 4px 4px 0 0; position: relative;">
        <span style="position: absolute; top: -20px; width: 100%; text-align: center; font-size: 12px; font-weight: bold;">90d</span>
      </div>
      <div style="margin-top: 10px; font-size: 11px; text-align: center;">Type II Var</div>
    </div>
    <div style="flex: 1; display: flex; flex-direction: column; align-items: center;">
      <div style="width: 100%; background-color: #0969da; height: 26px; border-radius: 4px 4px 0 0; position: relative;">
        <span style="position: absolute; top: -20px; width: 100%; text-align: center; font-size: 12px; font-weight: bold;">30d</span>
      </div>
      <div style="margin-top: 10px; font-size: 11px; text-align: center;">Type IB Var</div>
    </div>
    <div style="flex: 1; display: flex; flex-direction: column; align-items: center;">
      <div style="width: 100%; background-color: #0969da; height: 51px; border-radius: 4px 4px 0 0; position: relative;">
        <span style="position: absolute; top: -20px; width: 100%; text-align: center; font-size: 12px; font-weight: bold;">60d</span>
      </div>
      <div style="margin-top: 10px; font-size: 11px; text-align: center;">Renewal</div>
    </div>
  </div>
  <div style="margin-top: 10px; font-size: 12px; color: #666; text-align: center;">Regulatory Procedure Type</div>
</div>
