Instance: scenario1-05-technical-question
InstanceOf: Task
Title: "scenario1 05 technical question"
Description: "Example Task Information Request"
Usage: #example
* meta.versionId = "1"
* meta.lastUpdated = "2025-03-01T14:30:00+01:00"
* meta.profile = "http://hl7.org/fhir/uv/apix/StructureDefinition/apix-task"
// * identifier.type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-identifier-type#task-instance-uuid "Task Instance UUID"
* identifier.system = "urn:ietf:rfc:3986"
* identifier.value = "urn:uuid:778e7d2a-8b1c-4d9f-9a2e-1f6c9d8e7b3b"
* partOf = Reference(scenario1-01-initial-submission) "Initial Submission Task"
* status = #requested
* businessStatus = http://hl7.org/fhir/uv/apix/CodeSystem/apix-business-status#clock-stop "Clock Stop"
* intent = #proposal
* priority = #routine
* code = http://hl7.org/fhir/uv/apix/CodeSystem/apix-task-code#information-request "List of Questions / Information Request"
* groupIdentifier.use = #official
* groupIdentifier.system = "urn:ietf:rfc:3986"
* groupIdentifier.value = "urn:uuid:workflow-group-id-12345"
* authoredOn = "2025-03-01T14:30:00+01:00"
* lastModified = "2025-03-01T14:30:00+01:00"
* requester = Reference(org-ema-srm-hmed) "European Medicines Agency"
* owner = Reference(org-synthpharma-ag) "SynthPharma AG"
* input.type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-task-input-type#regulatory-document
* input.valueReference = Reference(docref-list-of-questions) "List of Questions (LoQ)"

Instance: docref-list-of-questions
InstanceOf: DocumentReference
Title: "docref list of questions"
Description: "Example DocumentReference Cover Letter"
Usage: #example
* meta.versionId = "1"
* meta.lastUpdated = "2025-03-01T14:30:00+01:00"
* meta.profile = "http://hl7.org/fhir/uv/apix/StructureDefinition/apix-documentreference"
* status = #current
* docStatus = #final
* version = "1.0"
* type = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#1.0 "Cover Letter"
* date = "2025-03-01T14:30:00+01:00"
* content.attachment.contentType = #application/fhir+json
* content.attachment.url = "https://api.ema.example/questionnaires/q-shelf-life-limit.json"
* content.attachment.title = "List of Questions (Questionnaire)"
* content.attachment.size = 12400
* content.attachment.creation = "2025-03-01T14:20:00+01:00"
* identifier[0].system = "urn:ietf:rfc:3986"
* identifier[0].value = "urn:uuid:40404040-4040-4040-4040-404040404040"
