Instance: Endpoint-1003
InstanceOf: EndpointSubscriptionNotify
Title: "Example basic APIX interaction Endpoint"
Description: "Example basic APIX interaction Endpoint, payload is very loosely defined; payload considerations are handled internally and not exposed. Note identifier."
Usage: #example

* id = "1003"
* meta.versionId = "1"
* meta.lastUpdated = "2026-02-02T00:22:09.017+00:00"

* identifier[0].system = "http://example.org/regulator-system"
* identifier[0].value = "findMEanywhereUsingThisSystemAndValue"

* status = #active

* managingOrganization = Reference(Organization-1002)

* connectionType[0].coding[0].system = "http://terminology.hl7.org/CodeSystem/endpoint-connection-type"
* connectionType[0].coding[0].code = #hl7-fhir-subscription-notify

* name = "Authority FHIR Subscription Notification Endpoint"

* payload[0].type[0].coding[0].system = "http://terminology.hl7.org/CodeSystem/endpoint-payload-type"
* payload[0].type[0].coding[0].code = #any
* payload[0].type[0].coding[0].display = "Any"

* address = "http://example.org/host.docker.internal:3001/fhir-subscription-notify"

Instance: Endpoint-1005
InstanceOf: EndpointSubscriptionNotify
Title: "Example APIX interaction Endpoint with header"
Description: "Example APIX interaction Endpoint with header information; payload is very loosely defined, sufficient where payload considerations are handled internally and not exposed. Note identifier.   n"
Usage: #example

* id = "1005"
* meta.versionId = "1"
* meta.lastUpdated = "2026-02-02T00:22:34.166+00:00"

* identifier[0].system = "http://example.org/submitter-system"
* identifier[0].value = "findMEanywhereUsingThisSystemAndValue"

* status = #active

* connectionType[0].coding[0].system = "http://terminology.hl7.org/CodeSystem/endpoint-connection-type"
* connectionType[0].coding[0].code = #hl7-fhir-subscription-notify

* name = "Best Company FHIR Subscription Notification Endpoint"

* payload[0].type[0].coding[0].system = "http://terminology.hl7.org/CodeSystem/endpoint-payload-type"
* payload[0].type[0].coding[0].code = #any
* payload[0].type[0].coding[0].display = "Any"

* address = "http://example.org/host.docker.internal:3000/fhir-subscription-notify"

* header[0] = "Authorization: Bearer {{token}}"