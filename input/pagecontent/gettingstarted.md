<!-- GETTING STARTED HEADER -->
<div style="margin-bottom:32px;">
  <h2 style="font-size:1.7em; font-weight:800; color:#111827; margin-bottom:10px;">Getting Started with APIX</h2>
  <p style="font-size:.95em; color:#6b7280; line-height:1.6; max-width:640px;">Whether you are a Regulatory Authority building an API gateway, a Pharmaceutical company connecting your RIM system, or a Technology Vendor building integration software — choose your path below.</p>
</div>

<hr style="border:none; border-top:1px solid #e5e7eb; margin:0 0 32px;"/>

<!-- PERSONA ROUTING GRID -->
<h2 id="choose-your-path" style="font-size:1.2em; font-weight:700; color:#111827; margin-bottom:16px;">Choose Your Path</h2>
<div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px; margin-bottom:36px;">
  <!-- Pharmaceutical Industry -->
  <div id="pharmaceutical-industry" style="background:#fff; border:1px solid #e5e7eb; border-radius:10px; padding:24px; position:relative; overflow:hidden;">
    <div style="position:absolute; top:0; left:0; right:0; height:4px; background:#2563eb;"></div>
    <div style="font-size:1.4em; margin-bottom:10px; margin-top:4px;">🏢</div>
    <div style="font-weight:700; color:#111827; font-size:1em; margin-bottom:6px;">Pharmaceutical Industry</div>
    <p style="font-size:.82em; color:#6b7280; line-height:1.5; margin-bottom:14px;">You want to automate regulatory submissions, track procedures in real-time, and eliminate manual portal uploads.</p>
    <ol style="font-size:.82em; color:#374151; padding-left:16px; line-height:1.9; margin:0;">
      <li>Review the <a href="usecases.html" style="color:#2563eb; font-weight:600;">Use Cases</a></li>
      <li>Study the <a href="workflow-overview.html" style="color:#2563eb; font-weight:600;">Workflow Overview</a></li>
      <li>Configure your RIM system for FHIR R5 Task-based exchange</li>
      <li>Test with the <a href="workflow.html" style="color:#2563eb; font-weight:600;">reference implementation</a></li>
    </ol>
  </div>
  <!-- Regulatory Authorities -->
  <div id="regulatory-authorities" style="background:#fff; border:1px solid #e5e7eb; border-radius:10px; padding:24px; position:relative; overflow:hidden;">
    <div style="position:absolute; top:0; left:0; right:0; height:4px; background:#10b981;"></div>
    <div style="font-size:1.4em; margin-bottom:10px; margin-top:4px;">🏛️</div>
    <div style="font-weight:700; color:#111827; font-size:1em; margin-bottom:6px;">Regulatory Authorities</div>
    <p style="font-size:.82em; color:#6b7280; line-height:1.5; margin-bottom:14px;">You are building or modernizing your regulatory exchange infrastructure with API-first architecture.</p>
    <ol style="font-size:.82em; color:#374151; padding-left:16px; line-height:1.9; margin:0;">
      <li>Review the <a href="architecture.html" style="color:#10b981; font-weight:600;">Architecture</a></li>
      <li>Set up an <a href="architecture.html" style="color:#10b981; font-weight:600;">R5-compliant FHIR server</a></li>
      <li>Configure <a href="apixsubscriptionTopic.html" style="color:#10b981; font-weight:600;">SubscriptionTopics</a></li>
      <li>Test <a href="subscriptions.html" style="color:#10b981; font-weight:600;">subscription notifications</a></li>
    </ol>
  </div>
  <!-- Technology Vendors -->
  <div id="technology-vendors" style="background:#fff; border:1px solid #e5e7eb; border-radius:10px; padding:24px; position:relative; overflow:hidden;">
    <div style="position:absolute; top:0; left:0; right:0; height:4px; background:#8b5cf6;"></div>
    <div style="font-size:1.4em; margin-bottom:10px; margin-top:4px;">💻</div>
    <div style="font-weight:700; color:#111827; font-size:1em; margin-bottom:6px;">Technology Vendors</div>
    <p style="font-size:.82em; color:#6b7280; line-height:1.5; margin-bottom:14px;">You are building RIM integrations, regulatory gateways, or FHIR server implementations for pharma and regulators.</p>
    <ol style="font-size:.82em; color:#374151; padding-left:16px; line-height:1.9; margin:0;">
      <li>Study the <a href="artifacts.html" style="color:#8b5cf6; font-weight:600;">FHIR Profiles</a></li>
      <li>Review the <a href="apixinteractionpattern.html" style="color:#8b5cf6; font-weight:600;">Interaction Pattern</a></li>
      <li>Implement the <a href="apixtask.html" style="color:#8b5cf6; font-weight:600;">Task workflow</a></li>
      <li>Validate with the <a href="https://validator.fhir.org" style="color:#8b5cf6; font-weight:600;">HL7 Validator</a></li>
    </ol>
  </div>
</div>

<hr style="border:none; border-top:1px solid #e5e7eb; margin:0 0 32px;"/>

<!-- THE JOURNEY IS INCREMENTAL -->
<div style="background:linear-gradient(135deg,#eff6ff,#faf5ff); border:1px solid #bfdbfe; border-radius:12px; padding:28px 32px; display:flex; align-items:center; gap:32px; margin-bottom:36px; flex-wrap:wrap;">
  <div style="flex:1; min-width:260px;">
    <div style="font-weight:700; color:#111827; font-size:1.05em; margin-bottom:8px;">The journey is incremental</div>
    <p style="font-size:.88em; color:#374151; line-height:1.6; margin:0;">You don't need to implement the entire specification on day one. Start with a <strong>simple Task-based submission</strong> to establish connectivity, then progressively add <strong>real-time subscriptions</strong> and <strong>document exchange</strong> as your infrastructure matures.</p>
  </div>
  <div style="display:flex; flex-direction:column; gap:10px; flex-shrink:0;">
    <a href="workflow-overview.html" style="display:block; background:#2563eb; color:#fff; padding:11px 22px; border-radius:7px; font-weight:600; font-size:.88em; text-decoration:none; text-align:center;">Start with Submission →</a>
    <a href="subscriptions.html" style="display:block; background:#8b5cf6; color:#fff; padding:11px 22px; border-radius:7px; font-weight:600; font-size:.88em; text-decoration:none; text-align:center;">Jump to Subscriptions →</a>
  </div>
</div>

<hr style="border:none; border-top:1px solid #e5e7eb; margin:0 0 32px;"/>

<!-- PRE-REQUISITES -->
<h2 style="font-size:1.2em; font-weight:700; color:#111827; margin-bottom:16px;">Prerequisites</h2>
<div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px; margin-bottom:36px;">
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:8px; padding:18px;">
    <div style="font-size:.72em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#6b7280; margin-bottom:6px;">Required</div>
    <div style="font-weight:700; color:#111827; margin-bottom:6px;">FHIR R5 Server</div>
    <p style="font-size:.82em; color:#6b7280; line-height:1.5; margin:0;">An R5-compliant FHIR server with support for Subscriptions, conditional create/update, and SMART Backend Services (e.g., HAPI FHIR, Smile CDR, Azure, AWS HealthLake, GCP Healthcare API).</p>
  </div>
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:8px; padding:18px;">
    <div style="font-size:.72em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#6b7280; margin-bottom:6px;">Required</div>
    <div style="font-weight:700; color:#111827; margin-bottom:6px;">OAuth2 / SMART</div>
    <p style="font-size:.82em; color:#6b7280; line-height:1.5; margin:0;">SMART Backend Services for system-level authentication using JWT bearer tokens. Mandatory for production use to ensure secure, audited access.</p>
  </div>
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:8px; padding:18px;">
    <div style="font-size:.72em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#6b7280; margin-bottom:6px;">Recommended</div>
    <div style="font-weight:700; color:#111827; margin-bottom:6px;">REST API Client</div>
    <p style="font-size:.82em; color:#6b7280; line-height:1.5; margin:0;">A REST client (e.g., Postman, cURL, or your RIM system) capable of sending FHIR JSON payloads over HTTPS. Essential for prototyping and testing.</p>
  </div>
</div>

<hr style="border:none; border-top:1px solid #e5e7eb; margin:0 0 32px;"/>

<!-- QUICK REFERENCE -->
<h2 style="font-size:1.2em; font-weight:700; color:#111827; margin-bottom:8px;">Quick Reference</h2>
<p style="font-size:.88em; color:#6b7280; margin-bottom:16px;">Essential starting points for each core APIX capability.</p>
<div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px; margin-bottom:36px;">
  <a href="workflow-overview.html" style="text-decoration:none; background:#f9fafb; border:1px solid #e5e7eb; border-radius:8px; padding:18px; display:block; text-align:center;">
    <div style="font-size:1.4em; margin-bottom:8px;">📤</div>
    <div style="font-weight:700; color:#111827; margin-bottom:4px; font-size:.95em;">Workflow Overview</div>
    <div style="font-size:.78em; color:#6b7280; margin-bottom:10px;">Business-friendly walkthrough</div>
    <div style="font-size:.78em; font-weight:700; color:#3b82f6;">Read →</div>
  </a>
  <a href="architecture.html" style="text-decoration:none; background:#f9fafb; border:1px solid #e5e7eb; border-radius:8px; padding:18px; display:block; text-align:center;">
    <div style="font-size:1.4em; margin-bottom:8px;">🏗️</div>
    <div style="font-weight:700; color:#111827; margin-bottom:4px; font-size:.95em;">Architecture</div>
    <div style="font-size:.78em; color:#6b7280; margin-bottom:10px;">System landscape & security</div>
    <div style="font-size:.78em; font-weight:700; color:#10b981;">Read →</div>
  </a>
  <a href="apixinteractionpattern.html" style="text-decoration:none; background:#f9fafb; border:1px solid #e5e7eb; border-radius:8px; padding:18px; display:block; text-align:center;">
    <div style="font-size:1.4em; margin-bottom:8px;">🔄</div>
    <div style="font-weight:700; color:#111827; margin-bottom:4px; font-size:.95em;">Interaction Pattern</div>
    <div style="font-size:.78em; color:#6b7280; margin-bottom:10px;">Technical protocol detail</div>
    <div style="font-size:.78em; font-weight:700; color:#8b5cf6;">Read →</div>
  </a>
</div>

<hr style="border:none; border-top:1px solid #e5e7eb; margin:0 0 32px;"/>

<!-- VALIDATE & BUILD -->
<h2 style="font-size:1.2em; font-weight:700; color:#111827; margin-bottom:12px;">Validate &amp; Build</h2>
<p style="font-size:.88em; color:#374151; line-height:1.6; margin-bottom:10px;">Once you have reviewed the architecture and workflow:</p>
<ol style="font-size:.88em; color:#374151; padding-left:20px; line-height:1.9; margin-bottom:32px;">
  <li><strong>Validate your FHIR resources</strong> — Use the <a href="https://validator.fhir.org" target="_blank" style="color:#2563eb; font-weight:600;">Official FHIR Validator</a> with the APIX IG package to check compliance with the profiles defined in this guide.</li>
  <li><strong>Test end-to-end</strong> — Post a Task to a test FHIR server, subscribe to status changes, and verify that notifications arrive at your webhook endpoint.</li>
  <li><strong>Connect your RIM</strong> — Use the provided examples as templates. Start with a simple shelf-life variation submission to establish connectivity.</li>
</ol>
