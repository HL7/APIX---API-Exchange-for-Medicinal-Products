### Introduction
APIX is an HL7 FHIR R5 Implementation Guide that defines a standardized, API-first framework for real-time exchange of regulatory information between regulators, marketing authorization holders, healthcare systems, and other stakeholders.  

It covers all regulated product types across the full regulatory lifecycle — from clinical trials to post-market changes to pharmacovigilance — using modern web standards already proven at global scale in healthcare, banking, and e-commerce.

### Why Build or Adopt APIX? – The Implementer’s Case

1. **You’re not inventing anything new – you’re reusing the internet’s most proven standards**  
   APIX runs on the same HL7 FHIR R5 + REST + OAuth2 + JSON foundation that already powers Epic, Cerner, national health systems, Apple Health, PayPal, Stripe, and virtually every modern bank and retailer. No proprietary formats, no custom gateways, no new protocols to learn or maintain.

2. **From months to seconds – real, measurable time savings**  
   Every submission, question, response, and decision becomes a discrete, instantly visible Task. Clock-stop to clock-restart happens in real time via Subscriptions. Agencies and companies can see where time is spent and can cut average procedure cycle times.

3. **Built-in, automatic performance dashboards**  
   Because every milestone is a timestamped status change on a FHIR Task, you get accurate cycle-time metrics (submission → validation → assessment → questions → response → decision) for free. Run organization-wide KPIs, therapeutic-area benchmarks, or SLA reports with simple FHIR searches.

4. **Future-proof innovation platform**  
   The same open API instantly unlocks third-party AI agents (auto-fill responses, risk scoring, translation), analytics vendors, RIM-system integrations, and startup tools. This will support an ecosystem of innovative solutions.

5. **One framework for everything – across all product types and procedures**  
   A single FHIR-based framework works for all regulated product types (e.g., drugs, devices, OTC, veterinary) and all regulatory procedures (e.g., clinical trials, post approval variations, adverse event reporting, master-files, inspections, health technology assessments). One integration at the regulator connects all companies; one integration at the company connects all regulators.

**In short:** APIX delivers the speed, transparency, and analytics of a singular modern fintech platform – but for every medicinal and healthcare product – using technology already running at global scale.

### In Scope
Regulated health products, including: 
- Human drugs
- Medical Devices
- Veterinary drugs
- Over the counter drugs
- Natural health products

Regulatory activities, including:
- Clinical trial applications (IND/CTA/IMPD)
- Market authorization applications (NDA/MAA), post-approval changes (variations, supplements, annual reports), and Questions/Response to Questions
- Adverse Event Reporting (Individual Case Safety Reports (ICSR)) and pharmacovigilance workflows
- Health Technology Assessment (HTA) submissions
- Establishment and inspection submissions (GMP, GCP, GLP facilities, audits, compliance)

Administrative activities, including:
- Payments
- Organization / site registration

### Out of Scope
- IDMP identifier requests (e.g., Pharmaceutical Product Identifier (PhPID) and Global Substance Identifier (GSID)) – refer to the [UMC IDMP Request and Publish API Implementation Guide](https://build.fhir.org/ig/Uppsala-Monitoring-Centre/WHO-UMC-IDMP-Service/index.html) for detail.
