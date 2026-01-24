Profile: APIXTask
Parent: Task
Id: apix-task
Title: "APIX Regulatory Task"
Description: "Task profile for APIX regulatory submission workflows"
* ^url = "http://hl7.org/fhir/uv/apix/StructureDefinition/apix-task"
* ^version = "0.1.0"
* ^status = #draft
* ^date = "2025-12-13"
* ^publisher = "Gravitate Health Project"

// Meta elements
* meta 1..1
  * versionId 1..1
  * lastUpdated 1..1
  * profile 1..1
    * ^fixedCanonical = "http://hl7.org/fhir/uv/apix/StructureDefinition/apix-task"

* text 1..1 MS
  * ^short = "Human-readable narrative"

// Contained DocumentReferences
* contained 0..* MS
  * ^short = "Embedded resources"
  * ^slicing.discriminator.type = #profile
  * ^slicing.discriminator.path = "$this"
  * ^slicing.rules = #open

* contained contains documentReference 0..*
  * ^short = "Embedded or Referenced Regulatory Document"
  * ^definition = "The official regulatory document content, either embedded (base64) within the Task or referenced via URI (Index Pattern)."

* contained[documentReference] only APIXDocumentReference

// Identifiers with slicing
* identifier 1..2
  * ^short = "Task instance UUID (required) + official regulator procedure number (optional)"
  * ^slicing.discriminator.type = #value
  * ^slicing.discriminator.path = "type.coding.code"
  * ^slicing.rules = #closed
  * ^slicing.description = "One mandatory technical UUID identifier and one optional regulator procedure number"

* identifier contains TaskInstance 1..1 and RegulatorProcedureNumber 0..1

* identifier[TaskInstance]
  * ^short = "Technical UUID for this specific Task instance"
  * type 1..1
    * coding 1..1
      * system = "http://terminology.hl7.org/CodeSystem/v2-0203"
      * code = #RI
  * system = "urn:ietf:rfc:3986"
  * value 1..1
    * ^patternString = "urn:uuid:"

* identifier[RegulatorProcedureNumber]
  * ^short = "Official regulator procedure/submission number (EMA, FDA, PMDA, etc.)"
  * MS
  * type 1..1
    * coding 1..1
      * system = "http://terminology.hl7.org/CodeSystem/v2-0203"
      * code = #RN
  * system 1..1
    * ^patternUri = "https://ema.europa.eu/procedure"
  * value 1..1
    * ^short = "The actual regulator-assigned procedure number (format varies by authority)"

* groupIdentifier 1..1 MS
  * ^short = "Parent/Set ID – groups all Tasks in the same regulatory procedure"

* status 1..1
  * ^binding.strength = #required
  * ^binding.valueSet = "http://hl7.org/fhir/ValueSet/task-status|5.0.0"

* businessStatus 0..1
  * ^short = "Detailed regulatory status (e.g., clock-stop)"
  * ^binding.strength = #required
  * ^binding.valueSet = Canonical(apix-business-status-vs)

* intent 1..1
  * ^fixedCode = #proposal
  * ^binding.strength = #required
  * ^binding.valueSet = "http://hl7.org/fhir/ValueSet/request-intent|5.0.0"

* priority 1..1 MS
  * ^binding.strength = #required
  * ^binding.valueSet = "http://hl7.org/fhir/ValueSet/request-priority|5.0.0"

* code 1..1
  * ^binding.strength = #extensible
  * ^binding.valueSet = Canonical(apix-submission-type-vs)

* description 0..0

* requestedPeriod 0..1 MS
  * ^short = "Requested period for task fulfilment"
  * ^definition = "The period during which the regulatory timeline (e.g., clock start to decision deadline) for the medicinal product procedure or response will be performed."
  * start 0..1 MS
    * ^short = "Clock-start / earliest allowed start"
    * ^definition = "The date/time when the regulatory clock starts or the earliest the task may begin."
    * ^comment = "Example: Day 0 of a marketing-authorisation procedure, validation completion date, etc."
  * end 0..1 MS
    * ^short = "Deadline / clock-stop date"
    * ^definition = "The latest date/time by which the task must be completed."
    * ^comment = "Example: Day 210 of centralised procedure, response deadline to List of Questions, etc."

* authoredOn 1..1

* lastModified 1..1

* requester only Reference(APIXOrganization)
* requester 1..1 MS
  * ^short = "The ''Author'' - e.g. Regulatory Authority or Senior Manager"
  * ^definition = "The person or system that **created** the Task and wants the work done. In regulatory context: The Regulatory Authority (e.g., FDA/EMA) or a senior manager initiating a submission review."

// For CodeableReference, we can constrain the allowed profile for the reference part using 'only CodeableReference(...)'.
* requestedPerformer only CodeableReference(APIXOrganization)
* requestedPerformer 1..1 MS
  * ^short = "The ''Desired Actor'' - e.g. Biologics Team or Dr. Smith"
  * ^definition = "The type of person or specific entity the requester **wants** to do the work. In regulatory context: 'Assign this CMC review to the Biologics Team' (Group) or 'Assign this to Dr. Smith' (Individual)."

* owner only Reference(APIXOrganization)
* owner 0..1 MS
  * ^short = "The ''Accountable Actor'' - e.g. Specific Regulatory Specialist"
  * ^definition = "The person or system currently **responsible** for executing the Task. Use this when a specific user has accepted the task and is currently performing it. Mandatory when status is 'in-progress'."

// Task Input with slicing
* input 0..* MS
  * ^short = "Input parameters for the task"
  * ^definition = "Additional information that may be needed for fulfilment of the task in the context of medicinal product regulatory procedures."
  * ^slicing.discriminator.type = #pattern
  * ^slicing.discriminator.path = "type.coding"
  * ^slicing.rules = #open
  * ^slicing.description = "Slicing by Task.input.type.coding to support regulatoryDocument and future input types"

* input contains regulatoryDocument 0..*

* input[regulatoryDocument]
  * ^short = "Regulatory document (CTD section, via DocumentReference index)"
  * type
    * coding 1..1
      * system = "http://hl7.org/fhir/uv/apix/CodeSystem/apix-task-input-type"
      * code = #regulatory-document
      * display = "Regulatory Document"
  * value[x] 1..1
    * ^type.code = "Reference"
    * ^type.targetProfile = "http://hl7.org/fhir/uv/apix/StructureDefinition/apix-documentreference"

// Task Output with slicing
* output 0..* MS
  * ^short = "Output produced by the task"
  * ^definition = "Outputs produced by the task in the context of medicinal product regulatory procedures."
  * ^slicing.discriminator.type = #pattern
  * ^slicing.discriminator.path = "type.coding"
  * ^slicing.rules = #open
  * ^slicing.description = "Slicing by Task.output.type.coding to support regulatoryDocument and future output types"

* output contains regulatoryDocument 0..*

* output[regulatoryDocument]
  * ^short = "Regulatory document produced as output (via DocumentReference index)"
  * type
    * coding 1..1
      * system = "http://hl7.org/fhir/uv/apix/CodeSystem/apix-task-output-type"
      * code = #regulatory-document
      * display = "Regulatory Document"
  * value[x] 1..1
    * ^type.code = "Reference"
    * ^type.targetProfile = "http://hl7.org/fhir/uv/apix/StructureDefinition/apix-documentreference"

* focus 0..0
* for 0..1 MS
* encounter 0..0
* executionPeriod 0..0
* relevantHistory 0..0
* restriction 0..0
