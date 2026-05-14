CodeSystem: APIXTEMPCODES
Id: apix-temp
Title: "Temporary APIX Codes"
Description: "These codes are intended to be added to the appropriate HL7 Terminology code system"
* ^status = #active
* ^caseSensitive = true
* ^experimental = false

// for https://terminology.hl7.org/7.1.0/en/CodeSystem-endpoint-connection-type.html
* #hl7-fhir-subscription-notify "HL7 FHIR Subscription Notification Endpoint" "Endpoint intended to receive HL7 FHIR Subscription Notifications"

CodeSystem: APIXDEMOCODES
Id: apix-demo
Title: "APIX Task Identifier Type Codes"
Description: "These codes are intended to be used to indicate the Task Identifier type"
* ^status = #active
* ^caseSensitive = true
* ^experimental = false

* #apixtaskinstance "APIX Task Instance ID" "APIX Required UUID for identifying a Task instance"
* #apixregulatorprocedureno "APIX Regulator Procedure Number" "APIX Regulator Procedure Number records the unique identifier for the procedure in a regulator system"
* #docsetid "Document Set Identifier" "The set identifier identifiys what document folder this document belongs too"
* #docverid "Document Version Identifier" "The document version identifier is the specific document instance identifier"