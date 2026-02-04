Instance: Subscription-TaskStatusChange-FullResource
InstanceOf: Subscription
Title: "Subscription for Task Status Change with Identifier Filter"
Description: "Subscription example to Task change status with an identifier filter, and sending full-resource."

* identifier[0].system = "submitterOrgSubscriptions"
* identifier[0].value = "task-miami10-status-subscription-1c5143fa-e247-405b-8bbc-a0f4025c11ad"

* status = #requested
* topic = "http://localhost:8080/fhir//SubscriptionTopic/1000"

* managingEntity.reference = "Organization/1004"

* reason = "Monitor status transitions for a specific Task"

* filterBy[0].resourceType = "Task"
* filterBy[0].filterParameter = "identifier"
* filterBy[0].value = "systeminternalToSubmitter|miami10"

* channelType.code = #rest-hook

* endpoint = "http://host.docker.internal:3001/fhir-subscription-notify"

* heartbeatPeriod = 300
* timeout = 5

* contentType = #application/fhir+json
* content = #full-resource

