<!-- USE CASE 3: AUTOMATION -->
<div style="margin-bottom:28px;">
  <a href="usecases.html" style="font-size:.7em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#7c3aed; text-decoration:none;">Use case 3 of 3</a>
  <h2 style="font-size:1.7em; font-weight:800; color:#111827; margin:6px 0 10px;">Automation</h2>
  <p style="font-size:.95em; color:#6b7280; line-height:1.6; max-width:760px;">Because every question and response arrives as a structured, machine-readable Task, the receiving system can act on it the moment it arrives. Nobody has to watch an inbox and decide where each message should go.</p>
</div>

<hr style="border:none; border-top:1px solid #e5e7eb; margin:0 0 32px;"/>

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
  <span><strong>Note:</strong> For a step-by-step technical walkthrough of this use case, visit the <a href="workflow.html#walkthrough">Workflow</a> page.</span>
</div>

<div style="display:flex; justify-content:space-between; gap:12px; flex-wrap:wrap; font-size:.85em; margin-top:24px;">
  <a href="usecases-status-tracking.html" style="color:#7c3aed; font-weight:600; text-decoration:none;">← Submission Tracking and Notifications</a>
  <a href="usecases-scenarios.html" style="color:#7c3aed; font-weight:600; text-decoration:none;">Example Scenarios →</a>
</div>
