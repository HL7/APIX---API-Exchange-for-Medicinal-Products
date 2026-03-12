//Instance: scenario1-07-final-decision
//InstanceOf: Task
//Title: "scenario1 07 final decision"
//Description: "Example Task Approval Letter / Positive Decision"
//Usage: #example
//* meta.versionId = "3"
//* meta.lastUpdated = "2025-04-20T09:00:00+01:00"
//* meta.profile = "http://hl7.org/fhir/uv/apix/StructureDefinition/apix-task"
// * identifier.type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-identifier-type#task-instance-uuid "Task Instance UUID"
//* identifier.system = "urn:ietf:rfc:3986"
//* identifier.value = "urn:uuid:999e7d2a-8b1c-4d9f-9a2e-1f6c9d8e7b3d"
//* partOf = Reference(scenario1-01-initial-submission) "Initial Submission Task"
//* status = #completed
//* businessStatus = http://hl7.org/fhir/uv/apix/CodeSystem/apix-business-status#approved "Approved"
//* intent = #proposal
//* priority = #routine
//* code = http://hl7.org/fhir/uv/apix/CodeSystem/apix-task-code#approval "Approval Letter / Positive Decision"
//* for = Reference(MedicinalProductDefinition/example-ma) "WonderDrug 50mg Tablets"
//* groupIdentifier.use = #official
//* groupIdentifier.system = "urn:ietf:rfc:3986"
//* groupIdentifier.value = "urn:uuid:workflow-group-id-12345"
// * groupIdentifier.type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-identifier-type#submission-group-uuid "Submission Group UUID"
//* requester = Reference(Organization/org-ema-srm-hmed) "European Medicines Agency"
//* owner = Reference(Organization/org-synthpharma-ag) "SynthPharma AG"


Instance: scenario1-07-final-decision
InstanceOf: Task
Title: "scenario1-07-final-decision"
Description: "Completetion of Scenario 01 initial submission Task - Example Task Type IB Variation. This is the initial submision Task but in the completed form"
Usage: #example
* meta.versionId = "3"
* meta.lastUpdated = "2026-04-20T09:00:00+01:00"
* meta.profile = "http://hl7.org/fhir/uv/apix/StructureDefinition/apix-task"
* identifier.use = #official
* identifier.system = "urn:ietf:rfc:3986"
* identifier.value = "urn:uuid:f1500e1d-599f-47a6-a38c-ca60a5189726"
// * identifier.type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-identifier-type#task-instance-uuid "Task Instance UUID"
* groupIdentifier.use = #official
* groupIdentifier.system = "urn:ietf:rfc:3986"
* groupIdentifier.value = "urn:uuid:workflow-group-id-12345"
// * groupIdentifier.type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-identifier-type#submission-group-uuid "Submission Group UUID"

* status = #completed

* businessStatus = http://hl7.org/fhir/uv/apix/CodeSystem/apix-business-status#approved "Approved"
* intent = #proposal
* priority = #routine
* code = apix-task-code#variation-type-ib "Type IB Variation"
* authoredOn = "2025-11-15T09:00:00+01:00"

* requester = Reference(org-synthpharma-ag) "SynthPharma AG"
* owner = Reference(org-ema-srm-hmed) "European Medicines Agency"
* input[0].type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-task-input-type#cover-letter "Cover Letter"
* input[0].valueReference = Reference(doc1)
* input[1].type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-task-input-type#regulatory-document "Regulatory Document"
* input[1].valueReference = Reference(doc2)
* input[2].type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-task-input-type#regulatory-document "Regulatory Document"
* input[2].valueReference = Reference(doc3)
* input[3].type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-task-input-type#regulatory-document "Regulatory Document"
* input[3].valueReference = Reference(doc4)
* input[4].type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-task-input-type#regulatory-document "Regulatory Document"
* input[4].valueReference = Reference(doc5)
* input[5].type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-task-input-type#stability-data "Stability Data"
* input[5].valueReference = Reference(doc6)
* input[6].type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-task-input-type#stability-data "Stability Data"
* input[6].valueReference = Reference(doc7)
* input[7].type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-task-input-type#stability-data "Stability Data"
* input[7].valueReference = Reference(doc8)

* lastModified = "2026-04-20T09:00:00+01:00"
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
//* content.attachment.data = "VGhpcyBpcyBhIHBsYWNlaG9sZGVyIGRvY3VtZW50IGZvciB2YWxpZGF0aW9uIHB1cnBvc2VzLgo="
* content.attachment.url = "http://example.org/FHIR/Binary/101"
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
//* content.attachment.data = "VGhpcyBpcyBhIHBsYWNlaG9sZGVyIGRvY3VtZW50IGZvciB2YWxpZGF0aW9uIHB1cnBvc2VzLgo="
* content.attachment.url = "http://example.org/FHIR/Binary/102"
* identifier[0].system = "urn:ietf:rfc:3986"
* identifier[0].value = "urn:uuid:80808080-8080-8080-8080-808080808080"
