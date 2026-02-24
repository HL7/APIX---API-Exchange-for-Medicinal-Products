Instance: scenario1-07-final-decision
InstanceOf: Task
Title: "scenario1 07 final decision"
Description: "Example Task Approval Letter / Positive Decision"
Usage: #example
* meta.versionId = "3"
* meta.lastUpdated = "2025-04-20T09:00:00+01:00"
* meta.profile = "http://hl7.org/fhir/uv/apix/StructureDefinition/apix-task"
// * identifier.type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-identifier-type#task-instance-uuid "Task Instance UUID"
* identifier.system = "urn:ietf:rfc:3986"
* identifier.value = "urn:uuid:999e7d2a-8b1c-4d9f-9a2e-1f6c9d8e7b3d"
* partOf = Reference(scenario1-01-initial-submission) "Initial Submission Task"
* status = #completed
* businessStatus = http://hl7.org/fhir/uv/apix/CodeSystem/apix-business-status#approved "Approved"
* intent = #proposal
* priority = #routine
* code = http://hl7.org/fhir/uv/apix/CodeSystem/apix-task-code#approval "Approval Letter / Positive Decision"
* for = Reference(MedicinalProductDefinition/example-ma) "WonderDrug 50mg Tablets"
* groupIdentifier.use = #official
* groupIdentifier.system = "urn:ietf:rfc:3986"
* groupIdentifier.value = "urn:uuid:workflow-group-id-12345"
// * groupIdentifier.type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-identifier-type#submission-group-uuid "Submission Group UUID"
* requester = Reference(Organization/org-ema-srm-hmed) "European Medicines Agency"
* owner = Reference(Organization/org-synthpharma-ag) "SynthPharma AG"
* authoredOn = "2025-04-20T09:00:00+01:00"
* lastModified = "2025-04-20T09:00:00+01:00"
* output[0].type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-task-output-type#regulatory-document
* output[0].type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-task-input-type#cover-letter "Cover Letter"
* output[0].valueReference = Reference(docref-approval-letter) "Approval Letter"
* output[+].type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-task-output-type#regulatory-document
* output[1].type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-task-input-type#cover-letter "Cover Letter"
* output[1].valueReference = Reference(docref-assessment-report) "Final Assessment Report"

Instance: docref-approval-letter
InstanceOf: DocumentReference
Title: "docref approval letter"
Description: "Example DocumentReference Cover Letter"
Usage: #example
* meta.versionId = "1"
* meta.lastUpdated = "2025-04-20T09:00:00+01:00"
* meta.profile = "http://hl7.org/fhir/uv/apix/StructureDefinition/apix-documentreference"
* status = #current
* type = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#1.0 "Cover Letter"
* date = "2025-04-20T09:00:00+01:00"
* content.attachment.contentType = #application/pdf
* content.attachment.title = "approval-letter.pdf"
* content.attachment.creation = "2025-04-20T09:00:00+01:00"
* content.attachment.data = "VGhpcyBpcyBhIHBsYWNlaG9sZGVyIGRvY3VtZW50IGZvciB2YWxpZGF0aW9uIHB1cnBvc2VzLgo="
* identifier[0].system = "urn:ietf:rfc:3986"
* identifier[0].value = "urn:uuid:70707070-7070-7070-7070-707070707070"


Instance: docref-assessment-report
InstanceOf: DocumentReference
Title: "docref assessment report"
Description: "Example DocumentReference Cover Letter"
Usage: #example
* meta.versionId = "1"
* meta.lastUpdated = "2025-04-20T09:00:00+01:00"
* meta.profile = "http://hl7.org/fhir/uv/apix/StructureDefinition/apix-documentreference"
* status = #current
* type = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#1.0 "Cover Letter"
* date = "2025-04-20T09:00:00+01:00"
* content.attachment.contentType = #application/pdf
* content.attachment.title = "final-assessment-report.pdf"
* content.attachment.creation = "2025-04-20T09:00:00+01:00"
* content.attachment.data = "VGhpcyBpcyBhIHBsYWNlaG9sZGVyIGRvY3VtZW50IGZvciB2YWxpZGF0aW9uIHB1cnBvc2VzLgo="
* identifier[0].system = "urn:ietf:rfc:3986"
* identifier[0].value = "urn:uuid:80808080-8080-8080-8080-808080808080"
