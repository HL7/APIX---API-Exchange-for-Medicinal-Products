Instance: scenario1-03-finance-invoice
InstanceOf: Task
Title: "scenario1 03 finance invoice original Task"
Description: "Example Task Request Payment - original"
Usage: #example
* meta.versionId = "1"
* meta.lastUpdated = "2025-11-21T09:00:00+01:00"
* meta.profile = "http://hl7.org/fhir/uv/apix/StructureDefinition/apix-task"
* text.status = #additional 
* text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"en\" lang=\"en\"><div style=\"font-family:-apple-system,BlinkMacSystemFont,&apos;Segoe UI&apos;,Roboto,Helvetica,Arial,sans-serif;background:linear-gradient(to bottom,#f2f6fa,#e8eef5);color:#1d1d1f;margin:0;padding:40px 20px;line-height:1.5;\"><div style=\"max-width:1000px;margin:0 auto;\"><div style=\"background:linear-gradient(135deg,#007aff,#5ac8fa);color:#ffffff;padding:40px 24px;border-radius:18px;text-align:center;box-shadow:0 10px 30px rgba(0,122,255,0.3);margin-bottom:36px;\"><div style=\"margin:0 0 8px 0;font-size:32px;font-weight:600;\">Task: Financial Review (Invoice)</div><p style=\"margin:0;opacity:0.95;font-size:17px;\">HL7 FHIR R5 – APIX Implementation Guide</p></div><div style=\"background:#ffffff;border-radius:18px;padding:32px;margin-bottom:32px;box-shadow:0 8px 28px rgba(0,0,0,0.08),0 2px 10px rgba(0,0,0,0.06);\"><div style=\"font-size:24px;font-weight:600;color:#007aff;margin:0 0 24px 0;padding-bottom:12px;border-bottom:1px solid #e5e5ea;display:flex;justify-content:space-between;align-items:center;\">Task Description</div><div style=\"font-size:18px;line-height:1.6;color:#333333;\">Financial Review: Payment Requested</div></div><div style=\"background:#ffffff;border-radius:18px;padding:32px;margin-bottom:32px;box-shadow:0 8px 28px rgba(0,0,0,0.08),0 2px 10px rgba(0,0,0,0.06);\"><div style=\"font-size:24px;font-weight:600;color:#007aff;margin:0 0 24px 0;padding-bottom:12px;border-bottom:1px solid #e5e5ea;display:flex;justify-content:space-between;align-items:center;\">Core Task Information</div><div style=\"display:grid;grid-template-columns:max-content auto;gap:12px 20px;align-items:baseline;\"><span style=\"font-weight:600;color:#555555;text-align:right;min-width:150px;\">Version ID</span><span style=\"color:#1d1d1f;\">1</span><span style=\"font-weight:600;color:#555555;text-align:right;min-width:150px;\">Task ID</span><span style=\"color:#1d1d1f;\">scenario1-03-finance-invoice</span><span style=\"font-weight:600;color:#555555;text-align:right;min-width:150px;\">Group Identifier</span><span style=\"color:#1d1d1f;\">urn:uuid:workflow-group-id-12345</span><span style=\"font-weight:600;color:#555555;text-align:right;min-width:150px;\">Parent Task</span><span style=\"color:#1d1d1f;\">scenario1-01-initial-submission</span><span style=\"font-weight:600;color:#555555;text-align:right;min-width:150px;\">Task Status</span><span style=\"color:#1d1d1f;\"><span style=\"padding:2px 8px;border-radius:12px;font-size:0.9em;font-weight:500;color:#ffffff;background:#17a2b8;\">requested</span></span><span style=\"font-weight:600;color:#555555;text-align:right;min-width:150px;\">Business Status</span><span style=\"color:#1d1d1f;\"><span style=\"padding:2px 8px;border-radius:12px;font-size:0.9em;font-weight:500;color:#ffffff;background:#ffc107;\">Payment Requested</span></span><span style=\"font-weight:600;color:#555555;text-align:right;min-width:150px;\">Intent</span><span style=\"color:#1d1d1f;\">order</span><span style=\"font-weight:600;color:#555555;text-align:right;min-width:150px;\">Priority</span><span style=\"color:#1d1d1f;\">routine</span></div><hr style=\"border:0;border-top:1px solid #eee;margin:20px 0;\" /><div style=\"display:grid;grid-template-columns:max-content auto;gap:12px 20px;align-items:baseline;\"><span style=\"font-weight:600;color:#555555;text-align:right;min-width:150px;\">Code</span><span style=\"color:#1d1d1f;\">Request Payment (request-payment)</span><span style=\"font-weight:600;color:#555555;text-align:right;min-width:150px;\">Authored</span><span style=\"color:#1d1d1f;\">2025-11-21T09:00:00+01:00</span><span style=\"font-weight:600;color:#555555;text-align:right;min-width:150px;\">Last Updated</span><span style=\"color:#1d1d1f;\">2025-11-21T09:00:00+01:00</span></div></div><div style=\"background:#ffffff;border-radius:18px;padding:32px;margin-bottom:32px;box-shadow:0 8px 28px rgba(0,0,0,0.08),0 2px 10px rgba(0,0,0,0.06);\"><div style=\"font-size:24px;font-weight:600;color:#007aff;margin:0 0 24px 0;padding-bottom:12px;border-bottom:1px solid #e5e5ea;display:flex;justify-content:space-between;align-items:center;\">Parties Involved</div><div style=\"margin-bottom:24px;padding-bottom:16px;border-bottom:1px solid #eeeeee;\"><span style=\"font-weight:600;color:#007aff;margin-bottom:4px;display:block;\">Requester</span><div style=\"font-size:16px;font-weight:500;margin-bottom:8px;color:#1d1d1f;\">Health Authority</div><div style=\"font-size:14px;color:#555555;line-height:1.5;\"><strong>Address:</strong> Regulatory Authority Headquarters, 1083 HS Capital City, Country<br /> <strong>Contact:</strong> Scientific and Regulatory Management<br /> <strong>Email:</strong> regulatory@health-authority.example</div></div><div style=\"margin-bottom:0;padding-bottom:0;border-bottom:none;\"><span style=\"font-weight:600;color:#007aff;margin-bottom:4px;display:block;\">Performer</span><div style=\"font-size:16px;font-weight:500;margin-bottom:8px;color:#1d1d1f;\">Pharma Co. Ltd.</div><div style=\"font-size:14px;color:#555555;line-height:1.5;\"><strong>Address:</strong> 123 Synthetic Research Blvd, 4000 Basel, Switzerland<br /> <strong>Contact:</strong> Dr. John Doe, Head of Regulatory Affairs<br /> <strong>Email:</strong> john.doe@synthpharma.example</div></div></div>


<div style=\"background:#ffffff;border-radius:18px;padding:32px;margin-bottom:32px;box-shadow:0 8px 28px rgba(0,0,0,0.08),0 2px 10px rgba(0,0,0,0.06);\"><div style=\"font-size:24px;font-weight:600;color:#007aff;margin:0 0 24px 0;padding-bottom:12px;border-bottom:1px solid #e5e5ea;display:flex;justify-content:space-between;align-items:center;\">Input Documents<span style=\"background:#007aff;color:#ffffff;font-size:14px;font-weight:600;padding:6px 14px;border-radius:20px;\">1 document</span></div>

<div style=\"margin:24px 0;padding:20px;background:#f8fbff;border-radius:14px;border-left:5px solid #007aff;\">

<div style=\"margin:0 0 16px 0;font-size:18px;color:#007aff;font-weight:600;\">Financial Documents</div><div style=\"background:#ffffff;border:1px solid #d1e4ff;border-radius:12px;padding:16px;margin-bottom:12px;box-shadow:0 2px 8px rgba(0,0,0,0.05);\"><div style=\"font-weight:600;color:#007aff;font-size:15px;\">Invoice</div><span style=\"font-family:Menlo,Monaco,Consolas,monospace;background:#e5f2ff;padding:2px 8px;border-radius:6px;font-size:13px;\">invoice</span><br /><a href=\"DocumentReference-docref-invoice.html\">http://example.org/FHIR/DocumentReference/docref-invoice</a><div>Invoice Regulatory Fee</div></div></div></div><div style=\"background:#ffffff;border-radius:18px;padding:32px;margin-bottom:32px;box-shadow:0 8px 28px rgba(0,0,0,0.08),0 2px 10px rgba(0,0,0,0.06);\">

<div style=\"font-size:24px;font-weight:600;color:#007aff;margin:0 0 24px 0;padding-bottom:12px;border-bottom:1px solid #e5e5ea;display:flex;justify-content:space-between;align-items:center;\">Output Documents</div><div style=\"text-align:center;padding:40px 20px;color:#888;background:#f9f9f9;border-radius:14px;\">No output content yet (waiting for payment).</div>

</div>

<div style=\"text-align:center;padding:50px;color:#666666;font-size:14px;\">HL7 FHIR R5 – API Exchange for Medicinal Products (APIX)<br />Generated Render</div>

</div>

</div>"



* identifier.system = "http://example.org/european-med-agency/task-id"
* identifier.value = "urn:uuid:5dbf06dc-e8f5-4f2b-bd69-a034dacb2836"
* identifier.type = http://terminology.hl7.org/CodeSystem/v2-0203#RI "Resource identifier"
* groupIdentifier.use = #official
* groupIdentifier.system = "http://example.org/european-med-agency/work-flow-group-id"
* groupIdentifier.value = "urn:uuid:workflow-group-id-12345"
* authoredOn = "2025-11-21T09:00:00+01:00"
* basedOn = Reference(scenario1-01-initial-submission)
* status = #requested
* intent = #proposal
* priority = #routine
* code = http://hl7.org/fhir/uv/apix/CodeSystem/apix-task-code#request-payment "Request Payment"
//* for = Reference(MedicinalProductDefinition/example-ma) "WonderDrug 50mg Tablets"
* lastModified = "2025-11-21T09:00:00+01:00"
* requester = Reference(org-ema-srm-hmed) "European Medicines Agency"
* owner = Reference(org-synthpharma-ag) "SynthPharma AG"
* input.type = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#invoice-reg-fee "Invoice Regulatory Fee"
* input.valueReference = Reference(docref-invoice)

Instance: docref-invoice
InstanceOf: DocumentReference
Title: "Invoice for Regulatory Submission Review"
Description: "Example DocumentReference Invoice"
Usage: #example
* id = "docref-invoice"
* status = #current
* docStatus = #final
* version = "1.0"
* type = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#invoice-reg-fee "Invoice Regulatory Fee"
* description = "Financial invoice for regulatory submission review"
* content.attachment.contentType = #application/pdf
* content.attachment.url = "https://api.ema.example/binaries/invoices/INV-2025-001.pdf"
* content.attachment.title = "INV-2025-001.pdf"
* content.attachment.size = 450000
* content.attachment.creation = "2025-03-05T08:00:00+01:00"
* identifier[0].system = "urn:ietf:rfc:3986"
* identifier[0].value = "urn:uuid:invoice-docref-uuid"
