Instance: scenario1-02-validation
InstanceOf: Task
Title: "scenario1 02 validation"
Description: "Example Task Type IB Variation"
Usage: #example
* meta.versionId = "2"
* meta.lastUpdated = "2025-11-20T14:30:00+01:00"
* meta.profile = "http://hl7.org/fhir/uv/apix/StructureDefinition/apix-task"
* basedOn = Reference(scenario1-01-initial-submission)
* identifier[0].use = #official
* identifier[=].system = "urn:ietf:rfc:3986"
* identifier[=].value = "urn:uuid:d7f9bc88-658f-418a-ba4c-40307099603e"
// * identifier[=].type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-identifier-type#task-instance-uuid "Task Instance UUID"
* identifier[+].use = #official
* identifier[=].system = "http://ema.europa.eu/procedure-number"
* identifier[=].value = "EMEA/H/C/001234/IB/0025"
// * identifier[=].type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-identifier-type#regulator-procedure-number "Regulator Procedure Number"
* groupIdentifier.use = #official
* groupIdentifier.system = "urn:ietf:rfc:3986"
* groupIdentifier.value = "urn:uuid:workflow-group-id-12345"
// * groupIdentifier.type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-identifier-type#submission-group-uuid "Submission Group UUID"
* status = #accepted
* businessStatus = http://hl7.org/fhir/uv/apix/CodeSystem/apix-business-status#validation-successful "Validation Successful"
* intent = #proposal
* priority = #routine
* code = apix-task-code#variation-type-ib "Type IB Variation"
* authoredOn = "2025-11-15T09:00:00+01:00"
* lastModified = "2025-11-20T14:30:00+01:00"
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
* input[8].type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-task-input-type#stability-data "Stability Data"
* input[8].valueReference = Reference(doc9)
* input[9].type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-task-input-type#stability-data "Stability Data"
* input[9].valueReference = Reference(doc10)
* output[0].type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-task-output-type#regulatory-document "Regulatory Document"
* output[0].valueReference = Reference(output-ack)
* output[1].type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-task-output-type#regulatory-document "Regulatory Document"
* output[1].valueReference = Reference(output-validation)

Instance: doc9
InstanceOf: DocumentReference
Title: "doc9"
Description: "Example DocumentReference"
Usage: #example
* status = #current
* type = #cmc-ds-stability-summary "DS Stability Summary"
* content.attachment.title = "CMC Doc 4 - DS Summary.pdf"


Instance: doc10
InstanceOf: DocumentReference
Title: "doc10"
Description: "Example DocumentReference"
Usage: #example
* status = #current
* type = #cmc-ds-stability-data "DS Stability Data"
* content.attachment.title = "CMC Doc 5 - DS Data.pdf"


Instance: output-ack
InstanceOf: DocumentReference
Title: "output ack"
Description: "Example DocumentReference Acknowledgement of Receipt"
Usage: #example
* status = #current
* type = #acknowledgement-receipt "Acknowledgement of Receipt"
* content.attachment.title = "Acknowledgement_Letter.pdf"
* content.attachment.contentType = #application/pdf


Instance: output-validation
InstanceOf: DocumentReference
Title: "output validation"
Description: "Example DocumentReference Validation Report"
Usage: #example
* status = #current
* type = #validation-report "Validation Report"
* content.attachment.title = "Validation_Report.pdf"
* content.attachment.contentType = #application/pdf
