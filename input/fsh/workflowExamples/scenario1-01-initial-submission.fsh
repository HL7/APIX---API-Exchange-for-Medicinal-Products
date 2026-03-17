Instance: scenario1-01-initial-submission
InstanceOf: Task
Title: "scenario1 01 initial submission"
Description: "Example Task Type IB Variation"
Usage: #example
* meta.versionId = "1"
* meta.lastUpdated = "2025-11-15T09:00:00+01:00"
* meta.profile = "http://hl7.org/fhir/uv/apix/StructureDefinition/apix-task"
* identifier.use = #official
* identifier.system = "http://example.org/european-med-agency/task-id"
* identifier.value = "urn:uuid:f1500e1d-599f-47a6-a38c-ca60a5189726"
* identifier.type = http://terminology.hl7.org/CodeSystem/v2-0203#RI "Resource identifier"
// * identifier.type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-identifier-type#task-instance-uuid "Task Instance UUID"
* groupIdentifier.use = #official
* groupIdentifier.system = "http://example.org/european-med-agency/work-flow-group-id"
* groupIdentifier.value = "urn:uuid:f1500e1d-599f-47a6-a38c-ca60a5189727"
// * groupIdentifier.type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-identifier-type#submission-group-uuid "Submission Group UUID"
* status = #requested
* businessStatus = http://hl7.org/fhir/uv/apix/CodeSystem/apix-business-status#submitted "Submitted"
* intent = #proposal
* priority = #routine
* code = apix-task-code#variation-type-ib "Type IB Variation"
* authoredOn = "2025-11-15T09:00:00+01:00"
* lastModified = "2025-11-15T09:00:00+01:00"
* requester = Reference(org-synthpharma-ag) "SynthPharma AG"
* owner = Reference(org-ema-srm-hmed) "European Medicines Agency"
* input[0].type = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#1.0 "Cover Letter"
* input[0].valueReference = Reference(doc1)
* input[1].type = #application-form "Application Form"
* input[1].valueReference = Reference(doc2)
* input[2].type = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#1.3.1 "SPC, Labelling and Package Leaflet"
* input[2].valueReference = Reference(doc3)
* input[3].type = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#1.3.1 "SPC, Labelling and Package Leaflet" 
* input[3].valueReference = Reference(doc4)
* input[4].type = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#1.3.2 "Mock-ups"
* input[4].valueReference = Reference(doc5)
* input[5].type = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#3.2.P.8.1 "Stability Summary and Conclusion"
* input[5].valueReference = Reference(doc6)
* input[6].type = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#3.2.P.8.3 "Stability Data"
* input[6].valueReference = Reference(doc7)
* input[7].type =  http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#3.2.S.7 "Stability (Drug Substance)" //http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#3.2.P.8.2 "Post-approval Stability Protocol and Commitment"
* input[7].valueReference = Reference(doc8)

Instance: doc1
InstanceOf: DocumentReference
Title: "doc1"
Description: "Example DocumentReference Cover Letter"
Usage: #example
* status = #current
* docStatus = #final
* version = "1.0"
//* category = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-module#m1 "Module 1"
* category = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#m1 "Module 1"

* type = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#1.0 "Cover Letter"
* content.attachment.contentType = #application/pdf
* content.attachment.url = "https://api.synthpharma.example/binaries/submission-123/m1/cover-letter.pdf"
* content.attachment.title = "Cover Letter.pdf"
* content.attachment.size = 1250000
* content.attachment.creation = "2025-11-15T08:30:00+01:00"

Instance: doc2
InstanceOf: DocumentReference
Title: "doc2"
Description: "Example DocumentReference Application Form"
Usage: #example
* status = #current
* docStatus = #final
* version = "1.0"
//* category = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-module#m1 "Module 1"
* category = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#m1 "Module 1"
* type = #application-form "Application Form"
* content.attachment.contentType = #application/pdf
* content.attachment.url = "https://api.synthpharma.example/binaries/submission-123/m1/app-form.pdf"
* content.attachment.title = "Application Form.pdf"
* content.attachment.size = 3400000
* content.attachment.creation = "2025-11-15T08:35:00+01:00"

Instance: doc3
InstanceOf: DocumentReference
Title: "doc3"
Description: "Example DocumentReference Annotated Label"
Usage: #example
* status = #current
* docStatus = #final
* version = "1.0"
//* category = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-module#m1 "Module 1"
* category = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#m1 "Module 1"
* type = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#1.3.1 "SPC, Labelling and Package Leaflet" //"annotated-label "Annotated Label"
* content.attachment.contentType = #application/fhir+json
* content.attachment.url = "https://api.synthpharma.example/bundles/submission-123/m1/annotated-label.json"
* content.attachment.title = "Annotated Label (Bundle)"
* content.attachment.size = 45000
* content.attachment.creation = "2025-11-14T16:00:00+01:00"

Instance: doc4
InstanceOf: DocumentReference
Title: "doc4"
Description: "Example DocumentReference Clean Label"
Usage: #example
* status = #current
* docStatus = #final
* version = "1.0"
//* category = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-module#m1 "Module 1"
* category = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#m1 "Module 1"
* type = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#1.3.1 "SPC, Labelling and Package Leaflet" //"clean-label "Clean Label"
* content.attachment.contentType = #application/fhir+json
* content.attachment.url = "https://api.synthpharma.example/bundles/submission-123/m1/clean-label.json"
* content.attachment.title = "Clean Label (Bundle)"
* content.attachment.size = 42000
* content.attachment.creation = "2025-11-14T16:05:00+01:00"

Instance: doc5
InstanceOf: DocumentReference
Title: "doc5"
Description: "Example DocumentReference Pack Mockup"
Usage: #example
* status = #current
* docStatus = #final
* version = "1.0"
* type = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#1.3.2 "Mock-ups" //"Pack Mockup"
* content.attachment.contentType = #text/html
* content.attachment.url = "https://api.synthpharma.example/binaries/submission-123/m1/mockup.html"
* content.attachment.title = "Pack Mockup.html"
* content.attachment.size = 890000
* content.attachment.creation = "2025-11-14T10:00:00+01:00"

Instance: doc6
InstanceOf: DocumentReference
Title: "doc6"
Description: "Example DocumentReference Stability Summary"
Usage: #example
* status = #current
* docStatus = #final
* version = "1.0"
* category = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#m3 "Module 3"
* type = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#3.2.P.8.1 "Stability Summary and Conclusion"
* content.attachment.contentType = #application/fhir+json
* content.attachment.url = "Binary/binary-1004"
* content.attachment.title = "STABILITY SUMMARY AND CONCLUSIONS ON STELBAT TABLETS, 20 MG"
* content.attachment.size = 116000
* content.attachment.creation = "2025-11-12T14:30:00+01:00"

Instance: doc7
InstanceOf: DocumentReference
Title: "doc7"
Description: "Example DocumentReference Stability Data"
Usage: #example
* status = #current
* docStatus = #final
* version = "1.0"
//* category = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-module#m3 "Module 3"
* category = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#m3 "Module 3"
* type = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#3.2.P.8.3 "Stability Data"
* content.attachment.contentType = #application/fhir+json
* content.attachment.url = "Binary/binary-1005"
* content.attachment.title = "STABILITY DATA ON STELBAT TABLETS, 20MG"
* content.attachment.size = 312000
* content.attachment.creation = "2025-11-12T14:35:00+01:00"

Instance: doc8
InstanceOf: DocumentReference
Title: "doc8"
Description: "Example DocumentReference Stability Data"
Usage: #example
* status = #current
* docStatus = #final
* version = "1.0"
//* category = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-module#m3 "Module 3"
* category = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#m3 "Module 3"
//* type = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#3.2.P.8.2 "Post-approval Stability Protocol and Commitment"
* type = http://hl7.org/fhir/uv/apix/CodeSystem/ctd-section#3.2.S.7 "Stability (Drug Substance)"
* content.attachment.contentType = #application/fhir+json
//* content.attachment.url = "https://api.synthpharma.example/bundles/submission-123/m3/stability-commitment.json"
* content.attachment.url = "Binary/binary-1006"
* content.attachment.title = "STABILITY DATA ON API"
* content.attachment.size = 238000
* content.attachment.creation = "2025-11-12T14:40:00+01:00"