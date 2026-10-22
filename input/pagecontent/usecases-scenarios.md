<!-- EXAMPLE SCENARIOS (index of the worked scenarios behind the IG's example instances) -->
<div style="margin-bottom:28px;">
  <a href="usecases.html" style="font-size:.7em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#2563eb; text-decoration:none;">Use Cases</a>
  <h2 style="font-size:1.7em; font-weight:800; color:#111827; margin:6px 0 10px;">Example Scenarios</h2>
  <p style="font-size:.95em; color:#6b7280; line-height:1.6; max-width:760px;">The use cases are backed by worked, end-to-end scenarios. All four are published in this IG as example Task, DocumentReference and Binary instances.</p>
</div>

<div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(230px,1fr)); gap:14px; margin-bottom:36px;">
  <a href="usecases-scenario-stability.html" style="text-decoration:none; background:#fff; border:1px solid #e5e7eb; border-top:3px solid #2563eb; border-radius:8px; padding:18px; display:block;">
    <div style="font-size:.7em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#2563eb; margin-bottom:6px;">Scenario 1 </div>
    <div style="font-weight:700; color:#111827; margin-bottom:6px;">Stability Update (Type IB Variation)</div>
    <p style="font-size:.82em; color:#6b7280; line-height:1.5; margin:0;">Submission, validation, fee, one round of questions and approval.</p>
  </a>
  <a href="usecases-scenario-icsr.html" style="text-decoration:none; background:#fff; border:1px solid #e5e7eb; border-top:3px solid #dc2626; border-radius:8px; padding:18px; display:block;">
    <div style="font-size:.7em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#dc2626; margin-bottom:6px;">Scenario 2 </div>
    <div style="font-weight:700; color:#111827; margin-bottom:6px;">ICSR: Initial and Follow-up Report</div>
    <p style="font-size:.82em; color:#6b7280; line-height:1.5; margin:0;">An E2B(R3) case report and its follow-up, on the same channel as every other exchange.</p>
  </a>
  <a href="usecases-scenario-cta.html" style="text-decoration:none; background:#fff; border:1px solid #e5e7eb; border-top:3px solid #7c3aed; border-radius:8px; padding:18px; display:block;">
    <div style="font-size:.7em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#7c3aed; margin-bottom:6px;">Scenario 3 </div>
    <div style="font-weight:700; color:#111827; margin-bottom:6px;">Clinical Trial Application</div>
    <p style="font-size:.82em; color:#6b7280; line-height:1.5; margin:0;">From application to authorisation, with a request for information and a deadline.</p>
  </a>
  <a href="usecases-scenario-label-negotiation.html" style="text-decoration:none; background:#fff; border:1px solid #e5e7eb; border-top:3px solid #ea580c; border-radius:8px; padding:18px; display:block;">
    <div style="font-size:.7em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#ea580c; margin-bottom:6px;">Scenario 4 </div>
    <div style="font-weight:700; color:#111827; margin-bottom:6px;">Label Negotiation with an Annotated ePI</div>
    <p style="font-size:.82em; color:#6b7280; line-height:1.5; margin:0;">Two rounds of tracked changes on a machine-readable label, then agreement.</p>
  </a>
</div>

### Scenario overview

| # | Scenario | Who starts it | Parent Task code | Rounds of Q&amp;A | Ends with | Status |
|---|---|---|---|---|---|---|
| 1 | [Stability update](usecases-scenario-stability.html) | Applicant | `variation-type-ib` | 1 information request | Approval letter + assessment report | Example instances in IG |
| 2 | [ICSR](usecases-scenario-icsr.html) | Marketing authorization holder | `icsr-initial` → `icsr-follow-up` | None | E2B(R3) acknowledgment (AA / CA) | Example instances in IG |
| 3 | [Clinical trial application](usecases-scenario-cta.html) | Sponsor | `clinical-trial-application` | 1 request for information | Authorisation decision | Example instances in IG |
| 4 | [Label negotiation](usecases-scenario-label-negotiation.html) | Applicant (variation); regulator (labelling rounds) | `variation-type-ii` + `labelling-comments` / `labelling-agreement` child Tasks | 2 labelling rounds + agreement | Approval letter + approved ePI | Example instances in IG |
{:.grid}

### Shared conventions {#shared-conventions}

All scenarios follow the same pattern. Only the Task type and its documents change.

| Convention | How it works |
|---|---|
| **Binary → DocumentReference → Task** | Each file is uploaded as a `Binary`, described by a `DocumentReference`, and attached to a `Task` through `Task.input` or `Task.output`. Tasks never point to a Binary directly. |
| **Inputs from the requester, outputs from the owner** | The party that creates the Task supplies `Task.input`. The party that does the work returns `Task.output`. |
| **One procedure, one `groupIdentifier`** | Every Task in a procedure (submission, invoice, questions, decision) carries the same `groupIdentifier`. |
| **Child Tasks point to the parent** | Questions, payments and follow-ups use `Task.basedOn` to reference the parent submission Task. |
| **Progress is a new Task version** | Status changes update the same Task, creating a new `meta.versionId`. In the IG the versions are shown as separate example instances (e.g. `-01` and `-02`), but in production they are versions of one Task. |
| **Terminal Tasks are never reopened** | A rejected or closed Task stays closed. A resubmission or a new review cycle is a new Task instance with the same `groupIdentifier`. |
| **Two status layers** | `Task.status` is the FHIR workflow state (`requested`, `accepted`, `completed`…). `Task.businessStatus` is the regulatory milestone (`submitted`, `clock-stop`, `approved`…). |
| **Parties** | All scenarios use the fictional applicant **SynthPharma AG** (`org-synthpharma-ag`) and the fictional regulator **Health Authority – Regulatory Review Division** (`org-ema-srm-hmed`). |
{:.grid}

### Open issues {#open-issues}

These questions are open for discussion by the project group.

1. **Tracked-change markup.** Is XHTML `<ins>` / `<del>` in the section narrative acceptable to the ePI community, or should annotations be carried another way? Alternatives: a separate comments document, or an extension on `Composition.section`. (Scenario 4)
2. **Annotated and clean every round?** Scenario 4 has the applicant return both in round 1 but only the clean ePI once it accepts everything. Should both always be required?
3. **Parent status during negotiation.** The variation Task stays `under-assessment` while labelling rounds are open, and the round Tasks carry the labelling statuses. Should the parent also show `clock-stop`?
4. **Superseded versions.** All ePI DocumentReferences stay `status = current` so that earlier Task versions still resolve. Should replaced versions become `superseded` once the next version is posted?
5. **Scenario 1 conventions.** Scenario 1 is hand-written and differs from Scenarios 2–4: it uses `ctd-section` codes for inputs and outputs and has no `meta.versionId`. Should it be aligned with the others?

<div style="display:flex; justify-content:space-between; gap:12px; flex-wrap:wrap; font-size:.85em; margin-top:24px;">
  <a href="usecases-automation.html" style="color:#2563eb; font-weight:600; text-decoration:none;">← Automation</a>
  <a href="usecases-scenario-stability.html" style="color:#2563eb; font-weight:600; text-decoration:none;">Scenario 1: Stability Update →</a>
</div>
