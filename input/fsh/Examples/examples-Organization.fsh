Instance: Organization-1002
InstanceOf: APIXOrganization
Title: "Organization example with Endpoint"
Description: "Organization example with Endpoint."


* id = "1002"
* meta.versionId = "1"
* meta.lastUpdated = "2026-02-02T00:22:09.017+00:00"

* identifier[0].system = "http://somesystemRegulator"
* identifier[0].value = "110"

* name = "Stupendous Regulator"

* contact[0].telecom[0].system = #phone
* contact[0].telecom[0].value = "8018425555"

* contact[0].telecom[1].system = #fax
* contact[0].telecom[1].value = "8018425556"

* contact[0].telecom[2].system = #email
* contact[0].telecom[2].value = "mushi@gaipan.gov"

* contact[0].address.line[0] = "789"
* contact[0].address.city = "Six-seven"
* contact[0].address.state = "MO"
* contact[0].address.postalCode = "90129"
* contact[0].address.country = "USA"

* endpoint[0].reference = "Endpoint/1003"
* endpoint[0].display = "Subscription notification endpoint"