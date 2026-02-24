Instance: example-ma
InstanceOf: MedicinalProductDefinition
Title: "Example Medicinal Product Definintion"
Description: "Example MedicinalProductDefinition"
Usage: #example
* id = "example-ma"
* identifier.system = "http://ema.europa.eu/identifier"
* identifier.value = "WONDERDRUG-500MG"
* status = http://hl7.org/fhir/publication-status#active "Active"
* domain = http://hl7.org/fhir/medicinal-product-domain#Human "Human use"
* name.productName = "WonderDrug 500 mg tablets"
* name.part[0].part = "WonderDrug"
* name.part[=].type = http://hl7.org/fhir/medicinal-product-name-part-type#InventedNamePart "Invented name part"
* name.part[+].part = "500 mg"
* name.part[=].type = http://hl7.org/fhir/medicinal-product-name-part-type#StrengthPart "Strength part"
* name.part[+].part = "tablets"
* name.part[=].type = http://hl7.org/fhir/medicinal-product-name-part-type#DoseFormPart "Pharmaceutical dose form part"
* name.usage.country = urn:iso:std:iso:3166#EE "Estonia"
* name.usage.language = urn:ietf:bcp:47#et "Estonian"
* contact.contact = Reference(org-synthpharma-ag)