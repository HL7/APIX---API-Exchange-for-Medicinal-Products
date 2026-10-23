# RWI-pharma Example Scenarios

> **Status:** Working document in `parking/`. Not part of the IG build.
>
> **Purpose:** Describe, in one place, the four worked example scenarios behind the IG's example instances.

## Contents

- [Shared conventions](#shared-conventions)
- [Scenario overview](#scenario-overview)
- [Scenario 1 — Stability Update (Type IB Variation)](#scenario-1--stability-update-type-ib-variation)
- [Scenario 2 — ICSR: Accepted, and Rejected then Resubmitted](#scenario-2--icsr-accepted-and-rejected-then-resubmitted)
- [Scenario 3 — Clinical Trial Application (CTA)](#scenario-3--clinical-trial-application-cta)
- [Scenario 4 — Label Negotiation with an Annotated ePI](#scenario-4--label-negotiation-with-an-annotated-epi)
- [Open questions](#open-questions)

---

## Shared conventions

All four scenarios follow the same pattern. Only the Task type and its documents change.

| Convention | How it works |
|---|---|
| **Binary → DocumentReference → Task** | Each file is uploaded as a `Binary`, described by a `DocumentReference`, and attached to a `Task` through `Task.input` or `Task.output`. |
| **Inputs from the requester, outputs from the owner** | The party that creates the Task supplies `Task.input`. The party that does the work returns `Task.output`. |
| **One procedure, one `groupIdentifier`** | Every Task in a procedure (submission, invoice, questions, decision) carries the same `groupIdentifier`. |
| **Child Tasks point to the parent** | Questions, payments and follow-ups use `Task.basedOn` to reference the parent submission Task. |
| **Progress is a new Task version** | Status changes update the same Task, creating a new `meta.versionId`. In the IG the versions are shown as separate example instances (e.g. `-01` and `-02`), but in production they are versions of one Task. |
| **Two status layers** | `Task.status` is the FHIR workflow state (`requested`, `accepted`, `completed`…). `Task.businessStatus` is the regulatory milestone (`submitted`, `clock-stop`, `approved`…). |
| **Parties** | All examples use the fictional applicant **SynthPharma AG** (`org-synthpharma-ag`) and the fictional regulator **Health Authority – Regulatory Review Division** (`org-ema-srm-hmed`). |

---

## Scenario overview

| # | Scenario | Who starts it | Parent Task code | Rounds of Q&A | Ends with | Status |
|---|---|---|---|---|---|---|
| 1 | Stability update | Applicant | `variation-type-ib` | 1 information request | Approval letter + assessment report | In IG |
| 2 | ICSR | Marketing authorization holder | `icsr` | None (2b: 1 rejection and resubmission) | E2B(R2) acknowledgment log + `complete` | In IG |
| 3 | Clinical trial application | Sponsor | `clinical-trial-application` | 1 request for information | Authorisation decision | In IG |
| 4 | Label negotiation | Applicant (variation); regulator (labelling rounds) | `variation-type-ii` + `labelling-comments` / `labelling-agreement` child Tasks | 2 labelling rounds + agreement | Approval letter + approved ePI | In IG |

---

## Scenario 1 — Stability Update (Type IB Variation)

**Source:** `input/fsh/workflowExamples/scenario1-*.fsh` (hand-written).
**Extended FDA version:** `parking/APIX-FDA-Shelf-Life-Update-Scenario.md` (24 → 36 month shelf life, NDA 214365 S-021, with validation failure, two IR cycles and fee handling).

### Story

SynthPharma AG submits a Type IB variation to update the product's stability data and the shelf-life statement in the labelling. The regulator validates the submission, invoices the fee, asks one round of questions about the stability data, receives the answers with an updated stability annex, and approves the change.

### Steps

| Step | Example instance | Created / updated by | `status` / `businessStatus` | Documents |
|---|---|---|---|---|
| 1. Submit | `scenario1-01-initial-submission` | Applicant (requester) → Regulator (owner) | `requested` / `submitted` | **Inputs:** cover letter, application form, annotated and clean draft labelling, mock-ups, 3.2.P.8.1 stability summary, 3.2.P.8.3 stability data, 3.2.S.7 drug-substance stability |
| 2. Validate | `scenario1-02-validation` | Regulator updates the parent | `accepted` / `validation-successful` | **Outputs:** acknowledgement of receipt, validation report |
| 3. Invoice | `scenario1-03-finance-invoice` | Regulator → Applicant (`request-payment`, `basedOn` parent) | `requested` | **Input:** invoice |
| 4. Pay | `scenario1-04-finance-payment` | Applicant updates the invoice Task | `completed` / `payment-received` | **Output:** proof of payment |
| 5. Ask | `scenario1-05-technical-question` | Regulator → Applicant (`information-request`, `basedOn` parent) | `requested` / `clock-stop` | **Input:** list of questions |
| 6. Answer | `scenario1-06-technical-response` | Applicant completes the question Task | `completed` | **Outputs:** questionnaire response, updated stability data annex |
| 7. Decide | `scenario1-07-final-decision` | Regulator completes the parent | `completed` / `approved` | **Outputs:** acknowledgement, validation report, approval letter, assessment report |

**Timeline:** submitted 15 Nov 2025 → validated 20 Nov → paid 22 Nov → questions 1 Dec → answered 5 Dec → approved 22 Dec 2025.

### What it demonstrates

- The full parent/child pattern: one parent submission Task, with payment and question Tasks hanging off it through `basedOn`.
- A clock stop opened by a regulator-owned question and closed by the applicant's response.
- CTD-sectioned inputs (`ctd-section` codes) so routing rules can read which modules a question touches.

### Fixes applied (19 Oct 2026)

- `scenario1-06-technical-response`: `businessStatus` changed from `clock-stop` to `clock-restart` once the response is complete, matching Scenario 3.
- `scenario1-06-technical-response`: removed the duplicate `output[=].type` line (`regulatory-document`), so the stability data annex is typed `3.2.P.8.3` only.
- Removed the stray quote from the code `applicant-questionnaireResponse`, both in `CodeSystem-ctd-section.fsh` and in the two places `scenario1-06` uses it.

Scenario 1 is still hand-written, so it differs from Scenarios 2–4 in conventions: it uses `ctd-section` codes for inputs and outputs and has no `meta.versionId`.

---

## Scenario 2 — ICSR: Accepted, and Rejected then Resubmitted

**Source:** `input/fsh/workflowExamples/scenario2-icsr.fsh` and `input/fsh/exampleBinaries/scenario2-icsr-binaries.fsh`, generated by `parking/gen_examples.py`. Edit the script, not the FSH.

### Story

SynthPharma AG sends two ICSRs for **WonderDrug 50 mg** as ICH E2B(R2) messages, one report per Task. **2a:** a nausea case (`CH-SYNTHPHARMA-2026-000456`) is accepted and completed. **2b:** a dizziness case (`CH-SYNTHPHARMA-2026-000512`) leaves out the MedDRA version (B.2.i.1a), is rejected with an acknowledgment log and validation report, and is accepted and completed after the company resubmits a corrected message on a new Task.

### Steps

| Step | Example instance | Version | `status` / `businessStatus` | Documents |
|---|---|---|---|---|
| 2a.1 Submit | `scenario2a-01-icsr-submitted` | 1 | `requested` / `submitted` | **Input:** `icsr-e2b-r2` |
| 2a.2 Accepted | `scenario2a-02-icsr-accepted` | 2 | `accepted` / `accepted` | **Output:** `icsr-e2b-r2-acklog` (01 / 01) |
| 2a.3 Complete | `scenario2a-03-icsr-complete` | 3 | `completed` / `complete` | — |
| 2b.1 Submit | `scenario2b-01-icsr-submitted` | 1 | `requested` / `submitted` | **Input:** `icsr-e2b-r2` (MedDRA version missing) |
| 2b.2 Rejected | `scenario2b-02-icsr-rejected` | 2 | `rejected` / `rejected` + `statusReason` | **Outputs:** `icsr-e2b-r2-acklog` (02 / 02), `validation-report` |
| 2b.3 Resubmit | `scenario2b-03-icsr-resubmitted` | 1 (new Task, `basedOn` 2b.1) | `requested` / `submitted` | **Input:** corrected `icsr-e2b-r2` |
| 2b.4 Accepted | `scenario2b-04-icsr-accepted` | 2 | `accepted` / `accepted` | **Output:** `icsr-e2b-r2-acklog` (01 / 01) |
| 2b.5 Complete | `scenario2b-05-icsr-complete` | 3 | `completed` / `complete` | — |

**Timeline:** 2a — 2 Oct 2026 09:30 → 09:45 → 10:02. 2b — 14 Oct 2026 11:00 → rejected 11:12 → resubmitted 15:40 → accepted 15:52 → complete 16:10.

### What it demonstrates

- Safety reporting uses the **same channel** as every other regulatory exchange.
- One report per Task (no batching), so each report has its own status and acknowledgment log.
- A rejected Task is final; the resubmission is a new Task with the same `groupIdentifier`, `basedOn` the rejected Task.
- `executionPeriod` records how long the regulator took to process each report.

---

## Scenario 3 — Clinical Trial Application (CTA)

**Source:** `input/fsh/workflowExamples/scenario3-cta.fsh` and `input/fsh/exampleBinaries/scenario3-cta-binaries.fsh`, generated by `parking/gen_examples.py`.

### Story

SynthPharma AG, as sponsor, applies to run study **WD-201**. The regulator validates the application and assigns trial number **CT-2026-000789**. During assessment it sends a request for information with three questions and a two-week deadline. The sponsor answers within the deadline, the clock restarts, and the trial is authorised.

### Steps

| Step | Example instance | Version | `status` / `businessStatus` | Documents |
|---|---|---|---|---|
| 1. Submit | `scenario3-01-cta-submission` | 1 | `requested` / `submitted` | **Inputs:** cover letter, application form, protocol WD-201 v1.0 |
| 2. Validate | `scenario3-02-cta-validated` | 2 | `accepted` / `validation-successful` | **Output:** validation report. **Adds identifier:** trial number `CT-2026-000789` |
| 3. Ask | `scenario3-03-cta-rfi` | 1 (new Task, `basedOn` the application) | `requested` / `request-for-information-issued` | **Input:** request for information. `requestedPeriod` ends 15 Oct 2026 |
| 4. Answer | `scenario3-04-cta-rfi-response` | 2 | `completed` / `clock-restart` | **Output:** response to questions |
| 5. Authorise | `scenario3-05-cta-authorised` | 3 | `completed` / `authorised` | **Outputs:** validation report, authorisation decision |

**Timeline:** submitted 1 Sep 2026 → validated 12 Sep → RFI 1 Oct (due 15 Oct) → answered 12 Oct → authorised 3 Nov 2026.

### What it demonstrates

- The pattern is not limited to marketing authorisations. Clinical trials use the same Task, DocumentReference and Subscription resources.
- The regulator's procedure number is added to `Task.identifier` when it is assigned, so both parties' identifiers live on one Task.
- `requestedPeriod` carries the response deadline, so systems can flag overdue responses automatically.
- Requester and owner swap on the RFI Task: the regulator asks (input), the sponsor answers (output).

---

## Scenario 4 — Label Negotiation with an Annotated ePI

**Source:** `input/fsh/workflowExamples/scenario4-label-negotiation.fsh` and `input/fsh/exampleBinaries/scenario4-label-negotiation-binaries.fsh`, generated by `parking/gen_examples.py`. Readable copies of the ePIs and PDFs are in `parking/example-source/` (`epi-*.xml`, `var-*.pdf`).

**Terminology:** uses the label-negotiation codes from the IG's Terminology page (Market Authorization). The codes the example needs were added to the IG's code systems:

| Code system | Codes added |
|---|---|
| `apix-task-code` | `variation-type-ii`, `labelling-comments`, `labelling-agreement` |
| `apix-business-status` | `labelling-comments-issued`, `counter-proposal-received`, `response-received`, `awaiting-applicant-response`, `labelling-agreed` |
| `apix-task-input-output-type` | `change-description`, `epi-bundle`, `proposed-labelling`, `labelling-comments`, `approved-labelling`, `approval-letter` |

### Story

Following a safety signal for nausea (the case from Scenario 2 is one of the reports behind it), SynthPharma AG submits a **Type II variation** (`VAR-II-2027-0012`) for **WonderDrug 50 mg film-coated tablets**. The variation adds nausea to SmPC section 4.8 and package leaflet section 4. The proposed product information is sent as a **FHIR ePI** in two forms: an **annotated** ePI that shows every change against the approved text, and a **clean** ePI.

The label text takes two rounds of comments to agree:

- **Round 1 – regulator comments.** The regulator returns the annotated ePI with its own tracked changes:
  - The frequency of nausea is raised from *uncommon* to *common*.
  - SmPC 4.2 and leaflet section 3 now say WonderDrug *"should be taken with food"*.
- **Round 1 – applicant response.** The applicant accepts the frequency change. It **counter-proposes** *"may be taken with food to reduce nausea"*, citing food-effect study WD-105, which shows no loss of exposure when the tablet is taken fasted.
- **Round 2 – regulator comments.** The regulator accepts the counter-proposal and changes the leaflet to plain language (*"feeling sick"*).
- **Round 2 – applicant response.** The applicant accepts all changes and returns the clean ePI.
- **Agreement.** The regulator asks the applicant to confirm the clean ePI as the final text, and the applicant confirms.
- **Decision.** The regulator approves the variation and returns the approval letter and the **approved ePI**.

### Design choices

| Choice | How it is modelled | Why |
|---|---|---|
| **One Task per round** | Each round is a new `labelling-comments` Task, created by the regulator, owned by the applicant, and `basedOn` the variation Task. | Mirrors the information requests in Scenarios 1 and 3. Each round has its own deadline (`requestedPeriod`) and timing (`executionPeriod`), and the number of rounds is the number of Tasks, which feeds the performance analytics directly. |
| **Separate agreement step** | A `labelling-agreement` Task, created by the regulator, asks the applicant to confirm the clean ePI. Completing it sets `labelling-agreed`. | The regulator decides when negotiation is over, and the applicant's confirmation is a timestamped event. Completing the Task is the confirmation, so no output document is needed. |
| **The ePI is the document, not a PDF** | Every proposal and counter-proposal is an ePI document `Bundle` (`Composition` + sections), stored as a Binary (`application/fhir+xml`) and described by a DocumentReference. | The label stays machine-readable throughout, and the agreed ePI can be published without re-keying. |
| **Annotated = tracked changes in the section narrative** | Changes are marked with XHTML `<ins>` and `<del>` in `Composition.section.text`. `class="rwi-mah"` or `class="rwi-ha"` shows who made the change, and `title` gives the reason. Changes are cumulative against the currently approved text. | `ins` and `del` are in the HTML subset that FHIR narrative allows, so any XHTML viewer can show the changes. The clean ePI has the same structure without markup. |
| **One document set per chain** | All annotated ePIs share one document set identifier, and all clean ePIs share another, whichever party authored the version. Each new version has `version` incremented and `relatesTo.code = replaces` pointing to the previous one. | Uses the `docsetid` / `docverid` pattern from Scenarios 2 and 3. Who changed what, and when, can be rebuilt from the DocumentReferences alone. |
| **Approved ePI reuses the agreed Binary** | The regulator's `approved-labelling` output is a regulator-authored DocumentReference that points to the **same Binary** as the applicant's clean ePI v5. | The approved text is provably the agreed text (same `attachment.hash`), and nothing is uploaded twice. |

### Steps

| Step | Example instance | Version | Created / updated by | `status` / `businessStatus` | Documents |
|---|---|---|---|---|---|
| 1. Submit variation | `scenario4-01-variation-submitted` | 1 | Applicant (requester) → Regulator (owner) | `requested` / `submitted` | **Inputs:** cover letter, application form, change description, `proposed-labelling` = annotated ePI v1, `epi-bundle` = clean ePI v1 |
| 2. Validate | `scenario4-02-variation-validated` | 2 | Regulator | `accepted` / `validation-successful` | **Output:** validation report. **Adds identifier:** procedure number `VAR-II-2027-0012` |
| 3. Assess | `scenario4-03-variation-under-assessment` | 3 | Regulator | `in-progress` / `under-assessment` | — |
| 4. Round 1 comments | `scenario4-04-labelling-comments-round1` | 1 (new Task, `basedOn` the variation) | Regulator (requester) → Applicant (owner) | `requested` / `labelling-comments-issued` | **Input:** `labelling-comments` = annotated ePI v2. Due 4 Mar 2027 |
| 5. Round 1 counter-proposal | `scenario4-05-labelling-comments-round1-response` | 2 | Applicant | `completed` / `counter-proposal-received` | **Outputs:** `proposed-labelling` = annotated ePI v3, `epi-bundle` = clean ePI v3 |
| 6. Round 2 comments | `scenario4-06-labelling-comments-round2` | 1 (new Task, `basedOn` the variation) | Regulator → Applicant | `requested` / `labelling-comments-issued` | **Input:** `labelling-comments` = annotated ePI v4. Due 18 Mar 2027 |
| 7. Round 2 acceptance | `scenario4-07-labelling-comments-round2-response` | 2 | Applicant | `completed` / `response-received` | **Output:** `epi-bundle` = clean ePI v5 |
| 8. Agreement requested | `scenario4-08-labelling-agreement` | 1 (new Task, `basedOn` the variation) | Regulator → Applicant | `requested` / `awaiting-applicant-response` | **Input:** `epi-bundle` = clean ePI v5 |
| 9. Labelling agreed | `scenario4-09-labelling-agreed` | 2 | Applicant | `completed` / `labelling-agreed` | — (completing the Task is the confirmation) |
| 10. Decide | `scenario4-10-variation-approved` | 4 | Regulator | `completed` / `approved` | **Outputs:** validation report, approval letter, `approved-labelling` = approved ePI (same Binary as clean v5) |

**Timeline:** submitted 11 Jan 2027 → validated 15 Jan → assessment 18 Jan → round 1 comments 22 Feb → counter-proposal 1 Mar → round 2 comments 8 Mar → accepted 10 Mar → agreed 11 Mar → approved 17 Mar 2027.

### Document chain

| ePI version | Form | Author | DocumentReference | Change summary |
|---|---|---|---|---|
| v1 | Annotated + clean | Applicant | `docref-epi-annotated-v1`, `docref-epi-clean-v1` | Adds nausea (*uncommon*) to SmPC 4.8 and leaflet section 4 |
| v2 | Annotated | Regulator | `docref-epi-annotated-v2` | Frequency → *common*; *"should be taken with food"* in SmPC 4.2 and leaflet section 3 |
| v3 | Annotated + clean | Applicant | `docref-epi-annotated-v3`, `docref-epi-clean-v3` | Accepts frequency; counter-proposes *"may be taken with food to reduce nausea"* |
| v4 | Annotated | Regulator | `docref-epi-annotated-v4` | Accepts counter-proposal; leaflet wording → *"feeling sick"* |
| v5 | Clean | Applicant | `docref-epi-clean-v5` | Agreed text, no markup (`Composition.status = final`) |
| Approved | Clean (same Binary as v5) | Regulator | `docref-epi-approved` | Approved product information |

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

> The ePI section and document-type codes use a placeholder code system (`http://example.org/epi-section`). Replace it with the section coding that the ePI IG in use requires.

### What it demonstrates

- **A true back-and-forth.** Both parties propose and counter-propose on the same machine-readable document, and every turn is timestamped.
- **No version confusion.** The version is recorded in the DocumentReference (`version`, `relatesTo`, document set identifier), not in file names.
- **The agreed label is ready to publish.** The approved output is an ePI Bundle.
- **Measurable negotiation.** The number of rounds, days per round, and applicant versus regulator time all come from the Task history.
- **Cross-scenario link.** The safety signal comes from the same product as Scenario 2, so safety reporting and labelling are shown running on one channel.

---

## Open questions

1. **Tracked-change markup.** Is XHTML `<ins>` / `<del>` in the section narrative acceptable to the ePI community, or should annotations be carried another way? Alternatives: a separate comments document, or an extension on `Composition.section`.
2. **Annotated and clean every round?** The example has the applicant return both in round 1 but only the clean ePI once it accepts everything. Should both always be required?
3. **Parent status during negotiation.** The variation Task stays `under-assessment` while labelling rounds are open, and the round Tasks carry the labelling statuses. Should the parent also show `clock-stop`?
4. **Superseded versions.** All ePI DocumentReferences stay `status = current` so that earlier Task versions still resolve. Should replaced versions become `superseded` once the next version is posted?
5. **Scenario 1 regeneration.** Should Scenario 1 be regenerated through `gen_examples.py`, so that all four scenarios share the same conventions (Task versions, `apix-task-input-output-type` codes, narratives)?
