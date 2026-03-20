CodeSystem: APIXTEMPCODES
Id: apix-temp
Title: "Temporary APIX Codes"
Description: "These codes are intended to be added to the appropriate HL7 Terminology code system"
* ^status = #active
* ^caseSensitive = true
* ^experimental = false

// for https://terminology.hl7.org/7.1.0/en/CodeSystem-endpoint-connection-type.html
* #hl7-fhir-subscription-notify "HL7 FHIR Subscription Notification Endpoint" "Endpoint intended to receive HL7 FHIR Subscription Notifications"