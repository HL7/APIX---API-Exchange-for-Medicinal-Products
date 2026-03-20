### Introduction
APIX is the global standard for the **automated, algorithmic exchange** of medicinal product information. Built on HL7 FHIR R5, it creates a single, interoperable network connecting industry, regulators, and healthcare systems worldwide—replacing static documents with real-time data.

*This guide defines the technical framework to make that vision a reality.*  

### Why Adopt APIX?

1. **One integration, all products & procedures**  
   Single FHIR framework covers every medicinal product type and every regulatory procedure — one connection at the agency reaches all companies; one connection at the company reaches all regulators.

2. **Built on the internet’s proven standards**  
   Same RESTful APIs and OAuth2 that already run global banking, eCommerce, and modern healthcare (SMART on FHIR). Zero proprietary formats.

3. **From months to seconds**  
   Submissions, questions, and decisions become real-time events. Cycle-time delays become visible and instantly actionable.

4. **Instant innovation platform**  
   Open APIs enable AI agents, predictive analytics, and seamless RIM/ERP integrations—no custom gateways required.

5. **Universal performance tracking**  
   Every milestone is a timestamped event. Run cycle-time KPIs and SLA reports with one simple search across the entire submission portfolio.

---

### Strategic Objectives

The APIX initiative is driven by two transformative goals:

#### 1. Real-Time Algorithmic Exchange
We are moving from a **document-centric** regulatory world to a **data-centric** one. Today’s reliance on static PDF dossiers and periodic submissions creates an information lag of months. APIX enables "algorithmic" exchange, where data flows seamlessly between systems, allowing for automated validation, real-time assessment, and "sub-second" synchronization of product information.

#### 2. The "ISO 20022" of Healthcare
Just as **ISO 20022** harmonized the global financial sector to allow real-time, cross-border payments, APIX serves as the universal language for medicinal product exchange. By providing a single, structured standard that works across all borders and regulatory domains, APIX eliminates technical silos and creates a frictionless global market for medicines.

---

### Global Submission Models

APIX is architecture-agnostic, supporting both centralized and decentralized exchange models. This ensures that regions can implement the system that best fits their national or regional infrastructure.

#### Centralized vs. Decentralized Exchange

<div style="text-align: center; margin: 20px 0;">
  <img src="centralizedvsdecentralizedexchangemodels.png" alt="Centralized vs Decentralized Exchange Models" width="800">
</div>

---

### Background: Solving the Fragmentation Crisis

The exchange of medicinal product information today is defined by extreme **fragmentation**. 

*   **Product Silos**: Different formats and portals are required for human drugs vs. veterinary drugs vs. medical devices.
*   **Procedure Silos**: Clinical trial applications, marketing authorizations, and post-approval changes often use entirely different communication channels.
*   **Information Lag**: Because information is trapped in documents (portals, email, letters), regulators and industry are often "flying blind" regarding the real-time status of their applications.

APIX solves this crisis by providing a single, harmonized, API-first layer. It aligns regulatory exchange with the same modern technologies used in international banking and eCommerce—ensuring that life-saving medicines move through the regulatory pipeline as fast as the data that defines them.

---

### In Scope
Phase I (2025 / 2026) focuses on the following:
- human medicinal products
- Regulatory submissions & procedural management (e.g., variations, supplements, question and response)
- Adverse Event Reporting (Individual case safety reports (ICSR))
- Payment of application fees

### Out of Scope
Phase II+ (2026+) will consider the following: 
- Remaining product types (Medical Devices, Veterinary drug, Over the counter drugs, Natural health products)
- Clinical trials 
- Master file
- Health Technology Assessment (HTA) dossiers 
- Establishment and inspection submissions (GMP, GCP, GLP facilities, audits, compliance)

---

### Governance & Collaboration
APIX is developed under the HL7 Vulcan Accelerator with active participation from regulators, pharmaceutical companies, and technology vendors.

### Get Involved
- Join the weekly calls.
- Test the reference implementation.

We welcome industry, solution providers, and regulators from every region to contribute.