Profile: EndpointSubscriptionNotify
Parent: Endpoint
Id: endpoint-subscription-notify
Title: "APIX Endpoint for FHIR Subscription Notifications"
Description: "Endpoint requiring identifier, name, and connectionType of hl7-fhir-subscription-notify."

// Require at least one identifier
* identifier 1..* MS

// Require name
* name 1..1 MS

// Require connectionType with the specific coding
* connectionType 1..* MS
* connectionType.coding 1..* MS
* connectionType.coding.system = "http://hl7.org/fhir/uv/apix/CodeSystem/apix-temp"
* connectionType.coding.code = #hl7-fhir-subscription-notify "HL7 FHIR Subscription Notification Endpoint"

