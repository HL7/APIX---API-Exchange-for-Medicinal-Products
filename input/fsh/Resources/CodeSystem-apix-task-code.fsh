CodeSystem: APIXTaskCodeCS
Id: apix-task-code
Title: "APIX Task Code System"
Description: "Code system for regulatory task types in APIX submissions"
* ^hierarchyMeaning = #is-a

* ^caseSensitive = true

* ^experimental = false

* #initial-submission "Initial Submission" "First submission of a new application or major variation"
* #supplement "Supplement / Variation" "Post-authorization change (Type IA, IB, II, extension, etc.)"
* #variation-type-ib "Type IB Variation" "Minor, post-approval change to a medicinal product's marketing authorization that has minimal impact on quality, safety, or efficacy"
//* #response-to-questions "Response to Information Request" "Applicant response to regulator questions"
* #information-request "List of Questions / Information Request" "Regulator raises questions or requests additional data"
//* #validation-report "Validation Report" "Technical or business validation outcome"
//* #approval "Approval Letter / Positive Decision" "Final positive regulatory decision"
//* #rejection "Rejection / Negative Decision" "Final negative regulatory decision"
* #withdrawal "Withdrawal by Applicant" "Applicant withdraws the procedure"
* #annual-report "Periodic Safety Update Report / Annual Report" "PSUR, DSUR, or other periodic report"
* #request-payment "Request Payment" "Requested payment of regulatory fees"

// Codes used by the ICSR and clinical trial application examples (see the Terminology page)
* #icsr-initial "Initial ICSR" "First ICH E2B(R3) report of a case, identified by its worldwide unique case identification number (C.1.8.1)."
* #icsr-follow-up "Follow-up ICSR" "ICH E2B(R3) report with new information for a case already reported; same worldwide unique case identification number (C.1.8.1) and a later date of most recent information (C.1.5)."
* #clinical-trial-application "Clinical Trial Application" "Initial application to conduct a clinical trial (e.g., EU CTA under CTR, US IND, Health Canada CTA)."

// Codes used by the label negotiation example (scenario 4; see the Terminology page)
* #variation-type-ii "Type II Variation" "Major change that may significantly affect quality, safety, or efficacy (EU)."
* #labelling-comments "Labelling Comments" "Regulator returns comments on, or a revised version of, the proposed product information for the applicant to accept or counter-propose."
* #labelling-agreement "Labelling Agreement" "Regulator and applicant confirm the final agreed product information text."
