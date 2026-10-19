<!-- USE CASE 1: UNIVERSAL SUBMISSIONS -->
<div style="margin-bottom:28px;">
  <a href="usecases.html" style="font-size:.7em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#2563eb; text-decoration:none;">Use case 1 of 3</a>
  <h2 style="font-size:1.7em; font-weight:800; color:#111827; margin:6px 0 10px;">Universal Submissions</h2>
  <p style="font-size:.95em; color:#6b7280; line-height:1.6; max-width:760px;">Every regulatory interaction uses the same building blocks: files are uploaded as <a href="architecture.html#binary-upload-guide-post-then-link">Binary</a>, described with <a href="apixdocumentReference.html">DocumentReference</a>, and orchestrated by a <a href="apixtask.html">Task</a>. Only the Task type and its documents change from one interaction to the next — not the channel, the portal, or the integration.</p>
</div>

<hr style="border:none; border-top:1px solid #e5e7eb; margin:0 0 32px;"/>

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
    <ol style="font-size:.82em; color:#374151; line-height:1.6; padding-left:18px; margin:0 0 10px;"><li style="margin-bottom:4px;">Applicant uploads the ICSR (e.g., ICH E2B(R3) XML) as Binary + DocumentReference.</li><li style="margin-bottom:4px;">Applicant posts a Task for the case report that references it.</li><li style="margin-bottom:4px;">Regulator acknowledges receipt by updating the Task and attaching the acknowledgment to <code>Task.output</code>.</li><li style="margin-bottom:4px;">Follow-up reports for the same case are linked to the original case Task.</li></ol>
    <div style="font-size:.8em; margin-top:auto;"><a href="Task-scenario2-01-icsr-initial.html" style="color:#dc2626; font-weight:600; text-decoration:none;">Example ICSR Task</a> · <a href="Task-scenario2-02-icsr-initial-acknowledged.html" style="color:#dc2626; font-weight:600; text-decoration:none;">Acknowledged</a> · <a href="Task-scenario2-03-icsr-follow-up.html" style="color:#dc2626; font-weight:600; text-decoration:none;">Follow-up</a></div>
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

<div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:8px; padding:14px 18px; font-size:.85em; color:#374151; display:flex; gap:10px; align-items:flex-start;">
  <span style="flex-shrink:0;">ℹ️</span>
  <span><strong>Note:</strong> For a step-by-step technical walkthrough of this use case, visit the <a href="workflow.html#walkthrough">Workflow</a> page.</span>
</div>

<div style="display:flex; justify-content:space-between; gap:12px; flex-wrap:wrap; font-size:.85em; margin-top:24px;">
  <a href="usecases.html" style="color:#2563eb; font-weight:600; text-decoration:none;">← Use Cases overview</a>
  <a href="usecases-status-tracking.html" style="color:#2563eb; font-weight:600; text-decoration:none;">Submission Tracking and Notifications →</a>
</div>
