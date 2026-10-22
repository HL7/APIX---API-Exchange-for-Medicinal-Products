<!-- EXAMPLE SCENARIO 3: CLINICAL TRIAL APPLICATION -->
<div style="margin-bottom:28px;">
  <a href="usecases-scenarios.html" style="font-size:.7em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#7c3aed; text-decoration:none;">Example scenario 3 of 4</a>
  <h2 style="font-size:1.7em; font-weight:800; color:#111827; margin:6px 0 10px;">Clinical Trial Application</h2>
  <p style="font-size:.95em; color:#6b7280; line-height:1.6; max-width:760px;">SynthPharma AG, as sponsor, applies to run study <strong>WD-201</strong>. The regulator validates the application and assigns trial number <strong>CT-2026-000789</strong>. During assessment it sends a request for information with three questions and a two-week deadline. The sponsor answers within the deadline, the clock restarts, and the trial is authorised.</p>
</div>

<div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(170px,1fr)); gap:10px; margin-bottom:28px; font-size:.82em;">
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:6px; padding:10px 12px;"><div style="color:#6b7280; font-size:.85em;">Use case</div><div style="font-weight:600; color:#111827;"><a href="usecases-universal-submissions.html">Universal Submissions</a></div></div>
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:6px; padding:10px 12px;"><div style="color:#6b7280; font-size:.85em;">Parent Task code</div><div style="font-weight:600; color:#111827;"><code>clinical-trial-application</code></div></div>
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:6px; padding:10px 12px;"><div style="color:#6b7280; font-size:.85em;">Duration</div><div style="font-weight:600; color:#111827;">1 Sep → 3 Nov 2026</div></div>
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:6px; padding:10px 12px;"><div style="color:#6b7280; font-size:.85em;">Ends with</div><div style="font-weight:600; color:#111827;">Authorisation decision</div></div>
</div>

### Steps

| Step | Example instance | Version | `status` / `businessStatus` | Documents |
|---|---|---|---|---|
| 1. Submit | [scenario3-01-cta-submission](Task-scenario3-01-cta-submission.html) | 1 | `requested` / `submitted` | **Inputs:** cover letter, application form, protocol WD-201 v1.0 |
| 2. Validate | [scenario3-02-cta-validated](Task-scenario3-02-cta-validated.html) | 2 | `accepted` / `validation-successful` | **Output:** validation report. **Adds identifier:** trial number `CT-2026-000789` |
| 3. Ask | [scenario3-03-cta-rfi](Task-scenario3-03-cta-rfi.html) | 1 (new Task, `basedOn` the application) | `requested` / `request-for-information-issued` | **Input:** request for information. `requestedPeriod` ends 15 Oct 2026 |
| 4. Answer | [scenario3-04-cta-rfi-response](Task-scenario3-04-cta-rfi-response.html) | 2 | `completed` / `clock-restart` | **Output:** response to questions |
| 5. Authorise | [scenario3-05-cta-authorised](Task-scenario3-05-cta-authorised.html) | 3 | `completed` / `authorised` | **Outputs:** validation report, authorisation decision |
{:.grid}

**Timeline:** submitted 1 Sep 2026 → validated 12 Sep → RFI 1 Oct (due 15 Oct) → answered 12 Oct → authorised 3 Nov 2026.

### What it demonstrates

- **Not limited to marketing authorisations.** Clinical trials use the same Task, DocumentReference and Subscription resources.
- **Both parties' identifiers on one Task.** The regulator's trial number is added to `Task.identifier` when it is assigned.
- **Deadlines systems can act on.** `requestedPeriod` carries the response deadline, so systems can flag overdue responses automatically.
- **Requester and owner swap on the RFI Task.** The regulator asks (input), and the sponsor answers (output).

<div style="display:flex; justify-content:space-between; gap:12px; flex-wrap:wrap; font-size:.85em; margin-top:24px;">
  <a href="usecases-scenario-icsr.html" style="color:#2563eb; font-weight:600; text-decoration:none;">← Scenario 2: ICSR</a>
  <a href="usecases-scenario-label-negotiation.html" style="color:#2563eb; font-weight:600; text-decoration:none;">Scenario 4: Label Negotiation →</a>
</div>
