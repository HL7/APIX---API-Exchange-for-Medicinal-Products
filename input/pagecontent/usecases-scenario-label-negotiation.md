<!-- EXAMPLE SCENARIO 4: LABEL NEGOTIATION WITH AN ANNOTATED ePI -->
<div style="margin-bottom:28px;">
  <a href="usecases.html" style="font-size:.7em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#c2410c; text-decoration:none;">Use Cases › Scenario 4 of 4 · Market authorization</a>
  <p style="font-size:.95em; color:#6b7280; line-height:1.6; max-width:760px;">Following a safety signal for nausea, SynthPharma AG submits a <strong>Type II variation</strong> (<code>VAR-II-2027-0012</code>) for <strong>WonderDrug 50 mg film-coated tablets</strong>. The variation adds nausea to SmPC section 4.8 and package leaflet section 4. The proposed product information is sent as a <strong>FHIR ePI</strong> in two forms: an <strong>annotated</strong> ePI that shows every change against the approved text, and a <strong>clean</strong> ePI. The label text takes two rounds of comments to agree.</p>
</div>

<div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(170px,1fr)); gap:10px; margin-bottom:28px; font-size:.82em;">
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:6px; padding:10px 12px;"><div style="color:#6b7280; font-size:.85em;">Starts it</div><div style="font-weight:600; color:#111827;">Applicant; regulator for each labelling round</div></div>
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:6px; padding:10px 12px;"><div style="color:#6b7280; font-size:.85em;">Task codes</div><div style="font-weight:600; color:#111827;"><code>variation-type-ii</code>, <code>labelling-comments</code>, <code>labelling-agreement</code></div></div>
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:6px; padding:10px 12px;"><div style="color:#6b7280; font-size:.85em;">Duration</div><div style="font-weight:600; color:#111827;">11 Jan → 17 Mar 2027</div></div>
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:6px; padding:10px 12px;"><div style="color:#6b7280; font-size:.85em;">Ends with</div><div style="font-weight:600; color:#111827;">Approval letter + approved ePI</div></div>
</div>

### The negotiation

- **Round 1 – regulator comments.** The regulator returns the annotated ePI with its own tracked changes:
  - The frequency of nausea is raised from *uncommon* to *common*.
  - SmPC 4.2 and leaflet section 3 now say WonderDrug *"should be taken with food"*.
- **Round 1 – applicant response.** The applicant accepts the frequency change. It **counter-proposes** *"may be taken with food to reduce nausea"*, citing food-effect study WD-105, which shows no loss of exposure when the tablet is taken fasted.
- **Round 2 – regulator comments.** The regulator accepts the counter-proposal and changes the leaflet to plain language (*"feeling sick"*).
- **Round 2 – applicant response.** The applicant accepts all changes and returns the clean ePI.
- **Agreement.** The regulator asks the applicant to confirm the clean ePI as the final text, and the applicant confirms.
- **Decision.** The regulator approves the variation and returns the approval letter and the **approved ePI**.

### Steps

<ol style="list-style:none; margin:0 0 14px; padding:0; display:flex; flex-wrap:wrap; gap:8px;">
  <li style="flex:1 1 150px; margin:0;"><a href="Task-scenario4-01-variation-submitted.html" style="height:100%; box-sizing:border-box; display:flex; flex-direction:column; gap:2px; text-decoration:none; color:#111827; border:1px solid #bfdbfe; background:#eff6ff; border-radius:8px; padding:8px 12px;"><span style="font-size:.72em; color:#4b5563;">Step 1</span><span style="font-weight:700; font-size:.9em;">Submit</span><code style="font-size:.72em; background:none; padding:0; color:#374151;">requested / submitted</code></a></li>
  <li style="flex:1 1 150px; margin:0;"><a href="Task-scenario4-02-variation-validated.html" style="height:100%; box-sizing:border-box; display:flex; flex-direction:column; gap:2px; text-decoration:none; color:#111827; border:1px solid #bfdbfe; background:#eff6ff; border-radius:8px; padding:8px 12px;"><span style="font-size:.72em; color:#4b5563;">Step 2</span><span style="font-weight:700; font-size:.9em;">Validated</span><code style="font-size:.72em; background:none; padding:0; color:#374151;">accepted / validation-successful</code></a></li>
  <li style="flex:1 1 150px; margin:0;"><a href="Task-scenario4-03-variation-under-assessment.html" style="height:100%; box-sizing:border-box; display:flex; flex-direction:column; gap:2px; text-decoration:none; color:#111827; border:1px solid #bfdbfe; background:#eff6ff; border-radius:8px; padding:8px 12px;"><span style="font-size:.72em; color:#4b5563;">Step 3</span><span style="font-weight:700; font-size:.9em;">Assessment</span><code style="font-size:.72em; background:none; padding:0; color:#374151;">in-progress / under-assessment</code></a></li>
  <li style="flex:1 1 150px; margin:0;"><a href="Task-scenario4-04-labelling-comments-round1.html" style="height:100%; box-sizing:border-box; display:flex; flex-direction:column; gap:2px; text-decoration:none; color:#111827; border:1px solid #bfdbfe; background:#eff6ff; border-radius:8px; padding:8px 12px;"><span style="font-size:.72em; color:#4b5563;">Step 4</span><span style="font-weight:700; font-size:.9em;">Comments R1</span><code style="font-size:.72em; background:none; padding:0; color:#374151;">requested / labelling-comments-issued</code></a></li>
  <li style="flex:1 1 150px; margin:0;"><a href="Task-scenario4-05-labelling-comments-round1-response.html" style="height:100%; box-sizing:border-box; display:flex; flex-direction:column; gap:2px; text-decoration:none; color:#111827; border:1px solid #86efac; background:#f0fdf4; border-radius:8px; padding:8px 12px;"><span style="font-size:.72em; color:#4b5563;">Step 5</span><span style="font-weight:700; font-size:.9em;">Counter-proposal</span><code style="font-size:.72em; background:none; padding:0; color:#374151;">completed / counter-proposal-received</code></a></li>
  <li style="flex:1 1 150px; margin:0;"><a href="Task-scenario4-06-labelling-comments-round2.html" style="height:100%; box-sizing:border-box; display:flex; flex-direction:column; gap:2px; text-decoration:none; color:#111827; border:1px solid #bfdbfe; background:#eff6ff; border-radius:8px; padding:8px 12px;"><span style="font-size:.72em; color:#4b5563;">Step 6</span><span style="font-weight:700; font-size:.9em;">Comments R2</span><code style="font-size:.72em; background:none; padding:0; color:#374151;">requested / labelling-comments-issued</code></a></li>
  <li style="flex:1 1 150px; margin:0;"><a href="Task-scenario4-07-labelling-comments-round2-response.html" style="height:100%; box-sizing:border-box; display:flex; flex-direction:column; gap:2px; text-decoration:none; color:#111827; border:1px solid #86efac; background:#f0fdf4; border-radius:8px; padding:8px 12px;"><span style="font-size:.72em; color:#4b5563;">Step 7</span><span style="font-weight:700; font-size:.9em;">Response</span><code style="font-size:.72em; background:none; padding:0; color:#374151;">completed / response-received</code></a></li>
  <li style="flex:1 1 150px; margin:0;"><a href="Task-scenario4-08-labelling-agreement.html" style="height:100%; box-sizing:border-box; display:flex; flex-direction:column; gap:2px; text-decoration:none; color:#111827; border:1px solid #bfdbfe; background:#eff6ff; border-radius:8px; padding:8px 12px;"><span style="font-size:.72em; color:#4b5563;">Step 8</span><span style="font-weight:700; font-size:.9em;">Agreement requested</span><code style="font-size:.72em; background:none; padding:0; color:#374151;">requested / awaiting-applicant-response</code></a></li>
  <li style="flex:1 1 150px; margin:0;"><a href="Task-scenario4-09-labelling-agreed.html" style="height:100%; box-sizing:border-box; display:flex; flex-direction:column; gap:2px; text-decoration:none; color:#111827; border:1px solid #86efac; background:#f0fdf4; border-radius:8px; padding:8px 12px;"><span style="font-size:.72em; color:#4b5563;">Step 9</span><span style="font-weight:700; font-size:.9em;">Agreed</span><code style="font-size:.72em; background:none; padding:0; color:#374151;">completed / labelling-agreed</code></a></li>
  <li style="flex:1 1 150px; margin:0;"><a href="Task-scenario4-10-variation-approved.html" style="height:100%; box-sizing:border-box; display:flex; flex-direction:column; gap:2px; text-decoration:none; color:#111827; border:1px solid #86efac; background:#f0fdf4; border-radius:8px; padding:8px 12px;"><span style="font-size:.72em; color:#4b5563;">Step 10</span><span style="font-weight:700; font-size:.9em;">Approved</span><code style="font-size:.72em; background:none; padding:0; color:#374151;">completed / approved</code></a></li>
</ol>

| Step | Example instance | Version | Created / updated by | `status` / `businessStatus` | Documents |
|---|---|---|---|---|---|
| 1. Submit variation | [scenario4-01-variation-submitted](Task-scenario4-01-variation-submitted.html) | 1 | Applicant (requester) → Regulator (owner) | `requested` / `submitted` | **Inputs:** cover letter, application form, change description, `proposed-labelling` = annotated ePI v1, `epi-bundle` = clean ePI v1 |
| 2. Validate | [scenario4-02-variation-validated](Task-scenario4-02-variation-validated.html) | 2 | Regulator | `accepted` / `validation-successful` | **Output:** validation report. **Adds identifier:** procedure number `VAR-II-2027-0012` |
| 3. Assess | [scenario4-03-variation-under-assessment](Task-scenario4-03-variation-under-assessment.html) | 3 | Regulator | `in-progress` / `under-assessment` | — |
| 4. Round 1 comments | [scenario4-04-labelling-comments-round1](Task-scenario4-04-labelling-comments-round1.html) | 1 (new Task, `basedOn` the variation) | Regulator (requester) → Applicant (owner) | `requested` / `labelling-comments-issued` | **Input:** `labelling-comments` = annotated ePI v2. Due 4 Mar 2027 |
| 5. Round 1 counter-proposal | [scenario4-05-labelling-comments-round1-response](Task-scenario4-05-labelling-comments-round1-response.html) | 2 | Applicant | `completed` / `counter-proposal-received` | **Outputs:** `proposed-labelling` = annotated ePI v3, `epi-bundle` = clean ePI v3 |
| 6. Round 2 comments | [scenario4-06-labelling-comments-round2](Task-scenario4-06-labelling-comments-round2.html) | 1 (new Task, `basedOn` the variation) | Regulator → Applicant | `requested` / `labelling-comments-issued` | **Input:** `labelling-comments` = annotated ePI v4. Due 18 Mar 2027 |
| 7. Round 2 acceptance | [scenario4-07-labelling-comments-round2-response](Task-scenario4-07-labelling-comments-round2-response.html) | 2 | Applicant | `completed` / `response-received` | **Output:** `epi-bundle` = clean ePI v5 |
| 8. Agreement requested | [scenario4-08-labelling-agreement](Task-scenario4-08-labelling-agreement.html) | 1 (new Task, `basedOn` the variation) | Regulator → Applicant | `requested` / `awaiting-applicant-response` | **Input:** `epi-bundle` = clean ePI v5 |
| 9. Labelling agreed | [scenario4-09-labelling-agreed](Task-scenario4-09-labelling-agreed.html) | 2 | Applicant | `completed` / `labelling-agreed` | — (completing the Task is the confirmation) |
| 10. Decide | [scenario4-10-variation-approved](Task-scenario4-10-variation-approved.html) | 4 | Regulator | `completed` / `approved` | **Outputs:** validation report, approval letter, `approved-labelling` = approved ePI (same Binary as clean v5) |
{:.grid}

**Timeline:** submitted 11 Jan 2027 → validated 15 Jan → assessment 18 Jan → round 1 comments 22 Feb → counter-proposal 1 Mar → round 2 comments 8 Mar → accepted 10 Mar → agreed 11 Mar → approved 17 Mar 2027.

### Document chain

| ePI version | Form | Author | DocumentReference | Change summary |
|---|---|---|---|---|
| v1 | Annotated + clean | Applicant | [docref-epi-annotated-v1](DocumentReference-docref-epi-annotated-v1.html), [docref-epi-clean-v1](DocumentReference-docref-epi-clean-v1.html) | Adds nausea (*uncommon*) to SmPC 4.8 and leaflet section 4 |
| v2 | Annotated | Regulator | [docref-epi-annotated-v2](DocumentReference-docref-epi-annotated-v2.html) | Frequency → *common*; *"should be taken with food"* in SmPC 4.2 and leaflet section 3 |
| v3 | Annotated + clean | Applicant | [docref-epi-annotated-v3](DocumentReference-docref-epi-annotated-v3.html), [docref-epi-clean-v3](DocumentReference-docref-epi-clean-v3.html) | Accepts frequency; counter-proposes *"may be taken with food to reduce nausea"* |
| v4 | Annotated | Regulator | [docref-epi-annotated-v4](DocumentReference-docref-epi-annotated-v4.html) | Accepts counter-proposal; leaflet wording → *"feeling sick"* |
| v5 | Clean | Applicant | [docref-epi-clean-v5](DocumentReference-docref-epi-clean-v5.html) | Agreed text, no markup (`Composition.status = final`) |
| Approved | Clean (same Binary as v5) | Regulator | [docref-epi-approved](DocumentReference-docref-epi-approved.html) | Approved product information |
{:.grid}

### What it demonstrates

- **A true back-and-forth.** Both parties propose and counter-propose on the same machine-readable document, and every turn is timestamped.
- **No version confusion.** The version is recorded in the DocumentReference (`version`, `relatesTo`, document set identifier), not in file names.
- **The agreed label is ready to publish.** The approved output is an ePI Bundle.
- **Measurable negotiation.** The number of rounds, days per round, and applicant versus regulator time all come from the Task history.
- **Cross-scenario link.** The safety signal comes from the same product as [Scenario 2](usecases-scenario-icsr.html), so safety reporting and labelling are shown running on one channel.

### Notes

- Create one `labelling-comments` Task per round, `basedOn` the variation, each with its own `requestedPeriod`.
- Keep one document set identifier per chain (annotated, clean) and link each new version with `relatesTo.code` = `replaces`.
- Point the regulator’s `approved-labelling` DocumentReference at the same Binary as the agreed clean ePI.
- Codes: [Terminology › Market Authorization](terminology.html#market-authorization).

<div style="display:flex; justify-content:space-between; gap:12px; flex-wrap:wrap; font-size:.85em; margin-top:24px;">
  <a href="usecases-scenario-cta.html" style="color:#2563eb; font-weight:600; text-decoration:none;">← Scenario 3: Clinical Trial Application</a>
  <a href="usecases.html" style="color:#2563eb; font-weight:600; text-decoration:none;">Use Cases overview →</a>
</div>
