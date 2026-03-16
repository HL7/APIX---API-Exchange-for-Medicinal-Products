Instance: scenario1-03-finance-invoice
InstanceOf: Task
Title: "scenario1 03 finance invoice original Task"
Description: "Example Task Request Payment - original"
Usage: #example
* meta.versionId = "1"
* meta.lastUpdated = "2025-03-05T09:00:00+01:00"
* meta.profile = "http://hl7.org/fhir/uv/apix/StructureDefinition/apix-task"
* identifier.system = "http://example.org/european-med-agency/task-id"
* identifier.value = "urn:uuid:5dbf06dc-e8f5-4f2b-bd69-a034dacb2836"
* identifier.type = http://terminology.hl7.org/CodeSystem/v2-0203#RI "Resource identifier"
* groupIdentifier.use = #official
* groupIdentifier.system = "http://example.org/european-med-agency/work-flow-group-id"
* groupIdentifier.value = "urn:uuid:workflow-group-id-12345"
* authoredOn = "2025-03-05T09:00:00+01:00"
* partOf = Reference(scenario1-01-initial-submission)
* status = #requested
* intent = #proposal
* priority = #routine
* code = http://hl7.org/fhir/uv/apix/CodeSystem/apix-task-code#request-payment "Request Payment"
//* for = Reference(MedicinalProductDefinition/example-ma) "WonderDrug 50mg Tablets"
* lastModified = "2025-03-05T09:00:00+01:00"
* requester = Reference(org-ema-srm-hmed) "European Medicines Agency"
* owner = Reference(org-synthpharma-ag) "SynthPharma AG"
* input.type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-task-input-type#regulatory-document "Regulatory Document"
* input.valueReference = Reference(docref-invoice)

Instance: docref-invoice
InstanceOf: DocumentReference
Title: "Invoice for Regulatiry Submission Review"
Description: "Example DocumentReference Invoice"
Usage: #example
* id = "docref-invoice"
* status = #current
* docStatus = #final
* version = "1.0"
* type = #invoice "Invoice"
* description = "Financial invoice for regulatory submission review"
* content.attachment.contentType = #application/pdf
* content.attachment.url = "https://api.ema.example/binaries/invoices/INV-2025-001.pdf"
* content.attachment.title = "INV-2025-001.pdf"
* content.attachment.size = 450000
* content.attachment.creation = "2025-03-05T08:00:00+01:00"
* identifier[0].system = "urn:ietf:rfc:3986"
* identifier[0].value = "urn:uuid:invoice-docref-uuid"
