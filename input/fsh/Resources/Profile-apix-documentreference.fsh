//"urn:uuid:778e7d2a-8b1c-4d9f-9a2e-1f6c9d8e7b3b"
Invariant: identifier-is-a-uuid
Description: "Identifier value must be a urn:uuid"
Severity: #error
Expression: "value.matches('^urn:uuid:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')"


Profile: APIXDocumentReference
Parent: DocumentReference
Id: apix-documentreference
Title: "APIX Regulatory DocumentReference"
Description: "DocumentReference profile used in APIX regulatory submissions. Supports both embedded base64 data and referenced binaries via URL (Index Pattern). Includes support for versioning, lifecycle status, and CTD section categorization."
* ^url = "http://hl7.org/fhir/uv/apix/StructureDefinition/apix-documentreference"


* ^date = "2025-12-20"


//* identifier 2..2 MS
//  * ^short = "Unique permanent identifier for this document set"
//  * ^definition = "Business identifier that remains constant across all versions (typically a UUID). Required for traceability in regulatory submissions."

// Identifiers with slicing
* identifier 2..2 MS 
  * ^short = "Document Set Identifier and Document Version Identifier "
  * ^definition = "Business identifiers that remains constant. Required for traceability in regulatory submissions."
  * ^slicing.discriminator[0].type = #value
  * ^slicing.discriminator[0].path = "type"
  * ^slicing.description = "slices illustrate the requirement to have one document set identifier and one document version identifier"
  * ^slicing.rules = #open

* identifier contains docSetIdentifier 1..1 MS and documentVersionIdentifier 1..1 MS

* identifier[docSetIdentifier] obeys identifier-is-a-uuid
  * ^short = "Document Set Identifier"
  * MS
  * type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-demo#docsetid "Document Set Identifier"
  * system 1..1
  * value 1..1

* identifier[documentVersionIdentifier] obeys identifier-is-a-uuid
  * ^short = "Document Version Identifier"
  * MS
  * system 1..1
  * value 1..1
  * type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-demo#docverid "Document Version Identifier"
  
* status 1..1
  * ^short = "current | superseded | entered-in-error"
  * ^definition = "Technical status of the document reference. Typically 'current' for submissions."

* docStatus 0..1 MS
  * ^short = "preliminary | final | amended | appended"
  * ^definition = "Lifecycle status of the document content."

* version 0..1 MS
  * ^short = "Business version of the document (e.g. 1.0, 2.1)"

* category 0..1 MS
  * ^short = "High-level categorization (e.g. CTD Module 1, Clinical Trial Data)"
  * ^binding.strength = #extensible
  * ^binding.valueSet = Canonical(apix-ctd-module-vs)

* type 1..1 MS
  * ^short = "CTD section code (e.g. 3.2.S.1.1)"
  * ^definition = "Coded representation of the specific document type or CTD section."
  * ^binding.strength = #required
  * ^binding.valueSet = Canonical(apix-ctd-section-vs)

* relatesTo 0..* MS
  * ^short = "Relationships to other documents"
  * ^definition = "Used to link this document to previous versions (supersedes) or related material."

* description 0..1 MS
  * ^short = "Human-readable summary of the document"

* subject MS
  * ^short = "Used to link to specific products, such as a `MedicinalProductDefinition`"

* securityLabel 0..* MS
  * ^short = "Confidentiality/Security labels"

* date 1..1
  * ^short = "Date/time this document reference was created"
  * ^definition = "The date and time this metadata record was created for the submission."

* content 1..1
  * ^short = "Document content"

* content.attachment 1..1
  * ^short = "Attachment with document data"

* content.attachment.contentType 1..1
  * ^short = "MIME type of the document"

* content.attachment.data 0..1
  * ^short = "Embedded base64 content (optional in Index Pattern)"
  * ^definition = "The full document content can be embedded here if desired, but for large files, use 'url' instead."

* content.attachment.url 1..1
  * ^short = "Reference to document on FHIR server or external URL"
  * ^definition = "The URL where the document content can be retrieved. This allows for the 'Index Pattern' where large binaries are stored separately."

* content.attachment.size 0..1 MS
  * ^short = "Size of the document in bytes"

* content.attachment.title 1..1
  * ^short = "Human-readable title of the document"

* content.attachment.creation 1..1
  * ^short = "Date/time the document was created"

* content.attachment.hash 0..1 MS
  * ^short = "Integrity check for the document content"
