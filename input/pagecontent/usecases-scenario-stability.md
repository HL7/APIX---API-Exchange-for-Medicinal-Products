<!-- EXAMPLE SCENARIO 1: STABILITY UPDATE (TYPE IB VARIATION) -->
<div style="margin-bottom:28px;">
  <a href="usecases.html" style="font-size:.7em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#1d4ed8; text-decoration:none;">Use Cases › Scenario 1 of 4 · Market authorization</a>
  <p style="font-size:.95em; color:#6b7280; line-height:1.6; max-width:760px;">SynthPharma AG submits a Type IB variation to update the product's stability data and the shelf-life statement in the labelling. The regulator validates the submission, invoices the fee, asks one round of questions about the stability data, receives the answers with an updated stability annex, and approves the change.</p>
</div>

<div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(170px,1fr)); gap:10px; margin-bottom:28px; font-size:.82em;">
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:6px; padding:10px 12px;"><div style="color:#6b7280; font-size:.85em;">Starts it</div><div style="font-weight:600; color:#111827;">Applicant</div></div>
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:6px; padding:10px 12px;"><div style="color:#6b7280; font-size:.85em;">Parent Task code</div><div style="font-weight:600; color:#111827;"><code>variation-type-ib</code></div></div>
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:6px; padding:10px 12px;"><div style="color:#6b7280; font-size:.85em;">Duration</div><div style="font-weight:600; color:#111827;">15 Nov → 22 Dec 2025</div></div>
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:6px; padding:10px 12px;"><div style="color:#6b7280; font-size:.85em;">Ends with</div><div style="font-weight:600; color:#111827;">Approval letter + assessment report</div></div>
</div>

### Steps

<ol style="list-style:none; margin:0 0 14px; padding:0; display:flex; flex-wrap:wrap; gap:8px;">
  <li style="flex:1 1 150px; margin:0;"><a href="Task-scenario1-01-initial-submission.html" style="height:100%; box-sizing:border-box; display:flex; flex-direction:column; gap:2px; text-decoration:none; color:#111827; border:1px solid #bfdbfe; background:#eff6ff; border-radius:8px; padding:8px 12px;"><span style="font-size:.72em; color:#4b5563;">Step 1</span><span style="font-weight:700; font-size:.9em;">Submit</span><code style="font-size:.72em; background:none; padding:0; color:#374151;">requested / submitted</code></a></li>
  <li style="flex:1 1 150px; margin:0;"><a href="Task-scenario1-02-validation.html" style="height:100%; box-sizing:border-box; display:flex; flex-direction:column; gap:2px; text-decoration:none; color:#111827; border:1px solid #bfdbfe; background:#eff6ff; border-radius:8px; padding:8px 12px;"><span style="font-size:.72em; color:#4b5563;">Step 2</span><span style="font-weight:700; font-size:.9em;">Validated</span><code style="font-size:.72em; background:none; padding:0; color:#374151;">accepted / validation-successful</code></a></li>
  <li style="flex:1 1 150px; margin:0;"><a href="Task-scenario1-03-finance-invoice.html" style="height:100%; box-sizing:border-box; display:flex; flex-direction:column; gap:2px; text-decoration:none; color:#111827; border:1px solid #bfdbfe; background:#eff6ff; border-radius:8px; padding:8px 12px;"><span style="font-size:.72em; color:#4b5563;">Step 3</span><span style="font-weight:700; font-size:.9em;">Invoice</span><code style="font-size:.72em; background:none; padding:0; color:#374151;">requested</code></a></li>
  <li style="flex:1 1 150px; margin:0;"><a href="Task-scenario1-04-finance-payment.html" style="height:100%; box-sizing:border-box; display:flex; flex-direction:column; gap:2px; text-decoration:none; color:#111827; border:1px solid #86efac; background:#f0fdf4; border-radius:8px; padding:8px 12px;"><span style="font-size:.72em; color:#4b5563;">Step 4</span><span style="font-weight:700; font-size:.9em;">Payment</span><code style="font-size:.72em; background:none; padding:0; color:#374151;">completed / payment-received</code></a></li>
  <li style="flex:1 1 150px; margin:0;"><a href="Task-scenario1-05-technical-question.html" style="height:100%; box-sizing:border-box; display:flex; flex-direction:column; gap:2px; text-decoration:none; color:#111827; border:1px solid #bfdbfe; background:#eff6ff; border-radius:8px; padding:8px 12px;"><span style="font-size:.72em; color:#4b5563;">Step 5</span><span style="font-weight:700; font-size:.9em;">Question</span><code style="font-size:.72em; background:none; padding:0; color:#374151;">requested / clock-stop</code></a></li>
  <li style="flex:1 1 150px; margin:0;"><a href="Task-scenario1-06-technical-response.html" style="height:100%; box-sizing:border-box; display:flex; flex-direction:column; gap:2px; text-decoration:none; color:#111827; border:1px solid #86efac; background:#f0fdf4; border-radius:8px; padding:8px 12px;"><span style="font-size:.72em; color:#4b5563;">Step 6</span><span style="font-weight:700; font-size:.9em;">Response</span><code style="font-size:.72em; background:none; padding:0; color:#374151;">completed / clock-restart</code></a></li>
  <li style="flex:1 1 150px; margin:0;"><a href="Task-scenario1-07-final-decision.html" style="height:100%; box-sizing:border-box; display:flex; flex-direction:column; gap:2px; text-decoration:none; color:#111827; border:1px solid #86efac; background:#f0fdf4; border-radius:8px; padding:8px 12px;"><span style="font-size:.72em; color:#4b5563;">Step 7</span><span style="font-weight:700; font-size:.9em;">Approved</span><code style="font-size:.72em; background:none; padding:0; color:#374151;">completed / approved</code></a></li>
</ol>

| Step | Example instance | Version | Created / updated by | `status` / `businessStatus` | Documents |
|---|---|---|---|---|---|
| 1. Submit | [scenario1-01-initial-submission](Task-scenario1-01-initial-submission.html) | 1 | Applicant (requester) → Regulator (owner) | `requested` / `submitted` | **Inputs:** cover letter, application form, annotated and clean draft labelling, mock-ups, 3.2.P.8.1 stability summary, 3.2.P.8.3 stability data, 3.2.S.7 drug-substance stability |
| 2. Validate | [scenario1-02-validation](Task-scenario1-02-validation.html) | 2 | Regulator | `accepted` / `validation-successful` | **Outputs:** acknowledgement of receipt, validation report |
| 3. Invoice | [scenario1-03-finance-invoice](Task-scenario1-03-finance-invoice.html) | 1 (new `request-payment` Task, `basedOn` the submission) | Regulator (requester) → Applicant (owner) | `requested` | **Input:** invoice |
| 4. Pay | [scenario1-04-finance-payment](Task-scenario1-04-finance-payment.html) | 2 | Applicant | `completed` / `payment-received` | **Output:** proof of payment |
| 5. Ask | [scenario1-05-technical-question](Task-scenario1-05-technical-question.html) | 1 (new `information-request` Task, `basedOn` the submission) | Regulator (requester) → Applicant (owner) | `requested` / `clock-stop` | **Input:** list of questions |
| 6. Answer | [scenario1-06-technical-response](Task-scenario1-06-technical-response.html) | 2 | Applicant | `completed` / `clock-restart` | **Outputs:** questionnaire response, updated stability data annex |
| 7. Decide | [scenario1-07-final-decision](Task-scenario1-07-final-decision.html) | 3 | Regulator | `completed` / `approved` | **Outputs:** acknowledgement, validation report, approval letter, assessment report |
{:.grid}

<div style="background:#eff6ff; border:1px solid #bfdbfe; border-radius:10px; padding:14px 18px; margin:4px 0 20px; font-size:.86em; color:#1e3a8a; line-height:1.6;">
  <div style="font-weight:700; margin-bottom:4px;">ℹ️ Task versions keep the same <code>Task.id</code></div>
  <p style="margin:0 0 6px;">When a Task is versioned (a new <code>meta.versionId</code>), every version must have the same <code>Task.id</code>. A Task that is not a new version of an existing Task, such as a resubmission or a child Task, is a different Task and must have a different <code>Task.id</code>.</p>
  <p style="margin:0;">In this IG, each version is published as a separate example instance so that it can be viewed on its own. In production, those instances are versions of one Task with one <code>Task.id</code>.</p>
</div>

**Timeline:** submitted 15 Nov 2025 → validated 20 Nov → paid 22 Nov → questions 1 Dec → answered 5 Dec → approved 22 Dec 2025.

### What it demonstrates

- **The full parent/child pattern.** One parent submission Task, with payment and question Tasks linked to it through `basedOn`.
- **A clock stop.** A regulator-owned question opens the clock stop, and the applicant's response closes it.
- **CTD-sectioned inputs.** Inputs carry `ctd-section` codes, so routing rules can read which modules a question touches (see [Notes](#notes)).

### Notes

- Link every child Task (invoice, question) to the submission with `basedOn` and give it the same `groupIdentifier`.
- The parent shows `clock-stop` while a question is open and `clock-restart` when it is answered.
- **Route questions on receipt.** The question Task’s type, product and document types (with CTD sections where the documents have them) tell the applicant’s or sponsor’s system which team (CMC, labelling, clinical, safety) should answer, and the due date comes from the Task.
- **Route responses on receipt.** The response is matched to the question through the Task’s identifiers and goes straight to the reviewer who asked (`Task.requester`), and the clock restarts.
- Codes: [Terminology › Market Authorization](terminology.html#market-authorization).

<div style="display:flex; justify-content:space-between; gap:12px; flex-wrap:wrap; font-size:.85em; margin-top:24px;">
  <a href="usecases.html" style="color:#2563eb; font-weight:600; text-decoration:none;">← Use Cases overview</a>
  <a href="usecases-scenario-icsr.html" style="color:#2563eb; font-weight:600; text-decoration:none;">Scenario 2: ICSR →</a>
</div>
