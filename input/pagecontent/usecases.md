<!-- USE CASES PAGE -->
<div style="margin-bottom:28px;">
  <h2 style="font-size:1.7em; font-weight:800; color:#111827; margin-bottom:10px;">Use Cases</h2>
  <p style="font-size:.95em; color:#6b7280; line-height:1.6; max-width:680px;">Once a regulator or company implements RWI-pharma, the same connection pattern supports every regulatory interaction for human biopharmaceutical products. The use cases below show what that makes possible.</p>
</div>

<div style="display:grid; grid-template-columns:repeat(3,1fr); gap:14px; margin-bottom:36px;">
  <a href="#universal-submissions" style="text-decoration:none; background:#fff; border:1px solid #e5e7eb; border-top:3px solid #2563eb; border-radius:8px; padding:18px; display:block;">
    <div style="font-size:.7em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#2563eb; margin-bottom:6px;">Use case 1</div>
    <div style="font-weight:700; color:#111827; margin-bottom:6px;">Universal Submissions</div>
    <p style="font-size:.82em; color:#6b7280; line-height:1.5; margin:0;">One pattern for post-approval changes, ICSRs, label negotiation, and health authority questions.</p>
  </a>
  <a href="#status-tracking" style="text-decoration:none; background:#fff; border:1px solid #e5e7eb; border-top:3px solid #059669; border-radius:8px; padding:18px; display:block;">
    <div style="font-size:.7em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#059669; margin-bottom:6px;">Use case 2</div>
    <div style="font-weight:700; color:#111827; margin-bottom:6px;">Real-Time Status Tracking &amp; Notifications</div>
    <p style="font-size:.82em; color:#6b7280; line-height:1.5; margin:0;">Follow every interaction step by step, like tracking a FedEx or Amazon package.</p>
  </a>
  <a href="#automation" style="text-decoration:none; background:#fff; border:1px solid #e5e7eb; border-top:3px solid #7c3aed; border-radius:8px; padding:18px; display:block;">
    <div style="font-size:.7em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#7c3aed; margin-bottom:6px;">Use case 3</div>
    <div style="font-weight:700; color:#111827; margin-bottom:6px;">Automation</div>
    <p style="font-size:.82em; color:#6b7280; line-height:1.5; margin:0;">Route questions and responses to the right people the moment they arrive.</p>
  </a>
</div>

<hr style="border:none; border-top:1px solid #e5e7eb; margin:0 0 32px;"/>

<!-- USE CASE 1: UNIVERSAL SUBMISSIONS -->
<div id="universal-submissions" style="display:flex; align-items:center; gap:12px; margin-bottom:10px;">
  <span style="display:inline-flex; align-items:center; justify-content:center; width:36px; height:36px; border-radius:50%; background:#2563eb; color:#fff; font-weight:800; font-size:.9em; flex-shrink:0;">1</span>
  <h2 style="font-size:1.4em; font-weight:800; color:#111827; margin:0;">Universal Submissions</h2>
</div>
<p style="font-size:.92em; color:#4b5563; line-height:1.65; max-width:760px; margin:0 0 20px;">Every regulatory interaction uses the same building blocks: files are uploaded as <a href="architecture.html#binary-upload-guide-post-then-link">Binary</a>, described with <a href="apixdocumentReference.html">DocumentReference</a>, and orchestrated by a <a href="apixtask.html">Task</a>. Only the Task type and its documents change from one interaction to the next — not the channel, the portal, or the integration.</p>
<div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-bottom:40px;">
  <div style="background:#fff; border:1px solid #e5e7eb; border-top:3px solid #2563eb; border-radius:8px; padding:18px 20px; display:flex; flex-direction:column;">
    <div style="font-size:.7em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#2563eb; margin-bottom:4px;">Post-approval change</div>
    <div style="font-weight:700; color:#111827; margin-bottom:10px;">Shelf-Life Update</div>
    <div style="background:#fef2f2; border-radius:6px; padding:8px 12px; margin-bottom:10px; font-size:.8em; color:#7f1d1d; line-height:1.5;"><span style="font-weight:700;">Today:</span> The variation dossier is compiled and uploaded to a procedure-specific portal or gateway; status is chased by email.</div>
    <div style="font-size:.75em; font-weight:700; color:#065f46; text-transform:uppercase; letter-spacing:.06em; margin-bottom:4px;">With RWI-pharma</div>
    <ol style="font-size:.82em; color:#374151; line-height:1.6; padding-left:18px; margin:0 0 10px;"><li style="margin-bottom:4px;">Applicant uploads the stability data and updated labelling as Binary + DocumentReference.</li><li style="margin-bottom:4px;">Applicant posts a Task (e.g., <code>supplement</code>) that references the documents in <code>Task.input</code>.</li><li style="margin-bottom:4px;">Regulator validates and reviews, raising questions if needed.</li><li style="margin-bottom:4px;">Regulator completes the Task and attaches the decision letter to <code>Task.output</code>.</li></ol>
    <div style="font-size:.8em; margin-top:auto;"><a href="workflow.html#walkthrough" style="color:#2563eb; font-weight:600; text-decoration:none;">Full walkthrough →</a> · <a href="Task-scenario1-01-initial-submission.html" style="color:#2563eb; font-weight:600; text-decoration:none;">Example Task</a></div>
  </div>
  <div style="background:#fff; border:1px solid #e5e7eb; border-top:3px solid #dc2626; border-radius:8px; padding:18px 20px; display:flex; flex-direction:column;">
    <div style="font-size:.7em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#dc2626; margin-bottom:4px;">Safety reporting</div>
    <div style="font-weight:700; color:#111827; margin-bottom:10px;">ICSR Submission</div>
    <div style="background:#fef2f2; border-radius:6px; padding:8px 12px; margin-bottom:10px; font-size:.8em; color:#7f1d1d; line-height:1.5;"><span style="font-weight:700;">Today:</span> Individual case safety reports travel through dedicated safety gateways, separate from every other regulatory channel.</div>
    <div style="font-size:.75em; font-weight:700; color:#065f46; text-transform:uppercase; letter-spacing:.06em; margin-bottom:4px;">With RWI-pharma</div>
    <ol style="font-size:.82em; color:#374151; line-height:1.6; padding-left:18px; margin:0 0 10px;"><li style="margin-bottom:4px;">Applicant uploads the ICSR (e.g., ICH E2B(R3) XML) as Binary + DocumentReference.</li><li style="margin-bottom:4px;">Applicant posts a Task for the case report that references it.</li><li style="margin-bottom:4px;">Regulator acknowledges receipt by updating the Task and attaching the acknowledgment to <code>Task.output</code>.</li><li style="margin-bottom:4px;">Follow-up reports for the same case reference the original case Task.</li></ol>
  </div>
  <div style="background:#fff; border:1px solid #e5e7eb; border-top:3px solid #ea580c; border-radius:8px; padding:18px 20px; display:flex; flex-direction:column;">
    <div style="font-size:.7em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#ea580c; margin-bottom:4px;">Product information</div>
    <div style="font-weight:700; color:#111827; margin-bottom:10px;">Label Negotiation</div>
    <div style="background:#fef2f2; border-radius:6px; padding:8px 12px; margin-bottom:10px; font-size:.8em; color:#7f1d1d; line-height:1.5;"><span style="font-weight:700;">Today:</span> Draft labels go back and forth as email attachments, and version control depends on file names.</div>
    <div style="font-size:.75em; font-weight:700; color:#065f46; text-transform:uppercase; letter-spacing:.06em; margin-bottom:4px;">With RWI-pharma</div>
    <ol style="font-size:.82em; color:#374151; line-height:1.6; padding-left:18px; margin:0 0 10px;"><li style="margin-bottom:4px;">Applicant posts the proposed labelling (e.g., ePI or annotated PDF) as a Task input.</li><li style="margin-bottom:4px;">Regulator returns comments or a revised draft in <code>Task.output</code>.</li><li style="margin-bottom:4px;">Each round creates a new Task version, so every proposal and counter-proposal is timestamped.</li><li style="margin-bottom:4px;">The agreed label is attached to the final decision.</li></ol>
  </div>
  <div style="background:#fff; border:1px solid #e5e7eb; border-top:3px solid #0d9488; border-radius:8px; padding:18px 20px; display:flex; flex-direction:column;">
    <div style="font-size:.7em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#0d9488; margin-bottom:4px;">Requests &amp; responses</div>
    <div style="font-weight:700; color:#111827; margin-bottom:10px;">Health Authority Question &amp; Response</div>
    <div style="background:#fef2f2; border-radius:6px; padding:8px 12px; margin-bottom:10px; font-size:.8em; color:#7f1d1d; line-height:1.5;"><span style="font-weight:700;">Today:</span> Information requests arrive by email or letter, and clock stops and deadlines are tracked by hand.</div>
    <div style="font-size:.75em; font-weight:700; color:#065f46; text-transform:uppercase; letter-spacing:.06em; margin-bottom:4px;">With RWI-pharma</div>
    <ol style="font-size:.82em; color:#374151; line-height:1.6; padding-left:18px; margin:0 0 10px;"><li style="margin-bottom:4px;">Regulator posts a question Task (e.g., <code>information-request</code>) with the questions as input.</li><li style="margin-bottom:4px;">Applicant is notified instantly and posts the response in <code>Task.output</code>.</li><li style="margin-bottom:4px;">Regulator reviews the response and completes the question Task; the clock restarts.</li></ol>
    <div style="font-size:.8em; margin-top:auto;"><a href="Task-scenario1-05-technical-question.html" style="color:#0d9488; font-weight:600; text-decoration:none;">Example question</a> · <a href="Task-scenario1-06-technical-response.html" style="color:#0d9488; font-weight:600; text-decoration:none;">Example response</a></div>
  </div>
</div>

<hr style="border:none; border-top:1px solid #e5e7eb; margin:0 0 32px;"/>

<!-- USE CASE 2: REAL-TIME STATUS TRACKING & NOTIFICATIONS -->
<div id="status-tracking" style="display:flex; align-items:center; gap:12px; margin-bottom:10px;">
  <span style="display:inline-flex; align-items:center; justify-content:center; width:36px; height:36px; border-radius:50%; background:#059669; color:#fff; font-weight:800; font-size:.9em; flex-shrink:0;">2</span>
  <h2 style="font-size:1.4em; font-weight:800; color:#111827; margin:0;">Real-Time Status Tracking &amp; Notifications</h2>
</div>
<p style="font-size:.92em; color:#4b5563; line-height:1.65; max-width:760px; margin:0 0 20px;">A consumer can follow a FedEx or Amazon package from “ordered” to “delivered” and get a notification at every step. RWI-pharma gives every party the same visibility into a regulatory interaction: each milestone is a Task status change, and each change is pushed to subscribers the moment it happens.</p>
<div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:10px; padding:18px 20px; margin-bottom:16px;">
  <div style="font-size:.72em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#6b7280; margin:0 0 6px;">📦 Package delivery</div>
  <div style="display:flex; gap:6px; flex-wrap:wrap; margin-bottom:14px;"><div style="flex:1; min-width:90px; text-align:center; background:#fffbeb; border:1px solid #e5e7eb; border-radius:6px; padding:8px 6px; font-size:.78em; font-weight:600; color:#92400e;">Order placed</div><div style="color:#9ca3af; align-self:center; font-size:.9em;">→</div><div style="flex:1; min-width:90px; text-align:center; background:#fffbeb; border:1px solid #e5e7eb; border-radius:6px; padding:8px 6px; font-size:.78em; font-weight:600; color:#92400e;">Shipped</div><div style="color:#9ca3af; align-self:center; font-size:.9em;">→</div><div style="flex:1; min-width:90px; text-align:center; background:#fffbeb; border:1px solid #e5e7eb; border-radius:6px; padding:8px 6px; font-size:.78em; font-weight:600; color:#92400e;">In transit</div><div style="color:#9ca3af; align-self:center; font-size:.9em;">→</div><div style="flex:1; min-width:90px; text-align:center; background:#fffbeb; border:1px solid #e5e7eb; border-radius:6px; padding:8px 6px; font-size:.78em; font-weight:600; color:#92400e;">Out for delivery</div><div style="color:#9ca3af; align-self:center; font-size:.9em;">→</div><div style="flex:1; min-width:90px; text-align:center; background:#fffbeb; border:1px solid #e5e7eb; border-radius:6px; padding:8px 6px; font-size:.78em; font-weight:600; color:#92400e;">Delivered</div></div>
  <div style="font-size:.72em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#6b7280; margin:0 0 6px;">📋 Regulatory interaction</div>
  <div style="display:flex; gap:6px; flex-wrap:wrap; margin-bottom:14px;"><div style="flex:1; min-width:90px; text-align:center; background:#ecfdf5; border:1px solid #e5e7eb; border-radius:6px; padding:8px 6px; font-size:.78em; font-weight:600; color:#047857;">Submitted<br/><code style="font-size:.9em;">requested</code></div><div style="color:#9ca3af; align-self:center; font-size:.9em;">→</div><div style="flex:1; min-width:90px; text-align:center; background:#ecfdf5; border:1px solid #e5e7eb; border-radius:6px; padding:8px 6px; font-size:.78em; font-weight:600; color:#047857;">Received<br/><code style="font-size:.9em;">received</code></div><div style="color:#9ca3af; align-self:center; font-size:.9em;">→</div><div style="flex:1; min-width:90px; text-align:center; background:#ecfdf5; border:1px solid #e5e7eb; border-radius:6px; padding:8px 6px; font-size:.78em; font-weight:600; color:#047857;">Validated<br/><code style="font-size:.9em;">accepted</code></div><div style="color:#9ca3af; align-self:center; font-size:.9em;">→</div><div style="flex:1; min-width:90px; text-align:center; background:#ecfdf5; border:1px solid #e5e7eb; border-radius:6px; padding:8px 6px; font-size:.78em; font-weight:600; color:#047857;">Under review<br/><code style="font-size:.9em;">in-progress</code></div><div style="color:#9ca3af; align-self:center; font-size:.9em;">→</div><div style="flex:1; min-width:90px; text-align:center; background:#ecfdf5; border:1px solid #e5e7eb; border-radius:6px; padding:8px 6px; font-size:.78em; font-weight:600; color:#047857;">Decision<br/><code style="font-size:.9em;">completed</code></div></div>
</div>

<div style="display:grid; grid-template-columns:repeat(3,1fr); gap:12px; margin-bottom:12px;">
  <div style="background:#fff; border:1px solid #e5e7eb; border-radius:8px; padding:16px;"><div style="font-weight:700; color:#003087; font-size:.88em; margin-bottom:4px;">🏷️ Tracking number</div><p style="font-size:.82em; color:#4b5563; line-height:1.55; margin:0;">The <a href="apixtask.html">Task</a> and its <code>groupIdentifier</code> identify the interaction and every related Task in the procedure.</p></div>
  <div style="background:#fff; border:1px solid #e5e7eb; border-radius:8px; padding:16px;"><div style="font-weight:700; color:#003087; font-size:.88em; margin-bottom:4px;">🔔 Push notifications</div><p style="font-size:.82em; color:#4b5563; line-height:1.55; margin:0;">A <a href="subscriptions.html">Subscription</a> delivers each status change to the subscriber’s endpoint instantly — no portal log-ins, no polling.</p></div>
  <div style="background:#fff; border:1px solid #e5e7eb; border-radius:8px; padding:16px;"><div style="font-weight:700; color:#003087; font-size:.88em; margin-bottom:4px;">🕓 Delivery history</div><p style="font-size:.82em; color:#4b5563; line-height:1.55; margin:0;">Every Task version is timestamped, so the full history can be replayed as a timeline or rolled up into dashboards.</p></div>
</div>
<div style="font-size:.85em; margin-bottom:28px;"><a href="subscriptions.html" style="color:#059669; font-weight:600; text-decoration:none;">How notifications work →</a></div>

<h3 id="scenario-examples" style="font-size:1.1em; font-weight:700; color:#111827; margin-bottom:8px;">Examples</h3>
<p style="font-size:.88em; color:#6b7280; line-height:1.6; max-width:720px; margin-bottom:20px;">Because every milestone is a timestamped, machine-readable event, the raw exchange data can be turned into decision-ready views with no manual data entry. Both examples below are built from the same underlying <code>Task</code> history.</p>

<!-- Scenario Example 1 -->
<div style="background:#fff; border:1px solid #e5e7eb; border-left:3px solid #8b5cf6; border-radius:8px; padding:20px; margin-bottom:24px;">
  <div style="font-size:.72em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#8b5cf6; margin-bottom:6px;">Scenario Example 1 &middot; Real-Time Status Tracking &amp; Notifications</div>
  <div style="font-weight:700; color:#111827; margin-bottom:8px;">Single-Procedure Lifecycle Timeline (Shelf-Life Update Test Scenario)</div>
  <p style="font-size:.82em; color:#6b7280; line-height:1.6; margin-bottom:14px;">This is the "FedEx tracking view" of one procedure at full fidelity. The timeline below is derived entirely from the timestamped <code>Task</code> versions of the shelf-life update test scenario (procedure <code>NDA-214365-S-021</code>): a terminally rejected first submission, filing review and user-fee clearance, two Information-Request clock stops (RTQ XML), and the closing approval. Hover over any bar or milestone to see the underlying Task ids and status transitions.</p>

<div style="border:1px solid #e5e7eb; border-radius:12px; padding:8px; background:#fcfcfb; overflow-x:auto; margin-bottom:24px;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1480 780" style="max-width:100%;height:auto;display:block;" font-family="system-ui, -apple-system, 'Segoe UI', sans-serif" role="img" aria-label="Gantt timeline of the shelf-life update procedure NDA-214365-S-021, 03 Aug 2026 to 03 Jun 2027">
<rect width="1480" height="780" fill="#fcfcfb"/>
<text x="28" y="40" font-size="21" font-weight="650" fill="#0b0b0b">Shelf-Life Update (24 → 36 Months) — Procedure Timeline</text>
<text x="28" y="64" font-size="13" fill="#52514e">Reconstructed from timestamped Tasks · groupIdentifier <tspan font-family="ui-monospace, Menlo, monospace">NDA-214365-S-021</tspan> · Day 0 = 03 Aug 2026 · Approved 03 Jun 2027 · 304 days total, 49 days in clock stops</text>
<g><rect x="28" y="81" width="18" height="12" rx="3" fill="#2a78d6"/><text x="52" y="92" font-size="12" fill="#52514e">Procedure active (regulator / exchange)</text><rect x="270" y="81" width="18" height="12" rx="3" fill="#ec835a"/><rect x="276" y="83" width="2" height="8" fill="#ffffff"/><rect x="280" y="83" width="2" height="8" fill="#ffffff"/><text x="294" y="92" font-size="12" fill="#52514e">Clock stop — awaiting applicant response</text><rect x="564" y="81" width="18" height="12" rx="3" fill="#d03b3b"/><text x="588" y="92" font-size="12" fill="#52514e">✕ Terminal validation failure</text><path d="M 793 79 l 7 7 l -7 7 l -7 -7 z" fill="none" stroke="#52514e" stroke-width="1.6"/><text x="808" y="92" font-size="12" fill="#52514e">Milestone</text><path d="M 899 79 l 7 7 l -7 7 l -7 -7 z" fill="#0ca30c"/><text x="914" y="92" font-size="12" fill="#52514e">✓ Approved</text></g>
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

  <p style="font-size:.82em; color:#6b7280; line-height:1.6; margin-bottom:10px;">The same feed rolls up across the whole portfolio, giving an applicant a live pipeline view of every procedure at every agency:</p>

<div style="font-family: sans-serif; border: 1px solid #ddd; padding: 20px; background: #fff;">
  <h4 style="margin-top:0; text-align:center;">Active Portfolio &mdash; All Procedures, All Regulators</h4>
  <div style="display:flex; gap:10px; flex-wrap:wrap; margin-bottom:14px;">
    <div style="flex:1; min-width:110px; background:#f9fafb; border:1px solid #e5e7eb; border-radius:8px; padding:10px 14px; text-align:center;"><div style="font-size:1.5em; font-weight:800; color:#111827;">47</div><div style="font-size:.72em; color:#6b7280; line-height:1.3;">Active procedures</div></div>
    <div style="flex:1; min-width:110px; background:#f9fafb; border:1px solid #e5e7eb; border-radius:8px; padding:10px 14px; text-align:center;"><div style="font-size:1.5em; font-weight:800; color:#111827;">8</div><div style="font-size:.72em; color:#6b7280; line-height:1.3;">In clock stop</div></div>
    <div style="flex:1; min-width:110px; background:#f9fafb; border:1px solid #e5e7eb; border-radius:8px; padding:10px 14px; text-align:center;"><div style="font-size:1.5em; font-weight:800; color:#111827;">5</div><div style="font-size:.72em; color:#6b7280; line-height:1.3;">Decisions expected &le; 30 days</div></div>
    <div style="flex:1; min-width:110px; background:#f9fafb; border:1px solid #e5e7eb; border-radius:8px; padding:10px 14px; text-align:center;"><div style="font-size:1.5em; font-weight:800; color:#111827;">23</div><div style="font-size:.72em; color:#6b7280; line-height:1.3;">Approvals year-to-date</div></div>
  </div>
  <div style="display:flex; gap:16px; justify-content:center; margin-bottom:12px; font-size:12px; color:#374151; flex-wrap:wrap;">
    <span style="display:inline-flex; align-items:center; gap:6px;"><span style="width:12px; height:12px; background:#60a5fa; border-radius:3px; display:inline-block;"></span>Validation</span>
    <span style="display:inline-flex; align-items:center; gap:6px;"><span style="width:12px; height:12px; background:#0969da; border-radius:3px; display:inline-block;"></span>Under assessment</span>
    <span style="display:inline-flex; align-items:center; gap:6px;"><span style="width:12px; height:12px; background:#d97706; border-radius:3px; display:inline-block;"></span>Clock stop</span>
    <span style="display:inline-flex; align-items:center; gap:6px;"><span style="width:12px; height:12px; background:#8b5cf6; border-radius:3px; display:inline-block;"></span>Decision phase</span>
  </div>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 250" style="max-width:100%; height:auto; display:block;" font-family="system-ui, sans-serif" role="img" aria-label="Stacked bar chart of active procedures per regulator, split by current phase">
    <line x1="130" y1="8" x2="130" y2="226" stroke="#e5e7eb" stroke-width="1"/><text x="130" y="242" font-size="11" fill="#6b7280" text-anchor="middle">0</text><line x1="238" y1="8" x2="238" y2="226" stroke="#e5e7eb" stroke-width="1"/><text x="238" y="242" font-size="11" fill="#6b7280" text-anchor="middle">3</text><line x1="346" y1="8" x2="346" y2="226" stroke="#e5e7eb" stroke-width="1"/><text x="346" y="242" font-size="11" fill="#6b7280" text-anchor="middle">6</text><line x1="454" y1="8" x2="454" y2="226" stroke="#e5e7eb" stroke-width="1"/><text x="454" y="242" font-size="11" fill="#6b7280" text-anchor="middle">9</text><line x1="562" y1="8" x2="562" y2="226" stroke="#e5e7eb" stroke-width="1"/><text x="562" y="242" font-size="11" fill="#6b7280" text-anchor="middle">12</text>
    <text x="120" y="30" font-size="12" fill="#374151" text-anchor="end">Regulator A</text>
    <rect x="130" y="16" width="70" height="20" rx="3" fill="#60a5fa"><title>Regulator A: 2 procedures in validation</title></rect>
    <text x="165.0" y="30" font-size="11" font-weight="700" fill="#1e3a5f" text-anchor="middle">2</text>
    <rect x="202" y="16" width="214" height="20" rx="3" fill="#0969da"><title>Regulator A: 6 procedures in under assessment</title></rect>
    <text x="309.0" y="30" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">6</text>
    <rect x="418" y="16" width="70" height="20" rx="3" fill="#d97706"><title>Regulator A: 2 procedures in clock stop</title></rect>
    <text x="453.0" y="30" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">2</text>
    <rect x="490" y="16" width="34" height="20" rx="3" fill="#8b5cf6"><title>Regulator A: 1 procedure in decision phase</title></rect>
    <text x="507.0" y="30" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">1</text>
    <text x="532" y="30" font-size="12" font-weight="700" fill="#111827">11</text>
    <text x="120" y="72" font-size="12" fill="#374151" text-anchor="end">Regulator B</text>
    <rect x="130" y="58" width="34" height="20" rx="3" fill="#60a5fa"><title>Regulator B: 1 procedure in validation</title></rect>
    <text x="147.0" y="72" font-size="11" font-weight="700" fill="#1e3a5f" text-anchor="middle">1</text>
    <rect x="166" y="58" width="178" height="20" rx="3" fill="#0969da"><title>Regulator B: 5 procedures in under assessment</title></rect>
    <text x="255.0" y="72" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">5</text>
    <rect x="346" y="58" width="34" height="20" rx="3" fill="#d97706"><title>Regulator B: 1 procedure in clock stop</title></rect>
    <text x="363.0" y="72" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">1</text>
    <rect x="382" y="58" width="34" height="20" rx="3" fill="#8b5cf6"><title>Regulator B: 1 procedure in decision phase</title></rect>
    <text x="399.0" y="72" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">1</text>
    <text x="424" y="72" font-size="12" font-weight="700" fill="#111827">8</text>
    <text x="120" y="114" font-size="12" fill="#374151" text-anchor="end">Regulator C</text>
    <rect x="130" y="100" width="34" height="20" rx="3" fill="#60a5fa"><title>Regulator C: 1 procedure in validation</title></rect>
    <text x="147.0" y="114" font-size="11" font-weight="700" fill="#1e3a5f" text-anchor="middle">1</text>
    <rect x="166" y="100" width="250" height="20" rx="3" fill="#0969da"><title>Regulator C: 7 procedures in under assessment</title></rect>
    <text x="291.0" y="114" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">7</text>
    <rect x="418" y="100" width="106" height="20" rx="3" fill="#d97706"><title>Regulator C: 3 procedures in clock stop</title></rect>
    <text x="471.0" y="114" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">3</text>
    <rect x="526" y="100" width="34" height="20" rx="3" fill="#8b5cf6"><title>Regulator C: 1 procedure in decision phase</title></rect>
    <text x="543.0" y="114" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">1</text>
    <text x="568" y="114" font-size="12" font-weight="700" fill="#111827">12</text>
    <text x="120" y="156" font-size="12" fill="#374151" text-anchor="end">Regulator D</text>
    <rect x="130" y="142" width="142" height="20" rx="3" fill="#0969da"><title>Regulator D: 4 procedures in under assessment</title></rect>
    <text x="201.0" y="156" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">4</text>
    <rect x="274" y="142" width="34" height="20" rx="3" fill="#d97706"><title>Regulator D: 1 procedure in clock stop</title></rect>
    <text x="291.0" y="156" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">1</text>
    <rect x="310" y="142" width="34" height="20" rx="3" fill="#8b5cf6"><title>Regulator D: 1 procedure in decision phase</title></rect>
    <text x="327.0" y="156" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">1</text>
    <text x="352" y="156" font-size="12" font-weight="700" fill="#111827">6</text>
    <text x="120" y="198" font-size="12" fill="#374151" text-anchor="end">Regulator E</text>
    <rect x="130" y="184" width="70" height="20" rx="3" fill="#60a5fa"><title>Regulator E: 2 procedures in validation</title></rect>
    <text x="165.0" y="198" font-size="11" font-weight="700" fill="#1e3a5f" text-anchor="middle">2</text>
    <rect x="202" y="184" width="214" height="20" rx="3" fill="#0969da"><title>Regulator E: 6 procedures in under assessment</title></rect>
    <text x="309.0" y="198" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">6</text>
    <rect x="418" y="184" width="34" height="20" rx="3" fill="#d97706"><title>Regulator E: 1 procedure in clock stop</title></rect>
    <text x="435.0" y="198" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">1</text>
    <rect x="454" y="184" width="34" height="20" rx="3" fill="#8b5cf6"><title>Regulator E: 1 procedure in decision phase</title></rect>
    <text x="471.0" y="198" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">1</text>
    <text x="496" y="198" font-size="12" font-weight="700" fill="#111827">10</text>
  </svg>
  <div style="margin-top:8px; font-size:12px; color:#666; text-align:center;">Procedures by current phase &middot; rolled up live from <code>Task.status</code> / <code>Task.businessStatus</code> across every connected regulator &middot; hover a segment for detail</div>
</div>
</div>

<!-- Scenario Example 2 -->
<div style="background:#fff; border:1px solid #e5e7eb; border-left:3px solid #003087; border-radius:8px; padding:20px; margin-bottom:24px;">
  <div style="font-size:.72em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#003087; margin-bottom:6px;">Scenario Example 2 &middot; Regulator Performance Dashboards</div>
  <div style="font-weight:700; color:#111827; margin-bottom:8px;">From the Same Data: Live Operations Board and Statutory Performance Reports</div>
  <p style="font-size:.82em; color:#6b7280; line-height:1.6; margin-bottom:16px;">Regulators get the mirror image of the applicant's tracking view &mdash; for free. Because every procedure is an RWI-pharma <code>Task</code> with a full, timestamped status history, an agency can generate performance dashboards directly from its own exchange data: a real-time board of current activity, and aggregated quarterly or annual performance reports.</p>

  <div style="font-weight:700; color:#111827; font-size:.92em; margin-bottom:8px;">A &mdash; Live Activity Board (Flight-Board View)</div>
  <p style="font-size:.82em; color:#6b7280; line-height:1.6; margin-bottom:14px;">A real-time view of everything currently in the house &mdash; like an airport departure board. Each status change anywhere in the agency updates the board instantly via the same subscription framework offered to applicants.</p>

<div style="background:#0b1220; border:1px solid #1e293b; border-radius:12px; padding:20px 22px; margin-bottom:20px; overflow-x:auto;">
  <div style="display:flex; justify-content:space-between; align-items:baseline; flex-wrap:wrap; gap:8px; margin-bottom:14px;">
    <div style="color:#f8fafc; font-weight:700; font-size:.95em; letter-spacing:.08em; font-family:ui-monospace,Menlo,Consolas,monospace;">ACTIVE PROCEDURES &mdash; LIVE</div>
    <div style="color:#64748b; font-size:.75em; font-family:ui-monospace,Menlo,Consolas,monospace;">auto-refreshed by subscription notifications &middot; last event 14:32:07 UTC</div>
  </div>
  <table style="width:100%; border-collapse:collapse; font-family:ui-monospace,Menlo,Consolas,monospace; font-size:.78em; min-width:720px;">
    <thead>
      <tr style="color:#64748b; text-align:left; letter-spacing:.1em;">
        <th style="padding:6px 10px; border-bottom:1px solid #1e293b; font-weight:600;">PROCEDURE</th>
        <th style="padding:6px 10px; border-bottom:1px solid #1e293b; font-weight:600;">PRODUCT</th>
        <th style="padding:6px 10px; border-bottom:1px solid #1e293b; font-weight:600;">TYPE</th>
        <th style="padding:6px 10px; border-bottom:1px solid #1e293b; font-weight:600;">CURRENT PHASE</th>
        <th style="padding:6px 10px; border-bottom:1px solid #1e293b; font-weight:600; text-align:right;">DAY</th>
        <th style="padding:6px 10px; border-bottom:1px solid #1e293b; font-weight:600;">STATUS</th>
      </tr>
    </thead>
    <tbody style="color:#e2e8f0;">
      <tr>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a;">SUB-2027-1204</td>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a;">Dermacort 1% cream</td>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a; color:#94a3b8;">Type IA Variation</td>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a;">Submission received</td>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a; text-align:right;">0</td>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a; color:#94a3b8; font-weight:700;">&#9679; RECEIVED</td>
      </tr>
      <tr>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a;">VAR-IB-2027-118</td>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a;">Cardizal 5 mg</td>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a; color:#94a3b8;">Type IB Variation</td>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a;">Technical validation</td>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a; text-align:right;">2</td>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a; color:#60a5fa; font-weight:700;">&#9679; VALIDATION</td>
      </tr>
      <tr>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a;">MAA-2027-0057</td>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a;">Virestat 200 mg</td>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a; color:#94a3b8;">Initial MAA</td>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a;">Filing review</td>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a; text-align:right;">12</td>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a; color:#60a5fa; font-weight:700;">&#9679; IN REVIEW</td>
      </tr>
      <tr>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a;">MAA-2027-0042</td>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a;">Oncomab 50 mg</td>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a; color:#94a3b8;">Initial MAA</td>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a;">CMC assessment</td>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a; text-align:right;">142</td>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a; color:#60a5fa; font-weight:700;">&#9679; IN REVIEW</td>
      </tr>
      <tr>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a;">NDA-214365-S-021</td>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a;">Stelbatolol 10 mg</td>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a; color:#94a3b8;">Supplement (shelf-life)</td>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a;">Awaiting applicant response (IR 001)</td>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a; text-align:right;">133</td>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a; color:#fbbf24; font-weight:700;">&#10074;&#10074; CLOCK STOP</td>
      </tr>
      <tr>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a;">REN-2027-031</td>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a;">Neurofen XR 75 mg</td>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a; color:#94a3b8;">Renewal</td>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a;">Decision preparation</td>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a; text-align:right;">55</td>
        <td style="padding:8px 10px; border-bottom:1px solid #16213a; color:#a78bfa; font-weight:700;">&#9670; DECISION DUE</td>
      </tr>
      <tr>
        <td style="padding:8px 10px;">VAR-II-2026-889</td>
        <td style="padding:8px 10px;">Oncomab 50 mg</td>
        <td style="padding:8px 10px; color:#94a3b8;">Type II Variation</td>
        <td style="padding:8px 10px;">Closed</td>
        <td style="padding:8px 10px; text-align:right;">201</td>
        <td style="padding:8px 10px; color:#34d399; font-weight:700;">&#10003; APPROVED</td>
      </tr>
    </tbody>
  </table>
</div>
<p style="font-size:.8em; color:#6b7280; line-height:1.6; margin-bottom:24px;">Every row is a parent RWI-pharma <code>Task</code>; the CURRENT PHASE column is <code>Task.businessStatus</code> and the STATUS column is <code>Task.status</code>. A <code>task-update</code> subscription notification flips the row the moment an assessor changes the Task &mdash; no polling, no data entry. Note the shelf-life test scenario (<code>NDA-214365-S-021</code>) sitting in its first clock stop, exactly as shown on the timeline in Scenario Example 1.</p>

  <div style="font-weight:700; color:#111827; font-size:.92em; margin-bottom:8px;">B &mdash; Quarterly &amp; Annual Performance Reports</div>
  <p style="font-size:.82em; color:#6b7280; line-height:1.6; margin-bottom:14px;">The same event history, aggregated over a reporting period, produces the statutory performance metrics that agencies publish today through manual compilation &mdash; outcome counts, average review times by procedure type, and bottleneck analysis. With RWI-pharma these are a query, not a project.</p>

  <p style="font-size:.85em; color:#374151; margin-bottom:8px;"><strong>Median time to approval</strong> &mdash; the headline figure of a regulator&rsquo;s annual performance report (e.g., a PDUFA-style report to Congress or an EMA annual report), computed directly from Task timestamps instead of manual compilation:</p>

<div style="font-family: sans-serif; border: 1px solid #ddd; padding: 20px; max-width: 640px; background: #fff;">
  <h4 style="margin-top:0; text-align:center;">Median Time to Application Approval (Months)</h4>
  <div style="display:flex; gap:18px; justify-content:center; margin-bottom:14px; font-size:12px; color:#374151;">
    <span style="display:inline-flex; align-items:center; gap:6px;"><span style="width:12px; height:12px; background:#0969da; border-radius:3px; display:inline-block;"></span>Priority</span>
    <span style="display:inline-flex; align-items:center; gap:6px;"><span style="width:12px; height:12px; background:#d97706; border-radius:3px; display:inline-block;"></span>Standard</span>
  </div>
  <div style="display:flex; align-items:flex-end; border-bottom:2px solid #333; gap:20px;">
    <div style="flex:1; display:flex; flex-direction:column; align-items:center;">
      <div style="display:flex; gap:3px; align-items:flex-end; height:200px;">
<div style="width:22px; background-color:#0969da; height:96px; border-radius:4px 4px 0 0; position:relative;"><span style="position:absolute; top:-16px; left:50%; transform:translateX(-50%); font-size:10px; font-weight:bold; color:#374151; white-space:nowrap;">8.0</span></div>
<div style="width:22px; background-color:#d97706; height:144px; border-radius:4px 4px 0 0; position:relative;"><span style="position:absolute; top:-16px; left:50%; transform:translateX(-50%); font-size:10px; font-weight:bold; color:#374151; white-space:nowrap;">12.0</span></div>
      </div>
      <div style="margin-top:8px; font-size:11px; color:#374151;">2021</div>
    </div>
    <div style="flex:1; display:flex; flex-direction:column; align-items:center;">
      <div style="display:flex; gap:3px; align-items:flex-end; height:200px;">
<div style="width:22px; background-color:#0969da; height:95px; border-radius:4px 4px 0 0; position:relative;"><span style="position:absolute; top:-16px; left:50%; transform:translateX(-50%); font-size:10px; font-weight:bold; color:#374151; white-space:nowrap;">7.9</span></div>
<div style="width:22px; background-color:#d97706; height:138px; border-radius:4px 4px 0 0; position:relative;"><span style="position:absolute; top:-16px; left:50%; transform:translateX(-50%); font-size:10px; font-weight:bold; color:#374151; white-space:nowrap;">11.5</span></div>
      </div>
      <div style="margin-top:8px; font-size:11px; color:#374151;">2022</div>
    </div>
    <div style="flex:1; display:flex; flex-direction:column; align-items:center;">
      <div style="display:flex; gap:3px; align-items:flex-end; height:200px;">
<div style="width:22px; background-color:#0969da; height:94px; border-radius:4px 4px 0 0; position:relative;"><span style="position:absolute; top:-16px; left:50%; transform:translateX(-50%); font-size:10px; font-weight:bold; color:#374151; white-space:nowrap;">7.8</span></div>
<div style="width:22px; background-color:#d97706; height:156px; border-radius:4px 4px 0 0; position:relative;"><span style="position:absolute; top:-16px; left:50%; transform:translateX(-50%); font-size:10px; font-weight:bold; color:#374151; white-space:nowrap;">13.0</span></div>
      </div>
      <div style="margin-top:8px; font-size:11px; color:#374151;">2023</div>
    </div>
    <div style="flex:1; display:flex; flex-direction:column; align-items:center;">
      <div style="display:flex; gap:3px; align-items:flex-end; height:200px;">
<div style="width:22px; background-color:#0969da; height:92px; border-radius:4px 4px 0 0; position:relative;"><span style="position:absolute; top:-16px; left:50%; transform:translateX(-50%); font-size:10px; font-weight:bold; color:#374151; white-space:nowrap;">7.7</span></div>
<div style="width:22px; background-color:#d97706; height:146px; border-radius:4px 4px 0 0; position:relative;"><span style="position:absolute; top:-16px; left:50%; transform:translateX(-50%); font-size:10px; font-weight:bold; color:#374151; white-space:nowrap;">12.2</span></div>
      </div>
      <div style="margin-top:8px; font-size:11px; color:#374151;">2024</div>
    </div>
    <div style="flex:1; display:flex; flex-direction:column; align-items:center;">
      <div style="display:flex; gap:3px; align-items:flex-end; height:200px;">
<div style="width:22px; background-color:#0969da; height:95px; border-radius:4px 4px 0 0; position:relative;"><span style="position:absolute; top:-16px; left:50%; transform:translateX(-50%); font-size:10px; font-weight:bold; color:#374151; white-space:nowrap;">7.9</span></div>
<div style="width:22px; background-color:#d97706; height:131px; border-radius:4px 4px 0 0; position:relative;"><span style="position:absolute; top:-16px; left:50%; transform:translateX(-50%); font-size:10px; font-weight:bold; color:#374151; white-space:nowrap;">10.9</span></div>
      </div>
      <div style="margin-top:8px; font-size:11px; color:#374151;">2025</div>
    </div>
  </div>
  <div style="margin-top:10px; font-size:12px; color:#666; text-align:center;">Fiscal Year of Approval &middot; computed from <code>Task.authoredOn</code> &rarr; <code>Task.lastModified</code> (approved)</div>
</div>

  <p style="font-size:.85em; color:#374151; margin:16px 0 8px;"><strong>First-cycle approval rate</strong> &mdash; the quality-of-review metric regulators publish each year, derived from the Task status history (was the application approved without a resubmission cycle?):</p>

<div style="font-family: sans-serif; border: 1px solid #ddd; padding: 20px; max-width: 640px; background: #fff;">
  <h4 style="margin-top:0; text-align:center;">Percent of Applications Approved on the First Cycle</h4>
  <div style="display:flex; gap:18px; justify-content:center; margin-bottom:14px; font-size:12px; color:#374151;">
    <span style="display:inline-flex; align-items:center; gap:6px;"><span style="width:12px; height:12px; background:#0969da; border-radius:3px; display:inline-block;"></span>Priority</span>
    <span style="display:inline-flex; align-items:center; gap:6px;"><span style="width:12px; height:12px; background:#d97706; border-radius:3px; display:inline-block;"></span>Standard</span>
  </div>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 290" style="max-width:100%; height:auto; display:block;" font-family="system-ui, sans-serif" role="img" aria-label="Line graph of percent of applications approved on the first cycle, fiscal years 2021 to 2025, Priority versus Standard">
    <line x1="44" y1="250" x2="560" y2="250" stroke="#e5e7eb" stroke-width="1"/><text x="36" y="254" font-size="11" fill="#6b7280" text-anchor="end">50%</text>
    <line x1="44" y1="200" x2="560" y2="200" stroke="#e5e7eb" stroke-width="1"/><text x="36" y="204" font-size="11" fill="#6b7280" text-anchor="end">60%</text>
    <line x1="44" y1="150" x2="560" y2="150" stroke="#e5e7eb" stroke-width="1"/><text x="36" y="154" font-size="11" fill="#6b7280" text-anchor="end">70%</text>
    <line x1="44" y1="100" x2="560" y2="100" stroke="#e5e7eb" stroke-width="1"/><text x="36" y="104" font-size="11" fill="#6b7280" text-anchor="end">80%</text>
    <line x1="44" y1="50" x2="560" y2="50" stroke="#e5e7eb" stroke-width="1"/><text x="36" y="54" font-size="11" fill="#6b7280" text-anchor="end">90%</text>
    <line x1="44" y1="250" x2="560" y2="250" stroke="#9ca3af" stroke-width="1.5"/>
    <text x="44" y="272" font-size="11" fill="#6b7280" text-anchor="middle">2021</text>
    <text x="156" y="272" font-size="11" fill="#6b7280" text-anchor="middle">2022</text>
    <text x="268" y="272" font-size="11" fill="#6b7280" text-anchor="middle">2023</text>
    <text x="380" y="272" font-size="11" fill="#6b7280" text-anchor="middle">2024</text>
    <text x="492" y="272" font-size="11" fill="#6b7280" text-anchor="middle">2025</text>
    <polyline points="44,190 156,210 268,175 380,160 492,170" fill="none" stroke="#d97706" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
    <polyline points="44,75 156,90 268,60 380,100 492,80" fill="none" stroke="#0969da" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
    <circle cx="44" cy="190" r="4.5" fill="#d97706" stroke="#ffffff" stroke-width="2"><title>Standard &middot; FY 2021: 62% approved on first cycle</title></circle>
    <circle cx="156" cy="210" r="4.5" fill="#d97706" stroke="#ffffff" stroke-width="2"><title>Standard &middot; FY 2022: 58% approved on first cycle</title></circle>
    <circle cx="268" cy="175" r="4.5" fill="#d97706" stroke="#ffffff" stroke-width="2"><title>Standard &middot; FY 2023: 65% approved on first cycle</title></circle>
    <circle cx="380" cy="160" r="4.5" fill="#d97706" stroke="#ffffff" stroke-width="2"><title>Standard &middot; FY 2024: 68% approved on first cycle</title></circle>
    <circle cx="492" cy="170" r="4.5" fill="#d97706" stroke="#ffffff" stroke-width="2"><title>Standard &middot; FY 2025: 66% approved on first cycle</title></circle>
    <circle cx="44" cy="75" r="4.5" fill="#0969da" stroke="#ffffff" stroke-width="2"><title>Priority &middot; FY 2021: 85% approved on first cycle</title></circle>
    <circle cx="156" cy="90" r="4.5" fill="#0969da" stroke="#ffffff" stroke-width="2"><title>Priority &middot; FY 2022: 82% approved on first cycle</title></circle>
    <circle cx="268" cy="60" r="4.5" fill="#0969da" stroke="#ffffff" stroke-width="2"><title>Priority &middot; FY 2023: 88% approved on first cycle</title></circle>
    <circle cx="380" cy="100" r="4.5" fill="#0969da" stroke="#ffffff" stroke-width="2"><title>Priority &middot; FY 2024: 80% approved on first cycle</title></circle>
    <circle cx="492" cy="80" r="4.5" fill="#0969da" stroke="#ffffff" stroke-width="2"><title>Priority &middot; FY 2025: 84% approved on first cycle</title></circle>
    <text x="36" y="65" font-size="11.5" font-weight="700" fill="#374151">85%</text>
    <text x="504" y="72" font-size="11.5" font-weight="700" fill="#374151">84%</text>
    <text x="504" y="86" font-size="11" fill="#374151">Priority</text>
    <text x="36" y="212" font-size="11.5" font-weight="700" fill="#374151">62%</text>
    <text x="504" y="168" font-size="11.5" font-weight="700" fill="#374151">66%</text>
    <text x="504" y="182" font-size="11" fill="#374151">Standard</text>
  </svg>
  <div style="margin-top:10px; font-size:12px; color:#666; text-align:center;">Fiscal Year of Application Receipt &middot; first-cycle = approved without a resubmission cycle &middot; hover a point for the value</div>
</div>

  <p style="font-size:.85em; color:#374151; margin:16px 0 8px;"><strong>Bottleneck detection</strong> &mdash; where does the time actually go?</p>

<div style="font-family: sans-serif; border: 1px solid #ddd; padding: 20px; max-width: 640px; background: #fff;">
  <h4 style="margin-top:0; text-align:center;">Average Days per Phase</h4>
  <div style="display:flex; gap:16px; justify-content:center; margin-bottom:12px; font-size:12px; color:#374151;">
    <span style="display:inline-flex; align-items:center; gap:6px;"><span style="width:12px; height:12px; background:#0969da; border-radius:3px; display:inline-block;"></span>Regulator clock</span>
    <span style="display:inline-flex; align-items:center; gap:6px;"><span style="width:12px; height:12px; background:#d97706; border-radius:3px; display:inline-block;"></span>Applicant clock</span>
  </div>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 226" style="max-width:100%; height:auto; display:block;" font-family="system-ui, sans-serif" role="img" aria-label="Horizontal bar chart of average days spent per procedure phase; scientific assessment is the longest at 75 days">
    <line x1="210.0" y1="6" x2="210.0" y2="202" stroke="#e5e7eb" stroke-width="1"/><text x="210.0" y="218" font-size="11" fill="#6b7280" text-anchor="middle">0</text><line x1="340.0" y1="6" x2="340.0" y2="202" stroke="#e5e7eb" stroke-width="1"/><text x="340.0" y="218" font-size="11" fill="#6b7280" text-anchor="middle">25</text><line x1="470.0" y1="6" x2="470.0" y2="202" stroke="#e5e7eb" stroke-width="1"/><text x="470.0" y="218" font-size="11" fill="#6b7280" text-anchor="middle">50</text><line x1="600.0" y1="6" x2="600.0" y2="202" stroke="#e5e7eb" stroke-width="1"/><text x="600.0" y="218" font-size="11" fill="#6b7280" text-anchor="middle">75</text>
    <text x="200" y="27" font-size="12" fill="#374151" text-anchor="end">Technical validation</text>
    <rect x="210" y="14" width="62.400000000000006" height="18" rx="4" fill="#0969da"><title>Technical validation: 12 days on average</title></rect>
    <text x="280.4" y="27" font-size="12" font-weight="700" fill="#111827">12d<tspan font-weight="400" fill="#6b7280"></tspan></text>
    <text x="200" y="65" font-size="12" fill="#374151" text-anchor="end">Scientific assessment</text>
    <rect x="210" y="52" width="390.0" height="18" rx="4" fill="#0969da"><title>Scientific assessment: 75 days on average</title></rect>
    <text x="608.0" y="65" font-size="12" font-weight="700" fill="#111827">75d</text>
    <text x="200" y="103" font-size="12" fill="#374151" text-anchor="end">Clock stop &mdash; awaiting applicant</text>
    <rect x="210" y="90" width="234.0" height="18" rx="4" fill="#d97706"><title>Clock stop &mdash; awaiting applicant: 45 days on average</title></rect>
    <text x="452.0" y="103" font-size="12" font-weight="700" fill="#111827">45d<tspan font-weight="400" fill="#6b7280"></tspan></text>
    <text x="200" y="141" font-size="12" fill="#374151" text-anchor="end">Response review</text>
    <rect x="210" y="128" width="109.2" height="18" rx="4" fill="#0969da"><title>Response review: 21 days on average</title></rect>
    <text x="327.2" y="141" font-size="12" font-weight="700" fill="#111827">21d<tspan font-weight="400" fill="#6b7280"></tspan></text>
    <text x="200" y="179" font-size="12" fill="#374151" text-anchor="end">Decision preparation</text>
    <rect x="210" y="166" width="52.0" height="18" rx="4" fill="#0969da"><title>Decision preparation: 10 days on average</title></rect>
    <text x="270.0" y="179" font-size="12" font-weight="700" fill="#111827">10d<tspan font-weight="400" fill="#6b7280"></tspan></text>
  </svg>
  <div style="margin-top:8px; font-size:12px; color:#666; text-align:center;">Average across procedures closed in the last 12 months &middot; days &middot; clock-stop time is applicant time, not regulator time</div>
</div>
</div>

<hr style="border:none; border-top:1px solid #e5e7eb; margin:0 0 32px;"/>

<!-- USE CASE 3: AUTOMATION -->
<div id="automation" style="display:flex; align-items:center; gap:12px; margin-bottom:10px;">
  <span style="display:inline-flex; align-items:center; justify-content:center; width:36px; height:36px; border-radius:50%; background:#7c3aed; color:#fff; font-weight:800; font-size:.9em; flex-shrink:0;">3</span>
  <h2 style="font-size:1.4em; font-weight:800; color:#111827; margin:0;">Automation</h2>
</div>
<p style="font-size:.92em; color:#4b5563; line-height:1.65; max-width:760px; margin:0 0 20px;">Because every question and response arrives as a structured, machine-readable Task, the receiving system can act on it the moment it arrives. Nobody has to watch an inbox and decide where each message should go.</p>
<div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-bottom:16px;">
  <div style="background:#fff; border:1px solid #e9d5ff; border-radius:10px; padding:20px;">
    <div style="font-size:.7em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#7c3aed; margin-bottom:4px;">Receiving a question</div>
    <div style="font-weight:700; color:#111827; margin-bottom:14px;">Route questions automatically on receipt</div>
    <div style="display:flex; gap:10px; align-items:flex-start; margin-bottom:10px;"><span style="flex-shrink:0; width:24px; height:24px; border-radius:50%; background:#f5f3ff; border:2px solid #7c3aed; color:#7c3aed; font-weight:800; font-size:.75em; display:inline-flex; align-items:center; justify-content:center;">1</span><span style="font-size:.84em; color:#374151; line-height:1.55;">The regulator posts a question Task with the questions attached.</span></div><div style="display:flex; gap:10px; align-items:flex-start; margin-bottom:10px;"><span style="flex-shrink:0; width:24px; height:24px; border-radius:50%; background:#f5f3ff; border:2px solid #7c3aed; color:#7c3aed; font-weight:800; font-size:.75em; display:inline-flex; align-items:center; justify-content:center;">2</span><span style="font-size:.84em; color:#374151; line-height:1.55;">The applicant’s system is notified instantly through its Subscription.</span></div><div style="display:flex; gap:10px; align-items:flex-start; margin-bottom:10px;"><span style="flex-shrink:0; width:24px; height:24px; border-radius:50%; background:#f5f3ff; border:2px solid #7c3aed; color:#7c3aed; font-weight:800; font-size:.75em; display:inline-flex; align-items:center; justify-content:center;">3</span><span style="font-size:.84em; color:#374151; line-height:1.55;">Routing rules read the Task — its type, the product, and the CTD sections of the referenced documents.</span></div><div style="display:flex; gap:10px; align-items:flex-start; margin-bottom:10px;"><span style="flex-shrink:0; width:24px; height:24px; border-radius:50%; background:#f5f3ff; border:2px solid #7c3aed; color:#7c3aed; font-weight:800; font-size:.75em; display:inline-flex; align-items:center; justify-content:center;">4</span><span style="font-size:.84em; color:#374151; line-height:1.55;">The question lands in the right team’s queue (for example CMC, labelling, clinical, or safety), with the response due date taken from the Task.</span></div>
  </div>
  <div style="background:#fff; border:1px solid #e9d5ff; border-radius:10px; padding:20px;">
    <div style="font-size:.7em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#7c3aed; margin-bottom:4px;">Receiving a response</div>
    <div style="font-weight:700; color:#111827; margin-bottom:14px;">Route responses automatically on receipt</div>
    <div style="display:flex; gap:10px; align-items:flex-start; margin-bottom:10px;"><span style="flex-shrink:0; width:24px; height:24px; border-radius:50%; background:#f5f3ff; border:2px solid #7c3aed; color:#7c3aed; font-weight:800; font-size:.75em; display:inline-flex; align-items:center; justify-content:center;">1</span><span style="font-size:.84em; color:#374151; line-height:1.55;">The applicant adds its response to the question Task’s <code>Task.output</code>.</span></div><div style="display:flex; gap:10px; align-items:flex-start; margin-bottom:10px;"><span style="flex-shrink:0; width:24px; height:24px; border-radius:50%; background:#f5f3ff; border:2px solid #7c3aed; color:#7c3aed; font-weight:800; font-size:.75em; display:inline-flex; align-items:center; justify-content:center;">2</span><span style="font-size:.84em; color:#374151; line-height:1.55;">The regulator’s system is notified instantly through its Subscription.</span></div><div style="display:flex; gap:10px; align-items:flex-start; margin-bottom:10px;"><span style="flex-shrink:0; width:24px; height:24px; border-radius:50%; background:#f5f3ff; border:2px solid #7c3aed; color:#7c3aed; font-weight:800; font-size:.75em; display:inline-flex; align-items:center; justify-content:center;">3</span><span style="font-size:.84em; color:#374151; line-height:1.55;">The response is matched to the original question and procedure through the Task’s identifiers.</span></div><div style="display:flex; gap:10px; align-items:flex-start; margin-bottom:10px;"><span style="flex-shrink:0; width:24px; height:24px; border-radius:50%; background:#f5f3ff; border:2px solid #7c3aed; color:#7c3aed; font-weight:800; font-size:.75em; display:inline-flex; align-items:center; justify-content:center;">4</span><span style="font-size:.84em; color:#374151; line-height:1.55;">It is routed straight to the reviewer who asked (<code>Task.requester</code>), and the clock restarts.</span></div>
  </div>
</div>

<div style="display:flex; gap:10px; flex-wrap:wrap; margin-bottom:36px;">
  <span style="background:#f5f3ff; border:1px solid #e9d5ff; color:#6d28d9; padding:6px 12px; border-radius:6px; font-size:.8em; font-weight:600;">✓ No manual triage</span>
  <span style="background:#f5f3ff; border:1px solid #e9d5ff; color:#6d28d9; padding:6px 12px; border-radius:6px; font-size:.8em; font-weight:600;">✓ No missed deadlines</span>
  <span style="background:#f5f3ff; border:1px solid #e9d5ff; color:#6d28d9; padding:6px 12px; border-radius:6px; font-size:.8em; font-weight:600;">✓ Clock stops start and end on their own</span>
</div>

<hr style="border:none; border-top:1px solid #e5e7eb; margin:0 0 32px;"/>

<div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:8px; padding:14px 18px; font-size:.85em; color:#374151; display:flex; gap:10px; align-items:flex-start;">
  <span style="flex-shrink:0;">ℹ️</span>
  <span><strong>Note:</strong> For a step-by-step technical walkthrough of these use cases, visit the <a href="workflow.html#walkthrough">Workflow</a> page.</span>
</div>
