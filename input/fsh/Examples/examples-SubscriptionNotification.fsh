Instance: Bundle-SubscriptionNotification-TaskIdOnly
InstanceOf: Bundle
Title: "SubscriptionNotification Task ID Only"
Description: "SubscriptionNotification Bundle example Task id only."
Usage: #example

* id = "eee72492-c236-41f7-a7ba-3af356204f4c"
* type = #subscription-notification

* entry[0].fullUrl = "09efceb7-abdc-4dc8-bc31-0788baf65dbd"
* entry[0].resource.resourceType = "SubscriptionStatus"
* entry[0].resource.id = "09efceb7-abdc-4dc8-bc31-0788baf65dbd"
* entry[0].resource.status = #active
* entry[0].resource.type = #event-notification
* entry[0].resource.eventsSinceSubscriptionStart = 2

* entry[0].resource.notificationEvent[0].eventNumber = 2
* entry[0].resource.notificationEvent[0].focus.reference = "Task/1010"

* entry[0].resource.subscription.reference = "Subscription/1008"
* entry[0].resource.topic = "http://localhost:8080/fhir//SubscriptionTopic/1001"

* entry[1].fullUrl = "Task/1010/_history/1"
* entry[1].request.method = #POST
* entry[1].request.url = "Task"