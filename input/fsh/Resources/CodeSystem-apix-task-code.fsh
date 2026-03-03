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
* #response-to-questions "Response to Information Request" "Applicant response to regulator questions"
* #information-request "List of Questions / Information Request" "Regulator raises questions or requests additional data"
* #validation-report "Validation Report" "Technical or business validation outcome"
* #approval "Approval Letter / Positive Decision" "Final positive regulatory decision"
* #rejection "Rejection / Negative Decision" "Final negative regulatory decision"
* #withdrawal "Withdrawal by Applicant" "Applicant withdraws the procedure"
* #annual-report "Periodic Safety Update Report / Annual Report" "PSUR, DSUR, or other periodic report"
* #request-payment "Request Payment" "Requested payment of regulatory fees"
