CodeSystem: APIXTaskInputOutputTypeCS
Id: apix-task-input-output-type
Title: "APIX Task Input and Output Types"
Description: "Types of documents and data exchanged as Task inputs and outputs. Inputs come from the requester; outputs come from the owner. This code system holds the types used by the IG's examples; see the Terminology page for a fuller example set."
* ^caseSensitive = true
* ^experimental = false

// Shared
* #cover-letter "Cover Letter" "Letter describing the submission and its contents."
* #application-form "Application Form" "Completed regional application form."
* #validation-report "Validation Report" "Outcome of technical or administrative validation."
// Clinical trials
* #protocol "Protocol" "Clinical trial protocol (or amended protocol)."
* #request-for-information "Request for Information" "Questions from the regulator during assessment of a trial."
* #response-to-questions "Response to Questions" "Applicant's response document to a list of questions."
* #authorisation-decision "Authorisation Decision" "Decision on a clinical trial application or modification."
// ICSR
* #icsr-e2b-r2 "ICSR (E2B(R2))" "A single individual case safety report as an ICH E2B(R2) XML message."
* #icsr-e2b-r3 "ICSR (E2B(R3))" "A single individual case safety report as an ICH E2B(R3) XML message."
* #susar-e2b-r2 "SUSAR (E2B(R2))" "A single SUSAR report from a clinical trial as an ICH E2B(R2) XML message."
* #susar-e2b-r3 "SUSAR (E2B(R3))" "A single SUSAR report from a clinical trial as an ICH E2B(R3) XML message."
* #icsr-e2b-r2-acklog "ICSR E2B(R2) Acknowledgment Log" "ICH E2B(R2) acknowledgment message (ichicsrack) returned for an ICSR, with the transmission and report acknowledgment codes and any errors."
* #icsr-e2b-r3-acklog "ICSR E2B(R3) Acknowledgment Log" "ICH E2B(R3) acknowledgment message returned for an ICSR, with the transmission (ACK.A.4) and report (ACK.B.r.6) acknowledgment codes and any errors."
* #susar-e2b-r2-acklog "SUSAR E2B(R2) Acknowledgment Log" "ICH E2B(R2) acknowledgment message (ichicsrack) returned for a SUSAR, with the transmission and report acknowledgment codes and any errors."
* #susar-e2b-r3-acklog "SUSAR E2B(R3) Acknowledgment Log" "ICH E2B(R3) acknowledgment message returned for a SUSAR, with the transmission (ACK.A.4) and report (ACK.B.r.6) acknowledgment codes and any errors."
// Market authorization: label negotiation (scenario 4)
* #change-description "Change Description and Justification" "Description of the proposed change, with current vs proposed comparison and justification."
* #epi-bundle "ePI Bundle" "Electronic product information as a FHIR document Bundle."
* #proposed-labelling "Proposed Labelling" "Proposed product information (e.g., annotated ePI, annotated PDF or Word)."
* #labelling-comments "Labelling Comments" "Regulator’s comments on, or revised version of, proposed labelling."
* #approved-labelling "Approved Labelling" "Final agreed product information."
* #approval-letter "Approval Letter" "Letter granting approval or authorization."
