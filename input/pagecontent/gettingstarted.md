<!-- GETTING STARTED HEADER -->
<div style="margin-bottom:32px;">
  <p style="font-size:.95em; color:#6b7280; line-height:1.6; max-width:640px;">Five simple steps to connect any two parties in a regulatory exchange — industry to regulator, regulator to industry, regulator to regulator, or industry to industry. Each step builds on the previous one, so start at the top and work down.</p>
</div>

<hr style="border:none; border-top:1px solid #e5e7eb; margin:0 0 32px;"/>

<!-- ========================================= -->
<!-- 5-STEP DETAILED WALKTHROUGH               -->
<!-- ========================================= -->

### Step 1: Connect via API

<!-- STEP 1: CONNECT -->
<div style="background:#fff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; border-radius:10px; padding:28px 32px; margin-bottom:20px; position:relative;">
  <div style="display:flex; align-items:flex-start; gap:20px; flex-wrap:wrap;">
    <div style="flex-shrink:0;">
      <div style="width:56px; height:56px; border-radius:50%; background:linear-gradient(135deg,#eff6ff,#dbeafe); border:3px solid #2563eb; display:flex; align-items:center; justify-content:center; font-size:1.5em; font-weight:800; color:#2563eb;">1</div>
    </div>
    <div style="flex:1; min-width:260px;">
      <p style="font-size:.9em; color:#374151; line-height:1.65; margin-bottom:12px;">Register your <strong>Organization</strong> and <strong>Endpoint</strong> on the receiving party's FHIR server, whether that is a regulator or a company. This tells the other party who you are and where to send notifications back to you.</p>
      <div style="background:#f0f9ff; border-radius:6px; padding:10px 14px; margin-bottom:12px;">
        <div style="font-size:.78em; color:#0369a1; font-weight:600; margin-bottom:4px;">💡 Think of it like…</div>
        <div style="font-size:.82em; color:#374151; line-height:1.5;">Registering a shipping address before you can send or receive packages. You only do this once.</div>
      </div>
      <div style="font-size:.82em; color:#6b7280;">✅ <strong>Business benefit:</strong> One-time setup — connects your organization to any party, regulator or company, that supports RWI-pharma.</div>
      <div style="margin-top:10px;"><a href="apixorganizationEndpoint.html" style="font-size:.82em; color:#2563eb; font-weight:600; text-decoration:none;">Deep dive: Organization &amp; Endpoint →</a></div>
    </div>
  </div>
</div>

### Step 2: Stream Files as Binary

<!-- STEP 2: STREAM -->
<div style="background:#fff; border:1px solid #99f6e4; border-left:5px solid #0d9488; border-radius:10px; padding:28px 32px; margin-bottom:20px; position:relative;">
  <div style="display:flex; align-items:flex-start; gap:20px; flex-wrap:wrap;">
    <div style="flex-shrink:0;">
      <div style="width:56px; height:56px; border-radius:50%; background:linear-gradient(135deg,#f0fdfa,#ccfbf1); border:3px solid #0d9488; display:flex; align-items:center; justify-content:center; font-size:1.5em; font-weight:800; color:#0d9488;">2</div>
    </div>
    <div style="flex:1; min-width:260px;">
      <p style="font-size:.9em; color:#374151; line-height:1.65; margin-bottom:12px;">Upload any file type — <strong>PDF, DOCX, XML, JSON, data sets</strong> — to the receiving party's FHIR server as a <strong>Binary</strong> resource. Files are stored securely and accessed on-demand by the recipient.</p>
      <div style="background:#f0fdfa; border-radius:6px; padding:10px 14px; margin-bottom:12px;">
        <div style="font-size:.78em; color:#0f766e; font-weight:600; margin-bottom:4px;">💡 Think of it like…</div>
        <div style="font-size:.82em; color:#374151; line-height:1.5;">Netflix for documents. Instead of mailing a box of DVDs (a giant ZIP file), each document is streamed individually — the recipient only downloads what they need, when they need it.</div>
      </div>
      <div style="font-size:.82em; color:#6b7280;">✅ <strong>Business benefit:</strong> No more massive portal uploads. Sub-second processing instead of hours of waiting.</div>
      <div style="margin-top:10px;"><a href="architecture.html#binary-upload-guide-post-then-link" style="font-size:.82em; color:#0d9488; font-weight:600; text-decoration:none;">Deep dive: Binary upload (Post-then-Link) →</a></div>
    </div>
  </div>
</div>

### Step 3: Describe with DocumentReference

<!-- STEP 3: DESCRIBE -->
<div style="background:#fff; border:1px solid #fed7aa; border-left:5px solid #ea580c; border-radius:10px; padding:28px 32px; margin-bottom:20px; position:relative;">
  <div style="display:flex; align-items:flex-start; gap:20px; flex-wrap:wrap;">
    <div style="flex-shrink:0;">
      <div style="width:56px; height:56px; border-radius:50%; background:linear-gradient(135deg,#fff7ed,#fed7aa); border:3px solid #ea580c; display:flex; align-items:center; justify-content:center; font-size:1.5em; font-weight:800; color:#ea580c;">3</div>
    </div>
    <div style="flex:1; min-width:260px;">
      <p style="font-size:.9em; color:#374151; line-height:1.65; margin-bottom:12px;">For each Binary you uploaded, create a <strong>DocumentReference</strong> resource that captures metadata — the file's <strong>category, version, type, and CTD section</strong>. This lets the recipient search, filter, and discover your documents without downloading them. In Step 4, these DocumentReferences are attached to a Task as inputs (if you created the Task) or outputs (if you are doing the work it asks for).</p>
      <div style="background:#fff7ed; border-radius:6px; padding:10px 14px; margin-bottom:12px;">
        <div style="font-size:.78em; color:#c2410c; font-weight:600; margin-bottom:4px;">💡 Think of it like…</div>
        <div style="font-size:.82em; color:#374151; line-height:1.5;">A library catalog card. The card describes the book (title, author, subject) so you can find it without reading every book on the shelf.</div>
      </div>
      <div style="font-size:.82em; color:#6b7280;">✅ <strong>Business benefit:</strong> Recipients instantly find the exact document they need. No more searching through ZIP files.</div>
      <div style="margin-top:10px;"><a href="apixdocumentReference.html" style="font-size:.82em; color:#ea580c; font-weight:600; text-decoration:none;">Deep dive: DocumentReference →</a></div>
    </div>
  </div>
</div>

### Step 4: Orchestrate with Task

<!-- STEP 4: ORCHESTRATE -->
<div style="background:#fff; border:1px solid #e9d5ff; border-left:5px solid #7c3aed; border-radius:10px; padding:28px 32px; margin-bottom:20px; position:relative;">
  <div style="display:flex; align-items:flex-start; gap:20px; flex-wrap:wrap;">
    <div style="flex-shrink:0;">
      <div style="width:56px; height:56px; border-radius:50%; background:linear-gradient(135deg,#faf5ff,#e9d5ff); border:3px solid #7c3aed; display:flex; align-items:center; justify-content:center; font-size:1.5em; font-weight:800; color:#7c3aed;">4</div>
    </div>
    <div style="flex:1; min-width:260px;">
      <p style="font-size:.9em; color:#374151; line-height:1.65; margin-bottom:12px;">Create a <strong>FHIR Task</strong> resource to initiate and track a regulatory activity — <em>any type of regulatory activity for human biopharmaceutical products</em>. The Task carries the DocumentReferences in both directions and progresses through status changes as the procedure advances.</p>
      <div style="background:#faf5ff; border-radius:6px; padding:10px 14px; margin-bottom:12px;">
        <div style="font-size:.78em; color:#7e22ce; font-weight:600; margin-bottom:4px;">💡 Think of it like…</div>
        <div style="font-size:.82em; color:#374151; line-height:1.5;">A FedEx tracking number. You create the shipment (Task), attach the packages (documents), and then both sender and receiver can track exactly where it is in the process at every step.</div>
      </div>
      <div style="background:#fff; border:1px solid #e9d5ff; border-radius:6px; padding:12px 16px; margin-bottom:12px;">
        <div style="font-size:.78em; font-weight:700; color:#7e22ce; margin-bottom:6px;">Inputs come from the requester, outputs from the owner</div>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-bottom:8px;">
          <div style="background:#faf5ff; border-radius:6px; padding:8px 12px;">
            <div style="font-size:.78em; font-weight:700; color:#374151;">Requester → <code>Task.input</code></div>
            <div style="font-size:.8em; color:#4b5563; line-height:1.5;">The party that creates the Task supplies what the work needs.</div>
          </div>
          <div style="background:#faf5ff; border-radius:6px; padding:8px 12px;">
            <div style="font-size:.78em; font-weight:700; color:#374151;">Owner → <code>Task.output</code></div>
            <div style="font-size:.8em; color:#4b5563; line-height:1.5;">The party that does the work returns the result.</div>
          </div>
        </div>
        <div style="font-size:.8em; color:#4b5563; line-height:1.55;"><strong>Example:</strong> on a Payment Task created by the regulator, the <em>invoice</em> is an input and the <em>proof of payment</em> returned by the applicant is an output. On a submission Task created by the applicant, the dossier documents are inputs and the regulator's decision letter is an output. See <a href="terminology.html">Terminology</a> for example input and output types.</div>
      </div>
      <div style="font-size:.82em; color:#6b7280; margin-bottom:8px;">✅ <strong>Business benefit:</strong> Every date and time is recorded. After the procedure, analyze and visualize cycle times across one or many regulatory activities.</div>
      <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:6px; padding:12px 16px; margin-bottom:12px;">
        <div style="font-size:.78em; font-weight:700; color:#374151; margin-bottom:6px;">What can you track?</div>
        <div style="display:flex; flex-wrap:wrap; gap:6px;">
          <span style="background:#eff6ff; border:1px solid #bfdbfe; color:#1d4ed8; padding:4px 10px; border-radius:4px; font-size:.75em; font-weight:600;">Clinical Trial Application</span>
          <span style="background:#ecfdf5; border:1px solid #a7f3d0; color:#047857; padding:4px 10px; border-radius:4px; font-size:.75em; font-weight:600;">NDA/MAA</span>
          <span style="background:#fff7ed; border:1px solid #fed7aa; color:#c2410c; padding:4px 10px; border-radius:4px; font-size:.75em; font-weight:600;">Shelf-life Update</span>
          <span style="background:#faf5ff; border:1px solid #e9d5ff; color:#7e22ce; padding:4px 10px; border-radius:4px; font-size:.75em; font-weight:600;">Label Negotiation</span>
          <span style="background:#fce7f3; border:1px solid #fbcfe8; color:#be185d; padding:4px 10px; border-radius:4px; font-size:.75em; font-weight:600;">Invoice Payment</span>
          <span style="background:#f0fdfa; border:1px solid #99f6e4; color:#0f766e; padding:4px 10px; border-radius:4px; font-size:.75em; font-weight:600;">Q&amp;A Exchange</span>
          <span style="background:#fffbeb; border:1px solid #fde68a; color:#92400e; padding:4px 10px; border-radius:4px; font-size:.75em; font-weight:600;">Decision Letter</span>
          <span style="background:#fef2f2; border:1px solid #fecaca; color:#b91c1c; padding:4px 10px; border-radius:4px; font-size:.75em; font-weight:600;">Adverse Event Report</span>
          <span style="background:#f0f9ff; border:1px solid #bae6fd; color:#0369a1; padding:4px 10px; border-radius:4px; font-size:.75em; font-weight:600;">Pre-submission Meeting</span>
        </div>
      </div>
      <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:6px; padding:12px 16px; margin-bottom:12px;">
        <div style="font-size:.78em; font-weight:700; color:#374151; margin-bottom:4px;">Task lifecycle</div>
        <p style="font-size:.8em; color:#6b7280; line-height:1.5; margin:0 0 4px;">As a regulatory activity progresses, the Task's status moves through these stages. Each transition is timestamped, creating a complete audit trail.</p>
        <div style="display:flex; align-items:center; justify-content:center; gap:0; margin-bottom:4px; flex-wrap:wrap; padding:10px 0 4px;">
  <div style="text-align:center; padding:0 8px;">
    <div style="width:18px; height:18px; border-radius:50%; background:#2563eb; margin:0 auto 8px;"></div>
    <div style="font-size:.78em; font-weight:700; color:#2563eb;">draft</div>
  </div>
  <div style="width:28px; height:2px; background:#d1d5db; flex-shrink:0;"></div>
  <div style="text-align:center; padding:0 8px;">
    <div style="width:18px; height:18px; border-radius:50%; background:#0d9488; margin:0 auto 8px;"></div>
    <div style="font-size:.78em; font-weight:700; color:#0d9488;">requested</div>
  </div>
  <div style="width:28px; height:2px; background:#d1d5db; flex-shrink:0;"></div>
  <div style="text-align:center; padding:0 8px;">
    <div style="width:18px; height:18px; border-radius:50%; background:#ea580c; margin:0 auto 8px;"></div>
    <div style="font-size:.78em; font-weight:700; color:#ea580c;">received</div>
  </div>
  <div style="width:28px; height:2px; background:#d1d5db; flex-shrink:0;"></div>
  <div style="text-align:center; padding:0 8px;">
    <div style="width:18px; height:18px; border-radius:50%; background:#f59e0b; margin:0 auto 8px;"></div>
    <div style="font-size:.78em; font-weight:700; color:#b45309;">accepted</div>
  </div>
  <div style="width:28px; height:2px; background:#d1d5db; flex-shrink:0;"></div>
  <div style="text-align:center; padding:0 8px;">
    <div style="width:18px; height:18px; border-radius:50%; background:#7c3aed; margin:0 auto 8px;"></div>
    <div style="font-size:.78em; font-weight:700; color:#7c3aed;">in-progress</div>
  </div>
  <div style="width:28px; height:2px; background:#d1d5db; flex-shrink:0;"></div>
  <div style="text-align:center; padding:0 8px;">
    <div style="width:18px; height:18px; border-radius:50%; background:#059669; margin:0 auto 8px;"></div>
    <div style="font-size:.78em; font-weight:700; color:#059669;">completed</div>
  </div>
</div>
        <div style="background:linear-gradient(135deg,#faf5ff,#eff6ff); border:1px solid #e9d5ff; border-radius:10px; padding:14px 18px; margin-bottom:0; display:flex; align-items:flex-start; gap:14px;">
  <div style="font-size:1.3em; flex-shrink:0;">📈</div>
  <div>
    <div style="font-weight:700; color:#111827; font-size:.92em; margin-bottom:6px;">Cycle-Time Analytics</div>
    <p style="font-size:.85em; color:#374151; line-height:1.6; margin:0;">Because every status change is timestamped, you can analyze the duration of each phase across one or many regulatory procedures. Visualize bottlenecks, benchmark SLA performance, and identify opportunities to accelerate time-to-market for your products.</p>
  </div>
</div>
      </div>
      <div style="margin-top:10px;"><a href="apixtask.html" style="font-size:.82em; color:#7c3aed; font-weight:600; text-decoration:none;">Deep dive: RWI-pharma Task Structure →</a></div>
    </div>
  </div>
</div>

### Step 5: Subscribe for Real-Time Updates

<!-- STEP 5: SUBSCRIBE -->
<div style="background:#fff; border:1px solid #a7f3d0; border-left:5px solid #059669; border-radius:10px; padding:28px 32px; margin-bottom:32px; position:relative;">
  <div style="display:flex; align-items:flex-start; gap:20px; flex-wrap:wrap;">
    <div style="flex-shrink:0;">
      <div style="width:56px; height:56px; border-radius:50%; background:linear-gradient(135deg,#ecfdf5,#a7f3d0); border:3px solid #059669; display:flex; align-items:center; justify-content:center; font-size:1.5em; font-weight:800; color:#059669;">5</div>
    </div>
    <div style="flex:1; min-width:260px;">
      <p style="font-size:.9em; color:#374151; line-height:1.65; margin-bottom:12px;">Set up a <strong>Subscription</strong> to receive instant notifications whenever Tasks are updated as the regulatory activity progresses. Both parties subscribe — so both sides know immediately when something changes.</p>
      <div style="background:#ecfdf5; border-radius:6px; padding:10px 14px; margin-bottom:12px;">
        <div style="font-size:.78em; color:#047857; font-weight:600; margin-bottom:4px;">💡 Think of it like…</div>
        <div style="font-size:.82em; color:#374151; line-height:1.5;">Package delivery notifications. You don't need to keep checking the website — you get a push notification the moment your package moves to the next step.</div>
      </div>
      <div style="font-size:.82em; color:#6b7280;">✅ <strong>Business benefit:</strong> No more logging into portals to check status. Your system is notified automatically in real-time.</div>
      <div style="margin-top:10px;"><a href="subscriptions.html" style="font-size:.82em; color:#059669; font-weight:600; text-decoration:none;">Deep dive: Notifications →</a></div>
    </div>
  </div>
</div>

<hr style="border:none; border-top:1px solid #e5e7eb; margin:0 0 32px;"/>

<!-- PRE-REQUISITES -->
### Prerequisites

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
### Validate & Build

<p style="font-size:.88em; color:#374151; line-height:1.6; margin-bottom:10px;">Once you have reviewed the architecture and workflow:</p>
<ol style="font-size:.88em; color:#374151; padding-left:20px; line-height:1.9; margin-bottom:32px;">
  <li><strong>Validate your FHIR resources</strong> — Use the <a href="https://validator.fhir.org" target="_blank" style="color:#2563eb; font-weight:600;">Official FHIR Validator</a> with the RWI-pharma IG package to check compliance with the profiles defined in this guide.</li>
  <li><strong>Test end-to-end</strong> — Post a Task to a test FHIR server, subscribe to status changes, and verify that notifications arrive at your webhook endpoint.</li>
  <li><strong>Connect your RIM</strong> — Use the provided examples as templates. Start with a simple shelf-life variation submission to establish connectivity.</li>
</ol>
