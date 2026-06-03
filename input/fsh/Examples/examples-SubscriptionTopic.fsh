Instance: TaskStatusChangeWithIdentifierFilter
InstanceOf: TaskStatusChangeWithIdentifierFilterTopic
Usage: #example
Description: "Triggers when a Task.status value changes. Allows subscriptions to filter by Task.identifier."
* id = "TaskStatusChangeWithIdentifierFilter"
* meta.versionId = "2"
* meta.lastUpdated = "2026-02-02T00:21:39.503+00:00"
* url = "http://hl7.org/fhir/uv/example/SubscriptionTopic/TaskStatusChangeWithIdentifierFilter"
* name = "TaskStatusChangeWithIdentifierFilter"
* title = "Task Status Change With Identifier Filter"
* status = #active
* description = "Triggers when a Task.status value changes. Allows subscriptions to filter by Task.identifier."
* resourceTrigger[0].resource = "Task"
* resourceTrigger[0].supportedInteraction[0] = #update
* resourceTrigger[0].fhirPathCriteria = "%previous.status != %current.status"
* canFilterBy.description = "Filter by business identifier"
* canFilterBy.resource = "Task"
* canFilterBy.filterParameter = "identifier"
* canFilterBy.filterDefinition = "http://hl7.org/fhir/SearchParameter/Task-identifier"
* canFilterBy.modifier = #exact


Instance: TaskCreationWithOrganizationAssignedFilter
InstanceOf: TaskCreationWithOrganizationAssignedFilterTopic
Usage: #example
Description: "SubscriptionTopic for a health authority to notify an organization when that organization has been assigned a new Task."
* id = "TaskCreationWithOrganizationAssignedFilter"
* meta.versionId = "2"
* meta.lastUpdated = "2026-02-02T00:21:39.733+00:00"
* url = "http://hl7.org/fhir/uv/example/SubscriptionTopic/TaskCreationWithOrganizationAssignedFilter"
* name = "TaskCreationWithOrganizationAssignedFilter"
* title = "Task Assignment and Creation With Organization Filter"
* status = #active
* description = "SubscriptionTopic for a health authority to notify an organization when that organization has been assigned a new Task."
* resourceTrigger[0].resource = "Task"
* resourceTrigger[0].supportedInteraction[0] = #create
* canFilterBy[0].description = "Filter by requested Performer Organization"
* canFilterBy[0].resource = "Task"
* canFilterBy[0].filterParameter = "owner"
* canFilterBy[0].filterDefinition = "http://hl7.org/fhir/SearchParameter/Task-owner"
* canFilterBy[0].modifier[0] = #exact
