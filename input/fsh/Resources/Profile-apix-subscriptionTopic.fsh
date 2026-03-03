Profile: TaskCreationWithOrganizationAssignedFilterTopic
Parent: SubscriptionTopic
Id: task-creation-with-organization-assigned-filter
Title: "APIX Task Assignment and Creation With Organization Filter"
Description: "SubscriptionTopic notifying an organization when a Task is created and assigned to them."

// Require name
* name = "TaskCreationWithOrganizationAssignedFilter"

// Require exactly one resourceTrigger
* resourceTrigger 1..1
* resourceTrigger.resource = #Task
* resourceTrigger.supportedInteraction 1..1
* resourceTrigger.supportedInteraction = #create
* resourceTrigger.fhirPathCriteria 0..0

// Require one canFilterBy
* canFilterBy 1..1
* canFilterBy.description = "Filter by Owner (assigned) Organization"
* canFilterBy.resource = #Task
* canFilterBy.filterParameter = "owner"
* canFilterBy.filterDefinition = "http://hl7.org/fhir/SearchParameter/Task-owner"
* canFilterBy.modifier 1..1
* canFilterBy.modifier = #exact

Profile: TaskStatusChangeWithIdentifierFilterTopic
Parent: SubscriptionTopic
Id: task-status-change-with-identifier-filter
Title: "APIX Task Status Change With Identifier Filter"
Description: "Triggers when a Task.status value changes and allows filtering by Task.identifier."

// Require name
* name = "TaskStatusChangeWithIdentifierFilter"

// Require exactly one resourceTrigger
* resourceTrigger 1..1
* resourceTrigger.resource = #Task
* resourceTrigger.supportedInteraction 1..1
* resourceTrigger.supportedInteraction = #update
* resourceTrigger.fhirPathCriteria 1..1
* resourceTrigger.fhirPathCriteria = "%previous.status != %current.status"

