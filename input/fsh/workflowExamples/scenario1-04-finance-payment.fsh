Instance: scenario1-04-finance-payment
InstanceOf: Task
Title: "scenario1 04 finance payment"
Description: "Example Task Request Payment"
Usage: #example
* meta.versionId = "2"
* meta.lastUpdated = "2025-03-06T14:00:00+01:00"
* meta.profile = "http://hl7.org/fhir/uv/apix/StructureDefinition/apix-task"
* identifier.system = "urn:ietf:rfc:3986"
* identifier.value = "urn:uuid:5dbf06dc-e8f5-4f2b-bd69-a034dacb2836"
* partOf = Reference(scenario1-01-initial-submission)
* status = #completed
* businessStatus = http://hl7.org/fhir/uv/apix/CodeSystem/apix-business-status#payment-received "Payment Received"
* intent = #proposal
* priority = #routine
* code = http://hl7.org/fhir/uv/apix/CodeSystem/apix-task-code#request-payment "Request Payment"
* for = Reference(MedicinalProductDefinition/example-ma) "WonderDrug 50mg Tablets"
* groupIdentifier.use = #official
* groupIdentifier.system = "urn:ietf:rfc:3986"
* groupIdentifier.value = "urn:uuid:workflow-group-id-12345"
* authoredOn = "2025-03-05T09:00:00+01:00"
* lastModified = "2025-03-06T14:00:00+01:00"
* requester = Reference(org-ema-srm-hmed) "European Medicines Agency"
* owner = Reference(org-synthpharma-ag) "SynthPharma AG"
* input.type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-task-input-type#regulatory-document "Regulatory Document"
* input.valueReference = Reference(docref-invoice)
* output.type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-task-output-type#regulatory-document "Regulatory Document"
* output.valueReference = Reference(docref-payment-proof)

Instance: docref-invoice
InstanceOf: DocumentReference
Title: "Invoice for Regulatiry Submission Review"
Description: "Example DocumentReference Invoice"
Usage: #example
* id = "docref-invoice"
* status = #current
* docStatus = #final
* version = "1.0"
* type = #m1.0 "Invoice"
* description = "Financial invoice for regulatory submission review"
* content.attachment.contentType = #application/pdf
* content.attachment.url = "https://api.ema.example/binaries/invoices/INV-2025-001.pdf"
* content.attachment.title = "INV-2025-001.pdf"
* content.attachment.size = 450000
* content.attachment.creation = "2025-03-05T08:00:00+01:00"
* identifier[0].system = "urn:ietf:rfc:3986"
* identifier[0].value = "urn:uuid:invoice-docref-uuid"

Instance: docref-payment-proof
InstanceOf: DocumentReference
Title: "docref payment proof"
Description: "Example DocumentReference Proof of Payment"
Usage: #example
* status = #current
* docStatus = #final
* version = "1.0"
* type = #m1.0 "Proof of Payment"
* relatesTo.code = #appends
* relatesTo.target = Reference(docref-invoice) "Invoice #INV-2025-001"
* content.attachment.contentType = #application/pdf
* content.attachment.url = "https://api.synthpharma.example/binaries/payments/confirm-inv-2025-001.pdf"
* content.attachment.title = "Payment-Confirmation.pdf"
* content.attachment.size = 280000
* content.attachment.creation = "2025-03-06T13:30:00+01:00"


