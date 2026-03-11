Instance: scenario1-06-technical-response
InstanceOf: Task
Title: "scenario1 06 technical response"
Description: "Example Task Response to Information Request"
Usage: #example
* meta.versionId = "1"
* meta.lastUpdated = "2025-03-15T10:00:00+01:00"
* meta.profile = "http://hl7.org/fhir/uv/apix/StructureDefinition/apix-task"
// * identifier.type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-identifier-type#task-instance-uuid "Task Instance UUID"
* identifier.system = "urn:ietf:rfc:3986"
* identifier.value = "urn:uuid:888e7d2a-8b1c-4d9f-9a2e-1f6c9d8e7b3c"
* partOf = Reference(scenario1-05-technical-question) "Technical Question Task"
* status = #in-progress
* businessStatus = http://hl7.org/fhir/uv/apix/CodeSystem/apix-business-status#submitted "Submitted"
* intent = #proposal
* priority = #routine
* code = http://hl7.org/fhir/uv/apix/CodeSystem/apix-task-code#response-to-questions "Response to Information Request"
* for = Reference(MedicinalProductDefinition/example-ma) "WonderDrug 50mg Tablets"
* groupIdentifier.use = #official
* groupIdentifier.system = "urn:ietf:rfc:3986"
* groupIdentifier.value = "urn:uuid:workflow-group-id-12345"
// * groupIdentifier.type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-identifier-type#submission-group-uuid "Submission Group UUID"
* requester = Reference(org-synthpharma-ag) "SynthPharma AG"
* owner = Reference(org-ema-srm-hmed) "European Medicines Agency"
* authoredOn = "2025-03-15T10:00:00+01:00"
* lastModified = "2025-03-15T10:00:00+01:00"
* output[0].type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-task-output-type#regulatory-document "Regulatory Document"
* output[0].type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-task-output-type#cover-letter "Cover Letter"
* output[0].valueReference = Reference(docref-responses-qresponse) "Applicant QuestionnaireResponse"
* output[+].type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-task-output-type#regulatory-document "Regulatory Document"
* output[1].type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-task-output-type#stability-data "Stability Data"
* output[1].valueReference = Reference(docref-stability-data-annex) "Annex: Updated Stability Data"

Instance: docref-responses-qresponse
InstanceOf: DocumentReference
Title: "docref responses qresponse"
Description: "Example DocumentReference Cover Letter / Response"
Usage: #example
* status = #current
* docStatus = #final
* version = "1.0"
* type = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#1.0 "Cover Letter" //"Response"
* relatesTo.code = http://hl7.org/fhir/document-relationship-type#appends
* relatesTo.target = Reference(docref-list-of-questions) "List of Questions (LoQ)"
* date = "2025-03-15T10:00:00+01:00"
* content.attachment.contentType = #application/fhir+json
* content.attachment.url = "https://api.synthpharma.example/questionnaire-responses/qr123.json"
* content.attachment.title = "Response to Questions (QuestionnaireResponse)"
* content.attachment.size = 18400
* content.attachment.creation = "2025-03-15T09:45:00+01:00"


Instance: docref-stability-data-annex
InstanceOf: DocumentReference
Title: "docref stability data annex"
Description: "Example DocumentReference Stability Data"
Usage: #example
* status = #current
* docStatus = #final
* version = "1.0"
* type = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#3.2.P.8.3 "Stability Data"
* date = "2025-03-15T10:00:00+01:00"
* content.attachment.contentType = #application/fhir+json
* content.attachment.url = "https://api.synthpharma.example/bundles/submission-123/m3/stability-data-v2.json"
* content.attachment.title = "Updated Stability Data (Transaction Bundle)"
* content.attachment.size = 5800000
* content.attachment.creation = "2025-03-14T11:00:00+01:00"
