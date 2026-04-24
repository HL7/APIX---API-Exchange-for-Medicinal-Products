//* statusReason
//needs constriant Mandatory when status = rejected or cancelled
Invariant: statusreason-conditional-require
Description: "A status reason is required when the status is rejected or cancelled."
Severity: #error
Expression: "((status = 'rejected') or (status = 'cancelled')) implies statusReason.exists()"
//Expression: "(((status = 'rejected') or (status = 'cancelled')) and statusReason.exists()) or (((status = 'rejected') or (status = 'cancelled')).not())"

//"urn:uuid:778e7d2a-8b1c-4d9f-9a2e-1f6c9d8e7b3b"
Invariant: identifier-is-uuid
Description: "Identifier value must be a urn:uuid"
Severity: #error
Expression: "value.matches('^urn:uuid:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')"

Invariant: identifier-has-a-uuid
Description: "Identifier has at least one value that is a urn:uuid"
Severity: #error
Expression: "identifier.value.exists(matches('^urn:uuid:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'))"
//"value.matches('^urn:uuid:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')"

Invariant: is-a-uuid
Description: "Identifier has at least one value that is a urn:uuid"
Severity: #error
Expression: "matches('^urn:uuid:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')"


Profile: APIXTask
Parent: Task
Id: apix-task
Title: "APIX Regulatory Task"
Description: "Task profile for APIX regulatory submission workflows"

// if placed on statusReason it will be ignored when statusReason is absent
* obeys statusreason-conditional-require

// Meta elements
* meta 1..1
  * versionId 1..1
//  * lastUpdated 1..1
  * lastUpdated ^short = "Automatically updated on every change"
//  * profile 1..1
//  * profile = "http://hl7.org/fhir/uv/apix/StructureDefinition/apix-task"

* text 1..1 MS
  * ^short = "Human-readable narrative"

// DEPRECATED - Contained DocumentReferences
//* contained 0..* MS
//  * ^short = "Embedded resources"
//  * ^slicing.discriminator.type = #profile
//  * ^slicing.discriminator.path = "$this"
//  * ^slicing.rules = #open
//* contained contains documentReference 0..*
//  * ^short = "Embedded or Referenced Regulatory Document"
//  * ^definition = "The official regulatory document content, either embedded (base64) within the Task or referenced via URI (Index Pattern)."
//* contained[documentReference] only APIXDocumentReference

// Identifiers with slicing
* identifier 1..* MS //obeys identifier-has-a-uuid
  * ^short = "Task instance UUID (required) + official regulator procedure number (optional), other identifiers allowed as well"
  * ^slicing.discriminator[0].type = #value
  * ^slicing.discriminator[0].path = "type"
  //* ^slicing.discriminator[1].type = #value
  //* ^slicing.discriminator[1].path = "system"
  //* ^slicing.discriminator[1].type = #exists
  //* ^slicing.discriminator[1].path = "value"

  * ^slicing.description = "slices illustrate the requirement to have at least one identifier that is a UUID for the Task instance, and optionally an offical regulator procedure number"
  * ^slicing.rules = #open
  //* ^slicing.description = "At least one mandatory technical UUID identifier. A regulator procedure number is optional."

* identifier contains TaskInstance 1..* MS and RegulatorProcedureNumber 0..1 MS

* identifier[TaskInstance] obeys identifier-is-uuid
  * ^short = "Technical UUID for this specific Task instance"
  //* ^defintion = "Slice highlights that a Technical UUID for this specific Task instance is needed"
  //* type = http://terminology.hl7.org/CodeSystem/v2-0203#RI "Resource identifier"
  * type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-demo#apixtaskinstance "APIX Task Instance ID"
  //* system = "urn:ietf:rfc:3986"
  * value 1..1
  * value obeys is-a-uuid

* identifier[RegulatorProcedureNumber]
  * ^short = "Official regulator procedure/submission number (EMA, FDA, PMDA, etc.)"
  //* ^definition = "Slice highlights that a procedure/submission number is useful."
  * MS
  * system 1..1
  //  * ^patternUri = "http://example.org/health.authority/procedure-number" //"https://ema.europa.eu/procedure"
  * value 1..1
    //* ^constraint[0].expression = "value.empty() or not(value.matches('^urn:uuid:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'))"
    * ^short = "The actual regulator-assigned procedure number (format varies by authority)"
  * type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-demo#apixregulatorprocedureno "APIX Regulator Procedure Number"

* groupIdentifier 1..1 MS
  * ^short = "Parent/Set ID – groups all Tasks in the same regulatory procedure"

* businessStatus 0..1
  * ^short = "Detailed regulatory status (e.g., clock-stop)"
  * ^binding.strength = #example
  * ^binding.valueSet = Canonical(apix-business-status-vs)
  * ^binding.description = "Detailed regulatory status such as clock-stop"
  
* statusReason ^short = "Required if status is rejected or cancelled"
* statusReason ^definition = "Required if status is rejected or cancelled. Reason for current status." 

* intent 1..1
* intent = http://hl7.org/fhir/request-intent#proposal

* code 1..1 MS
  * ^short = "Defines the regulatory message type and triggers specific business rules"
  * ^definition = "Defines the regulatory message type and triggers specific business rules"
  * ^binding.strength = #example
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
* authoredOn ^short = "Date/time the sender created the Task"
* authoredOn ^definition = "Starting point for regulatory cycle-time metrics."

* lastModified 1..1

* requester only Reference(APIXOrganization)
* requester 1..1 MS
  * ^short = "Organization that initiated the task"
  * ^definition = "The person or system that **created** the Task and wants the work done. In regulatory context: The Regulatory Authority (e.g., FDA/EMA) or a senior manager initiating a submission review."
  
* performer
* performer 0..1 MS
  * ^short = "Organization or individual who performed the task"
  * ^definition = "Organization or individual who performed the task. Can be different from the Task.owner."
 
//Deprecated
// For CodeableReference, we can constrain the allowed profile for the reference part using 'only CodeableReference(...)'.
//* requestedPerformer only CodeableReference(APIXOrganization)
//* requestedPerformer 0..1 MS
//  * ^short = "The ''Desired Actor'' - e.g. Biologics Team or Dr. Smith"
//  * ^definition = "The type of person or specific entity the requester **wants** to do the work. In regulatory context: 'Assign this CMC review to the Biologics Team' (Group) or 'Assign this to Dr. Smith' (Individual)."

* owner only Reference(APIXOrganization)
* owner 0..1 MS
  * ^short = "The Organization accountable for fulfilling the Task."
  * ^definition = "The organization, person or system currently **responsible** for fulfillng the Task."

// Task Input with slicing
* input 0..* MS
  * ^short = "Input parameters for the task"
  * ^definition = "Additional information that may be needed for fulfilment of the task in the context of medicinal product regulatory procedures."
* input.type MS
  * ^short = "Input type  indicates the type of input, such as the code used as a DocumentReference type"
  * ^binding.strength = #example
  * ^binding.valueSet = Canonical(apix-ctd-section-vs)
//* input ^slicing.discriminator.type = #value
//* input ^slicing.discriminator.path = "type"
//* input ^slicing.rules = #open  
//* input ^slicing.description = "Slicing to support regulatoryDocument and future input types"

//* input contains regulatoryDocument 0..* MS
//* input[regulatoryDocument]
//  * ^short = "Regulatory document (CTD section, via DocumentReference index)"
//* input[regulatoryDocument].type = http://hl7.org/fhir/uv/apix/CodeSystem/apix-task-input-type#regulatory-document "Regulatory Document"
//* input[regulatoryDocument].value[x] only Reference(APIXDocumentReference)

// Task Output with slicing
* output 0..* MS
  * ^short = "Output produced by the task"
  * ^definition = "Outputs produced by the task in the context of medicinal product regulatory procedures."
* output.type MS
  * ^short = "Output type indicates the type of output, such as the code used as a DocumentReference type"
  * ^binding.strength = #example
  * ^binding.valueSet = Canonical(apix-ctd-section-vs)
//  * ^slicing.discriminator.type = #value
//  * ^slicing.discriminator.path = "type"
//  * ^slicing.rules = #open
//  * ^slicing.description = "Slicing by Task.output.type.coding to support regulatoryDocument and future output types"

//* output contains regulatoryDocument 0..* MS
//* output[regulatoryDocument]
//  * ^short = "Regulatory document produced as output (via DocumentReference index)"
//* output[regulatoryDocument].type  = http://hl7.org/fhir/uv/apix/CodeSystem/apix-task-output-type#regulatory-document "Regulatory Document"
//* output[regulatoryDocument].value[x] only Reference(APIXDocumentReference)

* focus 0..1
* for 0..1 MS
  * ^short = "Identifies the medicinal product(s) that is the subject. For multiple products use Group or List FHIR Resource"
  * ^definition = "Identifies the medicinal product(s) that is the subject of the process, use Group or List FHIR Resource is there are multiple."

* basedOn MS
* basedOn ^short = "Reference to the parent Task (e.g. a response points to the question Task), ordered lineage of Tasks (oldest → newest)."
* encounter 0..0
* executionPeriod 0..1 MS
  * ^short = "Actual execution period"
  * ^definition = "The actual time period during which the task was performed (e.g., when validation actually started and when it was completed)."
  * start 0..1 MS
    * ^short = "Actual start time"
  * end 0..1 MS
    * ^short = "Actual completion time"
* relevantHistory 0..0
* restriction 0..0