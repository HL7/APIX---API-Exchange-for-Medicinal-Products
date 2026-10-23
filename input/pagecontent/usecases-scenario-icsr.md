<!-- EXAMPLE SCENARIO 2: ICSR ACCEPTED, AND ICSR REJECTED AND RESUBMITTED -->
<div style="margin-bottom:28px;">
  <a href="usecases.html" style="font-size:.7em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#b91c1c; text-decoration:none;">Use Cases › Scenario 2 of 4 · Safety reporting</a>
  <h2 style="font-size:1.7em; font-weight:800; color:#111827; margin:6px 0 10px;">ICSR: Accepted, and Rejected then Resubmitted</h2>
  <p style="font-size:.95em; color:#6b7280; line-height:1.6; max-width:760px;">SynthPharma AG sends two ICSRs for <strong>WonderDrug 50 mg</strong> as ICH E2B(R2) messages, one report per Task. The first is accepted straight away (2a). The second fails validation, is rejected, and is accepted after the company corrects and resubmits it (2b).</p>
</div>

<div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(170px,1fr)); gap:10px; margin-bottom:28px; font-size:.82em;">
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:6px; padding:10px 12px;"><div style="color:#6b7280; font-size:.85em;">Starts it</div><div style="font-weight:600; color:#111827;">Marketing authorization holder</div></div>
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:6px; padding:10px 12px;"><div style="color:#6b7280; font-size:.85em;">Task code</div><div style="font-weight:600; color:#111827;"><code>icsr</code></div></div>
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:6px; padding:10px 12px;"><div style="color:#6b7280; font-size:.85em;">Input / output</div><div style="font-weight:600; color:#111827;"><code>icsr-e2b-r2</code> / <code>icsr-e2b-r2-acklog</code></div></div>
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:6px; padding:10px 12px;"><div style="color:#6b7280; font-size:.85em;">Business statuses</div><div style="font-weight:600; color:#111827;"><code>submitted</code> · <code>accepted</code> · <code>rejected</code> · <code>complete</code></div></div>
</div>

### 2a. Accepted {#scenario-2a}

SynthPharma AG reports a case of nausea (case `CH-SYNTHPHARMA-2026-000456`). The regulator validates and loads the report, returns the acknowledgment log, and closes the Task.

<ol style="list-style:none; margin:0 0 14px; padding:0; display:flex; flex-wrap:wrap; gap:8px;">
  <li style="flex:1 1 150px; margin:0;"><a href="Task-scenario2a-01-icsr-submitted.html" style="height:100%; box-sizing:border-box; display:flex; flex-direction:column; gap:2px; text-decoration:none; color:#111827; border:1px solid #bfdbfe; background:#eff6ff; border-radius:8px; padding:8px 12px;"><span style="font-size:.72em; color:#4b5563;">Step 1</span><span style="font-weight:700; font-size:.9em;">Submit</span><code style="font-size:.72em; background:none; padding:0; color:#374151;">requested / submitted</code></a></li>
  <li style="flex:1 1 150px; margin:0;"><a href="Task-scenario2a-02-icsr-accepted.html" style="height:100%; box-sizing:border-box; display:flex; flex-direction:column; gap:2px; text-decoration:none; color:#111827; border:1px solid #bfdbfe; background:#eff6ff; border-radius:8px; padding:8px 12px;"><span style="font-size:.72em; color:#4b5563;">Step 2</span><span style="font-weight:700; font-size:.9em;">Accepted</span><code style="font-size:.72em; background:none; padding:0; color:#374151;">accepted / accepted</code></a></li>
  <li style="flex:1 1 150px; margin:0;"><a href="Task-scenario2a-03-icsr-complete.html" style="height:100%; box-sizing:border-box; display:flex; flex-direction:column; gap:2px; text-decoration:none; color:#111827; border:1px solid #86efac; background:#f0fdf4; border-radius:8px; padding:8px 12px;"><span style="font-size:.72em; color:#4b5563;">Step 3</span><span style="font-weight:700; font-size:.9em;">Complete</span><code style="font-size:.72em; background:none; padding:0; color:#374151;">completed / complete</code></a></li>
</ol>

| Step | Example instance | Version | `status` / `businessStatus` | Documents |
|---|---|---|---|---|
| 1. Submit | [scenario2a-01-icsr-submitted](Task-scenario2a-01-icsr-submitted.html) | 1 | `requested` / `submitted` | **Input:** ICSR (`icsr-2a-e2b-r2.xml`, `icsr-e2b-r2`) |
| 2. Accepted | [scenario2a-02-icsr-accepted](Task-scenario2a-02-icsr-accepted.html) | 2 | `accepted` / `accepted` | **Output:** acknowledgment log (`icsr-e2b-r2-acklog`): transmission 01, report 01 (loaded) |
| 3. Complete | [scenario2a-03-icsr-complete](Task-scenario2a-03-icsr-complete.html) | 3 | `completed` / `complete` | No new documents |
{:.grid}

**Timeline:** submitted 2 Oct 2026 09:30 → accepted 09:45 → complete 10:02.

### 2b. Rejected, resubmitted and accepted {#scenario-2b}

SynthPharma AG reports a case of dizziness (case `CH-SYNTHPHARMA-2026-000512`). The message leaves out the MedDRA version for the reaction term (B.2.i.1a), so the report fails validation. The regulator rejects the Task and returns the acknowledgment log and a validation report. The company corrects the message and resubmits it on a new Task, which is accepted and completed.

<ol style="list-style:none; margin:0 0 14px; padding:0; display:flex; flex-wrap:wrap; gap:8px;">
  <li style="flex:1 1 150px; margin:0;"><a href="Task-scenario2b-01-icsr-submitted.html" style="height:100%; box-sizing:border-box; display:flex; flex-direction:column; gap:2px; text-decoration:none; color:#111827; border:1px solid #bfdbfe; background:#eff6ff; border-radius:8px; padding:8px 12px;"><span style="font-size:.72em; color:#4b5563;">Step 1</span><span style="font-weight:700; font-size:.9em;">Submit</span><code style="font-size:.72em; background:none; padding:0; color:#374151;">requested / submitted</code></a></li>
  <li style="flex:1 1 150px; margin:0;"><a href="Task-scenario2b-02-icsr-rejected.html" style="height:100%; box-sizing:border-box; display:flex; flex-direction:column; gap:2px; text-decoration:none; color:#111827; border:1px solid #fca5a5; background:#fef2f2; border-radius:8px; padding:8px 12px;"><span style="font-size:.72em; color:#4b5563;">Step 2</span><span style="font-weight:700; font-size:.9em;">Rejected</span><code style="font-size:.72em; background:none; padding:0; color:#374151;">rejected / rejected</code></a></li>
  <li style="flex:1 1 150px; margin:0;"><a href="Task-scenario2b-03-icsr-resubmitted.html" style="height:100%; box-sizing:border-box; display:flex; flex-direction:column; gap:2px; text-decoration:none; color:#111827; border:1px solid #bfdbfe; background:#eff6ff; border-radius:8px; padding:8px 12px;"><span style="font-size:.72em; color:#4b5563;">Step 3</span><span style="font-weight:700; font-size:.9em;">Resubmit</span><code style="font-size:.72em; background:none; padding:0; color:#374151;">requested / submitted</code></a></li>
  <li style="flex:1 1 150px; margin:0;"><a href="Task-scenario2b-04-icsr-accepted.html" style="height:100%; box-sizing:border-box; display:flex; flex-direction:column; gap:2px; text-decoration:none; color:#111827; border:1px solid #bfdbfe; background:#eff6ff; border-radius:8px; padding:8px 12px;"><span style="font-size:.72em; color:#4b5563;">Step 4</span><span style="font-weight:700; font-size:.9em;">Accepted</span><code style="font-size:.72em; background:none; padding:0; color:#374151;">accepted / accepted</code></a></li>
  <li style="flex:1 1 150px; margin:0;"><a href="Task-scenario2b-05-icsr-complete.html" style="height:100%; box-sizing:border-box; display:flex; flex-direction:column; gap:2px; text-decoration:none; color:#111827; border:1px solid #86efac; background:#f0fdf4; border-radius:8px; padding:8px 12px;"><span style="font-size:.72em; color:#4b5563;">Step 5</span><span style="font-weight:700; font-size:.9em;">Complete</span><code style="font-size:.72em; background:none; padding:0; color:#374151;">completed / complete</code></a></li>
</ol>

| Step | Example instance | Version | `status` / `businessStatus` | Documents |
|---|---|---|---|---|
| 1. Submit | [scenario2b-01-icsr-submitted](Task-scenario2b-01-icsr-submitted.html) | 1 | `requested` / `submitted` | **Input:** ICSR (`icsr-2b-e2b-r2.xml`, `icsr-e2b-r2`) |
| 2. Rejected | [scenario2b-02-icsr-rejected](Task-scenario2b-02-icsr-rejected.html) | 2 | `rejected` / `rejected`, with `statusReason` | **Outputs:** acknowledgment log (`icsr-e2b-r2-acklog`): transmission 02, report 02 (not loaded), with the error; validation report (`validation-report`) |
| 3. Resubmit | [scenario2b-03-icsr-resubmitted](Task-scenario2b-03-icsr-resubmitted.html) | 1 (new Task, `basedOn` the rejected Task) | `requested` / `submitted` | **Input:** corrected ICSR (`icsr-2b-resubmission-e2b-r2.xml`, `icsr-e2b-r2`) |
| 4. Accepted | [scenario2b-04-icsr-accepted](Task-scenario2b-04-icsr-accepted.html) | 2 | `accepted` / `accepted` | **Output:** acknowledgment log: transmission 01, report 01 (loaded) |
| 5. Complete | [scenario2b-05-icsr-complete](Task-scenario2b-05-icsr-complete.html) | 3 | `completed` / `complete` | No new documents |
{:.grid}

**Timeline:** submitted 14 Oct 2026 11:00 → rejected 11:12 → resubmitted 15:40 → accepted 15:52 → complete 16:10.

### What it demonstrates

- **One channel for safety reporting.** Safety reports use the same channel as every other regulatory exchange. No separate safety gateway is needed.
- **The E2B message is unchanged.** The E2B(R2) message and acknowledgment log are carried as Binaries. The Task only describes the exchange around them.
- **One report per Task.** Each ICSR or SUSAR is sent on its own rather than in a batch, so each report has its own status and acknowledgment log, and a rejection affects only that report.
- **Rejection is explicit.** A rejected Task has `status` = `rejected`, a `statusReason`, and the acknowledgment log and validation report as outputs, so the sender knows what to fix without a separate channel.
- **Resubmission keeps the history.** A rejected Task is final, so the resubmission is a new Task. It shares the `groupIdentifier` and points to the rejected Task through `basedOn`, so one search returns both attempts.
- **Measured response time.** `executionPeriod` records how long the regulator took to process each report, which feeds the performance charts on the [Tracking and Dashboards](usecases-status-tracking.html#scenario-examples) page.

### Notes

- The same pattern applies to SUSARs (Task code `susar`, input `susar-e2b-r2` or `susar-e2b-r3`) and to E2B(R3) messages (`icsr-e2b-r3`, `icsr-e2b-r3-acklog`).
- The sample E2B(R2) messages are fictional and abbreviated. They show only key data elements and have not been validated against the ICH DTDs.
- The nausea case in 2a is one of the reports behind the safety signal that starts [Scenario 4](usecases-scenario-label-negotiation.html), so safety reporting and labelling are shown on the same product and the same channel.

### Implementing this

- Send one ICSR or SUSAR per Task. Do not batch reports in one message.
- Set `Task.input.type` to the E2B version you send (`icsr-e2b-r2`, `icsr-e2b-r3`, …).
- On rejection, set `status` = `rejected` with a `statusReason`, and return the acknowledgment log and a validation report.
- Resubmit on a new Task with the same `groupIdentifier` and `basedOn` the rejected Task. Never reopen a rejected Task.
- Codes: [Terminology › ICSR](terminology.html#individual-case-safety-reports-icsr).

<div style="display:flex; justify-content:space-between; gap:12px; flex-wrap:wrap; font-size:.85em; margin-top:24px;">
  <a href="usecases-scenario-stability.html" style="color:#2563eb; font-weight:600; text-decoration:none;">← Scenario 1: Stability Update</a>
  <a href="usecases-scenario-cta.html" style="color:#2563eb; font-weight:600; text-decoration:none;">Scenario 3: Clinical Trial Application →</a>
</div>
