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

**3. Single-Procedure Lifecycle Timeline (FDA Shelf-Life Update Test Scenario)**

The same reconstruction applied to one procedure at full fidelity. The timeline below is derived entirely from the timestamped Task versions of the FDA shelf-life update test scenario (procedure `NDA-214365-S-021`): a terminally rejected first submission, filing review and user-fee clearance, two Information-Request clock stops (RTQ XML), and the closing approval. Hover over any bar or milestone to see the underlying Task ids and status transitions.

<div style="border:1px solid #e5e7eb; border-radius:12px; padding:8px; background:#fcfcfb; overflow-x:auto; margin-bottom:24px;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1480 780" style="max-width:100%;height:auto;display:block;" font-family="system-ui, -apple-system, 'Segoe UI', sans-serif" role="img" aria-label="Gantt timeline of the FDA shelf-life update procedure NDA-214365-S-021, 03 Aug 2026 to 03 Jun 2027">
<rect width="1480" height="780" fill="#fcfcfb"/>
<text x="28" y="40" font-size="21" font-weight="650" fill="#0b0b0b">FDA Shelf-Life Update (24 → 36 Months) — Procedure Timeline</text>
<text x="28" y="64" font-size="13" fill="#52514e">Reconstructed from timestamped Tasks · groupIdentifier <tspan font-family="ui-monospace, Menlo, monospace">NDA-214365-S-021</tspan> · Day 0 = 03 Aug 2026 · Approved 03 Jun 2027 · 304 days total, 49 days in clock stops</text>
<g><rect x="28" y="81" width="18" height="12" rx="3" fill="#2a78d6"/><text x="52" y="92" font-size="12" fill="#52514e">Procedure active (FDA / exchange)</text><rect x="270" y="81" width="18" height="12" rx="3" fill="#ec835a"/><rect x="276" y="83" width="2" height="8" fill="#ffffff"/><rect x="280" y="83" width="2" height="8" fill="#ffffff"/><text x="294" y="92" font-size="12" fill="#52514e">Clock stop — awaiting applicant response</text><rect x="564" y="81" width="18" height="12" rx="3" fill="#d03b3b"/><text x="588" y="92" font-size="12" fill="#52514e">✕ Terminal validation failure</text><path d="M 793 79 l 7 7 l -7 7 l -7 -7 z" fill="none" stroke="#52514e" stroke-width="1.6"/><text x="808" y="92" font-size="12" fill="#52514e">Milestone</text><path d="M 899 79 l 7 7 l -7 7 l -7 -7 z" fill="#0ca30c"/><text x="914" y="92" font-size="12" fill="#52514e">✓ Approved</text></g>
<line x1="412.6" y1="126" x2="412.6" y2="726" stroke="#e1e0d9" stroke-width="1"/>
<text x="416.6" y="748" font-size="11.5" fill="#898781">Aug 2026</text>
<line x1="510.3" y1="126" x2="510.3" y2="726" stroke="#e1e0d9" stroke-width="1"/>
<text x="514.3" y="748" font-size="11.5" fill="#898781">Sep</text>
<line x1="604.8" y1="126" x2="604.8" y2="726" stroke="#e1e0d9" stroke-width="1"/>
<text x="608.8" y="748" font-size="11.5" fill="#898781">Oct</text>
<line x1="702.5" y1="126" x2="702.5" y2="726" stroke="#e1e0d9" stroke-width="1"/>
<text x="706.5" y="748" font-size="11.5" fill="#898781">Nov</text>
<line x1="797.0" y1="126" x2="797.0" y2="726" stroke="#e1e0d9" stroke-width="1"/>
<text x="801.0" y="748" font-size="11.5" fill="#898781">Dec</text>
<line x1="894.7" y1="126" x2="894.7" y2="726" stroke="#e1e0d9" stroke-width="1"/>
<text x="898.7" y="748" font-size="11.5" fill="#898781">Jan 2027</text>
<line x1="992.3" y1="126" x2="992.3" y2="726" stroke="#e1e0d9" stroke-width="1"/>
<text x="996.3" y="748" font-size="11.5" fill="#898781">Feb</text>
<line x1="1080.6" y1="126" x2="1080.6" y2="726" stroke="#e1e0d9" stroke-width="1"/>
<text x="1084.6" y="748" font-size="11.5" fill="#898781">Mar</text>
<line x1="1178.2" y1="126" x2="1178.2" y2="726" stroke="#e1e0d9" stroke-width="1"/>
<text x="1182.2" y="748" font-size="11.5" fill="#898781">Apr</text>
<line x1="1272.8" y1="126" x2="1272.8" y2="726" stroke="#e1e0d9" stroke-width="1"/>
<text x="1276.8" y="748" font-size="11.5" fill="#898781">May</text>
<line x1="1370.4" y1="126" x2="1370.4" y2="726" stroke="#e1e0d9" stroke-width="1"/>
<text x="1374.4" y="748" font-size="11.5" fill="#898781">Jun</text>
<line x1="400" y1="726" x2="1424" y2="726" stroke="#c3c2b7" stroke-width="1"/>
<text x="28" y="150" font-size="11" font-weight="700" letter-spacing="0.8" fill="#898781">SUBMISSION &amp; TECHNICAL VALIDATION</text>
<text x="386" y="182.0" font-size="12.5" fill="#52514e" text-anchor="end">Attempt 1 (eCTD 0045) — rejected, terminal</text>
<g><title>Attempt 1 (eCTD 0045) — rejected, terminal — 03 Aug 2026. submit-shelf-life-update attempt 1, Task 3e74ce8e… v1 requested -&gt; v2 rejected / validation-failed (terminal). Output: validation failure report (XML)</title><rect x="418.9" y="169.0" width="12.0" height="18" rx="4" fill="#d03b3b"/><text x="424.9" y="181.5" font-size="10" font-weight="700" fill="#ffffff" text-anchor="middle">✕</text><text x="438.9" y="182.0" font-size="11.5" fill="#898781">03 Aug · same day</text></g>
<text x="386" y="222.0" font-size="12.5" fill="#52514e" text-anchor="end">Attempt 2 (eCTD 0046) — received &amp; acknowledged</text>
<g><title>Attempt 2 (eCTD 0046) — received &amp; acknowledged — 03 Aug 2026. New parent Task 7f463290… v1 requested -&gt; v2 received / submission-received; acknowledge-receipt completed same day</title><rect x="418.9" y="209.0" width="12.0" height="18" rx="4" fill="#2a78d6"/><text x="438.9" y="222.0" font-size="11.5" fill="#898781">03 Aug · same day</text></g>
<text x="28" y="256" font-size="11" font-weight="700" letter-spacing="0.8" fill="#898781">FILING &amp; USER FEE</text>
<text x="386" y="288.0" font-size="12.5" fill="#52514e" text-anchor="end">Filing review</text>
<g><title>Filing review — 04 Aug 2026 → 02 Oct 2026 (59d). screen-submission-for-filing fbfd7f40… ; parent -&gt; accepted / filed-accepted-for-review</title><rect x="422.1" y="275.0" width="185.9" height="18" rx="4" fill="#2a78d6"/><text x="632.0" y="288.0" font-size="11.5" fill="#898781">04 Aug – 02 Oct · 59d</text><path d="M 608.0 275.0 l 9 9 l -9 9 l -9 -9 z" fill="#fcfcfb" stroke="#52514e" stroke-width="1.8"/><text x="617.0" y="308.0" font-size="11.5" font-weight="600" fill="#0b0b0b" text-anchor="end">Filed — accepted for review <tspan fill="#898781" font-weight="400">· 02 Oct</tspan></text></g>
<text x="386" y="328.0" font-size="12.5" fill="#52514e" text-anchor="end">User fee — assessed · invoiced · cleared</text>
<g><title>User fee — assessed · invoiced · cleared — 05 Aug 2026 → 13 Aug 2026 (8d). assess-user-fee, issue-user-fee-invoice, confirm-user-fee-payment -&gt; fee-cleared</title><rect x="425.2" y="315.0" width="25.2" height="18" rx="4" fill="#2a78d6"/><text x="458.4" y="328.0" font-size="11.5" fill="#898781">05 Aug – 13 Aug · 8d</text></g>
<text x="28" y="362" font-size="11" font-weight="700" letter-spacing="0.8" fill="#898781">ASSESSMENT</text>
<text x="386" y="394.0" font-size="12.5" fill="#52514e" text-anchor="end">Day 74 communication</text>
<g><title>Day 74 communication — 16 Oct 2026. issue-day-74-communication completed / day-74-communication-issued</title><path d="M 652.1 381.0 l 9 9 l -9 9 l -9 -9 z" fill="none" stroke="#52514e" stroke-width="1.8"/><text x="668.1" y="394.0" font-size="11.5" fill="#898781">16 Oct</text></g>
<text x="386" y="434.0" font-size="12.5" fill="#52514e" text-anchor="end">CMC &amp; labeling assessment</text>
<g><title>CMC &amp; labeling assessment — 19 Oct 2026 → 14 Dec 2026 (56d). conduct-shelf-life-assessment in-progress / assessment-underway (inputs incl. ePI XML labels)</title><rect x="661.5" y="421.0" width="176.4" height="18" rx="4" fill="#2a78d6"/><text x="846.0" y="434.0" font-size="11.5" fill="#898781">19 Oct – 14 Dec · 56d</text></g>
<text x="386" y="474.0" font-size="12.5" fill="#52514e" text-anchor="end">Clock stop — IR 001 (RTQ XML)</text>
<g><title>Clock stop — IR 001 (RTQ XML) — 14 Dec 2026 → 11 Jan 2027 (28d). respond-to-fda-ir-001: IR issued as RTQ XML, response received 11 Jan; assessment on-hold / awaiting-applicant-response</title><rect x="838.0" y="461.0" width="88.2" height="18" rx="4" fill="#ec835a"/><rect x="879.1" y="466.0" width="2.2" height="8" fill="#ffffff"/><rect x="883.1" y="466.0" width="2.2" height="8" fill="#ffffff"/><text x="934.2" y="474.0" font-size="11.5" fill="#898781">14 Dec – 11 Jan · 28d</text></g>
<text x="386" y="514.0" font-size="12.5" fill="#52514e" text-anchor="end">IR 001 response review</text>
<g><title>IR 001 response review — 12 Jan 2027 → 02 Feb 2027 (21d). conduct-shelf-life-assessment in-progress / response-under-review</title><rect x="929.3" y="501.0" width="66.2" height="18" rx="4" fill="#2a78d6"/><text x="1003.5" y="514.0" font-size="11.5" fill="#898781">12 Jan – 02 Feb · 21d</text></g>
<text x="386" y="554.0" font-size="12.5" fill="#52514e" text-anchor="end">Clock stop — IR 002 (RTQ XML)</text>
<g><title>Clock stop — IR 002 (RTQ XML) — 02 Feb 2027 → 23 Feb 2027 (21d). respond-to-fda-ir-002: IR issued as RTQ XML, response received 23 Feb; assessment on-hold / awaiting-applicant-response</title><rect x="995.5" y="541.0" width="66.2" height="18" rx="4" fill="#ec835a"/><rect x="1025.6" y="546.0" width="2.2" height="8" fill="#ffffff"/><rect x="1029.6" y="546.0" width="2.2" height="8" fill="#ffffff"/><text x="1069.7" y="554.0" font-size="11.5" fill="#898781">02 Feb – 23 Feb · 21d</text></g>
<text x="386" y="594.0" font-size="12.5" fill="#52514e" text-anchor="end">Response review &amp; continued assessment</text>
<g><title>Response review &amp; continued assessment — 24 Feb 2027 → 03 May 2027 (68d). conduct-shelf-life-assessment -&gt; completed / assessment-complete</title><rect x="1064.8" y="581.0" width="214.3" height="18" rx="4" fill="#2a78d6"/><text x="1303.1" y="594.0" font-size="11.5" fill="#898781">24 Feb – 03 May · 68d</text><path d="M 1279.1 581.0 l 9 9 l -9 9 l -9 -9 z" fill="#fcfcfb" stroke="#52514e" stroke-width="1.8"/><text x="1288.1" y="614.0" font-size="11.5" font-weight="600" fill="#0b0b0b" text-anchor="end">Assessment complete <tspan fill="#898781" font-weight="400">· 03 May</tspan></text></g>
<text x="28" y="628" font-size="11" font-weight="700" letter-spacing="0.8" fill="#898781">DECISION</text>
<text x="386" y="660.0" font-size="12.5" fill="#52514e" text-anchor="end">Decision preparation</text>
<g><title>Decision preparation — 04 May 2027 → 03 Jun 2027 (30d). prepare-regulatory-action in-progress / decision-preparation-underway</title><rect x="1282.2" y="647.0" width="94.5" height="18" rx="4" fill="#2a78d6"/><text x="1272.2" y="660.0" font-size="11.5" fill="#898781" text-anchor="end">04 May – 03 Jun · 30d</text></g>
<text x="386" y="700.0" font-size="12.5" fill="#52514e" text-anchor="end">Approval — parent Task closed</text>
<g><title>Approval — parent Task closed — 03 Jun 2027. Approval letter + approved clean label (ePI XML); parent 7f463290… v9 completed / approved</title><path d="M 1376.7 687.0 l 9 9 l -9 9 l -9 -9 z" fill="#0ca30c"/><text x="1376.7" y="699.5" font-size="9.5" font-weight="700" fill="#ffffff" text-anchor="middle">✓</text><text x="1360.7" y="700.0" font-size="12" font-weight="600" fill="#0b0b0b" text-anchor="end">Approved <tspan fill="#898781" font-weight="400">· 03 Jun</tspan></text></g>
</svg>
</div>

**4. Bottleneck Detection (Time Distribution)**

<pre class="mermaid">
pie title Avg. Duration by Phase (Days)
    "Validation" : 12
    "Assessment (Phase I)" : 75
    "Clock Stop (Company Time)" : 45
    "Final Decision" : 10
</pre>

**5. Regulator View: Annual Statutory Compliance**

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

**6. Procedure Duration Analysis**

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
