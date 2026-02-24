ValueSet: APIXCTDSectionVS
Id: apix-ctd-section-vs
Title: "APIX CTD/eCTD Section Code System"
Description: "Value set for CTD section codes used in APIX regulatory submissions"
* ^url = "http://hl7.org/fhir/uv/apix/ValueSet/apix-ctd-section-vs"

* ^status = #active
* ^experimental = false

* include codes from system APIXCTDSECTION where concept descendent-of #m1
* include codes from system APIXCTDSECTION where concept descendent-of #m2
* include codes from system APIXCTDSECTION where concept descendent-of #m3
* include codes from system APIXCTDSECTION where concept descendent-of #m4
* include codes from system APIXCTDSECTION where concept descendent-of #m5
