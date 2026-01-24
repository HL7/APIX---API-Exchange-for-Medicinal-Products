Profile: APIXOrganization
Parent: Organization
Id: apix-organization
Title: "APIX Organization"
Description: "Organization profile for APIX regulatory workflows, derived from and compatible with ePI requirements."
* ^url = "http://hl7.org/fhir/uv/apix/StructureDefinition/apix-organization"
* ^version = "0.1.0"
* ^status = #draft
* ^publisher = "Gravitate Health Project"

// Identifiers
* identifier 1..* MS
* identifier.system 1..1
* identifier.value 1..1

// Basic Metadata
* name 1..1 MS
* alias 0..* MS
* description 0..1 MS
* type 0..* MS 

// Contact details - aligned with Organization-uv-epi
// In R5, Organization.address is removed? Or at least in this context we use contact.address
* contact 0..* MS
* contact.telecom ^slicing.discriminator.type = #value
* contact.telecom ^slicing.discriminator.path = "system"
* contact.telecom ^slicing.rules = #open
* contact.telecom contains phone 0..1 and email 0..1 and url 0..1
* contact.telecom[phone].system = #phone
* contact.telecom[phone].value 1..
* contact.telecom[email].system = #email
* contact.telecom[email].value 1..
* contact.telecom[url].system = #url
* contact.telecom[url].value 1..

* contact.address 0..1 MS
* contact.address.text 0..1 MS
* contact.address.text ^short = "Full text representation of the address"
* contact.address.line 0..* MS
* contact.address.line ^short = "Street name, number, direction & P.O. Box etc."
* contact.address.city 0..1 MS
* contact.address.city ^short = "Name of city, town etc."
* contact.address.district 0..1 MS
* contact.address.district ^short = "District name (aka county)"
* contact.address.state 0..1 MS
* contact.address.state ^short = "Sub-unit of country (state, region, province)"
* contact.address.postalCode 0..1 MS
* contact.address.postalCode ^short = "Postal code for area"
* contact.address.country 0..1 MS
* contact.address.country ^short = "Country (e.g., can be ISO 3166 2 or 3 letter code)"
