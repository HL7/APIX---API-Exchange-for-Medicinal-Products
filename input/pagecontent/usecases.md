<!-- USE CASES OVERVIEW: the pattern, the four worked scenarios, and what each one shows -->
<div style="margin-bottom:28px;">
  <h2 style="font-size:1.7em; font-weight:800; color:#111827; margin:0 0 10px;">Use Cases</h2>
  <p style="font-size:.95em; color:#4b5563; line-height:1.6; max-width:760px; margin:0;">Four worked scenarios show how one Task-based pattern handles every regulatory interaction. Pick the one closest to your work. Each scenario lists every step with its example Task, status and documents.</p>
</div>

### One pattern for every interaction

<div style="display:flex; flex-wrap:wrap; align-items:stretch; gap:10px; margin-bottom:14px;">
  <div style="flex:1 1 200px; border:1px solid #d1d5db; border-radius:8px; padding:12px 16px;"><div style="font-weight:700; color:#003087;"><a href="https://hl7.org/fhir/R5/binary.html">Binary</a></div><div style="font-size:.85em; color:#4b5563;">The file: eCTD sequence, E2B message, ePI, PDF</div></div>
  <div aria-hidden="true" style="display:flex; align-items:center; color:#6b7280; font-size:1.2em;">→</div>
  <div style="flex:1 1 200px; border:1px solid #d1d5db; border-radius:8px; padding:12px 16px;"><div style="font-weight:700; color:#003087;"><a href="apixdocumentReference.html">DocumentReference</a></div><div style="font-size:.85em; color:#4b5563;">Describes the file: type, version, author</div></div>
  <div aria-hidden="true" style="display:flex; align-items:center; color:#6b7280; font-size:1.2em;">→</div>
  <div style="flex:1 1 200px; border:1px solid #d1d5db; border-radius:8px; padding:12px 16px;"><div style="font-weight:700; color:#003087;"><a href="apixtask.html">Task</a></div><div style="font-size:.85em; color:#4b5563;">Who asks, who acts, what it is, where it stands</div></div>
</div>

<div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:14px; font-size:.86em; color:#374151; line-height:1.55; margin-bottom:32px;">
  <div><strong style="color:#111827;">One channel.</strong> Submissions, safety reports, questions and labelling all use the same endpoint. Only the Task type and its documents change.</div>
  <div><strong style="color:#111827;">Every step is trackable.</strong> Each status change is a new Task version that a <a href="subscriptions.html">Subscription</a> pushes to the other party.</div>
  <div><strong style="color:#111827;">Ready to automate.</strong> A structured Task can be routed to the right team when it arrives, with no inbox triage.</div>
</div>

### Choose a scenario

<div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,420px),1fr)); gap:14px; margin-bottom:32px;">
  <div style="background:#fff; border:1px solid #e5e7eb; border-top:3px solid #2563eb; border-radius:8px; padding:18px; display:flex; flex-direction:column; gap:8px;">
    <div style="font-size:.7em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#1d4ed8;">Scenario 1 · Market authorization</div>
    <a href="usecases-scenario-stability.html" style="font-weight:700; color:#111827; font-size:1.05em; text-decoration:none;">Stability Update (Type IB Variation) →</a>
    <p style="font-size:.84em; color:#4b5563; line-height:1.5; margin:0;">Submission, validation, fee, one round of questions, approval.</p>
    <div style="display:grid; grid-template-columns:90px 1fr; gap:2px 10px; font-size:.8em; color:#374151;"><span style="color:#6b7280;">Starts it</span><span>Applicant</span><span style="color:#6b7280;">Task code</span><span><code>variation-type-ib</code></span></div>
    <div style="border-top:1px solid #f3f4f6; padding-top:8px; display:flex; flex-direction:column; gap:6px;">
      <div style="font-size:.68em; font-weight:700; text-transform:uppercase; letter-spacing:.08em; color:#6b7280;">Steps · each opens its Task</div>
      <div style="display:flex; flex-wrap:wrap; align-items:center; gap:6px;"><a href="Task-scenario1-01-initial-submission.html" title="requested / submitted" style="font-size:.78em; text-decoration:none; color:#1d4ed8; border:1px solid #bfdbfe; border-radius:999px; padding:2px 9px;">1 Submit</a><a href="Task-scenario1-02-validation.html" title="accepted / validation-successful" style="font-size:.78em; text-decoration:none; color:#1d4ed8; border:1px solid #bfdbfe; border-radius:999px; padding:2px 9px;">2 Validated</a><a href="Task-scenario1-03-finance-invoice.html" title="requested" style="font-size:.78em; text-decoration:none; color:#1d4ed8; border:1px solid #bfdbfe; border-radius:999px; padding:2px 9px;">3 Invoice</a><a href="Task-scenario1-04-finance-payment.html" title="completed / payment-received" style="font-size:.78em; text-decoration:none; color:#1d4ed8; border:1px solid #bfdbfe; border-radius:999px; padding:2px 9px;">4 Payment</a><a href="Task-scenario1-05-technical-question.html" title="requested / clock-stop" style="font-size:.78em; text-decoration:none; color:#1d4ed8; border:1px solid #bfdbfe; border-radius:999px; padding:2px 9px;">5 Question</a><a href="Task-scenario1-06-technical-response.html" title="completed / clock-restart" style="font-size:.78em; text-decoration:none; color:#1d4ed8; border:1px solid #bfdbfe; border-radius:999px; padding:2px 9px;">6 Response</a><a href="Task-scenario1-07-final-decision.html" title="completed / approved" style="font-size:.78em; text-decoration:none; color:#1d4ed8; border:1px solid #bfdbfe; border-radius:999px; padding:2px 9px;">7 Approved</a></div>
    </div>
  </div>
  <div style="background:#fff; border:1px solid #e5e7eb; border-top:3px solid #dc2626; border-radius:8px; padding:18px; display:flex; flex-direction:column; gap:8px;">
    <div style="font-size:.7em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#b91c1c;">Scenario 2 · Safety reporting</div>
    <a href="usecases-scenario-icsr.html" style="font-weight:700; color:#111827; font-size:1.05em; text-decoration:none;">ICSR: Accepted, and Rejected then Resubmitted →</a>
    <p style="font-size:.84em; color:#4b5563; line-height:1.5; margin:0;">Two E2B(R2) reports, one Task each. One fails validation and is resubmitted.</p>
    <div style="display:grid; grid-template-columns:90px 1fr; gap:2px 10px; font-size:.8em; color:#374151;"><span style="color:#6b7280;">Starts it</span><span>Marketing authorization holder</span><span style="color:#6b7280;">Task code</span><span><code>icsr</code></span></div>
    <div style="border-top:1px solid #f3f4f6; padding-top:8px; display:flex; flex-direction:column; gap:6px;">
      <div style="font-size:.68em; font-weight:700; text-transform:uppercase; letter-spacing:.08em; color:#6b7280;">Steps · each opens its Task</div>
      <div style="display:flex; flex-wrap:wrap; align-items:center; gap:6px;"><span style="font-size:.78em; font-weight:700; color:#4b5563; width:24px;">2a</span><a href="Task-scenario2a-01-icsr-submitted.html" title="requested / submitted" style="font-size:.78em; text-decoration:none; color:#b91c1c; border:1px solid #fecaca; border-radius:999px; padding:2px 9px;">1 Submit</a><a href="Task-scenario2a-02-icsr-accepted.html" title="accepted / accepted" style="font-size:.78em; text-decoration:none; color:#b91c1c; border:1px solid #fecaca; border-radius:999px; padding:2px 9px;">2 Accepted</a><a href="Task-scenario2a-03-icsr-complete.html" title="completed / complete" style="font-size:.78em; text-decoration:none; color:#b91c1c; border:1px solid #fecaca; border-radius:999px; padding:2px 9px;">3 Complete</a></div>
      <div style="display:flex; flex-wrap:wrap; align-items:center; gap:6px;"><span style="font-size:.78em; font-weight:700; color:#4b5563; width:24px;">2b</span><a href="Task-scenario2b-01-icsr-submitted.html" title="requested / submitted" style="font-size:.78em; text-decoration:none; color:#b91c1c; border:1px solid #fecaca; border-radius:999px; padding:2px 9px;">1 Submit</a><a href="Task-scenario2b-02-icsr-rejected.html" title="rejected / rejected" style="font-size:.78em; text-decoration:none; color:#991b1b; background:#fef2f2; border:1px solid #fca5a5; border-radius:999px; padding:2px 9px;">2 Rejected</a><a href="Task-scenario2b-03-icsr-resubmitted.html" title="requested / submitted" style="font-size:.78em; text-decoration:none; color:#b91c1c; border:1px solid #fecaca; border-radius:999px; padding:2px 9px;">3 Resubmit</a><a href="Task-scenario2b-04-icsr-accepted.html" title="accepted / accepted" style="font-size:.78em; text-decoration:none; color:#b91c1c; border:1px solid #fecaca; border-radius:999px; padding:2px 9px;">4 Accepted</a><a href="Task-scenario2b-05-icsr-complete.html" title="completed / complete" style="font-size:.78em; text-decoration:none; color:#b91c1c; border:1px solid #fecaca; border-radius:999px; padding:2px 9px;">5 Complete</a></div>
    </div>
  </div>
  <div style="background:#fff; border:1px solid #e5e7eb; border-top:3px solid #7c3aed; border-radius:8px; padding:18px; display:flex; flex-direction:column; gap:8px;">
    <div style="font-size:.7em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#6d28d9;">Scenario 3 · Clinical trials</div>
    <a href="usecases-scenario-cta.html" style="font-weight:700; color:#111827; font-size:1.05em; text-decoration:none;">Clinical Trial Application →</a>
    <p style="font-size:.84em; color:#4b5563; line-height:1.5; margin:0;">From application to authorisation, with a request for information and a deadline.</p>
    <div style="display:grid; grid-template-columns:90px 1fr; gap:2px 10px; font-size:.8em; color:#374151;"><span style="color:#6b7280;">Starts it</span><span>Sponsor</span><span style="color:#6b7280;">Task code</span><span><code>clinical-trial-application</code></span></div>
    <div style="border-top:1px solid #f3f4f6; padding-top:8px; display:flex; flex-direction:column; gap:6px;">
      <div style="font-size:.68em; font-weight:700; text-transform:uppercase; letter-spacing:.08em; color:#6b7280;">Steps · each opens its Task</div>
      <div style="display:flex; flex-wrap:wrap; align-items:center; gap:6px;"><a href="Task-scenario3-01-cta-submission.html" title="requested / submitted" style="font-size:.78em; text-decoration:none; color:#6d28d9; border:1px solid #ddd6fe; border-radius:999px; padding:2px 9px;">1 Submit</a><a href="Task-scenario3-02-cta-validated.html" title="accepted / validation-successful" style="font-size:.78em; text-decoration:none; color:#6d28d9; border:1px solid #ddd6fe; border-radius:999px; padding:2px 9px;">2 Validated</a><a href="Task-scenario3-03-cta-rfi.html" title="requested / request-for-information-issued" style="font-size:.78em; text-decoration:none; color:#6d28d9; border:1px solid #ddd6fe; border-radius:999px; padding:2px 9px;">3 Request for information</a><a href="Task-scenario3-04-cta-rfi-response.html" title="completed / clock-restart" style="font-size:.78em; text-decoration:none; color:#6d28d9; border:1px solid #ddd6fe; border-radius:999px; padding:2px 9px;">4 Response</a><a href="Task-scenario3-05-cta-authorised.html" title="completed / authorised" style="font-size:.78em; text-decoration:none; color:#6d28d9; border:1px solid #ddd6fe; border-radius:999px; padding:2px 9px;">5 Authorised</a></div>
    </div>
  </div>
  <div style="background:#fff; border:1px solid #e5e7eb; border-top:3px solid #ea580c; border-radius:8px; padding:18px; display:flex; flex-direction:column; gap:8px;">
    <div style="font-size:.7em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#c2410c;">Scenario 4 · Market authorization</div>
    <a href="usecases-scenario-label-negotiation.html" style="font-weight:700; color:#111827; font-size:1.05em; text-decoration:none;">Label Negotiation with an Annotated ePI →</a>
    <p style="font-size:.84em; color:#4b5563; line-height:1.5; margin:0;">A Type II variation with two rounds of tracked changes on the label, then agreement.</p>
    <div style="display:grid; grid-template-columns:90px 1fr; gap:2px 10px; font-size:.8em; color:#374151;"><span style="color:#6b7280;">Starts it</span><span>Applicant; regulator for each labelling round</span><span style="color:#6b7280;">Task code</span><span><code>variation-type-ii</code></span></div>
    <div style="border-top:1px solid #f3f4f6; padding-top:8px; display:flex; flex-direction:column; gap:6px;">
      <div style="font-size:.68em; font-weight:700; text-transform:uppercase; letter-spacing:.08em; color:#6b7280;">Steps · each opens its Task</div>
      <div style="display:flex; flex-wrap:wrap; align-items:center; gap:6px;"><a href="Task-scenario4-01-variation-submitted.html" title="requested / submitted" style="font-size:.78em; text-decoration:none; color:#c2410c; border:1px solid #fed7aa; border-radius:999px; padding:2px 9px;">1 Submit</a><a href="Task-scenario4-02-variation-validated.html" title="accepted / validation-successful" style="font-size:.78em; text-decoration:none; color:#c2410c; border:1px solid #fed7aa; border-radius:999px; padding:2px 9px;">2 Validated</a><a href="Task-scenario4-03-variation-under-assessment.html" title="in-progress / under-assessment" style="font-size:.78em; text-decoration:none; color:#c2410c; border:1px solid #fed7aa; border-radius:999px; padding:2px 9px;">3 Assessment</a><a href="Task-scenario4-04-labelling-comments-round1.html" title="requested / labelling-comments-issued" style="font-size:.78em; text-decoration:none; color:#c2410c; border:1px solid #fed7aa; border-radius:999px; padding:2px 9px;">4 Comments R1</a><a href="Task-scenario4-05-labelling-comments-round1-response.html" title="completed / counter-proposal-received" style="font-size:.78em; text-decoration:none; color:#c2410c; border:1px solid #fed7aa; border-radius:999px; padding:2px 9px;">5 Counter-proposal</a><a href="Task-scenario4-06-labelling-comments-round2.html" title="requested / labelling-comments-issued" style="font-size:.78em; text-decoration:none; color:#c2410c; border:1px solid #fed7aa; border-radius:999px; padding:2px 9px;">6 Comments R2</a><a href="Task-scenario4-07-labelling-comments-round2-response.html" title="completed / response-received" style="font-size:.78em; text-decoration:none; color:#c2410c; border:1px solid #fed7aa; border-radius:999px; padding:2px 9px;">7 Response</a><a href="Task-scenario4-08-labelling-agreement.html" title="requested / awaiting-applicant-response" style="font-size:.78em; text-decoration:none; color:#c2410c; border:1px solid #fed7aa; border-radius:999px; padding:2px 9px;">8 Agreement requested</a><a href="Task-scenario4-09-labelling-agreed.html" title="completed / labelling-agreed" style="font-size:.78em; text-decoration:none; color:#c2410c; border:1px solid #fed7aa; border-radius:999px; padding:2px 9px;">9 Agreed</a><a href="Task-scenario4-10-variation-approved.html" title="completed / approved" style="font-size:.78em; text-decoration:none; color:#c2410c; border:1px solid #fed7aa; border-radius:999px; padding:2px 9px;">10 Approved</a></div>
    </div>
  </div>
</div>

### What each scenario shows

Looking for a specific pattern? Find the scenario that demonstrates it.

| Scenario | Validation outcome | Rejection and resubmission | Fee and payment | Questions as child Tasks | Response deadline | Several review rounds | Structured content (E2B, ePI) |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| [1. Stability update](usecases-scenario-stability.html) | ✓ |  | ✓ | ✓ |  |  |  |
| [2. ICSR](usecases-scenario-icsr.html) | ✓ | ✓ |  |  |  |  | ✓ |
| [3. Clinical trial application](usecases-scenario-cta.html) | ✓ |  |  | ✓ | ✓ |  |  |
| [4. Label negotiation](usecases-scenario-label-negotiation.html) | ✓ |  |  | ✓ | ✓ | ✓ | ✓ |
{:.grid}

### Ready to build?

- [Workflow](workflow.html): the four phases, and the [conventions](workflow.html#conventions) every scenario follows.
- [Notifications](subscriptions.html): subscribe to status changes.
- [Terminology](terminology.html): Task codes, business statuses, and input and output types.
- [Tracking and Dashboards](usecases-status-tracking.html): timelines and performance views built from Task history.
