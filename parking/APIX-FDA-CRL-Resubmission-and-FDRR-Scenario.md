# APIX Test Scenario: FDA Complete Response (Cycle 1 → Cycle 2) and Formal Dispute Resolution (FDRR)

> **Companion scenario.** This document extends the conventions established in `APIX-FDA-Shelf-Life-Update-Scenario.md` (same folder). All identity, versioning, parent/child, and `Binary → DocumentReference → Task` rules from that scenario apply unchanged here. This scenario is a **parking-lot design document** — the new task codes and business status values it proposes are *not yet* part of the IG CodeSystems.

## 1. Purpose

This test scenario demonstrates how APIX represents the FDA lifecycle in which an application is **not approved on the first review cycle**:

- Complete first-cycle review of an original NDA
- FDA issues a **Complete Response Letter (CRL)** ending Cycle 1 without approval
- Applicant escalates part of the CRL deficiencies through **Formal Dispute Resolution (FDRR appeal)**
- Applicant makes a **Class 2 resubmission** addressing the remaining deficiencies
- FDA conducts **second-cycle review** on a new 6-month clock and approves

It exists to close a known analytics gap: with this model, *review-cycle count* and *first-cycle approval rate* become directly computable from Task data (see Section 12).

### 1.1 Regulatory grounding (research summary)

The scenario is aligned with actual FDA process, which differs from a naive "rejection letter → appeal → second cycle" reading in one important way:

- **FDA does not issue a "rejection letter" at the end of a failed cycle.** Under **21 CFR 314.110**, when FDA determines an application cannot be approved in its present form, it issues a **Complete Response Letter** describing *all* identified deficiencies. The CRL ends the review cycle; the application is neither approved nor terminally denied.
- **After a CRL the applicant has three formal options:** (1) **resubmit**, addressing all deficiencies — a **Class 1** resubmission starts a new **2-month** review clock, a **Class 2** resubmission a new **6-month** clock; (2) **withdraw** the application without prejudice; (3) **request an opportunity for a hearing** (within 60 days) on whether grounds exist for denial. If the applicant takes no action within **one year**, FDA may deem the application withdrawn (30 days to respond to the withdrawal notification).
- **It is the resubmission — not the appeal — that starts second-cycle review.** An appeal is a separate track: a **Formal Dispute Resolution Request (FDRR)** escalates a scientific or procedural disagreement (including CRL deficiencies) above the review division, submitted as an amendment to the application. Under PDUFA, FDA's goal is to **respond within 30 days**. The FDR decision may be granted, granted in part, or denied; if granted it may lead to approval or to an agreed resubmission path, but the FDRR itself carries no review clock for the application.

This scenario therefore models the CRL, the FDRR, and the Class 2 resubmission as **three distinct Task lineages within one procedure** (one shared `groupIdentifier`).

References: 21 CFR 314.110 (ecfr.gov); FDA CDER Formal Dispute Resolution page; FDA Guidance *Formal Dispute Resolution: Sponsor Appeals Above the Division Level* (2017); CDER MAPP 6020.4 (resubmission classification).

---

## 2. Scenario Summary

The applicant submits an original NDA for a new product. Cycle 1 proceeds normally (technical validation, receipt, fee, filing, Day 74 communication, assessment, one Information Request). At the action date FDA concludes the application cannot be approved in its present form and issues a **CRL** citing two deficiencies: one **CMC** deficiency and one **labeling** deficiency.

The applicant disputes the labeling deficiency and files an **FDRR**. FDA responds within the 30-day PDUFA goal: the appeal is **granted in part** — the labeling deficiency is withdrawn; the CMC deficiency stands.

The applicant then makes a **Class 2 resubmission** addressing the CMC deficiency (new stability and process validation data). FDA classifies the resubmission as Class 2, sets a new 6-month goal date, conducts second-cycle review with no further Information Requests, and **approves** the application.

Result across the procedure: **two review cycles, one CRL, one FDRR (granted in part), approval in Cycle 2** — i.e., this procedure counts as *not* a first-cycle approval in performance analytics.

---

## 3. Regulatory Assumptions

| Item | Assumption |
|---|---|
| Regulator | US FDA (CDER model) |
| Product type | Human drug product |
| Application type | Original NDA (505(b)(1)), standard review designation |
| Application number | NDA 219876 (fictitious) |
| Procedure identifier (`Task.groupIdentifier`) | `NDA-219876` |
| Submission IDs | `0001` (Cycle 1 original submission), `0012` (Class 2 resubmission opening Cycle 2) |
| Cycle 1 outcome | Complete Response Letter (21 CFR 314.110) with two deficiencies (CMC + labeling) |
| Appeal | FDRR against the labeling deficiency; FDA responds within the 30-day PDUFA goal; **granted in part** (labeling deficiency withdrawn, CMC deficiency stands) |
| Resubmission class | Class 2 → new 6-month review clock |
| Cycle 2 outcome | Approved |
| Post-CRL options not exercised | Withdrawal; request for hearing; deemed withdrawal after 1 year of inaction (all out of scope, noted in Section 13) |
| IR format | RTQ-compliant XML |
| Labeling exchange format | HL7 FHIR ePI XML documents |
| APIX pattern | `Binary → DocumentReference → Task` |
| Cycle 1 Day 0 | 15 Jan 2026 |
| Cycle 1 filing decision | 16 Mar 2026 (~60 days) |
| Cycle 1 action (CRL issued) | 13 Nov 2026 (10-month standard clock) |
| FDRR submitted / decided | 15 Dec 2026 / 14 Jan 2027 (30-day goal met) |
| Class 2 resubmission | 15 Mar 2027 |
| Cycle 2 goal date / approval | 15 Sep 2027 / 10 Sep 2027 |

---

## 4. APIX Actors

Identical to the Shelf-Life Scenario (Applicant, FDA Intake/Gateway, FDA Regulatory Project Manager, FDA Finance, FDA Review Team, FDA Decision Authority, APIX Server), plus:

| Actor | APIX Role | Description |
|---|---|---|
| FDA Office-Level Deciding Official | `Task.owner` for the FDRR Task | Official above the review division who decides the formal dispute (per the FDR guidance, appeals are decided above the division level) |

---

## 5. Proposed New Codes (not yet in the IG)

### 5.1 `apix-task-code` additions

| Code | Display | Used by |
|---|---|---|
| `complete-response` | Complete Response Letter | Output classification of the Cycle 1 action; enables cycle counting |
| `resubmission` | Resubmission after Complete Response | Parent code for post-CRL resubmissions |
| `resubmission-class-1` | Class 1 Resubmission (2-month clock) | *is-a* child of `resubmission` |
| `resubmission-class-2` | Class 2 Resubmission (6-month clock) | *is-a* child of `resubmission`; used in this scenario |
| `formal-dispute-resolution` | Formal Dispute Resolution Request (Appeal) | The FDRR Task |

### 5.2 `apix-business-status` additions

| Code | Meaning |
|---|---|
| `complete-response-issued` | Review cycle ended without approval; CRL issued; awaiting applicant action |
| `appeal-submitted` | FDRR received by FDA |
| `appeal-under-review` | FDRR under review above the division level (30-day PDUFA clock) |
| `appeal-decision-issued` | FDR decision issued (granted / granted in part / denied — carried in `Task.output`) |
| `resubmission-classified` | Resubmission classified (Class 1 or 2) and new goal date set |

**Deliberate modeling choice:** the CRL closes the cycle with `status = completed` + `businessStatus = complete-response-issued` — **not** `status = rejected`. `rejected` remains reserved for terminal outcomes (e.g., technical validation failure of an attempt, or denial after a hearing). This matches FDA semantics — a "complete response" means *FDA's review of this cycle is complete*, not that the application is dead — and keeps the existing `statusreason-conditional-require` invariant meaningful.

---

## 6. Parent Task Model Across Cycles

The Shelf-Life Scenario established that a submission attempt that ends terminally is closed and never reopened, and that the successor is a **brand-new parent Task instance sharing the same `groupIdentifier`**. This scenario applies the same rule at the *review-cycle* level:

```text
Cycle 1 parent Task  (submit-nda, eCTD 0001)      → closed at CRL: completed / complete-response-issued
FDRR Task            (file-fdrr)                   → separate lineage, basedOn Cycle 1 parent
Cycle 2 parent Task  (resubmit-nda, eCTD 0012)     → new instance, same groupIdentifier, basedOn Cycle 1 parent
```

- Every Task in all three lineages carries `groupIdentifier = NDA-219876`.
- `basedOn` provides the ordered lineage: the FDRR and the Cycle 2 parent both point back to the Cycle 1 parent; the FDR decision DocumentReference is also attached as an `input` to the Cycle 2 parent so Cycle 2 reviewers see the adjudicated scope.
- **Cycle counting rule:** number of review cycles = number of parent submission Tasks that passed technical validation; equivalently, CRL count + 1 when the procedure ends in approval.

---

## 7. Minimum Sample Files

### 7.1 Cycle 1 (applicant) — as in the Shelf-Life Scenario pattern

```text
form-fda-356h-original-nda.pdf
annotated-proposed-label-epi.xml
clean-proposed-label-epi.xml
module-2-quality-overall-summary.pdf
module-3-cmc-package.pdf
submission-manifest.json
response-to-fda-ir-001-rtq.xml
```

### 7.2 Cycle 1 (FDA)

```text
fda-receipt-acknowledgement.pdf
fda-user-fee-invoice.pdf
fda-filing-acceptance-letter.pdf
fda-day-74-communication.pdf
fda-information-request-001-rtq.xml
fda-complete-response-letter.pdf          ← ends Cycle 1 (two deficiencies: CMC, labeling)
```

### 7.3 FDRR lineage

```text
fdrr-request-nda-219876.pdf               ← applicant; submitted as an amendment to the application
fda-fdrr-acknowledgement.pdf
fda-fdrr-decision-letter.pdf              ← granted in part: labeling deficiency withdrawn, CMC stands
```

### 7.4 Cycle 2

```text
resubmission-cover-content (Task.text)    ← no separate cover letter, per APIX convention
updated-module-3-process-validation.pdf
updated-stability-package.pdf
final-clean-label-epi.xml
final-annotated-label-epi.xml
submission-manifest-0012.json
fda-resubmission-classification-letter.pdf  ← Class 2, goal date 15 Sep 2027
fda-approval-letter.pdf
approved-clean-label-epi.xml
```

---

## 8. Task.status / businessStatus Map for This Scenario

| Phase | `Task.status` | `Task.businessStatus` |
|---|---|---|
| Cycle 1 submission → filing → assessment | as in Shelf-Life Scenario (`requested`→`received`→`accepted`→`in-progress`, with `on-hold` for the IR clock stop) | same values as Shelf-Life Scenario |
| Cycle 1 action | `completed` | `complete-response-issued` ★ |
| FDRR submitted | `requested` | `appeal-submitted` ★ |
| FDRR under review | `in-progress` | `appeal-under-review` ★ |
| FDRR decided | `completed` | `appeal-decision-issued` ★ |
| Cycle 2 resubmission received | `received` | `submission-received` |
| Resubmission classified (Class 2, new goal date) | `accepted` | `resubmission-classified` ★ |
| Cycle 2 assessment | `in-progress` | `assessment-underway` |
| Cycle 2 action | `completed` | `approved` |

★ = proposed new code (Section 5).

---

## 9. Full Dated Task Script (Implementer Lifecycle Table)

**Procedure identifier for all Tasks:** `NDA-219876`

### Task Instance Registry

| Task (logical label) | Instance uuid |
|---|---|
| `submit-nda` (Cycle 1 – Parent 1) | `9c1f4a77-3d2e-4b6a-9f41-52a8c07d9b13` |
| `acknowledge-receipt` (Cycle 1) | `5d2b8e91-4c07-4f3a-b6d8-9e1a2c4f7a55` |
| `screen-submission-for-filing` | `1a7e3c55-8b2d-49e0-a3c7-6f9d0e8b4c21` |
| `user-fee` (assess / invoice / confirm — pattern per Shelf-Life Steps 7–9b) | `d4c9a2b8-1e5f-4a7c-9b3d-8e6f2a1c5d90` |
| `issue-day-74-communication` | `7b3f9d21-6a4e-4c8b-a1f5-3d7e9c2b8f64` |
| `conduct-nda-assessment` (Cycle 1) | `2e8c5f7a-9b1d-4e6f-8a3c-5d9b7f2e4a18` |
| `respond-to-fda-ir-001` | `f6a1d8c3-2b7e-4f9a-b5d1-7c3e8a9f2b46` |
| `prepare-regulatory-action` (Cycle 1 → CRL) | `8d5b2f9e-7c1a-4d3b-9e6f-2a8c4b7d1e35` |
| `file-fdrr` (appeal) | `3f9e7a2c-5d8b-4a1f-b7e3-9c2d6f8a4b57` |
| `resubmit-nda` (Cycle 2 – Parent 2, Class 2) | `6b4d1e8f-3a9c-4b7d-8f2e-1c5a9d3b7e42` |
| `acknowledge-receipt` (Cycle 2) | `a2c8f5d1-7e3b-4c9a-b1d6-8f4e2a7c9d13` |
| `classify-resubmission` | `e9d3b7f2-1c6a-4e8d-a5b9-3f7c1d8e2a64` |
| `conduct-nda-assessment` (Cycle 2) | `4a8f2d6b-9e1c-4f7a-8b3d-6c2e9a5f1d78` |
| `prepare-regulatory-action` (Cycle 2 → approval) | `b7e1c9f4-3d8a-4b2e-9f6c-1a5d8e3b7f29` |

### Lifecycle Table

| Step | Date | Actor | Business Step | Task.id | Instance (uuid) | Task.version | basedOn | status / businessStatus | Input (summary) | Output (summary) |
|------|------|-------|---------------|---------|-----------------|--------------|---------|-------------------------|-----------------|------------------|
| **— Cycle 1 —** |
| 1 | 15 Jan 2026 | Applicant | Submit original NDA (eCTD `0001`) | `submit-nda` (Parent 1) | `9c1f4a77…` | 1 | — | `requested` / — | Form 356h, labels (ePI XML), Module 2/3, manifest | — |
| 2 | 15 Jan 2026 | FDA (auto) | Technical validation passes | `submit-nda` (Parent 1) | `9c1f4a77…` | 2 | — | `received` / `submission-received` | — | — |
| 3 | 15 Jan 2026 | FDA | Acknowledge receipt | `acknowledge-receipt` | `5d2b8e91…` | 1 | Parent 1 | `completed` / `receipt-acknowledged` | — | Receipt acknowledgement |
| 4 | 16 Jan 2026 | FDA | Begin filing review | `screen-submission-for-filing` | `1a7e3c55…` | 1 | Parent 1 | `received` / `filing-review-underway` | Submission DocumentReferences | — |
| 5 | 20 Jan – 05 Feb 2026 | FDA / Applicant | User fee assessed, invoiced, cleared (identical pattern to Shelf-Life Scenario Steps 7–9b, incl. proof-validation failure handling) | `user-fee` | `d4c9a2b8…` | — | Parent 1 | `completed` / `fee-cleared` | Proof of payment | Invoice; payment confirmation |
| 6 | 16 Mar 2026 | FDA | Filing decision — accepted for review; standard designation; goal date 15 Nov 2026 | `screen-submission-for-filing` | `1a7e3c55…` | 2 | Parent 1 | `completed` / `filed-accepted-for-review` | — | Filing acceptance letter |
| 7 | 16 Mar 2026 | FDA | Parent 1 accepted; `requestedPeriod` = 15 Jan – 15 Nov 2026 | `submit-nda` (Parent 1) | `9c1f4a77…` | 3 | — | `accepted` / `filed-accepted-for-review` | — | — |
| 8 | 30 Mar 2026 | FDA | Day 74 communication | `issue-day-74-communication` | `7b3f9d21…` | 1 | Parent 1 | `completed` / `day-74-communication-issued` | — | Day 74 communication |
| 9 | 31 Mar 2026 | FDA | Begin Cycle 1 assessment | `conduct-nda-assessment` (C1) | `2e8c5f7a…` | 1 | Parent 1 | `in-progress` / `assessment-underway` | Module 2/3, labels | — |
| 10 | 08 Jun 2026 | FDA | Issue IR 001 (RTQ XML); assessment on hold | `respond-to-fda-ir-001` / `conduct-nda-assessment` | `f6a1d8c3…` / `2e8c5f7a…` | 1 / 2 | assessment | `requested` / `information-request-issued`; `on-hold` / `awaiting-applicant-response` | — | FDA IR 001 (RTQ XML) |
| 11 | 29 Jun 2026 | Applicant | IR 001 response received; assessment resumes | `respond-to-fda-ir-001` / `conduct-nda-assessment` | `f6a1d8c3…` / `2e8c5f7a…` | 2 / 3 | assessment | `completed` / `response-received`; `in-progress` / `response-under-review` | — | RTQ XML response |
| 12 | 20 Oct 2026 | FDA | Cycle 1 assessment complete — deficiencies remain (CMC, labeling) | `conduct-nda-assessment` (C1) | `2e8c5f7a…` | 4 | Parent 1 | `completed` / `assessment-complete` | — | Review conclusion |
| 13 | 21 Oct 2026 | FDA | Prepare regulatory action | `prepare-regulatory-action` (C1) | `8d5b2f9e…` | 1 | assessment (C1) | `in-progress` / `decision-preparation-underway` | — | — |
| 14 | 13 Nov 2026 | FDA | **Issue Complete Response Letter** (2 deficiencies) | `prepare-regulatory-action` (C1) | `8d5b2f9e…` | 2 | assessment (C1) | `completed` / `complete-response-issued` | — | **CRL** (output typed `complete-response` ★) |
| 15 | 13 Nov 2026 | FDA | **Close Cycle 1 parent** — cycle ends without approval; applicant now has the 314.110 options (resubmit / withdraw / hearing; 1-year deemed-withdrawal clock starts) | `submit-nda` (Parent 1) | `9c1f4a77…` | 6 | — | `completed` / `complete-response-issued` | — | CRL DocumentReference |
| **— FDRR (appeal) lineage —** |
| 16 | 15 Dec 2026 | Applicant | **File FDRR** against the labeling deficiency (submitted as amendment to NDA 219876) | `file-fdrr` | `3f9e7a2c…` | 1 | Parent 1 | `requested` / `appeal-submitted` ★ | FDRR request document; CRL reference | — |
| 17 | 16 Dec 2026 | FDA | FDRR acknowledged; escalated above the division; 30-day PDUFA clock (`requestedPeriod` = 15 Dec 2026 – 14 Jan 2027) | `file-fdrr` | `3f9e7a2c…` | 2 | Parent 1 | `in-progress` / `appeal-under-review` ★ | — | FDRR acknowledgement |
| 18 | 14 Jan 2027 | FDA (Office-level official) | **FDR decision: granted in part** — labeling deficiency withdrawn; CMC deficiency stands | `file-fdrr` | `3f9e7a2c…` | 3 | Parent 1 | `completed` / `appeal-decision-issued` ★ | — | FDR decision letter |
| **— Cycle 2 —** |
| 19 | 15 Mar 2027 | Applicant | **Class 2 resubmission** (eCTD `0012`) addressing the CMC deficiency; `code = resubmission-class-2` ★ | `resubmit-nda` (Parent 2) | `6b4d1e8f…` | 1 | Parent 1 | `requested` / — | Updated Module 3, stability package, final labels (ePI XML), manifest, **FDR decision letter** | — |
| 20 | 15 Mar 2027 | FDA (auto) | Technical validation passes | `resubmit-nda` (Parent 2) | `6b4d1e8f…` | 2 | Parent 1 | `received` / `submission-received` | — | — |
| 21 | 16 Mar 2027 | FDA | Acknowledge receipt | `acknowledge-receipt` (C2) | `a2c8f5d1…` | 1 | Parent 2 | `completed` / `receipt-acknowledged` | — | Receipt acknowledgement |
| 22 | 29 Mar 2027 | FDA | **Resubmission classified Class 2**; new 6-month goal date 15 Sep 2027; Parent 2 `requestedPeriod` = 15 Mar – 15 Sep 2027 | `classify-resubmission` / `resubmit-nda` | `e9d3b7f2…` / `6b4d1e8f…` | 1 / 3 | Parent 2 / — | `completed` / `resubmission-classified` ★; parent `accepted` / `resubmission-classified` ★ | — | Classification letter |
| 23 | 30 Mar 2027 | FDA | Begin Cycle 2 assessment (scope: CMC deficiency only, per FDR decision) | `conduct-nda-assessment` (C2) | `4a8f2d6b…` | 1 | Parent 2 | `in-progress` / `assessment-underway` | Resubmission package, FDR decision | — |
| 24 | 28 Jul 2027 | FDA | Cycle 2 assessment complete — no further IRs | `conduct-nda-assessment` (C2) | `4a8f2d6b…` | 2 | Parent 2 | `completed` / `assessment-complete` | — | Review conclusion |
| 25 | 29 Jul 2027 | FDA | Prepare regulatory action | `prepare-regulatory-action` (C2) | `b7e1c9f4…` | 1 | assessment (C2) | `in-progress` / `decision-preparation-underway` | Final labels (ePI XML) | — |
| 26 | 10 Sep 2027 | FDA | **Issue approval letter** (5 days ahead of goal date) | `prepare-regulatory-action` (C2) | `b7e1c9f4…` | 2 | assessment (C2) | `completed` / `approved` | — | Approval letter + approved clean label (ePI XML) |
| 27 | 10 Sep 2027 | FDA | Close Cycle 2 parent — procedure approved | `resubmit-nda` (Parent 2) | `6b4d1e8f…` | 5 | Parent 1 | `completed` / `approved` | — | Approval letter + approved label |

> **Note on parent versions:** Parent 1 versions 4–5 (the `on-hold` / `in-progress` transitions around IR 001) and Parent 2 version 4 (`in-progress` during Cycle 2 assessment) follow the same convention as the Shelf-Life Scenario Section 9 note and are reflected in the closing versions shown above.

---

## 10. Task Hierarchy (Parent / Child / Lineage Model)

```text
Task: submit-nda (Cycle 1 – PARENT 1)                 ← closed at CRL, never reopened
uuid: 9c1f4a77-3d2e-4b6a-9f41-52a8c07d9b13
status: completed
businessStatus: complete-response-issued ★
groupIdentifier: NDA-219876                             (eCTD submission ID 0001)
output: DocumentReference/fda-complete-response-letter
│
├── Task: acknowledge-receipt (C1)          — completed / receipt-acknowledged
├── Task: screen-submission-for-filing      — completed / filed-accepted-for-review
├── Task: user-fee (assess→invoice→confirm) — completed / fee-cleared
├── Task: issue-day-74-communication        — completed / day-74-communication-issued
├── Task: conduct-nda-assessment (C1)       — completed / assessment-complete
│   └── Task: respond-to-fda-ir-001         — completed / response-received
└── Task: prepare-regulatory-action (C1)    — completed / complete-response-issued ★
                                              output: CRL (typed complete-response ★)

Task: file-fdrr (APPEAL — separate lineage, no review clock)
uuid: 3f9e7a2c-5d8b-4a1f-b7e3-9c2d6f8a4b57
basedOn: submit-nda (Parent 1)
code: formal-dispute-resolution ★
requestedPeriod: 2026-12-15 → 2027-01-14                (30-day PDUFA response goal)
status: completed
businessStatus: appeal-decision-issued ★
output: DocumentReference/fda-fdrr-decision-letter      (granted in part)

Task: resubmit-nda (Cycle 2 – PARENT 2)               ← new instance, same procedure
uuid: 6b4d1e8f-3a9c-4b7d-8f2e-1c5a9d3b7e42
basedOn: submit-nda (Parent 1)                          (ordered lineage across cycles)
code: resubmission-class-2 ★
groupIdentifier: NDA-219876                             (eCTD submission ID 0012)
requestedPeriod: 2027-03-15 → 2027-09-15                (Class 2 = 6-month clock)
input: includes DocumentReference/fda-fdrr-decision-letter
status: completed
businessStatus: approved
│
├── Task: acknowledge-receipt (C2)          — completed / receipt-acknowledged
├── Task: classify-resubmission ★           — completed / resubmission-classified ★
├── Task: conduct-nda-assessment (C2)       — completed / assessment-complete
└── Task: prepare-regulatory-action (C2)    — completed / approved
                                              output: approval letter + approved ePI label
```

**Key rules (extending the Shelf-Life hierarchy rules)**

- A CRL **closes the cycle's parent Task** (`completed` / `complete-response-issued`) — it is never reopened. The next cycle is a brand-new parent instance (new uuid), same `groupIdentifier`, `basedOn` the prior cycle's parent.
- The **FDRR is its own lineage**, not a review cycle: it has the 30-day response clock in `requestedPeriod`, and its decision letter feeds Cycle 2 as an `input`.
- `status = rejected` is **not** used for the CRL. It remains reserved for terminal events (validation failure of an attempt; denial after hearing).

---

## 11. Parent / FDRR Task Lifecycles

```text
Parent 1 — submit-nda, instance 9c1f4a77… (Cycle 1)
2026-01-15  v1  requested    / —
2026-01-15  v2  received     / submission-received
2026-03-16  v3  accepted     / filed-accepted-for-review
2026-06-08  v4  on-hold      / awaiting-applicant-response   (IR 001 clock stop)
2026-06-29  v5  in-progress  / response-under-review
2026-11-13  v6  completed    / complete-response-issued ★    (CRL — cycle ends, application still alive)

FDRR — file-fdrr, instance 3f9e7a2c…
2026-12-15  v1  requested    / appeal-submitted ★
2026-12-16  v2  in-progress  / appeal-under-review ★         (30-day PDUFA goal)
2027-01-14  v3  completed    / appeal-decision-issued ★      (granted in part)

Parent 2 — resubmit-nda, instance 6b4d1e8f… (Cycle 2, Class 2)
2027-03-15  v1  requested    / —
2027-03-15  v2  received     / submission-received
2027-03-29  v3  accepted     / resubmission-classified ★     (goal date 15 Sep 2027)
2027-03-30  v4  in-progress  / assessment-underway
2027-09-10  v5  completed    / approved
```

---

## 12. Analytics Payoff — Cycle Metrics Become Computable

With this model, the performance metrics shown on the Use Cases page (Scenario Example 2B) derive mechanically from Task data:

| Metric | Derivation |
|---|---|
| Review cycle count | Parent submission Tasks passing validation per `groupIdentifier` (here: 2); equivalently CRL count + 1 |
| **First-cycle approval (yes/no)** | Procedure reaches `approved` with **zero** outputs typed `complete-response` in the group → here **no** |
| Time to approval (calendar) | Parent 1 `authoredOn` (15 Jan 2026) → Parent 2 `lastModified` at approval (10 Sep 2027) ≈ 20 months |
| FDA review time (clock) | Sum of each cycle's clock: Cycle 1 (15 Jan – 13 Nov 2026, minus the 21-day IR clock stop) + Cycle 2 (15 Mar – 10 Sep 2027) |
| Applicant "dark period" | CRL (13 Nov 2026) → resubmission (15 Mar 2027) — visible as the gap between Parent 1 closure and Parent 2 creation |
| FDRR 30-day goal adherence | `file-fdrr` `requestedPeriod.end` vs actual decision `lastModified` (met: 14 Jan 2027) |
| Class 1 vs Class 2 mix | Count of `resubmission-class-1` vs `resubmission-class-2` Tasks |

---

## 13. Out-of-Scope Paths (for future scenarios)

- **Withdrawal after CRL** — Parent 1 would instead be followed by an applicant withdrawal Task; procedure closes `cancelled` / `withdrawn` (statusReason required).
- **Request for hearing** (within 60 days) and denial after hearing — the only path where the procedure-level outcome is `rejected` (statusReason required).
- **Deemed withdrawal** — no applicant action within 1 year of the CRL; FDA notification, 30-day response window, then closure as withdrawn.
- **FDRR fully granted** — could lead directly to approval without a resubmission (Cycle 2 parent never created).
- **Escalation of a denied FDRR** to the next management level (the FDR guidance allows sequential appeals up the chain).

---

## 14. Developer Test Assertions

1. **Cycle separation:** Cycle 1 parent (`9c1f4a77…`) stops at version 6, `completed` / `complete-response-issued`, and is never updated again. Cycle 2 is a new instance (`6b4d1e8f…`) with the same `groupIdentifier` and `basedOn` → Parent 1.
2. **CRL is not a rejection:** no Task in the procedure ever has `status = rejected`; the `statusreason-conditional-require` invariant is never triggered.
3. **FDRR clock:** `file-fdrr.requestedPeriod` spans exactly 30 days; the decision version (`v3`) has `lastModified` ≤ `requestedPeriod.end`.
4. **FDRR is not a review cycle:** cycle count computed per Section 12 equals 2, not 3.
5. **Class 2 clock:** Parent 2 `requestedPeriod` spans 6 months from resubmission receipt; approval `lastModified` precedes the goal date.
6. **Decision traceability:** the FDR decision letter DocumentReference appears as `output` of `file-fdrr` **and** as `input` of Parent 2, and Cycle 2 assessment scope excludes the withdrawn labeling deficiency.
7. **First-cycle analytics:** a query for outputs typed `complete-response` within `groupIdentifier = NDA-219876` returns exactly one, so the procedure is excluded from the first-cycle approval numerator while a zero-CRL procedure (e.g., the Shelf-Life Scenario) is included.
8. **Pattern compliance:** every artifact (CRL, FDRR request, FDR decision, classification letter, approval letter, ePI labels) follows `Binary → DocumentReference → Task`; Tasks never reference `Binary` directly.

---

## 15. IG-Ready Scenario Statement

This scenario demonstrates how APIX represents an FDA procedure that is not approved on the first review cycle, aligned with 21 CFR 314.110 and FDA's formal dispute resolution process. Cycle 1 of an original NDA ends with a Complete Response Letter citing CMC and labeling deficiencies; the parent Task for the cycle is closed as `completed` / `complete-response-issued`, leaving the procedure open under its shared `groupIdentifier`. The applicant escalates the labeling deficiency through a Formal Dispute Resolution Request, modeled as a distinct Task lineage with the 30-day PDUFA response goal carried in `requestedPeriod`; the appeal is granted in part. The applicant then makes a Class 2 resubmission — a new parent Task instance carrying the 6-month review clock and the FDR decision as input — and FDA approves in Cycle 2. Review-cycle count, first-cycle approval status, clock-stop time, applicant response time, and appeal-goal adherence are all directly computable from the Task version history, closing the analytics gap identified for cross-cycle performance reporting.
