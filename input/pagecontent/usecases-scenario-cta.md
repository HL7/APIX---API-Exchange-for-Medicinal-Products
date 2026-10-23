<!-- EXAMPLE SCENARIO 3: CLINICAL TRIAL APPLICATION -->
<div style="margin-bottom:28px;">
  <a href="usecases.html" style="font-size:.7em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#6d28d9; text-decoration:none;">Use Cases › Scenario 3 of 4 · Clinical trials</a>
  <p style="font-size:.95em; color:#6b7280; line-height:1.6; max-width:760px;">SynthPharma AG, as sponsor, applies to run study <strong>WD-201</strong>. The regulator validates the application and assigns trial number <strong>CT-2026-000789</strong>. During assessment it sends a request for information with three questions and a two-week deadline. The sponsor answers within the deadline, the clock restarts, and the trial is authorised.</p>
</div>

<div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(170px,1fr)); gap:10px; margin-bottom:28px; font-size:.82em;">
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:6px; padding:10px 12px;"><div style="color:#6b7280; font-size:.85em;">Starts it</div><div style="font-weight:600; color:#111827;">Sponsor</div></div>
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:6px; padding:10px 12px;"><div style="color:#6b7280; font-size:.85em;">Parent Task code</div><div style="font-weight:600; color:#111827;"><code>clinical-trial-application</code></div></div>
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:6px; padding:10px 12px;"><div style="color:#6b7280; font-size:.85em;">Duration</div><div style="font-weight:600; color:#111827;">1 Sep → 3 Nov 2026</div></div>
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:6px; padding:10px 12px;"><div style="color:#6b7280; font-size:.85em;">Ends with</div><div style="font-weight:600; color:#111827;">Authorisation decision</div></div>
</div>

### Steps

<ol style="list-style:none; margin:0 0 14px; padding:0; display:flex; flex-wrap:wrap; gap:8px;">
  <li style="flex:1 1 150px; margin:0;"><a href="Task-scenario3-01-cta-submission.html" style="height:100%; box-sizing:border-box; display:flex; flex-direction:column; gap:2px; text-decoration:none; color:#111827; border:1px solid #bfdbfe; background:#eff6ff; border-radius:8px; padding:8px 12px;"><span style="font-size:.72em; color:#4b5563;">Step 1</span><span style="font-weight:700; font-size:.9em;">Submit</span><code style="font-size:.72em; background:none; padding:0; color:#374151;">requested / submitted</code></a></li>
  <li style="flex:1 1 150px; margin:0;"><a href="Task-scenario3-02-cta-validated.html" style="height:100%; box-sizing:border-box; display:flex; flex-direction:column; gap:2px; text-decoration:none; color:#111827; border:1px solid #bfdbfe; background:#eff6ff; border-radius:8px; padding:8px 12px;"><span style="font-size:.72em; color:#4b5563;">Step 2</span><span style="font-weight:700; font-size:.9em;">Validated</span><code style="font-size:.72em; background:none; padding:0; color:#374151;">accepted / validation-successful</code></a></li>
  <li style="flex:1 1 150px; margin:0;"><a href="Task-scenario3-03-cta-rfi.html" style="height:100%; box-sizing:border-box; display:flex; flex-direction:column; gap:2px; text-decoration:none; color:#111827; border:1px solid #bfdbfe; background:#eff6ff; border-radius:8px; padding:8px 12px;"><span style="font-size:.72em; color:#4b5563;">Step 3</span><span style="font-weight:700; font-size:.9em;">Request for information</span><code style="font-size:.72em; background:none; padding:0; color:#374151;">requested / request-for-information-issued</code></a></li>
  <li style="flex:1 1 150px; margin:0;"><a href="Task-scenario3-04-cta-rfi-response.html" style="height:100%; box-sizing:border-box; display:flex; flex-direction:column; gap:2px; text-decoration:none; color:#111827; border:1px solid #86efac; background:#f0fdf4; border-radius:8px; padding:8px 12px;"><span style="font-size:.72em; color:#4b5563;">Step 4</span><span style="font-weight:700; font-size:.9em;">Response</span><code style="font-size:.72em; background:none; padding:0; color:#374151;">completed / clock-restart</code></a></li>
  <li style="flex:1 1 150px; margin:0;"><a href="Task-scenario3-05-cta-authorised.html" style="height:100%; box-sizing:border-box; display:flex; flex-direction:column; gap:2px; text-decoration:none; color:#111827; border:1px solid #86efac; background:#f0fdf4; border-radius:8px; padding:8px 12px;"><span style="font-size:.72em; color:#4b5563;">Step 5</span><span style="font-weight:700; font-size:.9em;">Authorised</span><code style="font-size:.72em; background:none; padding:0; color:#374151;">completed / authorised</code></a></li>
</ol>

| Step | Example instance | Version | Created / updated by | `status` / `businessStatus` | Documents |
|---|---|---|---|---|---|
| 1. Submit | [scenario3-01-cta-submission](Task-scenario3-01-cta-submission.html) | 1 | Sponsor (requester) → Regulator (owner) | `requested` / `submitted` | **Inputs:** cover letter, application form, protocol WD-201 v1.0 |
| 2. Validate | [scenario3-02-cta-validated](Task-scenario3-02-cta-validated.html) | 2 | Regulator | `accepted` / `validation-successful` | **Output:** validation report. **Adds identifier:** trial number `CT-2026-000789` |
| 3. Ask | [scenario3-03-cta-rfi](Task-scenario3-03-cta-rfi.html) | 1 (new Task, `basedOn` the application) | Regulator (requester) → Sponsor (owner) | `requested` / `request-for-information-issued` | **Input:** request for information. `requestedPeriod` ends 15 Oct 2026 |
| 4. Answer | [scenario3-04-cta-rfi-response](Task-scenario3-04-cta-rfi-response.html) | 2 | Sponsor | `completed` / `clock-restart` | **Output:** response to questions |
| 5. Authorise | [scenario3-05-cta-authorised](Task-scenario3-05-cta-authorised.html) | 3 | Regulator | `completed` / `authorised` | **Outputs:** validation report, authorisation decision |
{:.grid}

<div style="background:#eff6ff; border:1px solid #bfdbfe; border-radius:10px; padding:14px 18px; margin:4px 0 20px; font-size:.86em; color:#1e3a8a; line-height:1.6;">
  <div style="font-weight:700; margin-bottom:4px;">ℹ️ Task versions keep the same <code>Task.id</code></div>
  <p style="margin:0 0 6px;">When a Task is versioned (a new <code>meta.versionId</code>), every version must have the same <code>Task.id</code>. A Task that is not a new version of an existing Task, such as a resubmission or a child Task, is a different Task and must have a different <code>Task.id</code>.</p>
  <p style="margin:0;">In this IG, each version is published as a separate example instance so that it can be viewed on its own. In production, those instances are versions of one Task with one <code>Task.id</code>.</p>
</div>

**Timeline:** submitted 1 Sep 2026 → validated 12 Sep → RFI 1 Oct (due 15 Oct) → answered 12 Oct → authorised 3 Nov 2026.

### What it demonstrates

- **Not limited to marketing authorisations.** Clinical trials use the same Task, DocumentReference and Subscription resources.
- **Both parties' identifiers on one Task.** The regulator's trial number is added to `Task.identifier` when it is assigned.
- **Deadlines systems can act on.** `requestedPeriod` carries the response deadline, so systems can flag overdue responses automatically.
- **Requester and owner swap on the RFI Task.** The regulator asks (input), and the sponsor answers (output).

### Notes

- Add the regulator’s trial number to `Task.identifier` when it is assigned, alongside the Task instance ID.
- Put the response deadline in `requestedPeriod.end` on the request-for-information Task, so both systems can flag overdue responses.
- **Route questions on receipt.** The question Task’s type, product and document types (with CTD sections where the documents have them) tell the applicant’s or sponsor’s system which team (CMC, labelling, clinical, safety) should answer, and the due date comes from the Task.
- **Route responses on receipt.** The response is matched to the question through the Task’s identifiers and goes straight to the reviewer who asked (`Task.requester`), and the clock restarts.
- Codes: [Terminology › Clinical Trials](terminology.html#clinical-trials).

<div style="display:flex; justify-content:space-between; gap:12px; flex-wrap:wrap; font-size:.85em; margin-top:24px;">
  <a href="usecases-scenario-icsr.html" style="color:#2563eb; font-weight:600; text-decoration:none;">← Scenario 2: ICSR</a>
  <a href="usecases-scenario-label-negotiation.html" style="color:#2563eb; font-weight:600; text-decoration:none;">Scenario 4: Label Negotiation →</a>
</div>
