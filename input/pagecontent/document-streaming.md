<!-- DOCUMENT STREAMING PAGE -->
<div style="margin-bottom:32px;">
  <h2 style="font-size:1.7em; font-weight:800; color:#111827; margin-bottom:10px;">Document Streaming</h2>
  <p style="font-size:.95em; color:#6b7280; line-height:1.6; max-width:640px;">How APIX modernizes document exchange by moving from bulk portal uploads to a Netflix-style "streaming" metadata model.</p>
</div>

<hr style="border:none; border-top:1px solid #e5e7eb; margin:0 0 32px;"/>

<!-- THE PROBLEM -->
<div style="background:#fef2f2; border:1px solid #fecaca; border-radius:12px; padding:24px 32px; margin-bottom:32px;">
  <div style="font-weight:700; color:#991b1b; font-size:.92em; margin-bottom:12px; text-transform:uppercase; letter-spacing:0.05em;">The "DVD Delivery" Problem</div>
  <p style="font-size:.88em; color:#7f1d1d; line-height:1.6; margin-bottom:16px;">Today's regulatory portals operate like the old mail-order DVD business. When a company submits an application, they package hundreds or thousands of PDFs into a massive ZIP file (eCTD) and upload it via a portal.</p>
  <ul style="font-size:.85em; color:#7f1d1d; line-height:1.6; padding-left:20px; margin:0;">
    <li>The company's system is locked up pushing gigabytes of data.</li>
    <li>The regulator's system is locked up receiving, virus-scanning, and storing it.</li>
    <li>Reviewers must download the entire massive package just to find and read a single 5-page clinical summary.</li>
  </ul>
</div>

<!-- THE SOLUTION -->
<div style="background:linear-gradient(135deg,#eff6ff,#faf5ff); border:1px solid #bfdbfe; border-radius:12px; padding:28px 32px; margin-bottom:32px;">
  <div style="font-weight:700; color:#111827; font-size:1.05em; margin-bottom:12px;">The APIX Solution: The Netflix Model</div>
  <p style="font-size:.88em; color:#374151; line-height:1.6; margin-bottom:16px;">APIX changes this paradigm by treating documents like a modern streaming service treats movies. Instead of forcing the regulator to download the whole "DVD box set" upfront, APIX separates the <strong>catalog</strong> from the <strong>content</strong>.</p>

  <div style="display:grid; grid-template-columns:1fr 1fr; gap:20px;">
    <div style="background:#fff; border:1px solid #e5e7eb; border-radius:8px; padding:18px;">
      <div style="font-weight:700; color:#003087; margin-bottom:6px; font-size:.9em;">1. The Catalog (DocumentReference)</div>
      <p style="font-size:.85em; color:#4b5563; line-height:1.6; margin:0;">The company sends lightweight metadata — titles, CTD sections, file types, and unique identifiers. The regulator's system indexes this instantly. This is the "Netflix menu."</p>
    </div>
    <div style="background:#fff; border:1px solid #e5e7eb; border-radius:8px; padding:18px;">
      <div style="font-weight:700; color:#003087; margin-bottom:6px; font-size:.9em;">2. The Content (Binary)</div>
      <p style="font-size:.85em; color:#4b5563; line-height:1.6; margin:0;">The actual heavy PDF/JSON files are stored securely on the FHIR server. They are only "streamed" (downloaded) at the exact moment a human reviewer clicks to read them.</p>
    </div>
  </div>
</div>

<hr style="border:none; border-top:1px solid #e5e7eb; margin:0 0 32px;"/>

<!-- BUSINESS BENEFITS -->
<h2 style="font-size:1.3em; font-weight:700; color:#111827; margin-bottom:16px;">Why This Matters for Business Leaders</h2>

<div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px; margin-bottom:32px;">
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:8px; padding:18px;">
    <div style="font-size:1.6em; margin-bottom:10px;">⚡</div>
    <div style="font-weight:700; color:#111827; margin-bottom:6px;">Sub-second Processing</div>
    <p style="font-size:.85em; color:#4b5563; line-height:1.6; margin:0;">Because the regulator only processes the lightweight "catalog" during the initial submission, wait times drop from hours to milliseconds.</p>
  </div>
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:8px; padding:18px;">
    <div style="font-size:1.6em; margin-bottom:10px;">💾</div>
    <div style="font-weight:700; color:#111827; margin-bottom:6px;">Drastic Cost Reduction</div>
    <p style="font-size:.85em; color:#4b5563; line-height:1.6; margin:0;">Regulators no longer need massive, expensive staging servers to hold gigabytes of ZIP files while they are unzipped and scanned.</p>
  </div>
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:8px; padding:18px;">
    <div style="font-size:1.6em; margin-bottom:10px;">🎯</div>
    <div style="font-weight:700; color:#111827; margin-bottom:6px;">Precision Updates</div>
    <p style="font-size:.85em; color:#4b5563; line-height:1.6; margin:0;">When answering a regulatory question, the company only sends the specific new document, rather than re-uploading an entire sequence folder.</p>
  </div>
</div>

<div style="background:#f0fdfa; border:1px solid #99f6e4; border-radius:8px; padding:14px 18px; font-size:.85em; color:#0f766e; display:flex; gap:10px; align-items:flex-start;">
  <span style="flex-shrink:0;">🔍</span>
  <span><strong>Technical Deep-Dive:</strong> For the exact sequence of how client systems upload the Binary and then link it via the DocumentReference, see the <a href="architecture.html#binary-upload-guide-post-then-link" style="color:#0f766e; font-weight:600; text-decoration:underline;">Post-then-Link</a> section of the Architecture guide.</span>
</div>
