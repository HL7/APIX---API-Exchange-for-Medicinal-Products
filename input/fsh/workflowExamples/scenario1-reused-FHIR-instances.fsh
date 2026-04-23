Instance: org-synthpharma-ag
InstanceOf: Organization
Title: "Organization SynthPharma AG"
Description: "Example Organization SynthPharma AG"
Usage: #example
* id = "org-synthpharma-ag"
* name = "SynthPharma AG"
* contact[0].address.type = #physical
* contact[0].address.text = "123 Synthetic Research Blvd, 4000 Basel, Switzerland"
* contact[0].address.line = "123 Synthetic Research Blvd"
* contact[0].address.city = "Basel"
* contact[0].address.district = "Basel-Stadt"
* contact[0].address.state = "Basel-Stadt"
* contact[0].address.postalCode = "4000"
* contact[0].address.country = "Switzerland"
* contact.name.text = "Dr. John Doe, Head of Regulatory Affairs"
* contact.telecom.system = #email
* contact.telecom.value = "john.doe@synthpharma.example"
* contact.telecom.use = #work

Instance: org-ema-srm-hmed
InstanceOf: Organization
Title: "Organization Health Authority – Regulatory Review Division"
Description: "Example Organization Health Authority – Regulatory Review Division"
Usage: #example
* id = "org-ema-srm-hmed"
* name = "Health Authority – Regulatory Review Division"

* contact[0].address.type = #physical
* contact[0].address.text = "Regulatory Authority Headquarters, 1083 HS Capital City, Country"
* contact[0].address.line = "Regulatory Authority Headquarters"
* contact[0].address.city = "Capital City"
* contact[0].address.postalCode = "1083 HS"
* contact[0].address.country = "Country"
* contact.name.text = "Scientific and Regulatory Management"
* contact.telecom.system = #email
* contact.telecom.value = "regulatory@health-authority.example"
* contact.telecom.use = #work

