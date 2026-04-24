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
* meta.lastUpdated = "2025-12-22T09:00:00+01:00"
* meta.profile = "http://hl7.org/fhir/uv/apix/StructureDefinition/apix-task"

* text.status = #additional 
* text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"en\" lang=\"en\"><div style=\"font-family:-apple-system,BlinkMacSystemFont,&apos;Segoe UI&apos;,Roboto,Helvetica,Arial,sans-serif;background:linear-gradient(to bottom,#f2f6fa,#e8eef5);color:#1d1d1f;margin:0;padding:40px 20px;line-height:1.5;\"><div style=\"max-width:1000px;margin:0 auto;\"><div style=\"background:linear-gradient(135deg,#007aff,#5ac8fa);color:#ffffff;padding:40px 24px;border-radius:18px;text-align:center;box-shadow:0 10px 30px rgba(0,122,255,0.3);margin-bottom:36px;\"><div style=\"margin:0 0 8px 0;font-size:32px;font-weight:600;\">Task: Approval Letter / Positive Decision</div><p style=\"margin:0;opacity:0.95;font-size:17px;\">HL7 FHIR R5 – APIX Implementation Guide</p></div><div style=\"background:#ffffff;border-radius:18px;padding:32px;margin-bottom:32px;box-shadow:0 8px 28px rgba(0,0,0,0.08),0 2px 10px rgba(0,0,0,0.06);\"><div style=\"font-size:24px;font-weight:600;color:#007aff;margin:0 0 24px 0;padding-bottom:12px;border-bottom:1px solid #e5e5ea;display:flex;justify-content:space-between;align-items:center;\">Task Description</div><div style=\"font-size:18px;line-height:1.6;color:#333333;\">Final Decision: Approval for Type IB Variation</div></div><div style=\"background:#ffffff;border-radius:18px;padding:32px;margin-bottom:32px;box-shadow:0 8px 28px rgba(0,0,0,0.08),0 2px 10px rgba(0,0,0,0.06);\"><div style=\"font-size:24px;font-weight:600;color:#007aff;margin:0 0 24px 0;padding-bottom:12px;border-bottom:1px solid #e5e5ea;display:flex;justify-content:space-between;align-items:center;\">Core Task Information</div><div style=\"display:grid;grid-template-columns:max-content auto;gap:12px 20px;align-items:baseline;\"><span style=\"font-weight:600;color:#555555;text-align:right;min-width:150px;\">Version ID</span><span style=\"color:#1d1d1f;\">3</span>

<span style=\"font-weight:600;color:#555555;text-align:right;min-width:150px;\">Task ID</span><span style=\"color:#1d1d1f;\">in production system will be the same as  scenario1-01-initial-submission</span>

<span style=\"font-weight:600;color:#555555;text-align:right;min-width:150px;\">Instance UUID</span><span style=\"color:#1d1d1f;\">urn:uuid:999e7d2a-8b1c-4d9f-9a2e-1f6c9d8e7b3d</span><span style=\"font-weight:600;color:#555555;text-align:right;min-width:150px;\">Group Identifier</span><span style=\"color:#1d1d1f;\">urn:uuid:workflow-group-id-12345</span><span style=\"font-weight:600;color:#555555;text-align:right;min-width:150px;\">Procedure ID</span><span style=\"color:#1d1d1f;\">PROC-2025-12345</span><span style=\"font-weight:600;color:#555555;text-align:right;min-width:150px;\">Task Status</span><span style=\"color:#1d1d1f;\"><span style=\"padding:2px 8px;border-radius:12px;font-size:0.9em;font-weight:500;color:#ffffff;background:#28a745;\">completed</span></span><span style=\"font-weight:600;color:#555555;text-align:right;min-width:150px;\">Business Status</span><span style=\"color:#1d1d1f;\"><span style=\"padding:2px 8px;border-radius:12px;font-size:0.9em;font-weight:500;color:#ffffff;background:#28a745;\">Approved</span></span><span style=\"font-weight:600;color:#555555;text-align:right;min-width:150px;\">Intent</span><span style=\"color:#1d1d1f;\">proposal</span><span style=\"font-weight:600;color:#555555;text-align:right;min-width:150px;\">Priority</span><span style=\"color:#1d1d1f;\">routine</span></div><hr style=\"border:0;border-top:1px solid #eee;margin:20px 0;\" /><div style=\"display:grid;grid-template-columns:max-content auto;gap:12px 20px;align-items:baseline;\"><span style=\"font-weight:600;color:#555555;text-align:right;min-width:150px;\">Code</span><span style=\"color:#1d1d1f;\">Type IB Variation (variation-type-ib)</span><span style=\"font-weight:600;color:#555555;text-align:right;min-width:150px;\">Authored</span><span style=\"color:#1d1d1f;\">2025-11-15T09:00:00+01:00</span><span style=\"font-weight:600;color:#555555;text-align:right;min-width:150px;\">Last Updated</span><span style=\"color:#1d1d1f;\">2025-12-22T09:00:00+01:00</span></div></div><div style=\"background:#ffffff;border-radius:18px;padding:32px;margin-bottom:32px;box-shadow:0 8px 28px rgba(0,0,0,0.08),0 2px 10px rgba(0,0,0,0.06);\"><div style=\"font-size:24px;font-weight:600;color:#007aff;margin:0 0 24px 0;padding-bottom:12px;border-bottom:1px solid #e5e5ea;display:flex;justify-content:space-between;align-items:center;\">Parties Involved</div>

<div style=\"margin-bottom:24px;padding-bottom:16px;border-bottom:1px solid #eeeeee;\"><span style=\"font-weight:600;color:#007aff;margin-bottom:4px;display:block;\">Requester</span><div style=\"font-size:16px;font-weight:500;margin-bottom:8px;color:#1d1d1f;\">SynthPharma AG</div><div style=\"font-size:14px;color:#555555;line-height:1.5;\"><strong>Address:</strong> 123 Synthetic Research Blvd, 4000 Basel, Switzerland<br /> <strong>Contact:</strong> Dr. John Doe, Head of Regulatory Affairs<br /> <strong>Email:</strong> john.doe@synthpharma.example</div></div><div style=\"margin-bottom:0;padding-bottom:0;border-bottom:none;\"><span style=\"font-weight:600;color:#007aff;margin-bottom:4px;display:block;\">Performer</span><div style=\"font-size:16px;font-weight:500;margin-bottom:8px;color:#1d1d1f;\">Health Authority – Regulatory Review Division</div><div style=\"font-size:14px;color:#555555;line-height:1.5;\"><strong>Address:</strong> Regulatory Authority Headquarters, 1083 HS Capital City, Country<br /> <strong>Contact:</strong> Scientific and Regulatory Management<br /> <strong>Email:</strong> regulatory@health-authority.example</div></div></div>


<div style=\"background:#ffffff;border-radius:18px;padding:32px;margin-bottom:32px;box-shadow:0 8px 28px rgba(0,0,0,0.08),0 2px 10px rgba(0,0,0,0.06);\"><div style=\"font-size:24px;font-weight:600;color:#007aff;margin:0 0 24px 0;padding-bottom:12px;border-bottom:1px solid #e5e5ea;display:flex;justify-content:space-between;align-items:center;\">Input Documents<span style=\"background:#007aff;color:#ffffff;font-size:14px;font-weight:600;padding:6px 14px;border-radius:20px;\">8 documents</span></div><div style=\"margin:24px 0;padding:20px;background:#f8fbff;border-radius:14px;border-left:5px solid #007aff;\">

<div style=\"margin:0 0 16px 0;font-size:18px;color:#007aff;font-weight:600;\">Module 1</div>

<div style=\"background:#ffffff;border:1px solid #d1e4ff;border-radius:12px;padding:16px;margin-bottom:12px;box-shadow:0 2px 8px rgba(0,0,0,0.05);\"><div style=\"font-weight:600;color:#007aff;font-size:15px;\">Cover Letter</div><span style=\"font-family:Menlo,Monaco,Consolas,monospace;background:#e5f2ff;padding:2px 8px;border-radius:6px;font-size:13px;\">cover-letter</span><br /><a href=\"DocumentReference-doc1.html\">http://example.org/FHIR/DocumentReference/cover-letter</a><div>Cover Letter</div></div>

<div style=\"background:#ffffff;border:1px solid #d1e4ff;border-radius:12px;padding:16px;margin-bottom:12px;box-shadow:0 2px 8px rgba(0,0,0,0.05);\"><div style=\"font-weight:600;color:#007aff;font-size:15px;\">Application Form</div><span style=\"font-family:Menlo,Monaco,Consolas,monospace;background:#e5f2ff;padding:2px 8px;border-radius:6px;font-size:13px;\">application-form</span><br /><a href=\"DocumentReference-doc2.html\">http://example.org/FHIR/DocumentReference/application-form</a><div>Application Form</div></div>

<div style=\"background:#ffffff;border:1px solid #d1e4ff;border-radius:12px;padding:16px;margin-bottom:12px;box-shadow:0 2px 8px rgba(0,0,0,0.05);\"><div style=\"font-weight:600;color:#007aff;font-size:15px;\">Annotated Label</div><span style=\"font-family:Menlo,Monaco,Consolas,monospace;background:#e5f2ff;padding:2px 8px;border-radius:6px;font-size:13px;\">annotated-label</span><br /><a href=\"DocumentReference-doc3.html\">http://example.org/FHIR/DocumentReference/annotated-label</a><div>SPC, Labelling and Package Leaflet</div></div>

<div style=\"background:#ffffff;border:1px solid #d1e4ff;border-radius:12px;padding:16px;margin-bottom:12px;box-shadow:0 2px 8px rgba(0,0,0,0.05);\"><div style=\"font-weight:600;color:#007aff;font-size:15px;\">Clean Label</div><span style=\"font-family:Menlo,Monaco,Consolas,monospace;background:#e5f2ff;padding:2px 8px;border-radius:6px;font-size:13px;\">clean-label</span><br /><a href=\"DocumentReference-doc4.html\">http://example.org/FHIR/DocumentReference/clean-label</a><div>SPC, Labelling and Package Leaflet</div></div>

<div style=\"background:#ffffff;border:1px solid #d1e4ff;border-radius:12px;padding:16px;margin-bottom:12px;box-shadow:0 2px 8px rgba(0,0,0,0.05);\"><div style=\"font-weight:600;color:#007aff;font-size:15px;\">Pack Mockup</div><span style=\"font-family:Menlo,Monaco,Consolas,monospace;background:#e5f2ff;padding:2px 8px;border-radius:6px;font-size:13px;\">pack-mockup</span><br /><a href=\"DocumentReference-doc5.html\">http://example.org/FHIR/DocumentReference/mock-ups</a><div>Mock-ups</div></div>

</div><div style=\"margin:24px 0;padding:20px;background:#f8fbff;border-radius:14px;border-left:5px solid #007aff;\"><div style=\"margin:0 0 16px 0;font-size:18px;color:#007aff;font-weight:600;\">Module 3</div>

<div style=\"background:#ffffff;border:1px solid #d1e4ff;border-radius:12px;padding:16px;margin-bottom:12px;box-shadow:0 2px 8px rgba(0,0,0,0.05);\"><div style=\"font-weight:600;color:#007aff;font-size:15px;\">Stability Summary</div><span style=\"font-family:Menlo,Monaco,Consolas,monospace;background:#e5f2ff;padding:2px 8px;border-radius:6px;font-size:13px;\">cmc-stability-summary</span><br /><a href=\"DocumentReference-doc6.html\">http://example.org/FHIR/DocumentReference/stability-summary</a><div>Stability Summary and Conclusion</div></div>

<div style=\"background:#ffffff;border:1px solid #d1e4ff;border-radius:12px;padding:16px;margin-bottom:12px;box-shadow:0 2px 8px rgba(0,0,0,0.05);\"><div style=\"font-weight:600;color:#007aff;font-size:15px;\">Stability Data</div><span style=\"font-family:Menlo,Monaco,Consolas,monospace;background:#e5f2ff;padding:2px 8px;border-radius:6px;font-size:13px;\">cmc-stability-data</span><br /><a href=\"DocumentReference-doc7.html\">http://example.org/FHIR/DocumentReference/stability-data</a><div>Stability Data</div></div>

<div style=\"background:#ffffff;border:1px solid #d1e4ff;border-radius:12px;padding:16px;margin-bottom:12px;box-shadow:0 2px 8px rgba(0,0,0,0.05);\"><div style=\"font-weight:600;color:#007aff;font-size:15px;\">DS Stability Data</div><span style=\"font-family:Menlo,Monaco,Consolas,monospace;background:#e5f2ff;padding:2px 8px;border-radius:6px;font-size:13px;\">cmc-ds-stability-data</span><br /><a href=\"DocumentReference-doc8.html\">http://example.org/FHIR/DocumentReference/stability-drug-substance</a><div>Stability (Drug Substance)</div></div>

</div>
</div>

<div style=\"background:#ffffff;border-radius:18px;padding:32px;margin-bottom:32px;box-shadow:0 8px 28px rgba(0,0,0,0.08),0 2px 10px rgba(0,0,0,0.06);\">


<div style=\"font-size:24px;font-weight:600;color:#007aff;margin:0 0 24px 0;padding-bottom:12px;border-bottom:1px solid #e5e5ea;display:flex;justify-content:space-between;align-items:center;\">Output Documents<span style=\"background:#34c759;color:#ffffff;font-size:14px;font-weight:600;padding:6px 14px;border-radius:20px;\">4 documents</span></div><div style=\"margin:24px 0;padding:20px;background:#f2fff5;border-radius:14px;border-left:5px solid #34c759;\"><div style=\"margin:0 0 16px 0;font-size:18px;color:#34c759;font-weight:600;\">Regulator Output</div>


<div style=\"background:#ffffff;border:1px solid #ccebd3;border-radius:12px;padding:16px;margin-bottom:12px;box-shadow:0 2px 8px rgba(0,0,0,0.05);\"><div style=\"font-weight:600;color:#34c759;font-size:15px;\">Acknowledgement of Receipt</div><span style=\"font-family:Menlo,Monaco,Consolas,monospace;background:#e6f9eb;padding:2px 8px;border-radius:6px;font-size:13px;\">acknowledgement-receipt</span><br /><a href=\"DocumentReference-output-ack.html\">http://example.org/FHIR/DocumentReference/output-ack</a><div>Acknowledgement of Receipt</div></div>

<div style=\"background:#ffffff;border:1px solid #ccebd3;border-radius:12px;padding:16px;margin-bottom:12px;box-shadow:0 2px 8px rgba(0,0,0,0.05);\"><div style=\"font-weight:600;color:#34c759;font-size:15px;\">Validation Report</div><span style=\"font-family:Menlo,Monaco,Consolas,monospace;background:#e6f9eb;padding:2px 8px;border-radius:6px;font-size:13px;\">validation-report</span><br/><a href=\"DocumentReference-output-validation.html\">http://example.org/FHIR/DocumentReference/output-validation</a><div>Validation Report</div></div>

<div style=\"background:#ffffff;border:1px solid #ccebd3;border-radius:12px;padding:16px;margin-bottom:12px;box-shadow:0 2px 8px rgba(0,0,0,0.05);\"><div style=\"font-weight:600;color:#34c759;font-size:15px;\">Approval Letter</div><span style=\"font-family:Menlo,Monaco,Consolas,monospace;background:#e6f9eb;padding:2px 8px;border-radius:6px;font-size:13px;\">regulatory-document</span><br/><a href=\"DocumentReference-docref-approval-letter.html\">http://example.org/FHIR/DocumentReference/docref-approval-letter</a><div>Approval Letter</div></div>

<div style=\"background:#ffffff;border:1px solid #d1e4ff;border-radius:12px;padding:16px;margin-bottom:12px;box-shadow:0 2px 8px rgba(0,0,0,0.05);\"><div style=\"font-weight:600;color:#34c759;font-size:15px;\">Final Assessment Report</div><span style=\"font-family:Menlo,Monaco,Consolas,monospace;background:#e6f9eb;padding:2px 8px;border-radius:6px;font-size:13px;\">regulatory-document</span><br/><a href=\"DocumentReference-docref-assessment-report.html\">http://example.org/FHIR/DocumentReference/docref-assessment-report</a><div>Final Assessment Report</div>
</div>

</div></div>

<div style=\"text-align:center;padding:50px;color:#666666;font-size:14px;\">HL7 FHIR R5 – API Exchange for Medicinal Products (APIX)<br />Generated Render</div></div></div>"


* identifier.use = #official
* identifier.system = "http://example.org/health-authority/task-id"
* identifier.value = "urn:uuid:f1500e1d-599f-47a6-a38c-ca60a5189726"
* identifier.type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-demo#apixtaskinstance "APIX Task Instance ID"
// * identifier.type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-identifier-type#task-instance-uuid "Task Instance UUID"

* identifier[+].use = #official
* identifier[=].system = "http://example.org/health.authority/procedure-number"
* identifier[=].value = "PROC-2025-12345" //"EMEA/H/C/001234/IB/0025"
* identifier[=].type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-demo#apixregulatorprocedureno "APIX Regulator Procedure Number"

* groupIdentifier.use = #official
* groupIdentifier.system = "http://example.org/health-authority/work-flow-group-id"
* groupIdentifier.value = "urn:uuid:workflow-group-id-12345"
// * groupIdentifier.type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-identifier-type#submission-group-uuid "Submission Group UUID"

* status = #completed
* businessStatus = http://hl7.org/fhir/uv/apix/CodeSystem/apix-business-status#approved "Approved"
* intent = #proposal
* priority = #routine
* code = apix-task-code#variation-type-ib "Type IB Variation"
* authoredOn = "2025-11-15T09:00:00+01:00"

* requester = Reference(org-synthpharma-ag) "SynthPharma AG"
* owner = Reference(org-ema-srm-hmed) "Health Authority"
* input[0].type = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#1.0 "Cover Letter"
* input[0].valueReference = Reference(doc1)
* input[1].type = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#application-form "Application Form"
* input[1].valueReference = Reference(doc2)
* input[2].type = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#1.14.1.2 "Annotated draft labeling text"
* input[2].valueReference = Reference(doc3)
* input[3].type = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#1.14.1.3 "Draft labeling text"
* input[3].valueReference = Reference(doc4)
* input[4].type = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#1.3.2 "Mock-ups"
* input[4].valueReference = Reference(doc5)
* input[5].type = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#3.2.P.8.1 "Stability Summary and Conclusion"
* input[5].valueReference = Reference(doc6)
* input[6].type = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#3.2.P.8.3 "Stability Data"
* input[6].valueReference = Reference(doc7)
* input[7].type =  http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#3.2.S.7 "Stability (Drug Substance)" //http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#3.2.P.8.2 "Post-approval Stability Protocol and Commitment"
* input[7].valueReference = Reference(doc8)

* lastModified = "2025-12-22T09:00:00+01:00"

* output[0].type = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#acknowledgement-receipt "Acknowledgement of Receipt"
* output[=].valueReference = Reference(output-ack) "Acknowledgement of Receipt"
* output[+].type = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#validation-report "Validation Report"
* output[=].valueReference = Reference(output-validation) "Validation Report"

* output[+].type = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#approval-letter "Approval Letter"
* output[=].valueReference = Reference(docref-approval-letter) "Approval Letter"
* output[+].type = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#assessment-report "Assessment Report"
* output[=].valueReference = Reference(docref-assessment-report) "Final Assessment Report"

Instance: docref-approval-letter
InstanceOf: DocumentReference
Title: "docref approval letter"
Description: "Example DocumentReference Approval Letter"
Usage: #example
* meta.versionId = "1"
* meta.lastUpdated = "2025-12-22T09:00:00+01:00"
* meta.profile = "http://hl7.org/fhir/uv/apix/StructureDefinition/apix-documentreference"
* status = #current
* type = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#approval-letter "Approval Letter"
* date = "2025-12-22T09:00:00+01:00"
* content.attachment.contentType = #application/pdf
* content.attachment.title = "approval-letter.pdf"
* content.attachment.creation = "2025-12-22T09:00:00+01:00"
//* content.attachment.data = "VGhpcyBpcyBhIHBsYWNlaG9sZGVyIGRvY3VtZW50IGZvciB2YWxpZGF0aW9uIHB1cnBvc2VzLgo="
* content.attachment.url = "http://example.org/FHIR/Binary/101"
* identifier[0].system = "http://example.org/health-authority/docref-id"
* identifier[0].value = "urn:uuid:70707070-7070-7070-7070-707070707070"


Instance: docref-assessment-report
InstanceOf: DocumentReference
Title: "docref assessment report"
Description: "Example DocumentReference Assessment Report"
Usage: #example
* meta.versionId = "1"
* meta.lastUpdated = "2025-12-22T09:00:00+01:00"
* meta.profile = "http://hl7.org/fhir/uv/apix/StructureDefinition/apix-documentreference"
* status = #current
* type = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#assessment-report "Assessment Report"
* date = "2025-12-22T09:00:00+01:00"
* content.attachment.contentType = #application/pdf
* content.attachment.title = "final-assessment-report.pdf"
* content.attachment.creation = "2025-12-22T09:00:00+01:00"
//* content.attachment.data = "VGhpcyBpcyBhIHBsYWNlaG9sZGVyIGRvY3VtZW50IGZvciB2YWxpZGF0aW9uIHB1cnBvc2VzLgo="
* content.attachment.url = "http://example.org/FHIR/Binary/102"
* identifier[0].system = "urn:ietf:rfc:3986"
* identifier[0].value = "urn:uuid:80808080-8080-8080-8080-808080808080"
