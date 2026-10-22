<!-- EXAMPLE SCENARIO 4: LABEL NEGOTIATION WITH AN ANNOTATED ePI -->
<div style="margin-bottom:28px;">
  <a href="usecases-scenarios.html" style="font-size:.7em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#ea580c; text-decoration:none;">Example scenario 4 of 4</a>
  <h2 style="font-size:1.7em; font-weight:800; color:#111827; margin:6px 0 10px;">Label Negotiation with an Annotated ePI</h2>
  <p style="font-size:.95em; color:#6b7280; line-height:1.6; max-width:760px;">Following a safety signal for nausea, SynthPharma AG submits a <strong>Type II variation</strong> (<code>VAR-II-2027-0012</code>) for <strong>WonderDrug 50 mg film-coated tablets</strong>. The variation adds nausea to SmPC section 4.8 and package leaflet section 4. The proposed product information is sent as a <strong>FHIR ePI</strong> in two forms: an <strong>annotated</strong> ePI that shows every change against the approved text, and a <strong>clean</strong> ePI. The label text takes two rounds of comments to agree.</p>
</div>

<div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(170px,1fr)); gap:10px; margin-bottom:28px; font-size:.82em;">
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:6px; padding:10px 12px;"><div style="color:#6b7280; font-size:.85em;">Use case</div><div style="font-weight:600; color:#111827;"><a href="usecases-universal-submissions.html">Universal Submissions</a></div></div>
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

### Design choices

| Choice | How it is modelled | Why |
|---|---|---|
| **One Task per round** | Each round is a new `labelling-comments` Task, created by the regulator, owned by the applicant, and `basedOn` the variation Task. | Mirrors the information requests in Scenarios 1 and 3. Each round has its own deadline (`requestedPeriod`) and timing (`executionPeriod`), and the number of rounds is the number of Tasks, which feeds the performance analytics directly. |
| **Separate agreement step** | A `labelling-agreement` Task, created by the regulator, asks the applicant to confirm the clean ePI. Completing it sets `labelling-agreed`. | The regulator decides when negotiation is over, and the applicant's confirmation is a timestamped event. Completing the Task is the confirmation, so no output document is needed. |
| **The ePI is the document, not a PDF** | Every proposal and counter-proposal is an ePI document `Bundle` (`Composition` + sections), stored as a Binary (`application/fhir+xml`) and described by a DocumentReference. | The label stays machine-readable throughout, and the agreed ePI can be published without re-keying. |
| **Annotated = tracked changes in the section narrative** | Changes are marked with XHTML `<ins>` and `<del>` in `Composition.section.text`. `class="rwi-mah"` or `class="rwi-ha"` shows who made the change, and `title` gives the reason. Changes are cumulative against the currently approved text. | `ins` and `del` are in the HTML subset that FHIR narrative allows, so any XHTML viewer can show the changes. The clean ePI has the same structure without markup. |
| **One document set per chain** | All annotated ePIs share one document set identifier, and all clean ePIs share another, whichever party authored the version. Each new version has `version` incremented and `relatesTo.code = replaces` pointing to the previous one. | Uses the `docsetid` / `docverid` pattern from Scenarios 2 and 3. Who changed what, and when, can be rebuilt from the DocumentReferences alone. |
| **Approved ePI reuses the agreed Binary** | The regulator's `approved-labelling` output is a regulator-authored DocumentReference that points to the **same Binary** as the applicant's clean ePI v5. | The approved text is provably the agreed text (same `attachment.hash`), and nothing is uploaded twice. |
{:.grid}

### Example: annotated ePI section (v3, SmPC 4.2)

```xml
<section>
  <title value="4.2 Posology and method of administration"/>
  <code><coding><system value="http://example.org/epi-section"/><code value="smpc-4.2"/></coding></code>
  <text><status value="additional"/><div xmlns="http://www.w3.org/1999/xhtml"><p>The recommended dose is one 50 mg tablet once daily.
    <del class="rwi-ha" title="HA round 1: advise intake with food to reduce nausea">The tablet can be taken with or without food.</del>
    <ins class="rwi-mah" title="Applicant counter-proposal: food-effect study WD-105 shows no loss of exposure when taken fasted">WonderDrug may be taken with food to reduce nausea.</ins></p></div></text>
</section>
```

<div style="background:#fffbeb; border:1px solid #fde68a; border-radius:8px; padding:12px 16px; font-size:.85em; color:#78350f; margin-bottom:24px;"><strong>Note:</strong> the ePI section and document-type codes use a placeholder code system (<code>http://example.org/epi-section</code>). Replace it with the section coding that the ePI IG in use requires.</div>

### What it demonstrates

- **A true back-and-forth.** Both parties propose and counter-propose on the same machine-readable document, and every turn is timestamped.
- **No version confusion.** The version is recorded in the DocumentReference (`version`, `relatesTo`, document set identifier), not in file names.
- **The agreed label is ready to publish.** The approved output is an ePI Bundle.
- **Measurable negotiation.** The number of rounds, days per round, and applicant versus regulator time all come from the Task history.
- **Cross-scenario link.** The safety signal comes from the same product as [Scenario 2](usecases-scenario-icsr.html), so safety reporting and labelling are shown running on one channel.

### Notes

- The label-negotiation codes are listed on the [Terminology](terminology.html) page (Market Authorization).
- Open questions about this scenario (tracked-change markup, annotated and clean every round, parent status, superseded versions) are listed under [Open issues](usecases-scenarios.html#open-issues).

<div style="display:flex; justify-content:space-between; gap:12px; flex-wrap:wrap; font-size:.85em; margin-top:24px;">
  <a href="usecases-scenario-cta.html" style="color:#2563eb; font-weight:600; text-decoration:none;">← Scenario 3: Clinical Trial Application</a>
  <a href="usecases-scenarios.html" style="color:#2563eb; font-weight:600; text-decoration:none;">Example Scenarios overview →</a>
</div>
