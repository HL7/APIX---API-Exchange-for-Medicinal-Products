<!-- EXAMPLE SCENARIO 2: ICSR INITIAL AND FOLLOW-UP REPORT -->
<div style="margin-bottom:28px;">
  <a href="usecases-scenarios.html" style="font-size:.7em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#dc2626; text-decoration:none;">Example scenario 2 of 4</a>
  <h2 style="font-size:1.7em; font-weight:800; color:#111827; margin:6px 0 10px;">ICSR: Initial and Follow-up Report</h2>
  <p style="font-size:.95em; color:#6b7280; line-height:1.6; max-width:760px;">SynthPharma AG reports a case of nausea with <strong>WonderDrug 50 mg</strong> (case <code>CH-SYNTHPHARMA-2026-000456</code>). The ICH E2B(R3) message goes to the regulator as an initial ICSR and is acknowledged within 15 minutes. A week later the company sends a follow-up for the same case: the drug was withdrawn and the reaction resolved (positive dechallenge). The follow-up is also acknowledged.</p>
</div>

<div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(170px,1fr)); gap:10px; margin-bottom:28px; font-size:.82em;">
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:6px; padding:10px 12px;"><div style="color:#6b7280; font-size:.85em;">Use case</div><div style="font-weight:600; color:#111827;"><a href="usecases-universal-submissions.html">Universal Submissions</a></div></div>
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:6px; padding:10px 12px;"><div style="color:#6b7280; font-size:.85em;">Task codes</div><div style="font-weight:600; color:#111827;"><code>icsr-initial</code> → <code>icsr-follow-up</code></div></div>
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:6px; padding:10px 12px;"><div style="color:#6b7280; font-size:.85em;">Duration</div><div style="font-weight:600; color:#111827;">2 → 9 Oct 2026</div></div>
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:6px; padding:10px 12px;"><div style="color:#6b7280; font-size:.85em;">Ends with</div><div style="font-weight:600; color:#111827;">E2B(R3) acknowledgment (AA / CA)</div></div>
</div>

### Steps

| Step | Example instance | Version | `status` / `businessStatus` | Documents |
|---|---|---|---|---|
| 1. Initial report | [scenario2-01-icsr-initial](Task-scenario2-01-icsr-initial.html) | 1 | `requested` / `submitted` | **Input:** initial ICSR (`icsr-initial.xml`, E2B(R3)) |
| 2. Acknowledged | [scenario2-02-icsr-initial-acknowledged](Task-scenario2-02-icsr-initial-acknowledged.html) | 2 | `completed` / `icsr-accepted` (AA / CA) | **Output:** E2B(R3) acknowledgment |
| 3. Follow-up report | [scenario2-03-icsr-follow-up](Task-scenario2-03-icsr-follow-up.html) | 1 (new Task, `basedOn` the initial Task) | `requested` / `submitted` | **Input:** follow-up ICSR |
| 4. Acknowledged | [scenario2-04-icsr-follow-up-acknowledged](Task-scenario2-04-icsr-follow-up-acknowledged.html) | 2 | `completed` / `icsr-accepted` (AA / CA) | **Output:** E2B(R3) acknowledgment |
{:.grid}

**Timeline:** initial report 2 Oct 2026 09:30 → acknowledged 09:45 → follow-up 9 Oct 10:15 → acknowledged 10:30.

### What it demonstrates

- **One channel for safety reporting.** Safety reports use the same channel as every other regulatory exchange. No separate safety gateway is needed.
- **The E2B(R3) message is unchanged.** It is carried as a Binary. The Task only describes the exchange around it.
- **The full case history in one search.** Follow-ups for a case share the initial report's `groupIdentifier` and point to it through `basedOn`.
- **Measured acknowledgment time.** `executionPeriod` records how long the regulator took to acknowledge, which feeds the performance charts on the [Submission Tracking and Notifications](usecases-status-tracking.html#scenario-examples) page.

### Notes

- The nausea case is one of the reports behind the safety signal that starts [Scenario 4](usecases-scenario-label-negotiation.html), so safety reporting and labelling are shown on the same product and the same channel.
- The codes used are listed on the [Terminology](terminology.html) page.

<div style="display:flex; justify-content:space-between; gap:12px; flex-wrap:wrap; font-size:.85em; margin-top:24px;">
  <a href="usecases-scenario-stability.html" style="color:#2563eb; font-weight:600; text-decoration:none;">← Scenario 1: Stability Update</a>
  <a href="usecases-scenario-cta.html" style="color:#2563eb; font-weight:600; text-decoration:none;">Scenario 3: Clinical Trial Application →</a>
</div>
