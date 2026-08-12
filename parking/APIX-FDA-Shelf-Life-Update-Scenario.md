# APIX Test Scenario: FDA Shelf-Life Update from 24 Months to 36 Months

## 1. Purpose

This test scenario demonstrates how APIX can reproduce the end-to-end FDA regulatory process for a post-approval application to update the approved shelf life of a human drug product from **24 months to 36 months**.

The purpose is to prove that APIX can support the full bidirectional regulatory workflow between company and regulator, including:

- Initial application submission
- Technical / gateway validation (including a demonstrated terminal failure and corrected resubmission)
- Receipt acknowledgement (only after technical validation succeeds)
- User fee assessment, invoicing, and fee clearance (including proof-of-payment validation and re-issue)
- Administrative screening / filing review
- Filing determination (accepted for review or refuse-to-file)
- Day 74 communication
- FDA assessment
- Two sequential FDA Information Request cycles
- Applicant responses
- FDA review wrap-up
- FDA approval letter and approved labeling
- Final closure of the regulatory activity as approved

All exchanged content uses the agreed APIX pattern:

```text
Binary → DocumentReference → Task
```

The APIX server acts as a mailbox / exchange layer. The server receives and stores resources, supports notification of new or updated content, and allows client applications to retrieve and process the content. Processing of the business meaning of the content occurs in the client application, not in the APIX server itself.

---

## 2. Scenario Summary

The applicant submits an application to FDA requesting approval to update the product shelf life from **24 months to 36 months**.

The submission includes:

- Form FDA 356h
- Annotated drug label (FHIR ePI XML)
- Clean proposed drug label (FHIR ePI XML)
- CMC / Module 3 stability summary
- Supporting stability data table
- Submission manifest (machine-readable package index)

There is **no separate cover letter document**. The content that would normally appear in a cover letter is carried in the parent `Task.text`.

FDA receives the application via the exchange layer and performs automated technical validation. **The first submission fails technical validation and is terminally rejected**; the applicant submits a corrected package the same day as a new parent Task, which passes validation. FDA then acknowledges receipt, determines that a user fee is required, issues an invoice, confirms payment (with support for proof-of-payment validation failure and automatic re-issue of the payment Task while reusing the same invoice DocumentReference), performs filing review, accepts the application into substantive review, issues a Day 74 communication, conducts the assessment, issues two sequential Information Requests (RTQ-compliant XML), reviews the applicant responses (also RTQ-compliant XML), and ultimately approves the shelf-life update.

---

## 3. Regulatory Assumptions

| Item | Assumption |
|---|---|
| Regulator | US FDA (CDER/CBER model) |
| Product type | Human drug product |
| Application type | Post-approval NDA/BLA supplement (treated as Prior Approval Supplement equivalent for this scenario) |
| Application number | NDA 214365 (fictitious) |
| Procedure / supplement number | S-021 (fictitious Prior Approval Supplement) |
| Procedure identifier (`Task.groupIdentifier`) | `NDA-214365-S-021` |
| Submission IDs | `0045` (first attempt – fails validation), `0046` (resubmission – passes) |
| Change requested | Shelf-life extension from 24 months to 36 months |
| Supporting data | CMC / Module 3 stability data supporting 36-month shelf life |
| Labeling impact | Clean and annotated labeling updated to reflect 36-month shelf life, exchanged as FHIR ePI XML documents |
| Administrative content | Form FDA 356h and submission manifest |
| User fee | Required |
| Information requests | Two FDA IR cycles |
| IR / IR-response format | RTQ-compliant XML |
| Outcome | Approved |
| Cover letter | Not included as a separate document |
| Cover letter replacement | Parent `Task.text` |
| APIX pattern | `Binary → DocumentReference → Task` |
| Submission date / Day 0 | 03 Aug 2026 |
| Technical validation | Same day (automated); first submission fails (terminal), corrected resubmission passes the same day |
| Filing decision target | 02 Oct 2026 (~60 days) |
| Day 74 communication | 16 Oct 2026 |
| Final FDA action | 03 Jun 2027 |

---

## 4. APIX Actors

| Actor | APIX Role | Description |
|---|---|---|
| Applicant / Sponsor | `Task.requester` for the initial application and response tasks | Company regulatory team submitting the shelf-life update |
| FDA Intake / Gateway | Automated owner for receipt and technical validation | Receives and performs initial technical processing |
| FDA Regulatory Project Manager | `Task.owner` for filing and review coordination tasks | Coordinates filing review, assessment, IRs, and action preparation |
| FDA Finance / User Fee Function | `Task.owner` for fee-related tasks | Issues invoice and confirms fee clearance |
| FDA Review Team | `Task.owner` for assessment tasks | Reviews CMC, stability data, and labeling |
| FDA Decision Authority | `Task.owner` for regulatory action task | Issues final approval |
| APIX Server | Exchange layer / mailbox | Stores resources and supports retrieval and notification |

---

## 5. Core APIX Pattern

Every file exchanged in the scenario must follow this pattern:

```text
Binary
  ↓
DocumentReference
  ↓
Task.input or Task.output
```

Tasks must not point directly to raw file content. Every submitted, received, or issued artifact should be discoverable through a `DocumentReference`, which then points to the underlying `Binary`.

---

## 6. Parent Task Narrative

The parent Task represents the overall regulatory activity and remains open for the entire life of the procedure. It is only set to `completed` when FDA issues the final decision.

The `Task.text` carries the narrative content that would normally be included in a cover letter.

### Parent Task (initial state)

This is the **second (corrected) submission attempt** — the first attempt was terminally rejected at technical validation (see Section 9, Steps 1–2).

```text
Task.id: submit-shelf-life-update (attempt 2)
Task instance (resource id): urn:uuid:7f463290-c655-471c-966c-15f275f46535
Task.meta.versionId: 2
Task.status: received
Task.businessStatus: submission-received
Task.requester: Applicant
Task.owner: FDA
Task.authoredOn: 2026-08-03
Task.groupIdentifier: NDA-214365-S-021
```

### Task.text

```text
The applicant is submitting this application to request approval to update the approved shelf life of [Product Name] from 24 months to 36 months.

The proposed change is supported by updated CMC / Module 3 stability data demonstrating that the product remains within approved specifications through 36 months when stored under the approved storage conditions.

The application includes Form FDA 356h, annotated and clean proposed labeling as FHIR ePI XML documents, a Module 3 stability summary, supporting stability data tables, and a submission manifest.

The applicant requests FDA review and approval of the proposed shelf-life update and associated labeling revisions.
```

---

## 7. Minimum Sample Files

### 7.1 Applicant-Originated Files

```text
form-fda-356h-supplement.pdf
annotated-label-shelf-life-change-epi.xml
clean-label-proposed-36-month-shelf-life-epi.xml
module-3-stability-summary.pdf
stability-data-table-36-months.xlsx
submission-manifest.json
```

The annotated and clean labels are exchanged as **HL7 FHIR ePI documents (XML Bundles)**, not PDFs.

`submission-manifest.json` is the machine-readable index of the submission package — the APIX analogue of the eCTD backbone (`index.xml` / `us-regional.xml`). It declares the submission metadata (application number NDA 214365, supplement S-021, eCTD submission ID), lists every file in the package with its CTD section mapping and checksum, and is what the FDA gateway consumes during automated technical validation to verify completeness and integrity and to reconcile the declared contents against the DocumentReferences attached as `Task.input`.

### 7.2 FDA-Originated Files

```text
fda-technical-validation-failure-report.xml
fda-receipt-acknowledgement.pdf
fda-user-fee-invoice.pdf
fda-user-fee-payment-confirmation.pdf
fda-filing-acceptance-letter.pdf
fda-day-74-communication.pdf
fda-information-request-001-rtq.xml
fda-information-request-002-rtq.xml
fda-approval-letter.pdf
approved-clean-label-36-month-shelf-life-epi.xml
```

The Information Requests are **RTQ-compliant XML documents**. The technical validation failure report is the structured output attached to the terminally rejected first submission (Section 9, Step 2). The approved clean label is returned as a FHIR ePI XML document.

### 7.3 Applicant Response Files

```text
response-to-fda-ir-001-rtq.xml
updated-stability-summary-ir-001.pdf
response-to-fda-ir-002-rtq.xml
updated-stability-justification-ir-002.pdf
final-clean-label-36-month-shelf-life-epi.xml
final-annotated-label-36-month-shelf-life-epi.xml
```

The IR responses are **RTQ-compliant XML documents**; the final clean and annotated labels are FHIR ePI XML documents.

---

## 8. Recommended Business Status Values

| `Task.status` | `Task.businessStatus` | Meaning |
|---|---|---|
| `requested` | — | Company has created / is about to submit |
| `received` | `submission-received` | Gateway / technical receipt (after validation pass) |
| `rejected` | `validation-failed` | Technical validation failed (terminal for that attempt) |
| `completed` | `receipt-acknowledged` | Formal receipt acknowledgement issued |
| `received` | `filing-review-underway` | Administrative / filing review in progress |
| `accepted` | `filed-accepted-for-review` | Filing determination – accepted for substantive review |
| `in-progress` | `fee-assessment-underway` | User fee assessment |
| `completed` | `fee-invoice-issued` | Invoice issued |
| `completed` | `fee-cleared` | Payment confirmed |
| `rejected` | `validation-failed` | Proof-of-payment validation failed (terminal for that payment Task) |
| `completed` | `day-74-communication-issued` | Day 74 letter issued |
| `in-progress` | `assessment-underway` | Substantive CMC / labeling review |
| `requested` | `information-request-issued` | IR issued to applicant |
| `on-hold` | `awaiting-applicant-response` | Assessment paused pending IR response |
| `completed` | `response-received` | Applicant response received |
| `in-progress` | `response-under-review` | Review of IR response underway |
| `completed` | `assessment-complete` | Scientific assessment finished |
| `in-progress` | `decision-preparation-underway` | Preparing final action |
| `completed` | `approved` | Final positive decision |

---

## 9. Full Dated Task Script (Implementer Lifecycle Table)

**Procedure identifier (`Task.groupIdentifier`) for the entire procedure:** `NDA-214365-S-021` (fictitious NDA 214365, Prior Approval Supplement S-021)  
**Assumed Day 0:** 03 Aug 2026 (the date the corrected resubmission passes technical validation)

**Identity and versioning conventions used in the table:**

- `Task.id` is the human-readable logical label. The **Instance (uuid)** is the actual FHIR resource id — logical labels repeat across submission attempts, uuids never do.
- **Task.version** is the FHIR `meta.versionId` of that instance *after* the step's update is applied.
- **Procedure ID** is the shared `Task.groupIdentifier` (`NDA-214365-S-021`) carried by every Task in the procedure, including the terminally rejected first attempt. The two submission attempts are distinguished by eCTD submission ID (`0045` failed, `0046` passed).

### Task Instance Registry

| Task (logical label) | Instance uuid |
|---|---|
| `submit-shelf-life-update` (attempt 1 – terminally rejected) | `3e74ce8e-720d-4403-8f3d-2fabed8fad26` |
| `submit-shelf-life-update` (attempt 2 – Parent) | `7f463290-c655-471c-966c-15f275f46535` |
| `acknowledge-receipt` | `8b47d104-7ef3-48d4-a57c-8784b075ab58` |
| `screen-submission-for-filing` | `fbfd7f40-e42c-477b-8348-a7deba5da9e6` |
| `assess-user-fee` | `b05b405b-9eff-40df-bd2e-e7d33b82604e` |
| `issue-user-fee-invoice` | `6ec59e0d-0732-4581-b9bc-3ad6350a10f7` |
| `confirm-user-fee-payment` | `44d9bb6a-d43e-4123-b6ad-13b01e64de0d` |
| `issue-day-74-communication` | `cfe8f5be-e91d-4771-bef4-4b3f6ecdefa6` |
| `conduct-shelf-life-assessment` | `a1b6977d-66dd-443e-9e40-c6776d444de0` |
| `respond-to-fda-ir-001` | `e0632f0c-bdca-40d1-8eea-bad663f70d18` |
| `respond-to-fda-ir-002` | `425f70ed-674e-42f6-ad48-48d4c4848e81` |
| `prepare-regulatory-action` | `e41e79a4-aa10-46b1-af3d-c022ca5bb06a` |

### Lifecycle Table

| Step | Date | Actor | Business Step | Task.id | Instance (uuid) | Task.version | basedOn | Procedure ID | status / businessStatus | Input (summary) | Output (summary) |
|------|------|-------|---------------|---------|-----------------|--------------|---------|--------------|-------------------------|-----------------|------------------|
| 1 | 03 Aug 2026 | Applicant | Submit shelf-life update package — **first attempt** (eCTD submission ID `0045`) | `submit-shelf-life-update` (attempt 1) | `3e74ce8e…` | 1 | — | NDA-214365-S-021 | `requested` / — (pending technical validation) | Form 356h, annotated label (ePI XML), clean label (ePI XML), Module 3 stability summary, stability data table, submission manifest | — |
| 2 | 03 Aug 2026 | FDA (auto) | Technical / gateway validation **fails** — attempt is terminal | `submit-shelf-life-update` (attempt 1) | `3e74ce8e…` | 2 | — | NDA-214365-S-021 | `rejected` / `validation-failed` (**terminal**) | Original submission DocumentReferences | Structured validation failure report (XML) |
| 3 | 03 Aug 2026 | Applicant | **Resubmit corrected package** as a new parent Task (eCTD submission ID `0046`) | `submit-shelf-life-update` (attempt 2 – Parent) | `7f463290…` | 1 | — | NDA-214365-S-021 | `requested` / — (pending technical validation) | Corrected submission package (same six files, corrected) | — |
| 4 | 03 Aug 2026 | FDA (auto) | Technical / gateway validation **passes** | `submit-shelf-life-update` (Parent) | `7f463290…` | 2 | — | NDA-214365-S-021 | `received` / `submission-received` | Resubmitted DocumentReferences | — |
| 5 | 03 Aug 2026 | FDA | Acknowledge receipt (only after validation pass) | `acknowledge-receipt` | `8b47d104…` | 1 | Parent | NDA-214365-S-021 | `completed` / `receipt-acknowledged` | — | FDA receipt acknowledgement |
| 6 | 04 Aug 2026 | FDA | Begin administrative / filing review | `screen-submission-for-filing` | `fbfd7f40…` | 1 | Parent | NDA-214365-S-021 | `received` / `filing-review-underway` | Original submission DocumentReferences | — |
| 7 | 05 Aug 2026 | FDA | Assess user fee requirement | `assess-user-fee` | `b05b405b…` | 1 | Parent | NDA-214365-S-021 | `in-progress` / `fee-assessment-underway` | Form 356h + application metadata | — |
| 8 | 06 Aug 2026 | FDA | Issue user fee invoice | `issue-user-fee-invoice` | `6ec59e0d…` | 1 | assess-user-fee | NDA-214365-S-021 | `completed` / `fee-invoice-issued` | — | FDA user fee invoice (DocumentReference) |
| 9a | 13 Aug 2026 | Applicant | Submit proof of payment | `confirm-user-fee-payment` | `44d9bb6a…` | 1 | assess-user-fee | NDA-214365-S-021 | `requested` → under validation | Proof-of-payment DocumentReference(s) | — |
| 9b | 13 Aug 2026 | FDA | Validate proof of payment | `confirm-user-fee-payment` | `44d9bb6a…` | 2 | assess-user-fee | NDA-214365-S-021 | Pass → `completed` / `fee-cleared`<br>Fail → `rejected` / `validation-failed` then new Task (new uuid) re-using **same** invoice DocumentReference | Proof DocumentReference(s) | Payment confirmation **or** validation failure report + new payment Task (same DocRef) |
| 10 | 02 Oct 2026 | FDA | Filing decision – accepted for review | `screen-submission-for-filing` | `fbfd7f40…` | 2 | Parent | NDA-214365-S-021 | `completed` / `filed-accepted-for-review` | — | FDA filing acceptance letter |
| 11 | 02 Oct 2026 | FDA | Parent moves to accepted | `submit-shelf-life-update` (Parent) | `7f463290…` | 3 | — | NDA-214365-S-021 | `accepted` / `filed-accepted-for-review` | — | — |
| 12 | 16 Oct 2026 | FDA | Day 74 communication | `issue-day-74-communication` | `cfe8f5be…` | 1 | Parent | NDA-214365-S-021 | `completed` / `day-74-communication-issued` | — | Day 74 communication |
| 13 | 19 Oct 2026 | FDA | Initiate CMC and labeling assessment | `conduct-shelf-life-assessment` | `a1b6977d…` | 1 | Parent | NDA-214365-S-021 | `in-progress` / `assessment-underway` | Module 3 stability summary, stability data, annotated + clean labels (ePI XML) | — |
| 14 | 14 Dec 2026 | FDA | Issue first Information Request | `respond-to-fda-ir-001` | `e0632f0c…` | 1 | conduct-shelf-life-assessment | NDA-214365-S-021 | `requested` / `information-request-issued` | — | FDA IR 001 (RTQ XML) |
| 15 | 14 Dec 2026 | FDA | Place assessment on hold | `conduct-shelf-life-assessment` | `a1b6977d…` | 2 | Parent | NDA-214365-S-021 | `on-hold` / `awaiting-applicant-response` | Link to IR 001 | — |
| 16 | 11 Jan 2027 | Applicant | Submit response to IR 001 | `respond-to-fda-ir-001` | `e0632f0c…` | 2 | conduct-shelf-life-assessment | NDA-214365-S-021 | `completed` / `response-received` | — | RTQ XML response + updated stability summary |
| 17 | 12 Jan 2027 | FDA | Resume review of IR 001 response | `conduct-shelf-life-assessment` | `a1b6977d…` | 3 | Parent | NDA-214365-S-021 | `in-progress` / `response-under-review` | Applicant IR 001 response package | — |
| 18 | 02 Feb 2027 | FDA | Issue second Information Request | `respond-to-fda-ir-002` | `425f70ed…` | 1 | conduct-shelf-life-assessment | NDA-214365-S-021 | `requested` / `information-request-issued` | — | FDA IR 002 (RTQ XML) |
| 19 | 02 Feb 2027 | FDA | Place assessment on hold again | `conduct-shelf-life-assessment` | `a1b6977d…` | 4 | Parent | NDA-214365-S-021 | `on-hold` / `awaiting-applicant-response` | Link to IR 002 | — |
| 20 | 23 Feb 2027 | Applicant | Submit response to IR 002 | `respond-to-fda-ir-002` | `425f70ed…` | 2 | conduct-shelf-life-assessment | NDA-214365-S-021 | `completed` / `response-received` | — | RTQ XML response, updated stability justification, final labels (ePI XML) |
| 21 | 24 Feb 2027 | FDA | Resume assessment after second response | `conduct-shelf-life-assessment` | `a1b6977d…` | 5 | Parent | NDA-214365-S-021 | `in-progress` / `response-under-review` | Applicant IR 002 response package | — |
| 22 | 05 Apr 2027 | FDA | Continue assessment | `conduct-shelf-life-assessment` | `a1b6977d…` | 6 | Parent | NDA-214365-S-021 | `in-progress` / `assessment-underway` | — | — |
| 23 | 03 May 2027 | FDA | Assessment complete | `conduct-shelf-life-assessment` | `a1b6977d…` | 7 | Parent | NDA-214365-S-021 | `completed` / `assessment-complete` | — | Final review conclusion (optional) |
| 24 | 04 May 2027 | FDA | Prepare regulatory action | `prepare-regulatory-action` | `e41e79a4…` | 1 | conduct-shelf-life-assessment | NDA-214365-S-021 | `in-progress` / `decision-preparation-underway` | Final labels (ePI XML) | — |
| 25 | 03 Jun 2027 | FDA | Issue approval letter | `prepare-regulatory-action` | `e41e79a4…` | 2 | conduct-shelf-life-assessment | NDA-214365-S-021 | `completed` / `approved` | — | FDA approval letter + approved clean label (ePI XML) |
| 26 | 03 Jun 2027 | FDA | Close parent regulatory activity | `submit-shelf-life-update` (Parent) | `7f463290…` | 9 | — | NDA-214365-S-021 | `completed` / `approved` | — | FDA approval letter + approved clean label (ePI XML) |

> **Note on parent versions 4–8:** the parent Task also transitions `on-hold` / `in-progress` around each IR cycle and into `decision-preparation-underway` (see Section 11 status history). Those parent updates (versions 4–8) are not repeated as separate table rows; version 9 in Step 26 reflects them.

---

## 10. Recommended Task Hierarchy (Parent / Child Model)

```text
Task: submit-shelf-life-update (attempt 1)        ← TERMINAL, not part of the hierarchy below
uuid: 3e74ce8e-720d-4403-8f3d-2fabed8fad26
status: rejected
businessStatus: validation-failed
groupIdentifier: NDA-214365-S-021                   (same procedure, eCTD submission ID 0045)
output: DocumentReference/fda-technical-validation-failure-report

Task: submit-shelf-life-update (attempt 2)        ← PARENT (stays open until final decision)
uuid: 7f463290-c655-471c-966c-15f275f46535
status: completed
businessStatus: approved
groupIdentifier: NDA-214365-S-021                   (eCTD submission ID 0046)
text: Application narrative replacing traditional cover letter
│
├── Task: acknowledge-receipt
│   basedOn: Parent
│   status: completed
│   businessStatus: receipt-acknowledged
│
├── Task: screen-submission-for-filing
│   basedOn: Parent
│   status: completed
│   businessStatus: filed-accepted-for-review
│
├── Task: assess-user-fee
│   basedOn: Parent
│   status: completed
│   businessStatus: fee-cleared
│   │
│   ├── Task: issue-user-fee-invoice
│   │   basedOn: assess-user-fee
│   │   status: completed
│   │   businessStatus: fee-invoice-issued
│   │   output: DocumentReference/fda-user-fee-invoice
│   │
│   └── Task: confirm-user-fee-payment
│       basedOn: assess-user-fee
│       status: completed (or rejected on validation failure)
│       businessStatus: fee-cleared (or validation-failed)
│       │
│       └── [On proof validation failure]
│           New Task: confirm-user-fee-payment-reissue
│           basedOn: assess-user-fee
│           input: same DocumentReference/fda-user-fee-invoice  (re-used)
│
├── Task: issue-day-74-communication
│   basedOn: Parent
│   status: completed
│   businessStatus: day-74-communication-issued
│
├── Task: conduct-shelf-life-assessment
│   basedOn: Parent
│   status: completed
│   businessStatus: assessment-complete
│   │
│   ├── Task: respond-to-fda-ir-001
│   │   basedOn: conduct-shelf-life-assessment
│   │   status: completed
│   │   businessStatus: response-received
│   │
│   └── Task: respond-to-fda-ir-002
│       basedOn: conduct-shelf-life-assessment
│       status: completed
│       businessStatus: response-received
│
└── Task: prepare-regulatory-action
    basedOn: conduct-shelf-life-assessment
    status: completed
    businessStatus: approved
```

**Key hierarchy rules**

- The **parent Task** remains open for the entire procedure and is only set to `completed` when the final decision is issued.
- Every discrete interaction is a **child Task**.
- Child Tasks link via `basedOn`.
- All Tasks share the same `groupIdentifier` (`NDA-214365-S-021`), including the terminally rejected first attempt.
- A terminally rejected attempt is never reopened — the resubmission is a brand-new parent Task instance (new uuid) that shares the same `groupIdentifier`.

---

## 11. Parent Task Lifecycle

```text
Attempt 1 — Task instance 3e74ce8e-720d-4403-8f3d-2fabed8fad26 (terminal)
Task.id: submit-shelf-life-update
groupIdentifier: NDA-214365-S-021

Status history (versionId shown):
2026-08-03  v1  requested    / —                            (submitted, pending technical validation)
2026-08-03  v2  rejected     / validation-failed            (terminal — validation failure report attached)

Attempt 2 (Parent) — Task instance 7f463290-c655-471c-966c-15f275f46535
Task.id: submit-shelf-life-update
groupIdentifier: NDA-214365-S-021

Status history (versionId shown):
2026-08-03  v1  requested    / —                            (corrected resubmission, pending validation)
2026-08-03  v2  received     / submission-received          (after technical validation pass)
2026-10-02  v3  accepted     / filed-accepted-for-review
2026-12-14  v4  on-hold      / awaiting-applicant-response  (IR 001)
2027-01-12  v5  in-progress  / response-under-review
2027-02-02  v6  on-hold      / awaiting-applicant-response  (IR 002)
2027-02-24  v7  in-progress  / response-under-review
2027-05-04  v8  in-progress  / decision-preparation-underway
2027-06-03  v9  completed    / approved
```

---

## 12. Detailed Step Descriptions (Early Steps – FDA-Aligned)

### Steps 1–2: Applicant submits shelf-life update package — first attempt fails technical validation (terminal)

Applicant creates the parent Task with narrative in `Task.text` and attaches all DocumentReferences as `input` (eCTD submission ID `0045`).

```text
Task.id: submit-shelf-life-update (attempt 1)
Task instance: urn:uuid:3e74ce8e-720d-4403-8f3d-2fabed8fad26
Task.status: requested
Task.groupIdentifier: NDA-214365-S-021
Task.input: [Form 356h, annotated label (ePI XML), clean label (ePI XML), Module 3 summary, stability data, manifest]
```

FDA (or the exchange layer) runs automated technical validation equivalent to ESG high-level + eCTD checks. In this scenario the first attempt **fails**:

```text
Task instance: urn:uuid:3e74ce8e-… (versionId 2)
Task.status: rejected
Task.businessStatus: validation-failed          (terminal)
Task.output: DocumentReference/fda-technical-validation-failure-report
```

The attempt is terminal — the rejected Task is never reopened. This mirrors FDA policy: a technically deficient electronic submission is not considered received until it passes validation.

### Steps 3–4: Applicant resubmits corrected package — validation passes

The applicant creates a **new** parent Task (new uuid, eCTD submission ID `0046`) with the corrected package, sharing the same `groupIdentifier`:

```text
Task.id: submit-shelf-life-update (attempt 2 – Parent)
Task instance: urn:uuid:7f463290-c655-471c-966c-15f275f46535
Task.status: requested → received                (versionId 1 → 2 after validation pass)
Task.businessStatus: submission-received
Task.groupIdentifier: NDA-214365-S-021
Task.input: [corrected submission package]
```

### Step 5: Acknowledge receipt (only after validation success)

```text
Task.id: acknowledge-receipt
Task.basedOn: submit-shelf-life-update (attempt 2)
Task.status: completed
Task.businessStatus: receipt-acknowledged
Task.output: DocumentReference/fda-receipt-acknowledgement
```

### Steps 6–11: Filing review, fee, and acceptance for review

Filing review is a distinct regulatory step. Only after successful filing determination is the parent moved to `accepted` / `filed-accepted-for-review`.

Fee handling follows the previously agreed pattern: on proof-of-payment validation failure the payment Task is rejected and a new payment Task is created that **re-uses the same invoice DocumentReference**.

---

## 13–15. Information Request Cycles, Assessment Completion and Approval

(The IR cycles, assessment completion, and final approval steps remain as previously defined. Parent is placed `on-hold` while awaiting applicant responses and returned to `in-progress` when responses are received. Final approval is attached as output on both the action Task and the parent Task, which is then closed as `completed` / `approved`.)

---

## 16. End-to-End Resource Traceability

Full Binary → DocumentReference → Task traces for initial submission, IRs, and approval are unchanged from the prior version of this scenario.

---

## 17. Developer Test Assertions

### 17.1–17.4

End-to-end workflow, bidirectional exchange, no direct Binary references from Tasks, cover letter replacement via `Task.text`.

### 17.5 Fee Workflow (including validation failure)

Supports invoice issuance, proof submission, and the recommended re-issue pattern that re-uses the same invoice DocumentReference when only the proof fails validation.

### 17.6 Technical Validation before Receipt Acknowledgement

Technical validation is performed before formal receipt acknowledgement. Failure is terminal for that parent Task attempt (mirrors FDA: not considered received until validation passes). The scenario demonstrates this concretely: the first submission (instance `3e74ce8e…`, eCTD `0045`) is terminally rejected with a structured validation failure report, and the corrected resubmission (instance `7f463290…`, eCTD `0046`) passes and becomes the parent Task for the rest of the procedure.

### 17.7 Filing Review distinct from Technical Receipt

“Received / receipt-acknowledged” is distinct from “accepted / filed-accepted-for-review”. The latter occurs only after filing determination.

### 17.8 Two Information Request Cycles + Pause/Resume

Supports multiple IR cycles with parent assessment moving to `on-hold` / `awaiting-applicant-response` and back to `in-progress`.

### 17.9 Approval Outcome

Final positive outcome uses `status = completed` + `businessStatus = approved` on both the action Task and the parent Task.

### 17.10 Complete Traceability + Parent/Child Model

Every artifact is traceable. Parent remains open for the life of the procedure; discrete interactions are child Tasks linked by `basedOn` and a shared `groupIdentifier` (`NDA-214365-S-021`).

### 17.11 Instance Identity and Versioning

Every Task instance is identified by a uuid (the FHIR resource id); logical Task labels may repeat across submission attempts, but uuids never do. Every state change increments `meta.versionId`, and the lifecycle table records the expected version after each step, so implementers can assert the full version history of each instance — including that a terminally rejected instance stops at version 2 and is never updated again.

---

## 18. IG-Ready Scenario Statement

This scenario demonstrates how APIX can reproduce the end-to-end FDA process for a post-approval application to update the shelf life of a human drug product from 24 months to 36 months, aligned with current ESG NextGen / eCTD receipt, technical validation, filing review, and review practices.

The applicant submits Form FDA 356h, annotated and clean proposed labeling as FHIR ePI XML documents, CMC / Module 3 stability data, supporting stability tables, and a submission manifest for the fictitious procedure NDA 214365 / S-021. No separate cover letter is included; the application narrative is carried in `Task.text`.

FDA performs automated technical validation. Receipt is acknowledged only after validation succeeds. The scenario demonstrates the failure path concretely: the first submission fails technical validation and is terminally rejected with a structured validation failure report, and the applicant resubmits a corrected package as a new parent Task instance, which passes. After technical acceptance, FDA conducts filing review, issues a user fee invoice, confirms payment (with automated proof-validation failure handling that re-uses the same invoice DocumentReference), accepts the application for substantive review, issues a Day 74 communication, conducts CMC and labeling assessment, issues two sequential Information Requests as RTQ-compliant XML, receives and reviews the applicant's RTQ-compliant XML responses, prepares the regulatory action, and issues an approval letter with approved ePI labeling.

All exchanged artifacts follow the APIX `Binary → DocumentReference → Task` pattern. The parent Task remains open for the life of the procedure; discrete interactions are handled as child Tasks. The design is fully automatable at scale while preserving the regulatory distinctions required by FDA process.
