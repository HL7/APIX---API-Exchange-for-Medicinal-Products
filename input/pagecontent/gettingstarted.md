<!-- GETTING STARTED HEADER -->
<div style="margin-bottom:32px;">
  <h2 style="font-size:1.7em; font-weight:800; color:#111827; margin-bottom:10px;">Getting Started with APIX</h2>
  <p style="font-size:.95em; color:#6b7280; line-height:1.6; max-width:640px;">Five simple steps to connect your systems to a regulator. Each step builds on the previous one — start at the top and work your way down.</p>
</div>

<hr style="border:none; border-top:1px solid #e5e7eb; margin:0 0 32px;"/>

<!-- ========================================= -->
<!-- 5-STEP DETAILED WALKTHROUGH               -->
<!-- ========================================= -->

<!-- STEP 1: CONNECT -->
<div style="background:#fff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; border-radius:10px; padding:28px 32px; margin-bottom:20px; position:relative;">
  <div style="display:flex; align-items:flex-start; gap:20px; flex-wrap:wrap;">
    <div style="flex-shrink:0;">
      <div style="width:56px; height:56px; border-radius:50%; background:linear-gradient(135deg,#eff6ff,#dbeafe); border:3px solid #2563eb; display:flex; align-items:center; justify-content:center; font-size:1.5em; font-weight:800; color:#2563eb;">1</div>
    </div>
    <div style="flex:1; min-width:260px;">
      <div style="font-size:.72em; font-weight:700; text-transform:uppercase; letter-spacing:.12em; color:#2563eb; margin-bottom:4px;">Step 1</div>
      <div style="font-weight:800; color:#111827; font-size:1.15em; margin-bottom:8px;">Connect via API</div>
      <p style="font-size:.9em; color:#374151; line-height:1.65; margin-bottom:12px;">Register your <strong>Organization</strong> and <strong>Endpoint</strong> on the regulator's FHIR server. This tells the regulator who you are and where to send notifications back to you.</p>
      <div style="background:#f0f9ff; border-radius:6px; padding:10px 14px; margin-bottom:12px;">
        <div style="font-size:.78em; color:#0369a1; font-weight:600; margin-bottom:4px;">💡 Think of it like…</div>
        <div style="font-size:.82em; color:#374151; line-height:1.5;">Registering a shipping address before you can send or receive packages. You only do this once.</div>
      </div>
      <div style="font-size:.82em; color:#6b7280;">✅ <strong>Business benefit:</strong> One-time setup — connects your company to any regulator that supports APIX.</div>
      <div style="margin-top:10px;"><a href="apixorganizationEndpoint.html" style="font-size:.82em; color:#2563eb; font-weight:600; text-decoration:none;">Deep dive: Organization &amp; Endpoint →</a></div>
    </div>
  </div>
</div>

<!-- STEP 2: STREAM -->
<div style="background:#fff; border:1px solid #99f6e4; border-left:5px solid #0d9488; border-radius:10px; padding:28px 32px; margin-bottom:20px; position:relative;">
  <div style="display:flex; align-items:flex-start; gap:20px; flex-wrap:wrap;">
    <div style="flex-shrink:0;">
      <div style="width:56px; height:56px; border-radius:50%; background:linear-gradient(135deg,#f0fdfa,#ccfbf1); border:3px solid #0d9488; display:flex; align-items:center; justify-content:center; font-size:1.5em; font-weight:800; color:#0d9488;">2</div>
    </div>
    <div style="flex:1; min-width:260px;">
      <div style="font-size:.72em; font-weight:700; text-transform:uppercase; letter-spacing:.12em; color:#0d9488; margin-bottom:4px;">Step 2</div>
      <div style="font-weight:800; color:#111827; font-size:1.15em; margin-bottom:8px;">Stream Files as Binary</div>
      <p style="font-size:.9em; color:#374151; line-height:1.65; margin-bottom:12px;">Upload any file type — <strong>PDF, DOCX, XML, JSON, data sets</strong> — to the regulator's FHIR server as a <strong>Binary</strong> resource. Files are stored securely and accessed on-demand by the reviewer.</p>
      <div style="background:#f0fdfa; border-radius:6px; padding:10px 14px; margin-bottom:12px;">
        <div style="font-size:.78em; color:#0f766e; font-weight:600; margin-bottom:4px;">💡 Think of it like…</div>
        <div style="font-size:.82em; color:#374151; line-height:1.5;">Netflix for documents. Instead of mailing a box of DVDs (a giant ZIP file), each document is streamed individually — the reviewer only downloads what they need, when they need it.</div>
      </div>
      <div style="font-size:.82em; color:#6b7280;">✅ <strong>Business benefit:</strong> No more massive portal uploads. Sub-second processing instead of hours of waiting.</div>
      <div style="margin-top:10px;"><a href="document-streaming.html" style="font-size:.82em; color:#0d9488; font-weight:600; text-decoration:none;">Deep dive: Document Streaming →</a></div>
    </div>
  </div>
</div>

<!-- STEP 3: DESCRIBE -->
<div style="background:#fff; border:1px solid #fed7aa; border-left:5px solid #ea580c; border-radius:10px; padding:28px 32px; margin-bottom:20px; position:relative;">
  <div style="display:flex; align-items:flex-start; gap:20px; flex-wrap:wrap;">
    <div style="flex-shrink:0;">
      <div style="width:56px; height:56px; border-radius:50%; background:linear-gradient(135deg,#fff7ed,#fed7aa); border:3px solid #ea580c; display:flex; align-items:center; justify-content:center; font-size:1.5em; font-weight:800; color:#ea580c;">3</div>
    </div>
    <div style="flex:1; min-width:260px;">
      <div style="font-size:.72em; font-weight:700; text-transform:uppercase; letter-spacing:.12em; color:#ea580c; margin-bottom:4px;">Step 3</div>
      <div style="font-weight:800; color:#111827; font-size:1.15em; margin-bottom:8px;">Describe with DocumentReference</div>
      <p style="font-size:.9em; color:#374151; line-height:1.65; margin-bottom:12px;">For each Binary you uploaded, create a <strong>DocumentReference</strong> resource that captures metadata — the file's <strong>category, version, type, and CTD section</strong>. This lets the regulator search, filter, and discover your documents without downloading them.</p>
      <div style="background:#fff7ed; border-radius:6px; padding:10px 14px; margin-bottom:12px;">
        <div style="font-size:.78em; color:#c2410c; font-weight:600; margin-bottom:4px;">💡 Think of it like…</div>
        <div style="font-size:.82em; color:#374151; line-height:1.5;">A library catalog card. The card describes the book (title, author, subject) so you can find it without reading every book on the shelf.</div>
      </div>
      <div style="font-size:.82em; color:#6b7280;">✅ <strong>Business benefit:</strong> Reviewers instantly find the exact document they need. No more searching through ZIP files.</div>
      <div style="margin-top:10px;"><a href="apixdocumentReference.html" style="font-size:.82em; color:#ea580c; font-weight:600; text-decoration:none;">Deep dive: DocumentReference →</a></div>
    </div>
  </div>
</div>

<!-- STEP 4: ORCHESTRATE -->
<div style="background:#fff; border:1px solid #e9d5ff; border-left:5px solid #7c3aed; border-radius:10px; padding:28px 32px; margin-bottom:20px; position:relative;">
  <div style="display:flex; align-items:flex-start; gap:20px; flex-wrap:wrap;">
    <div style="flex-shrink:0;">
      <div style="width:56px; height:56px; border-radius:50%; background:linear-gradient(135deg,#faf5ff,#e9d5ff); border:3px solid #7c3aed; display:flex; align-items:center; justify-content:center; font-size:1.5em; font-weight:800; color:#7c3aed;">4</div>
    </div>
    <div style="flex:1; min-width:260px;">
      <div style="font-size:.72em; font-weight:700; text-transform:uppercase; letter-spacing:.12em; color:#7c3aed; margin-bottom:4px;">Step 4</div>
      <div style="font-weight:800; color:#111827; font-size:1.15em; margin-bottom:8px;">Orchestrate with Task</div>
      <p style="font-size:.9em; color:#374151; line-height:1.65; margin-bottom:12px;">Create a <strong>FHIR Task</strong> resource to initiate and track a regulatory activity — <em>any type of activity, for any type of regulated product</em>. The Task references your DocumentReferences and progresses through status changes as the procedure advances.</p>
      <div style="background:#faf5ff; border-radius:6px; padding:10px 14px; margin-bottom:12px;">
        <div style="font-size:.78em; color:#7e22ce; font-weight:600; margin-bottom:4px;">💡 Think of it like…</div>
        <div style="font-size:.82em; color:#374151; line-height:1.5;">A FedEx tracking number. You create the shipment (Task), attach the packages (documents), and then both sender and receiver can track exactly where it is in the process at every step.</div>
      </div>
      <div style="font-size:.82em; color:#6b7280; margin-bottom:8px;">✅ <strong>Business benefit:</strong> Every date and time is recorded. After the procedure, analyze and visualize cycle times across one or many regulatory activities.</div>
      <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:6px; padding:12px 16px; margin-bottom:12px;">
        <div style="font-size:.78em; font-weight:700; color:#374151; margin-bottom:6px;">What can you track?</div>
        <div style="display:flex; flex-wrap:wrap; gap:6px;">
          <span style="background:#eff6ff; border:1px solid #bfdbfe; color:#1d4ed8; padding:4px 10px; border-radius:4px; font-size:.75em; font-weight:600;">Clinical Trial Application</span>
          <span style="background:#ecfdf5; border:1px solid #a7f3d0; color:#047857; padding:4px 10px; border-radius:4px; font-size:.75em; font-weight:600;">MAA</span>
          <span style="background:#fff7ed; border:1px solid #fed7aa; color:#c2410c; padding:4px 10px; border-radius:4px; font-size:.75em; font-weight:600;">Shelf-life Update</span>
          <span style="background:#faf5ff; border:1px solid #e9d5ff; color:#7e22ce; padding:4px 10px; border-radius:4px; font-size:.75em; font-weight:600;">Label Update</span>
          <span style="background:#fce7f3; border:1px solid #fbcfe8; color:#be185d; padding:4px 10px; border-radius:4px; font-size:.75em; font-weight:600;">Invoice Payment</span>
          <span style="background:#f0fdfa; border:1px solid #99f6e4; color:#0f766e; padding:4px 10px; border-radius:4px; font-size:.75em; font-weight:600;">Q&amp;A Exchange</span>
          <span style="background:#fffbeb; border:1px solid #fde68a; color:#92400e; padding:4px 10px; border-radius:4px; font-size:.75em; font-weight:600;">Decision Letter</span>
        </div>
      </div>
      <div style="margin-top:10px;"><a href="apixtask.html" style="font-size:.82em; color:#7c3aed; font-weight:600; text-decoration:none;">Deep dive: APIX Task Structure →</a></div>
    </div>
  </div>
</div>

<!-- STEP 5: SUBSCRIBE -->
<div style="background:#fff; border:1px solid #a7f3d0; border-left:5px solid #059669; border-radius:10px; padding:28px 32px; margin-bottom:32px; position:relative;">
  <div style="display:flex; align-items:flex-start; gap:20px; flex-wrap:wrap;">
    <div style="flex-shrink:0;">
      <div style="width:56px; height:56px; border-radius:50%; background:linear-gradient(135deg,#ecfdf5,#a7f3d0); border:3px solid #059669; display:flex; align-items:center; justify-content:center; font-size:1.5em; font-weight:800; color:#059669;">5</div>
    </div>
    <div style="flex:1; min-width:260px;">
      <div style="font-size:.72em; font-weight:700; text-transform:uppercase; letter-spacing:.12em; color:#059669; margin-bottom:4px;">Step 5</div>
      <div style="font-weight:800; color:#111827; font-size:1.15em; margin-bottom:8px;">Subscribe for Real-Time Updates</div>
      <p style="font-size:.9em; color:#374151; line-height:1.65; margin-bottom:12px;">Set up a <strong>Subscription</strong> to receive instant notifications whenever Tasks are updated as the regulatory activity progresses. Both company and regulator subscribe — so both sides know immediately when something changes.</p>
      <div style="background:#ecfdf5; border-radius:6px; padding:10px 14px; margin-bottom:12px;">
        <div style="font-size:.78em; color:#047857; font-weight:600; margin-bottom:4px;">💡 Think of it like…</div>
        <div style="font-size:.82em; color:#374151; line-height:1.5;">Package delivery notifications. You don't need to keep checking the website — you get a push notification the moment your package moves to the next step.</div>
      </div>
      <div style="font-size:.82em; color:#6b7280;">✅ <strong>Business benefit:</strong> No more logging into portals to check status. Your system is notified automatically in real-time.</div>
      <div style="margin-top:10px;"><a href="subscriptions.html" style="font-size:.82em; color:#059669; font-weight:600; text-decoration:none;">Deep dive: Real-Time Subscriptions →</a></div>
    </div>
  </div>
</div>

<hr style="border:none; border-top:1px solid #e5e7eb; margin:0 0 32px;"/>

<!-- ========================================= -->
<!-- TASK LIFECYCLE TIMELINE                   -->
<!-- ========================================= -->
<h2 style="font-size:1.2em; font-weight:700; color:#111827; margin-bottom:8px;">Task Lifecycle</h2>
<p style="font-size:.88em; color:#6b7280; margin-bottom:20px;">As a regulatory activity progresses, the Task's status moves through these stages. Each transition is timestamped, creating a complete audit trail.</p>

<div style="display:flex; align-items:center; justify-content:center; gap:0; margin-bottom:12px; flex-wrap:wrap; padding:16px 0;">
  <div style="text-align:center; padding:0 12px;">
    <div style="width:18px; height:18px; border-radius:50%; background:#2563eb; margin:0 auto 8px;"></div>
    <div style="font-size:.78em; font-weight:700; color:#2563eb;">draft</div>
  </div>
  <div style="width:40px; height:2px; background:#d1d5db; flex-shrink:0;"></div>
  <div style="text-align:center; padding:0 12px;">
    <div style="width:18px; height:18px; border-radius:50%; background:#0d9488; margin:0 auto 8px;"></div>
    <div style="font-size:.78em; font-weight:700; color:#0d9488;">requested</div>
  </div>
  <div style="width:40px; height:2px; background:#d1d5db; flex-shrink:0;"></div>
  <div style="text-align:center; padding:0 12px;">
    <div style="width:18px; height:18px; border-radius:50%; background:#ea580c; margin:0 auto 8px;"></div>
    <div style="font-size:.78em; font-weight:700; color:#ea580c;">received</div>
  </div>
  <div style="width:40px; height:2px; background:#d1d5db; flex-shrink:0;"></div>
  <div style="text-align:center; padding:0 12px;">
    <div style="width:18px; height:18px; border-radius:50%; background:#f59e0b; margin:0 auto 8px;"></div>
    <div style="font-size:.78em; font-weight:700; color:#b45309;">accepted</div>
  </div>
  <div style="width:40px; height:2px; background:#d1d5db; flex-shrink:0;"></div>
  <div style="text-align:center; padding:0 12px;">
    <div style="width:18px; height:18px; border-radius:50%; background:#7c3aed; margin:0 auto 8px;"></div>
    <div style="font-size:.78em; font-weight:700; color:#7c3aed;">in-progress</div>
  </div>
  <div style="width:40px; height:2px; background:#d1d5db; flex-shrink:0;"></div>
  <div style="text-align:center; padding:0 12px;">
    <div style="width:18px; height:18px; border-radius:50%; background:#059669; margin:0 auto 8px;"></div>
    <div style="font-size:.78em; font-weight:700; color:#059669;">completed</div>
  </div>
</div>

<!-- CYCLE-TIME ANALYTICS TEASER -->
<div style="background:linear-gradient(135deg,#faf5ff,#eff6ff); border:1px solid #e9d5ff; border-radius:10px; padding:20px 24px; margin-bottom:32px; display:flex; align-items:flex-start; gap:14px;">
  <div style="font-size:1.3em; flex-shrink:0;">📈</div>
  <div>
    <div style="font-weight:700; color:#111827; font-size:.92em; margin-bottom:6px;">Cycle-Time Analytics</div>
    <p style="font-size:.85em; color:#374151; line-height:1.6; margin:0;">Because every status change is timestamped, you can analyze the duration of each phase across one or many regulatory procedures. Visualize bottlenecks, benchmark SLA performance, and identify opportunities to accelerate time-to-market for your products.</p>
  </div>
</div>

<hr style="border:none; border-top:1px solid #e5e7eb; margin:0 0 32px;"/>

<!-- ========================================= -->
<!-- PERSONA ROUTING (SIMPLIFIED)              -->
<!-- ========================================= -->
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

<!-- VALIDATE & BUILD -->
<h2 style="font-size:1.2em; font-weight:700; color:#111827; margin-bottom:12px;">Validate &amp; Build</h2>
<p style="font-size:.88em; color:#374151; line-height:1.6; margin-bottom:10px;">Once you have reviewed the architecture and workflow:</p>
<ol style="font-size:.88em; color:#374151; padding-left:20px; line-height:1.9; margin-bottom:32px;">
  <li><strong>Validate your FHIR resources</strong> — Use the <a href="https://validator.fhir.org" target="_blank" style="color:#2563eb; font-weight:600;">Official FHIR Validator</a> with the APIX IG package to check compliance with the profiles defined in this guide.</li>
  <li><strong>Test end-to-end</strong> — Post a Task to a test FHIR server, subscribe to status changes, and verify that notifications arrive at your webhook endpoint.</li>
  <li><strong>Connect your RIM</strong> — Use the provided examples as templates. Start with a simple shelf-life variation submission to establish connectivity.</li>
</ol>
