CodeSystem: APIXBusinessStatusCS
Id: apix-business-status
Title: "APIX Regulatory Business Status"
Description: "Code system for regulatory business status in APIX submissions"
* ^url = "http://hl7.org/fhir/uv/apix/CodeSystem/apix-business-status"
* ^version = "0.1.0"
* ^status = #draft
* ^caseSensitive = true
* ^content = #complete
* ^date = "2025-12-13"
* ^publisher = "Gravitate Health Project"

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
