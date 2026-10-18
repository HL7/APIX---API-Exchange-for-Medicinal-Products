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
* #icsr-message "ICSR Message" "ICH E2B(R3) ICSR message containing one or more case safety reports."
* #icsr-acknowledgment "ICSR Acknowledgment" "ICH E2B(R3) acknowledgment message returned for an ICSR message, carrying the transmission (ACK.A.4) and report (ACK.B.r.6) acknowledgment codes."
