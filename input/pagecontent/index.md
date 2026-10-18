<!-- HERO -->
<div style="text-align:center; padding:40px 20px 24px;">
  <div style="font-size:.75em; font-weight:700; text-transform:uppercase; letter-spacing:.22em; color:#003087; margin-bottom:16px;">HL7 FHIR R5 · Global Standard</div>
  <h1 style="font-size:2.4em; font-weight:800; line-height:1.15; margin-bottom:16px; color:#111827;">Regulatory exchange,<br/><span style="background:linear-gradient(135deg,#003087,#7c3aed); -webkit-background-clip:text; -webkit-text-fill-color:transparent;">reimagined.</span></h1>
  <p style="font-size:1.02em; color:#4b5563; max-width:680px; margin:0 auto 24px; line-height:1.6;">Regulatory exchange is globally fragmented across authorities, product lines, procedures, and technologies. This IG establishes a common Task- and Subscription-based framework for regulatory workflows and interactions, enabling them to be exchanged, tracked, and acted upon with machine-readable status and event-driven notifications.</p>
  <div style="display:flex; gap:12px; justify-content:center; flex-wrap:wrap;">
    <a href="gettingstarted.html" style="display:inline-block; background:#003087; color:#fff; padding:14px 28px; border-radius:8px; font-weight:700; font-size:1em; text-decoration:none;">Get Started</a>
  </div>
</div>

<div style="text-align:center; padding:0 20px 40px;">
  <img src="apix-before-after.svg" alt="Before and after RWI-pharma. Before: industry connects to each regulator using different exchange methods — email, secure email, FTP, AS2, HTTPS, portals, and mail — that vary per product type, per procedure, and per country. After: industry uses one standardized FHIR API connection pattern (Task, DocumentReference, Binary, Subscription) with every regulator, regardless of product type, procedure, or country." style="max-width:100%; width:820px; border:1px solid #e5e7eb; border-radius:12px; box-shadow:0 4px 16px rgba(0,0,0,.06);"/>
</div>

<!-- ABOUT THIS IG -->
<h2 id="about" style="font-size:1.3em; font-weight:700; color:#111827; margin-bottom:12px;">About this IG</h2>

<div style="margin-bottom:24px;">
  <p style="font-size:.88em; color:#374151; line-height:1.7; margin-bottom:12px;">The Regulatory Workflows and Interactions - pharma Implementation Guide defines how FHIR can support end-to-end digital regulatory workflows and interactions between applicants and regulatory authorities for human biopharmaceutical products.</p>
  <p style="font-size:.88em; color:#374151; line-height:1.7; margin-bottom:12px;">Today, regulatory exchange is highly fragmented. Authorities may use different mechanisms across product lines and procedures, including portals, gateways, email, secure email, FTP, HTTPS, and physical mail. These differences multiply across regulators globally, creating significant complexity for industry and limiting interoperability.</p>
  <p style="font-size:.88em; color:#374151; line-height:1.7; margin-bottom:12px;">Applicants also frequently lack end-to-end visibility into the status of their regulatory interactions. Consumers can track a FedEx or Amazon delivery through each major step and receive notifications as it progresses, yet applicants often cannot similarly track a critical regulatory interaction or receive automated notifications when key milestones occur.</p>
  <p style="font-size:.88em; color:#374151; line-height:1.7; margin:0;">Using <a href="apixtask.html">Task</a>, <a href="apixdocumentReference.html">DocumentReference</a>, <a href="architecture.html#binary-upload-guide-post-then-link">Binary</a>, <a href="apixsubscription.html">Subscription</a>, APIs, and related FHIR capabilities, the guide enables regulatory activities to be interoperable, traceable, trackable, and event-driven, replacing fragmented exchange mechanisms with a standardized digital workflow.</p>
</div>

<!-- SCOPE -->
<h3 id="scope" style="font-size:1.1em; font-weight:700; color:#111827; margin-bottom:12px;">Scope</h3>

<p style="font-size:.88em; color:#374151; line-height:1.7; margin-bottom:16px;">This Implementation Guide focuses on human biopharmaceutical products and the regulatory procedures and interactions associated with their development, authorization, and lifecycle management.</p>

<div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-bottom:14px;">
  <div style="background:#ecfdf5; border:1px solid #a7f3d0; border-radius:8px; padding:16px;">
    <div style="font-weight:700; color:#065f46; margin-bottom:6px; font-size:.9em;">✅ In Scope</div>
    <p style="font-size:.82em; color:#064e3b; line-height:1.5; margin:0 0 6px;">Regulatory procedures and interactions, including but not limited to:</p>
    <ul style="font-size:.85em; color:#064e3b; line-height:1.7; padding-left:16px; margin:0;">
      <li>Clinical trial regulatory interactions</li>
      <li>Adverse event and safety-related interactions</li>
      <li>Product information and label negotiation</li>
      <li>Marketing authorization procedures</li>
      <li>Regulatory requests and responses</li>
      <li>Post-approval changes and lifecycle management</li>
      <li>Other regulatory procedures involving interactions between applicants and regulatory authorities</li>
    </ul>
  </div>
  <div style="background:#fef2f2; border:1px solid #fecaca; border-radius:8px; padding:16px;">
    <div style="font-weight:700; color:#991b1b; margin-bottom:6px; font-size:.9em;">⛔ Out of Scope (current phase)</div>
    <p style="font-size:.82em; color:#7f1d1d; line-height:1.5; margin:0 0 6px;">The following product domains are out of scope for the current phase:</p>
    <ul style="font-size:.85em; color:#7f1d1d; line-height:1.7; padding-left:16px; margin:0;">
      <li>Medical devices</li>
      <li>Veterinary drugs</li>
      <li>Over-the-counter drugs</li>
      <li>Natural health products</li>
      <li>Food</li>
      <li>Cosmetics</li>
      <li>Inspections</li>
    </ul>
  </div>
</div>

<p style="font-size:.82em; color:#6b7280; line-height:1.6; margin-bottom:32px;">These domains are out of scope for the current phase only. Subsequent phases of the project are expected to expand the scope to support regulatory workflows and interactions in these and other regulated-product domains.</p>

<hr style="border:none; border-top:1px solid #e5e7eb; margin:0 0 32px;"/>

<!-- ========================================= -->
<!-- HOW IT WORKS — 5-STEP PIPELINE            -->
<!-- ========================================= -->
<div style="padding:0 20px 8px;">
  <div style="text-align:center; margin-bottom:28px;">
    <h2 style="font-size:1.5em; font-weight:800; color:#111827; margin-bottom:8px;">How It Works</h2>
    <p style="font-size:.92em; color:#6b7280; max-width:540px; margin:0 auto; line-height:1.55;">Five steps to connect any two parties, industry or regulator, in either direction.</p>
  </div>
</div>

<div style="display:flex; align-items:flex-start; justify-content:center; gap:0; margin-bottom:36px; flex-wrap:nowrap;">
  <!-- Step 1: Connect -->
  <div style="text-align:center; flex:1; max-width:160px; padding:0 4px;">
    <div style="width:56px; height:56px; border-radius:50%; background:linear-gradient(135deg,#eff6ff,#dbeafe); border:3px solid #2563eb; display:flex; align-items:center; justify-content:center; margin:0 auto 12px; font-size:1.3em; box-shadow:0 2px 8px rgba(37,99,235,.15);">🔌</div>
    <div style="font-size:.7em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#2563eb; margin-bottom:4px;">Step 1</div>
    <div style="font-weight:700; color:#111827; font-size:.92em; margin-bottom:6px;">Connect</div>
    <p style="font-size:.78em; color:#6b7280; line-height:1.5; margin:0;">Register your organization via API</p>
  </div>
  <!-- Arrow -->
  <div style="display:flex; align-items:center; padding-top:18px; flex-shrink:0; color:#d1d5db; font-size:1.2em;">→</div>
  <!-- Step 2: Stream -->
  <div style="text-align:center; flex:1; max-width:160px; padding:0 4px;">
    <div style="width:56px; height:56px; border-radius:50%; background:linear-gradient(135deg,#f0fdfa,#ccfbf1); border:3px solid #0d9488; display:flex; align-items:center; justify-content:center; margin:0 auto 12px; font-size:1.3em; box-shadow:0 2px 8px rgba(13,148,136,.15);">📤</div>
    <div style="font-size:.7em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#0d9488; margin-bottom:4px;">Step 2</div>
    <div style="font-weight:700; color:#111827; font-size:.92em; margin-bottom:6px;">Stream</div>
    <p style="font-size:.78em; color:#6b7280; line-height:1.5; margin:0;">Upload files (PDF, XML, JSON, data sets) as FHIR Binary resources</p>
  </div>
  <!-- Arrow -->
  <div style="display:flex; align-items:center; padding-top:18px; flex-shrink:0; color:#d1d5db; font-size:1.2em;">→</div>
  <!-- Step 3: Describe -->
  <div style="text-align:center; flex:1; max-width:160px; padding:0 4px;">
    <div style="width:56px; height:56px; border-radius:50%; background:linear-gradient(135deg,#fff7ed,#fed7aa); border:3px solid #ea580c; display:flex; align-items:center; justify-content:center; margin:0 auto 12px; font-size:1.3em; box-shadow:0 2px 8px rgba(234,88,12,.15);">🏷️</div>
    <div style="font-size:.7em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#ea580c; margin-bottom:4px;">Step 3</div>
    <div style="font-weight:700; color:#111827; font-size:.92em; margin-bottom:6px;">Describe</div>
    <p style="font-size:.78em; color:#6b7280; line-height:1.5; margin:0;">Create DocumentReference metadata for each file</p>
  </div>
  <!-- Arrow -->
  <div style="display:flex; align-items:center; padding-top:18px; flex-shrink:0; color:#d1d5db; font-size:1.2em;">→</div>
  <!-- Step 4: Orchestrate -->
  <div style="text-align:center; flex:1; max-width:160px; padding:0 4px;">
    <div style="width:56px; height:56px; border-radius:50%; background:linear-gradient(135deg,#faf5ff,#e9d5ff); border:3px solid #7c3aed; display:flex; align-items:center; justify-content:center; margin:0 auto 12px; font-size:1.3em; box-shadow:0 2px 8px rgba(124,58,237,.15);">📋</div>
    <div style="font-size:.7em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#7c3aed; margin-bottom:4px;">Step 4</div>
    <div style="font-weight:700; color:#111827; font-size:.92em; margin-bottom:6px;">Orchestrate</div>
    <p style="font-size:.78em; color:#6b7280; line-height:1.5; margin:0;">Create a Task to initiate and track any regulatory activity</p>
  </div>
  <!-- Arrow -->
  <div style="display:flex; align-items:center; padding-top:18px; flex-shrink:0; color:#d1d5db; font-size:1.2em;">→</div>
  <!-- Step 5: Subscribe -->
  <div style="text-align:center; flex:1; max-width:160px; padding:0 4px;">
    <div style="width:56px; height:56px; border-radius:50%; background:linear-gradient(135deg,#ecfdf5,#a7f3d0); border:3px solid #059669; display:flex; align-items:center; justify-content:center; margin:0 auto 12px; font-size:1.3em; box-shadow:0 2px 8px rgba(5,150,105,.15);">🔔</div>
    <div style="font-size:.7em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#059669; margin-bottom:4px;">Step 5</div>
    <div style="font-weight:700; color:#111827; font-size:.92em; margin-bottom:6px;">Subscribe</div>
    <p style="font-size:.78em; color:#6b7280; line-height:1.5; margin:0;">Get real-time notifications as activities progress</p>
  </div>
</div>

<div style="text-align:center; padding:0 20px 24px;">
  <a href="gettingstarted.html" style="color:#003087; font-weight:600; font-size:.9em; text-decoration:none;">See the full step-by-step walkthrough →</a>
</div>

<!-- WHY ADOPT (merged with Submit / Track / Analyze) -->
<div style="text-align:center; padding:16px 20px 8px;">
  <h2 style="font-size:1.5em; font-weight:800; color:#111827; margin-bottom:10px;">Why adopt RWI-pharma</h2>
  <p style="font-size:.95em; color:#6b7280; max-width:520px; margin:0 auto 28px; line-height:1.55;">Replace fragmented portals, emails, and static documents with a single, modern API standard.</p>
</div>

<div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-bottom:16px;">
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:10px; padding:24px; display:flex; flex-direction:column;">
    <div style="font-size:1.4em; margin-bottom:10px;">🌐</div>
    <div style="font-weight:700; color:#003087; margin-bottom:6px;">One Universal Interface</div>
    <p style="font-size:.88em; color:#4b5563; line-height:1.6; margin:0 0 12px; flex:1;">One common FHIR framework for regulatory workflows and interactions across procedures and authorities — one connection at the agency reaches all companies; one connection at the company reaches all regulators.</p>
    <a href="usecases.html" style="color:#003087; font-weight:600; font-size:.85em; text-decoration:none;">Explore use cases →</a>
  </div>
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:10px; padding:24px; display:flex; flex-direction:column;">
    <div style="font-size:1.4em; margin-bottom:10px;">📤</div>
    <div style="font-weight:700; color:#003087; margin-bottom:6px;">Submit via Web-Standard APIs</div>
    <p style="font-size:.88em; color:#4b5563; line-height:1.6; margin:0 0 12px; flex:1;">Post regulatory submissions directly via FHIR APIs, using the same RESTful APIs and OAuth2 that already run global banking, eCommerce, and modern healthcare (SMART on FHIR). Zero proprietary formats.</p>
    <a href="workflow.html" style="color:#003087; font-weight:600; font-size:.85em; text-decoration:none;">See the workflow →</a>
  </div>
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:10px; padding:24px; display:flex; flex-direction:column;">
    <div style="font-size:1.4em; margin-bottom:10px;">📊</div>
    <div style="font-weight:700; color:#003087; margin-bottom:6px;">Track in Real Time</div>
    <p style="font-size:.88em; color:#4b5563; line-height:1.6; margin:0 0 12px; flex:1;">FedEx-style status tracking for every regulatory procedure. Submissions, questions, and decisions become real-time events — delays become visible and instantly actionable.</p>
    <a href="subscriptions.html" style="color:#003087; font-weight:600; font-size:.85em; text-decoration:none;">How notifications work →</a>
  </div>
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:10px; padding:24px; display:flex; flex-direction:column;">
    <div style="font-size:1.4em; margin-bottom:10px;">📈</div>
    <div style="font-weight:700; color:#003087; margin-bottom:6px;">Instant Analytics</div>
    <p style="font-size:.88em; color:#4b5563; line-height:1.6; margin:0 0 12px; flex:1;">Every milestone is a timestamped event. Run cycle-time KPIs and SLA reports with one simple search across the entire submission portfolio.</p>
    <a href="apixtask.html" style="color:#003087; font-weight:600; font-size:.85em; text-decoration:none;">Task milestones →</a>
  </div>
</div>

<div style="text-align:center; padding:8px 20px 36px;">
  <a href="usecases.html" style="color:#003087; font-weight:600; font-size:.88em; text-decoration:none;">Explore all use cases →</a>
</div>

<hr style="border:none; border-top:1px solid #e5e7eb; margin:0 0 32px;"/>

<!-- GOVERNANCE -->
<h2 style="font-size:1.3em; font-weight:700; color:#111827; margin-bottom:12px;">Governance &amp; Participation</h2>
<div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-bottom:32px;">
  <div style="background:#fff; border:1px solid #e5e7eb; border-radius:10px; padding:20px;">
    <div style="font-size:1.3em; margin-bottom:8px;">🤝</div>
    <div style="font-weight:700; color:#003087; margin-bottom:6px;">Governance & Collaboration</div>
    <p style="font-size:.85em; color:#4b5563; line-height:1.6; margin:0;">RWI-pharma is developed under the HL7 Vulcan Accelerator with active participation from regulators, pharmaceutical companies, and technology vendors.</p>
  </div>
  <div style="background:#fff; border:1px solid #e5e7eb; border-radius:10px; padding:20px;">
    <div style="font-size:1.3em; margin-bottom:8px;">🚀</div>
    <div style="font-weight:700; color:#003087; margin-bottom:6px;">Get Involved</div>
    <p style="font-size:.85em; color:#4b5563; line-height:1.6; margin:0;">Join the weekly calls. Test the reference implementation. We welcome industry, solution providers, and regulators from every region to contribute.</p>
  </div>
</div>
