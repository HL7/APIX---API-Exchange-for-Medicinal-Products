<div style="background:#fffbeb; border:1px solid #fde68a; border-left:5px solid #d97706; border-radius:10px; padding:18px 22px; margin-bottom:28px;">
  <div style="font-weight:800; color:#92400e; margin-bottom:6px;">⚠️ Example terminology only</div>
  <p style="font-size:.9em; color:#78350f; line-height:1.65; margin:0;">Each regulator will have its own terminology to suit its unique processes and requirements. The code systems and value sets on this page are <strong>examples</strong>, intended to show how Task codes, business statuses, and input and output types <em>can</em> be organised for different kinds of regulatory interaction. They are not a required or harmonised vocabulary.</p>
</div>

<style>
table.term-table {width:100%; border-collapse:collapse; margin:4px 0 22px; font-size:.86em; line-height:1.5;}
table.term-table th {background:#f3f4f6; color:#111827; font-weight:700; text-align:left; padding:8px 10px; border:1px solid #d1d5db;}
table.term-table td {padding:7px 10px; border:1px solid #e5e7eb; vertical-align:top;}
table.term-table tbody tr:nth-child(even) td {background:#f9fafb;}
table.term-table td:first-child {white-space:nowrap;}
table.term-table code {background:#eef2ff; color:#3730a3; padding:1px 5px; border-radius:4px; font-size:.95em;}
table.term-io th:nth-child(3), table.term-io th:nth-child(4), table.term-io td:nth-child(3), table.term-io td:nth-child(4) {text-align:center; width:70px; color:#047857; font-weight:700;}
</style>

This page shows example values for the four [Task](apixtask.html) elements that carry regulatory meaning, grouped by domain: Market Authorization, Clinical Trials, and Individual Case Safety Reports (ICSR).

### How the terminology is organised

There are three code systems. Each domain section below has an example value set for each of the four Task elements.

| Task element | Code system (id) | Example value sets per domain |
|---|---|---|
| `Task.code` | `apix-task-code` | `apix-ma-task-code-vs`, `apix-ct-task-code-vs`, `apix-icsr-task-code-vs` |
| `Task.businessStatus` | `apix-business-status` | `apix-ma-business-status-vs`, `apix-ct-business-status-vs`, `apix-icsr-business-status-vs` |
| `Task.input.type` | `apix-task-input-output-type` | `apix-ma-task-input-type-vs`, `apix-ct-task-input-type-vs`, `apix-icsr-task-input-type-vs` |
| `Task.output.type` | `apix-task-input-output-type` (same code system) | `apix-ma-task-output-type-vs`, `apix-ct-task-output-type-vs`, `apix-icsr-task-output-type-vs` |
{: .term-table}

Conventions used throughout:

- **Inputs come from the requester, outputs from the owner.** The party that creates the Task supplies `Task.input`; the party that does the work returns `Task.output`. For example, on a Payment Task created by the regulator, the invoice is an input and the proof of payment is an output.
- **One code system for input and output types.** The same document type can be an input on one Task and an output on another (for example, proposed labelling or a questionnaire response), so input and output types share one code system and differ only by value set.
- **Task codes are hierarchical.** Grouping codes (marked *grouping*) organise the Market Authorization sub-areas and the domain roots, so a value set can include a whole branch.
- **Shared terms.** Some business statuses and input/output types apply to every domain. They are listed once, in [Shared terms](#shared-terms), and included in each domain's value sets.

### Shared terms {#shared-terms}

Used by all three domains. The ICSR value sets use only `submitted`, `rejected` and `validation-report` from this list.

#### Business status (shared)

| Code | Display | Definition |
|---|---|---|
| `submitted` | Submitted | The application has been submitted by the applicant. |
| `received` | Received | The application or submission has been received by the regulator. |
| `receipt-acknowledged` | Receipt Acknowledged | Receipt has been formally acknowledged to the sender. |
| `validation-successful` | Validation Successful | The technical and administrative validation has been completed successfully. |
| `validation-failed` | Validation Failed | The submission failed validation and cannot proceed. |
| `under-assessment` | Under Assessment | The submission is currently undergoing scientific review. |
| `clock-stop` | Clock Stop | The review timeline is paused, typically waiting for applicant response to questions. |
| `clock-restart` | Clock Restart | The review timeline has resumed following receipt of a response. |
| `consolidated-review` | Consolidated Review | Comments from multiple assessors are being consolidated. |
| `decision-pending` | Decision Pending | The assessment is complete and the final decision is being prepared. |
| `approved` | Approved | The application has been approved. |
| `rejected` | Rejected | The application has been rejected. |
| `withdrawn` | Withdrawn | The application has been withdrawn by the applicant. |
{: .term-table}

#### Input and output types (shared)

| Code | Display | Definition |
|---|---|---|
| `cover-letter` | Cover Letter | Letter describing the submission and its contents. |
| `application-form` | Application Form | Completed regional application form. |
| `supporting-document` | Supporting Document | Any other document supporting the Task. |
| `acknowledgment-of-receipt` | Acknowledgment of Receipt | Confirmation that the submission was received. |
| `validation-report` | Validation Report | Outcome of technical or administrative validation. |
| `assessment-report` | Assessment Report | Regulator’s assessment of the submission. |
| `decision-letter` | Decision Letter | Formal communication of the regulatory decision. |
| `questionnaire` | Questionnaire | Structured list of questions. |
| `questionnaire-response` | Questionnaire Response | Structured answers to a questionnaire. |
| `correspondence` | Correspondence | General correspondence between the parties. |
{: .term-table}


### Market Authorization

#### Task codes — `apix-ma-task-code-vs`

| Code | Display | Definition |
|---|---|---|
| `market-authorization` *(grouping)* | Market Authorization | Grouping: Tasks for the marketing authorization lifecycle of a human biopharmaceutical product. |
{: .term-table}


##### Pre-submission

| Code | Display | Definition |
|---|---|---|
| `pre-submission` *(grouping)* | Pre-Submission | Grouping: interactions before a marketing application is filed. |
| &nbsp;&nbsp;&nbsp;&nbsp;`pre-submission-meeting-request` | Pre-Submission Meeting Request | Request for a meeting with the regulator before filing (e.g., FDA pre-NDA/Type B meeting, EMA pre-submission meeting, Health Canada pre-submission meeting). |
| &nbsp;&nbsp;&nbsp;&nbsp;`scientific-advice-request` | Scientific Advice Request | Request for scientific or regulatory advice on development or the planned application (e.g., EMA scientific advice / protocol assistance, FDA Type C meeting). |
| &nbsp;&nbsp;&nbsp;&nbsp;`eligibility-request` | Eligibility Request | Request to confirm eligibility for a procedure or route (e.g., EU centralised procedure eligibility). |
| &nbsp;&nbsp;&nbsp;&nbsp;`designation-request` | Designation Request | Request for a designation or expedited pathway (e.g., orphan, breakthrough therapy, PRIME, priority review). |
| &nbsp;&nbsp;&nbsp;&nbsp;`notice-of-intent-to-submit` | Notice of Intent to Submit | Notification of the planned submission date and scope of a marketing application. |
{: .term-table}


##### NDA/MAA

| Code | Display | Definition |
|---|---|---|
| `marketing-application` *(grouping)* | Marketing Application (NDA/MAA) | Grouping: the initial marketing application and the regulator activities that process it. |
| &nbsp;&nbsp;&nbsp;&nbsp;`initial-submission` | Initial Submission | First submission of a new application or major variation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`new-drug-application` | New Drug Application (NDA) | Initial marketing application for a new drug (US NDA; analogous national applications). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`biologics-license-application` | Biologics License Application (BLA) | Initial marketing application for a biological product (US BLA). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`marketing-authorisation-application` | Marketing Authorisation Application (MAA) | Initial application for a marketing authorisation (e.g., EU centralised, decentralised, or national procedure). |
| &nbsp;&nbsp;&nbsp;&nbsp;`acknowledge-receipt` | Acknowledge Receipt | Regulator confirms the submission was received and is technically readable. |
| &nbsp;&nbsp;&nbsp;&nbsp;`validate-submission` | Validate Submission | Technical and administrative validation (completeness) of a submission. |
| &nbsp;&nbsp;&nbsp;&nbsp;`filing-review` | Filing Review | Regulator decides whether the application is sufficiently complete to be filed for review (e.g., FDA 60-day filing review). |
| &nbsp;&nbsp;&nbsp;&nbsp;`assess-application` | Assess Application | Scientific assessment of the application (quality, non-clinical, clinical, labelling). |
| &nbsp;&nbsp;&nbsp;&nbsp;`issue-regulatory-decision` | Issue Regulatory Decision | Preparation and issue of the final regulatory action (approval, complete response, refusal). |
| &nbsp;&nbsp;&nbsp;&nbsp;`resubmission` | Resubmission | Applicant resubmits an application after a negative or complete-response decision. |
| &nbsp;&nbsp;&nbsp;&nbsp;`appeal` | Appeal / Re-examination | Applicant requests formal dispute resolution, re-examination, or appeal of a decision. |
| &nbsp;&nbsp;&nbsp;&nbsp;`withdrawal` | Withdrawal by Applicant | Applicant withdraws the procedure. |
{: .term-table}


##### Payments

| Code | Display | Definition |
|---|---|---|
| `payment` *(grouping)* | Payments | Grouping: fees and payments linked to a regulatory procedure. |
| &nbsp;&nbsp;&nbsp;&nbsp;`assess-fee` | Assess Fee | Regulator determines the fee due for a submission. |
| &nbsp;&nbsp;&nbsp;&nbsp;`request-payment` | Request Payment | Requested payment of regulatory fees. |
| &nbsp;&nbsp;&nbsp;&nbsp;`fee-waiver-request` | Fee Waiver or Reduction Request | Applicant requests a waiver, reduction, or deferral of fees. |
| &nbsp;&nbsp;&nbsp;&nbsp;`refund-request` | Refund Request | Applicant requests a refund of fees paid. |
{: .term-table}


##### Question and response

| Code | Display | Definition |
|---|---|---|
| `question-and-response` *(grouping)* | Question and Response | Grouping: questions raised during a procedure and the responses to them. |
| &nbsp;&nbsp;&nbsp;&nbsp;`information-request` | List of Questions / Information Request | Regulator raises questions or requests additional data. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`list-of-outstanding-issues` | List of Outstanding Issues | Regulator issues the issues that remain unresolved after the first round of questions (e.g., EU LoOI). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`clarification-request` | Clarification Request | Regulator requests a minor clarification that does not stop the clock. |
| &nbsp;&nbsp;&nbsp;&nbsp;`response-timeline-extension-request` | Response Timeline Extension Request | Applicant requests more time to respond to questions (clock-stop extension). |
{: .term-table}


##### Label negotiation

| Code | Display | Definition |
|---|---|---|
| `label-negotiation` *(grouping)* | Label Negotiation | Grouping: agreement of the product information (labelling) text between applicant and regulator, for initial applications and post-approval label changes. |
| &nbsp;&nbsp;&nbsp;&nbsp;`labelling-proposal` | Labelling Proposal | Applicant submits proposed product information, or a counter-proposal, for review. |
| &nbsp;&nbsp;&nbsp;&nbsp;`labelling-comments` | Labelling Comments | Regulator returns comments on, or a revised version of, the proposed product information for the applicant to accept or counter-propose. |
| &nbsp;&nbsp;&nbsp;&nbsp;`labelling-agreement` | Labelling Agreement | Regulator and applicant confirm the final agreed product information text. |
{: .term-table}


##### Post-approval changes

| Code | Display | Definition |
|---|---|---|
| `post-approval-change` *(grouping)* | Post-Approval Change | Grouping: changes to an authorized product and lifecycle maintenance. |
| &nbsp;&nbsp;&nbsp;&nbsp;`supplement` | Supplement / Variation | Post-authorization change (Type IA, IB, II, extension, etc.). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`variation-type-ia` | Type IA Variation | Minor "do and tell" change notified after implementation (EU). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`variation-type-ib` | Type IB Variation | Minor, post-approval change to a medicinal product's marketing authorization that has minimal impact on quality, safety, or efficacy |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`variation-type-ii` | Type II Variation | Major change that may significantly affect quality, safety, or efficacy (EU). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`line-extension` | Line Extension | Extension of a marketing authorisation (e.g., new strength, pharmaceutical form, or route). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`prior-approval-supplement` | Prior Approval Supplement (PAS) | Major change requiring approval before distribution (US). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`cbe-30` | Changes Being Effected in 30 Days (CBE-30) | Moderate change that may be distributed 30 days after receipt (US). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`cbe-0` | Changes Being Effected (CBE-0) | Moderate change that may be distributed on receipt (US). |
| &nbsp;&nbsp;&nbsp;&nbsp;`annual-report` | Annual / Periodic Report (Authorized Product) | Periodic report for an authorized product (e.g., PSUR/PBRER, US NDA/BLA annual report). Clinical-trial annual reports use annual-safety-report. |
| &nbsp;&nbsp;&nbsp;&nbsp;`renewal` | Renewal | Renewal of a marketing authorisation. |
| &nbsp;&nbsp;&nbsp;&nbsp;`marketing-authorisation-transfer` | Marketing Authorisation Transfer | Transfer of a marketing authorisation to a new holder. |
{: .term-table}


#### Business status — `apix-ma-business-status-vs`

Domain-specific statuses:

| Code | Display | Definition |
|---|---|---|
| `meeting-granted` | Meeting Granted | The requested meeting has been granted and scheduled. |
| `meeting-denied` | Meeting Denied | The requested meeting has been denied. |
| `written-response-only` | Written Response Only | The regulator will answer the meeting questions in writing instead of meeting. |
| `preliminary-responses-issued` | Preliminary Responses Issued | Preliminary written responses to the meeting questions have been issued. |
| `meeting-held` | Meeting Held | The meeting has taken place. |
| `minutes-issued` | Minutes Issued | Final meeting minutes or advice letter have been issued. |
| `designation-granted` | Designation Granted | The requested designation or eligibility has been granted or confirmed. |
| `designation-denied` | Designation Denied | The requested designation or eligibility has been denied. |
| `filing-review-underway` | Filing Review Underway | The regulator is deciding whether to file the application for review. |
| `filed-accepted-for-review` | Filed — Accepted for Review | The application has been filed and accepted for substantive review. |
| `refused-to-file` | Refused to File | The application was not accepted for review. |
| `complete-response-issued` | Complete Response Issued | The review cycle ended without approval; deficiencies were communicated (e.g., FDA complete response letter). |
| `resubmission-received` | Resubmission Received | A resubmission following a complete response or refusal has been received. |
| `appeal-submitted` | Appeal Submitted | An appeal, re-examination, or dispute-resolution request has been submitted. |
| `appeal-under-review` | Appeal Under Review | The appeal is being reviewed. |
| `appeal-decision-issued` | Appeal Decision Issued | The outcome of the appeal has been issued. |
| `fee-assessment-underway` | Fee Assessment Underway | The regulator is determining the fee due. |
| `payment-requested` | Payment Requested | A fee payment has been requested by the regulator. |
| `payment-received` | Payment Received | The fee payment has been received and confirmed. |
| `payment-overdue` | Payment Overdue | The fee payment was not received by the due date. |
| `fee-waiver-granted` | Fee Waiver Granted | The fee waiver, reduction, or deferral has been granted. |
| `fee-waiver-denied` | Fee Waiver Denied | The fee waiver, reduction, or deferral has been denied. |
| `refund-issued` | Refund Issued | A fee refund has been issued. |
| `questions-issued` | Questions Issued | Questions or an information request have been sent to the applicant. |
| `awaiting-applicant-response` | Awaiting Applicant Response | The regulator is waiting for the applicant to respond. |
| `response-received` | Response Received | The applicant’s response has been received. |
| `response-under-review` | Response Under Review | The regulator is reviewing the applicant’s response. |
| `response-accepted` | Response Accepted | The response resolves the questions raised. |
| `further-information-required` | Further Information Required | The response did not resolve all questions; further information is needed. |
| `extension-granted` | Extension Granted | A requested extension of the response timeline has been granted. |
| `extension-denied` | Extension Denied | A requested extension of the response timeline has been denied. |
| `labelling-under-review` | Labelling Under Review | The regulator is reviewing the proposed product information. |
| `labelling-comments-issued` | Labelling Comments Issued | The regulator has returned comments or a revised version to the applicant. |
| `counter-proposal-received` | Counter-Proposal Received | The applicant has returned a counter-proposal on the product information. |
| `labelling-agreed` | Labelling Agreed | Applicant and regulator have agreed the product information text. |
| `notification-accepted` | Notification Accepted | A notified change (e.g., Type IA) has been accepted. |
| `change-implemented` | Change Implemented | The approved change has been implemented. |
{: .term-table}


Also included from shared terms: `submitted`, `received`, `receipt-acknowledged`, `validation-successful`, `validation-failed`, `under-assessment`, `clock-stop`, `clock-restart`, `consolidated-review`, `decision-pending`, `approved`, `rejected`, `withdrawn`.


**Typical progressions:**

- *Pre-submission meeting:* submitted → received → meeting-granted (or written-response-only / meeting-denied) → preliminary-responses-issued → meeting-held → minutes-issued
- *NDA/MAA:* submitted → received → receipt-acknowledged → validation-successful → filing-review-underway → filed-accepted-for-review → under-assessment → (clock-stop ↔ clock-restart) → decision-pending → approved | complete-response-issued | rejected
- *Payment:* fee-assessment-underway → payment-requested → payment-received (or payment-overdue)
- *Question and response:* questions-issued → awaiting-applicant-response → response-received → response-under-review → response-accepted | further-information-required
- *Label negotiation:* labelling-under-review → labelling-comments-issued → counter-proposal-received → (repeat) → labelling-agreed
- *Post-approval change:* submitted → received → validation-successful → under-assessment → decision-pending → approved → change-implemented (Type IA: submitted → notification-accepted)


**Worked example:** a Type II variation with two rounds of label negotiation on an annotated ePI — [submitted](Task-scenario4-01-variation-submitted.html), [validated](Task-scenario4-02-variation-validated.html), [under assessment](Task-scenario4-03-variation-under-assessment.html), [labelling comments round 1](Task-scenario4-04-labelling-comments-round1.html), [counter-proposal](Task-scenario4-05-labelling-comments-round1-response.html), [labelling comments round 2](Task-scenario4-06-labelling-comments-round2.html), [response](Task-scenario4-07-labelling-comments-round2-response.html), [agreement requested](Task-scenario4-08-labelling-agreement.html), [labelling agreed](Task-scenario4-09-labelling-agreed.html), [approved](Task-scenario4-10-variation-approved.html).


#### Input and output types — `apix-ma-task-input-type-vs` / `apix-ma-task-output-type-vs`

Domain-specific types:

| Code | Display | Definition |
|---|---|---|
| `meeting-request-letter` | Meeting Request Letter | Request for a meeting, with proposed format and date. |
| `briefing-package` | Briefing Package | Background document and the sponsor’s questions for a meeting or advice request. |
| `preliminary-responses` | Preliminary Responses | Regulator’s preliminary written answers to meeting questions. |
| `meeting-minutes` | Meeting Minutes | Final record of a meeting or advice outcome. |
| `designation-decision` | Designation Decision | Decision on a designation or eligibility request. |
| `ectd-sequence` | eCTD Sequence | An eCTD submission sequence (backbone and documents). |
| `cmc-documents` | CMC Documents | Chemistry, manufacturing, and controls documentation. |
| `stability-data` | Stability Data | Stability study data and summaries. |
| `clinical-study-report` | Clinical Study Report | Clinical study report supporting the application. |
| `risk-management-plan` | Risk Management Plan | Risk management plan or REMS. |
| `epi-bundle` | ePI Bundle | Electronic product information as a FHIR document Bundle. |
| `proposed-labelling` | Proposed Labelling | Proposed product information (e.g., annotated PDF or Word). |
| `labelling-comments` | Labelling Comments | Regulator’s comments on, or revised version of, proposed labelling. |
| `approved-labelling` | Approved Labelling | Final agreed product information. |
| `invoice` | Invoice | Fee invoice issued by the regulator. |
| `proof-of-payment` | Proof of Payment | Evidence that the fee has been paid. |
| `fee-waiver-justification` | Fee Waiver Justification | Justification for a fee waiver, reduction, or deferral. |
| `payment-receipt` | Payment Receipt | Regulator’s confirmation that payment was received. |
| `list-of-questions` | List of Questions | Questions or information request from the regulator. |
| `response-to-questions` | Response to Questions | Applicant’s response document to a list of questions. |
| `change-description` | Change Description and Justification | Description of the proposed change, with current vs proposed comparison and justification. |
| `complete-response-letter` | Complete Response Letter | Letter describing the deficiencies that prevent approval. |
| `approval-letter` | Approval Letter | Letter granting approval or authorization. |
{: .term-table}

Value set membership (including shared types):

| Code | Display | Input | Output |
|---|---|:-:|:-:|
| `cover-letter` | Cover Letter | ✓ |  |
| `application-form` | Application Form | ✓ |  |
| `supporting-document` | Supporting Document | ✓ |  |
| `acknowledgment-of-receipt` | Acknowledgment of Receipt |  | ✓ |
| `validation-report` | Validation Report |  | ✓ |
| `assessment-report` | Assessment Report |  | ✓ |
| `decision-letter` | Decision Letter |  | ✓ |
| `questionnaire` | Questionnaire | ✓ |  |
| `questionnaire-response` | Questionnaire Response |  | ✓ |
| `correspondence` | Correspondence |  | ✓ |
| `meeting-request-letter` | Meeting Request Letter | ✓ |  |
| `briefing-package` | Briefing Package | ✓ |  |
| `preliminary-responses` | Preliminary Responses |  | ✓ |
| `meeting-minutes` | Meeting Minutes |  | ✓ |
| `designation-decision` | Designation Decision |  | ✓ |
| `ectd-sequence` | eCTD Sequence | ✓ |  |
| `cmc-documents` | CMC Documents | ✓ |  |
| `stability-data` | Stability Data | ✓ |  |
| `clinical-study-report` | Clinical Study Report | ✓ |  |
| `risk-management-plan` | Risk Management Plan | ✓ |  |
| `epi-bundle` | ePI Bundle | ✓ | ✓ |
| `proposed-labelling` | Proposed Labelling | ✓ | ✓ |
| `labelling-comments` | Labelling Comments | ✓ | ✓ |
| `approved-labelling` | Approved Labelling |  | ✓ |
| `invoice` | Invoice | ✓ |  |
| `proof-of-payment` | Proof of Payment |  | ✓ |
| `fee-waiver-justification` | Fee Waiver Justification | ✓ |  |
| `payment-receipt` | Payment Receipt |  | ✓ |
| `list-of-questions` | List of Questions | ✓ | ✓ |
| `response-to-questions` | Response to Questions |  | ✓ |
| `change-description` | Change Description and Justification | ✓ |  |
| `complete-response-letter` | Complete Response Letter |  | ✓ |
| `approval-letter` | Approval Letter |  | ✓ |
{: .term-table .term-io}


### Clinical Trials

#### Task codes — `apix-ct-task-code-vs`

| Code | Display | Definition |
|---|---|---|
| `clinical-trial` *(grouping)* | Clinical Trial | Grouping: regulatory interactions for clinical trials of human biopharmaceutical products. |
| `clinical-trial-application` | Clinical Trial Application | Initial application to conduct a clinical trial (e.g., EU CTA under CTR, US IND, Health Canada CTA). |
| `add-member-state` | Addition of Member State Concerned | Extension of an authorized trial to an additional member state (EU CTR). |
| `substantial-modification` | Substantial Modification / Protocol Amendment | Change likely to substantially affect participant safety or rights, or data reliability; requires authorization (EU) or amendment submission (US). |
| `non-substantial-modification` | Non-Substantial Modification | Change that does not require authorization but must be recorded or notified. |
| `information-amendment` | Information Amendment | Submission of essential new information that is not a protocol amendment (US IND). |
| `trial-start-notification` | Trial Start Notification | Notification of start of trial or first participant visit. |
| `end-of-recruitment-notification` | End of Recruitment Notification | Notification that recruitment has ended. |
| `temporary-halt-notification` | Temporary Halt Notification | Notification that the trial has been temporarily halted. |
| `restart-request` | Restart After Temporary Halt | Request to restart a trial after a temporary halt. |
| `early-termination-notification` | Early Termination Notification | Notification that the trial ended early. |
| `end-of-trial-notification` | End of Trial Notification | Notification that the trial has ended. |
| `urgent-safety-measure` | Urgent Safety Measure | Notification of an urgent safety measure taken to protect participants. |
| `serious-breach-notification` | Serious Breach Notification | Notification of a serious breach of the protocol or GCP. |
| `annual-safety-report` | Annual Safety Report (Clinical Trial) | Annual report for an investigational product under clinical development (e.g., DSUR, US IND annual report). Authorized-product periodic reports use annual-report. |
| `clinical-trial-results-summary` | Clinical Trial Results Summary | Summary of results (and lay summary) after the end of the trial. |
| `clinical-hold` | Clinical Hold | Regulator orders a delay or suspension of a proposed or ongoing trial (US IND). |
| `clinical-hold-response` | Complete Response to Clinical Hold | Sponsor responds to all clinical hold issues and requests that the hold be lifted. |
{: .term-table}


Also included from Market Authorization: `information-request`, `withdrawal`.


#### Business status — `apix-ct-business-status-vs`

Domain-specific statuses:

| Code | Display | Definition |
|---|---|---|
| `request-for-information-issued` | Request for Information Issued | The regulator has sent a request for information to the sponsor. |
| `authorised` | Authorised | The trial or modification has been authorised. |
| `authorised-with-conditions` | Authorised with Conditions | The trial or modification has been authorised subject to conditions. |
| `not-authorised` | Not Authorised | The trial or modification has not been authorised. |
| `may-proceed` | May Proceed | The review period has ended without objection and the trial may proceed (e.g., US IND 30-day review). |
| `on-clinical-hold` | On Clinical Hold | The trial is on clinical hold. |
| `clinical-hold-lifted` | Clinical Hold Lifted | The clinical hold has been lifted. |
| `trial-ongoing` | Trial Ongoing | The trial has started and is ongoing. |
| `recruitment-ended` | Recruitment Ended | Recruitment has ended. |
| `temporarily-halted` | Temporarily Halted | The trial is temporarily halted. |
| `trial-ended` | Trial Ended | The trial has ended. |
| `terminated-early` | Terminated Early | The trial was terminated early. |
| `results-submitted` | Results Submitted | The results summary has been submitted. |
{: .term-table}


Also included from shared terms: `submitted`, `received`, `receipt-acknowledged`, `validation-successful`, `validation-failed`, `under-assessment`, `clock-stop`, `clock-restart`, `decision-pending`, `withdrawn`.


**Typical progressions:**

- *Clinical trial application:* submitted → received → validation-successful → under-assessment → (request-for-information-issued: clock-stop ↔ clock-restart) → authorised | authorised-with-conditions | not-authorised; US IND: received → may-proceed | on-clinical-hold
- *Trial lifecycle:* authorised → trial-ongoing → recruitment-ended → trial-ended → results-submitted (or temporarily-halted / terminated-early)


**Worked example:** a clinical trial application from submission to authorisation, including a request for information — [submission](Task-scenario3-01-cta-submission.html), [validated](Task-scenario3-02-cta-validated.html), [request for information](Task-scenario3-03-cta-rfi.html), [response](Task-scenario3-04-cta-rfi-response.html), [authorised](Task-scenario3-05-cta-authorised.html).


#### Input and output types — `apix-ct-task-input-type-vs` / `apix-ct-task-output-type-vs`

Domain-specific types:

| Code | Display | Definition |
|---|---|---|
| `protocol` | Protocol | Clinical trial protocol (or amended protocol). |
| `protocol-synopsis` | Protocol Synopsis | Summary of the protocol. |
| `investigators-brochure` | Investigator’s Brochure | Investigator’s brochure. |
| `impd` | Investigational Medicinal Product Dossier | IMPD or equivalent quality/non-clinical/clinical data for the investigational product. |
| `informed-consent-form` | Informed Consent Form | Participant information sheet and informed consent form. |
| `modification-description` | Modification Description | Description and justification of a modification, with tracked changes. |
| `dsur` | DSUR | Development Safety Update Report. |
| `results-summary` | Results Summary | Summary of clinical trial results. |
| `lay-summary` | Lay Summary | Summary of results for a lay audience. |
| `request-for-information` | Request for Information | Questions from the regulator during assessment of a trial. |
| `authorisation-decision` | Authorisation Decision | Decision on a clinical trial application or modification. |
| `clinical-hold-letter` | Clinical Hold Letter | Letter describing the reasons for a clinical hold. |
{: .term-table}

Value set membership (including shared types):

| Code | Display | Input | Output |
|---|---|:-:|:-:|
| `cover-letter` | Cover Letter | ✓ |  |
| `application-form` | Application Form | ✓ |  |
| `supporting-document` | Supporting Document | ✓ |  |
| `acknowledgment-of-receipt` | Acknowledgment of Receipt |  | ✓ |
| `validation-report` | Validation Report |  | ✓ |
| `assessment-report` | Assessment Report |  | ✓ |
| `decision-letter` | Decision Letter |  | ✓ |
| `questionnaire` | Questionnaire | ✓ |  |
| `questionnaire-response` | Questionnaire Response |  | ✓ |
| `correspondence` | Correspondence |  | ✓ |
| `response-to-questions` | Response to Questions |  | ✓ |
| `protocol` | Protocol | ✓ |  |
| `protocol-synopsis` | Protocol Synopsis | ✓ |  |
| `investigators-brochure` | Investigator’s Brochure | ✓ |  |
| `impd` | Investigational Medicinal Product Dossier | ✓ |  |
| `informed-consent-form` | Informed Consent Form | ✓ |  |
| `modification-description` | Modification Description | ✓ |  |
| `dsur` | DSUR | ✓ |  |
| `results-summary` | Results Summary | ✓ |  |
| `lay-summary` | Lay Summary | ✓ |  |
| `request-for-information` | Request for Information | ✓ | ✓ |
| `authorisation-decision` | Authorisation Decision |  | ✓ |
| `clinical-hold-letter` | Clinical Hold Letter |  | ✓ |
{: .term-table .term-io}


### Individual Case Safety Reports (ICSR) {#individual-case-safety-reports-icsr}

#### Task codes — `apix-icsr-task-code-vs`

| Code | Display | Definition |
|---|---|---|
| `icsr` | Individual Case Safety Report | Transmission of a single individual case safety report (ICSR) as an ICH E2B(R2) or E2B(R3) message. The input type gives the E2B version. |
| `susar` | Suspected Unexpected Serious Adverse Reaction | Transmission of a single SUSAR report from a clinical trial as an ICH E2B(R2) or E2B(R3) message. The input type gives the E2B version. |
{: .term-table}


#### Business status — `apix-icsr-business-status-vs`

| Code | Display | Definition |
|---|---|---|
| `submitted` | Submitted | The sender has submitted the safety report. *(Shared term.)* |
| `accepted` | Accepted | The safety report passed validation and was loaded by the receiver; the acknowledgment log has been returned. |
| `rejected` | Rejected | The safety report failed validation and was not loaded; the acknowledgment log and a validation report have been returned. *(Shared term.)* |
| `complete` | Complete | Processing of the accepted safety report is complete and no further action is expected on the Task. |
{: .term-table}


The sender sets `submitted` when it creates the Task (and when it resubmits on a new Task). The regulator then sets `accepted` or `rejected`, and `complete` when processing is finished.


**Typical progressions:**

| Path | `Task.status` | `Task.businessStatus` |
|---|---|---|
| Accepted | requested → accepted → completed | `submitted` → `accepted` → `complete` |
| Rejected and resubmitted | Task 1: requested → rejected<br/>Task 2 (`basedOn` Task 1, same `groupIdentifier`): requested → accepted → completed | Task 1: `submitted` → `rejected`<br/>Task 2: `submitted` → `accepted` → `complete` |
{: .term-table}

A rejected Task is final, so a resubmission is a new Task. `Task.statusReason` is required when `Task.status` = `rejected`.


**Worked examples:**

- *Accepted:* an E2B(R2) ICSR — [submitted](Task-scenario2a-01-icsr-submitted.html), [accepted](Task-scenario2a-02-icsr-accepted.html), [complete](Task-scenario2a-03-icsr-complete.html).
- *Rejected and resubmitted:* an E2B(R2) ICSR with a validation error — [submitted](Task-scenario2b-01-icsr-submitted.html), [rejected](Task-scenario2b-02-icsr-rejected.html), [resubmitted](Task-scenario2b-03-icsr-resubmitted.html), [accepted](Task-scenario2b-04-icsr-accepted.html), [complete](Task-scenario2b-05-icsr-complete.html).


#### Input and output types — `apix-icsr-task-input-type-vs` / `apix-icsr-task-output-type-vs`

| Code | Display | Definition |
|---|---|---|
| `icsr-e2b-r2` | ICSR (E2B(R2)) | A single individual case safety report as an ICH E2B(R2) XML message. |
| `icsr-e2b-r3` | ICSR (E2B(R3)) | A single individual case safety report as an ICH E2B(R3) XML message. |
| `susar-e2b-r2` | SUSAR (E2B(R2)) | A single SUSAR report from a clinical trial as an ICH E2B(R2) XML message. |
| `susar-e2b-r3` | SUSAR (E2B(R3)) | A single SUSAR report from a clinical trial as an ICH E2B(R3) XML message. |
| `icsr-e2b-r2-acklog` | ICSR E2B(R2) Acknowledgment Log | ICH E2B(R2) acknowledgment message (`ichicsrack`) returned for an ICSR, with the transmission and report acknowledgment codes and any errors. |
| `icsr-e2b-r3-acklog` | ICSR E2B(R3) Acknowledgment Log | ICH E2B(R3) acknowledgment message returned for an ICSR, with the transmission (ACK.A.4) and report (ACK.B.r.6) acknowledgment codes and any errors. |
| `susar-e2b-r2-acklog` | SUSAR E2B(R2) Acknowledgment Log | ICH E2B(R2) acknowledgment message (`ichicsrack`) returned for a SUSAR, with the transmission and report acknowledgment codes and any errors. |
| `susar-e2b-r3-acklog` | SUSAR E2B(R3) Acknowledgment Log | ICH E2B(R3) acknowledgment message returned for a SUSAR, with the transmission (ACK.A.4) and report (ACK.B.r.6) acknowledgment codes and any errors. |
{: .term-table}

`validation-report` is a [shared term](#shared-terms).

Value set membership:

| Code | Display | Input | Output |
|---|---|:-:|:-:|
| `icsr-e2b-r2` | ICSR (E2B(R2)) | ✓ |  |
| `icsr-e2b-r3` | ICSR (E2B(R3)) | ✓ |  |
| `susar-e2b-r2` | SUSAR (E2B(R2)) | ✓ |  |
| `susar-e2b-r3` | SUSAR (E2B(R3)) | ✓ |  |
| `icsr-e2b-r2-acklog` | ICSR E2B(R2) Acknowledgment Log |  | ✓ |
| `icsr-e2b-r3-acklog` | ICSR E2B(R3) Acknowledgment Log |  | ✓ |
| `susar-e2b-r2-acklog` | SUSAR E2B(R2) Acknowledgment Log |  | ✓ |
| `susar-e2b-r3-acklog` | SUSAR E2B(R3) Acknowledgment Log |  | ✓ |
| `validation-report` | Validation Report |  | ✓ |
{: .term-table .term-io}

<div style="background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; border-radius:10px; padding:14px 18px; margin:8px 0 22px;">
  <div style="font-weight:700; color:#1e3a8a; margin-bottom:4px;">Recommendation: one report per Task</div>
  <p style="font-size:.88em; color:#1e3a8a; line-height:1.6; margin:0;">Send each ICSR and each SUSAR on its own, as one E2B message on one Task, rather than bundling several reports in one batch message. Each report then gets its own Task status, business status and acknowledgment log, so one rejected report does not hold up the others and a resubmission only has to resend that report.</p>
</div>

The content of the report itself (case, reporter, reactions, drugs) stays in the ICH E2B message. These codes only describe the exchange around it.
