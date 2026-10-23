CodeSystem: APIXBusinessStatusCS
Id: apix-business-status
Title: "APIX Regulatory Business Status"
Description: "Code system for regulatory business status in APIX submissions"

* ^caseSensitive = true
* ^experimental = false




* #submitted "Submitted" "The application has been submitted by the applicant."
* #received "Received" "The application or submission has been received by the regulator."
* #validation-successful "Validation Successful" "The technical and administrative validation has been completed successfully."
* #validation-failed "Validation Failed" "The submission failed validation and cannot proceed."
* #under-assessment "Under Assessment" "The submission is currently undergoing scientific review."
* #clock-stop "Clock Stop" "The review timeline is paused, typically waiting for applicant response to questions."
* #clock-restart "Clock Restart" "The review timeline has resumed following receipt of a response."
* #consolidated-review "Consolidated Review" "Comments from multiple assessors are being consolidated."
* #decision-pending "Decision Pending" "The assessment is complete and the final decision is being prepared."
* #approved "Approved" "The application has been approved."
* #rejected "Rejected" "The application has been rejected."
* #withdrawn "Withdrawn" "The application has been withdrawn by the applicant."
* #payment-requested "Payment Requested" "A fee payment has been requested by the regulator."
* #payment-received "Payment Received" "The fee payment has been received and confirmed."

// Statuses used by the ICSR and clinical trial application examples (see the Terminology page)
* #accepted "Accepted" "The safety report passed validation and was loaded by the receiver; the acknowledgment log has been returned."
* #complete "Complete" "Processing of the accepted safety report is complete and no further action is expected on the Task."
* #request-for-information-issued "Request for Information Issued" "The regulator has sent a request for information to the sponsor."
* #authorised "Authorised" "The trial or modification has been authorised."

// Statuses used by the label negotiation example (scenario 4; see the Terminology page)
* #labelling-comments-issued "Labelling Comments Issued" "The regulator has returned comments or a revised version to the applicant."
* #counter-proposal-received "Counter-Proposal Received" "The applicant has returned a counter-proposal on the product information."
* #response-received "Response Received" "The applicant’s response has been received."
* #awaiting-applicant-response "Awaiting Applicant Response" "The regulator is waiting for the applicant to respond."
* #labelling-agreed "Labelling Agreed" "Applicant and regulator have agreed the product information text."
