<!-- WORKFLOW DEEP-DIVE HEADER -->
<div style="margin-bottom:32px;">
  <h2 style="font-size:1.7em; font-weight:800; color:#111827; margin-bottom:10px;">Workflow Deep-Dive</h2>
  <p style="font-size:.95em; color:#6b7280; line-height:1.6; max-width:640px;">Detailed technical walkthrough of a "shelf-life update" scenario, illustrating every FHIR resource exchange between a Company and a Regulator.</p>
</div>

<div style="background:#eff6ff; border:1px solid #bfdbfe; border-radius:8px; padding:14px 18px; margin-bottom:32px; font-size:.85em; color:#1d4ed8; display:flex; gap:10px; align-items:flex-start;">
  <span style="flex-shrink:0;">💡</span>
  <span><strong>Looking for a business-friendly overview?</strong> Start with the <a href="workflow-overview.html" style="color:#1d4ed8; font-weight:600;">Workflow Overview</a> page first.</span>
</div>

<!-- NOTIFICATION CALLOUT -->
<div style="background:#fef3c7; border:1px solid #fcd34d; border-radius:10px; padding:20px 24px; margin-bottom:36px;">
  <div style="font-weight:700; color:#92400e; margin-bottom:8px; font-size:.95em;">⚠️ Notification Mechanism</div>
  <p style="font-size:.88em; color:#78350f; line-height:1.65; margin:0;">The Regulator does <strong>not</strong> directly "send" messages. Instead, it updates <code>Task.status</code> on the server. The Company receives notifications via its Subscription whenever a change occurs.</p>
</div>

<hr style="border:none; border-top:1px solid #e5e7eb; margin:0 0 36px;"/>

<!-- PHASE 0 -->
<div style="background:linear-gradient(135deg,#f0f9ff,#eff6ff); border:1px solid #bfdbfe; border-radius:12px; padding:24px 28px; margin-bottom:32px;">
  <div style="display:flex; align-items:center; gap:10px; margin-bottom:16px;">
    <span style="display:inline-flex; align-items:center; justify-content:center; width:36px; height:36px; border-radius:50%; background:#003087; color:#fff; font-weight:800; font-size:.85em;">0</span>
    <span style="font-size:1.15em; font-weight:700; color:#003087;">Registration &amp; Connection</span>
  </div>
  <div style="background:#fff; border:1px solid #e5e7eb; border-radius:8px; padding:16px 20px; margin-bottom:12px;">
    <div style="font-weight:700; color:#111827; font-size:.92em; margin-bottom:6px;">Step 0.1 — Company Registers with Regulator</div>
    <p style="font-size:.85em; color:#4b5563; line-height:1.65; margin:0;">One-time registration with the Regulator's API portal. The Regulator registers the Company as an <code>Organization</code> and provides API credentials. The Company also registers an <code>Endpoint</code> for subscription notifications.</p>
  </div>
  <div style="background:#fff; border:1px solid #e5e7eb; border-radius:8px; padding:16px 20px;">
    <div style="font-weight:700; color:#111827; font-size:.92em; margin-bottom:6px;">Step 0.2 — Company Connects to API</div>
    <p style="font-size:.85em; color:#4b5563; line-height:1.65; margin:0;">The Company authenticates via OAuth2, confirming authorization to post resources for their medicinal products.</p>
  </div>
</div>

<!-- PHASE 1 -->
<div style="background:linear-gradient(135deg,#ecfdf5,#f0fdf4); border:1px solid #a7f3d0; border-radius:12px; padding:24px 28px; margin-bottom:32px;">
  <div style="display:flex; align-items:center; gap:10px; margin-bottom:16px;">
    <span style="display:inline-flex; align-items:center; justify-content:center; width:36px; height:36px; border-radius:50%; background:#047857; color:#fff; font-weight:800; font-size:.85em;">1</span>
    <span style="font-size:1.15em; font-weight:700; color:#047857;">Submission &amp; Validation</span>
  </div>

  <div style="background:#fff; border:1px solid #e5e7eb; border-radius:8px; padding:16px 20px; margin-bottom:12px;">
    <div style="font-weight:700; color:#111827; font-size:.92em; margin-bottom:6px;">Step 1.0 — Company Prepares Submission</div>
    <p style="font-size:.85em; color:#4b5563; line-height:1.65; margin:0;">Granular <strong>"Index Pattern"</strong> instead of monolithic ZIP — high performance and scalability even for massive datasets.</p>
  </div>

  <div style="background:#fff; border:1px solid #e5e7eb; border-radius:8px; padding:16px 20px; margin-bottom:12px;">
    <div style="font-weight:700; color:#111827; font-size:.92em; margin-bottom:6px;">Step 1.1 — Upload Binaries &amp; Bundles</div>
    <table style="width:100%; font-size:.83em; border-collapse:collapse; margin-top:8px;">
      <thead><tr style="background:#f9fafb; text-align:left;">
        <th style="padding:8px 10px; border-bottom:1px solid #e5e7eb;">Content Type</th>
        <th style="padding:8px 10px; border-bottom:1px solid #e5e7eb;">FHIR Resource</th>
      </tr></thead>
      <tbody>
        <tr><td style="padding:8px 10px; border-bottom:1px solid #f3f4f6; color:#4b5563;">PDF Documents</td><td style="padding:8px 10px; border-bottom:1px solid #f3f4f6;"><code>Binary</code></td></tr>
        <tr><td style="padding:8px 10px; border-bottom:1px solid #f3f4f6; color:#4b5563;">Structured Labeling (JSON)</td><td style="padding:8px 10px; border-bottom:1px solid #f3f4f6;">Document <code>Bundle</code></td></tr>
        <tr><td style="padding:8px 10px; color:#4b5563;">CMC Data</td><td style="padding:8px 10px;">Transaction <code>Bundle</code></td></tr>
      </tbody>
    </table>
  </div>

  <div style="background:#fff; border:1px solid #e5e7eb; border-radius:8px; padding:16px 20px; margin-bottom:12px;">
    <div style="font-weight:700; color:#111827; font-size:.92em; margin-bottom:6px;">Step 1.2 — Create DocumentReferences</div>
    <p style="font-size:.85em; color:#4b5563; line-height:1.65; margin:0;">Each upload gets a <code>DocumentReference</code> — a "Library Card" with metadata and a pointer to the uploaded resource.</p>
  </div>

  <div style="background:#fff; border:1px solid #e5e7eb; border-radius:8px; padding:16px 20px; margin-bottom:12px;">
    <div style="font-weight:700; color:#111827; font-size:.92em; margin-bottom:6px;">Step 1.3 — Create &amp; Post the Task</div>
    <p style="font-size:.85em; color:#4b5563; line-height:1.65; margin-bottom:8px;">The <code>Task</code> is the "Orchestrator" — it holds procedure metadata and references every <code>DocumentReference</code> in <code>Task.input</code>.</p>
    <div style="font-size:.82em; color:#6b7280;">📎 <a href="Task-scenario1-01-initial-submission.json" target="_blank" style="color:#1d4ed8;">JSON</a> · <a href="Task-scenario1-01-initial-submission.html" target="_blank" style="color:#1d4ed8;">HTML View</a></div>
  </div>

  <div style="background:#fff; border:1px solid #e5e7eb; border-radius:8px; padding:16px 20px;">
    <div style="font-weight:700; color:#111827; font-size:.92em; margin-bottom:6px;">Step 2.0 — Regulator Validates</div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-top:10px;">
      <div style="background:#ecfdf5; border:1px solid #a7f3d0; border-radius:6px; padding:12px 16px;">
        <div style="font-weight:700; color:#065f46; font-size:.85em;">✅ Passes</div>
        <p style="font-size:.82em; color:#064e3b; margin:4px 0 6px;">Status → <strong>Accepted</strong>. Receipt &amp; results attached.</p>
        <div style="font-size:.78em;">📎 <a href="Task-scenario1-02-validation.json" target="_blank" style="color:#1d4ed8;">JSON</a> · <a href="Task-scenario1-02-validation.html" target="_blank" style="color:#1d4ed8;">HTML</a></div>
      </div>
      <div style="background:#fef2f2; border:1px solid #fecaca; border-radius:6px; padding:12px 16px;">
        <div style="font-weight:700; color:#991b1b; font-size:.85em;">❌ Fails</div>
        <p style="font-size:.82em; color:#7f1d1d; margin:4px 0 0;">Missing docs requested → Company re-submits → Re-validation.</p>
      </div>
    </div>
  </div>
</div>

<!-- PHASE 2 -->
<div style="background:linear-gradient(135deg,#faf5ff,#fdf4ff); border:1px solid #e9d5ff; border-radius:12px; padding:24px 28px; margin-bottom:32px;">
  <div style="display:flex; align-items:center; gap:10px; margin-bottom:6px;">
    <span style="display:inline-flex; align-items:center; justify-content:center; width:36px; height:36px; border-radius:50%; background:#7e22ce; color:#fff; font-weight:800; font-size:.85em;">2</span>
    <span style="font-size:1.15em; font-weight:700; color:#7e22ce;">Review Cycles</span>
  </div>
  <p style="font-size:.85em; color:#6b7280; margin:0 0 20px;">Multiple reviews happen <strong>in parallel</strong>.</p>

  <div style="background:#fff; border-left:4px solid #3b82f6; border-radius:0 8px 8px 0; padding:14px 20px; margin-bottom:12px;">
    <div style="font-weight:700; color:#1d4ed8; font-size:.88em;">Track A — Compliance Check</div>
    <p style="font-size:.83em; color:#4b5563; margin:4px 0 0;">Regulator checks compliance of the scientific data.</p>
  </div>

  <div style="background:#fff; border-left:4px solid #f59e0b; border-radius:0 8px 8px 0; padding:14px 20px; margin-bottom:12px;">
    <div style="font-weight:700; color:#b45309; font-size:.88em; margin-bottom:8px;">Track B — Financial Review</div>
    <ol style="font-size:.83em; color:#4b5563; line-height:1.75; padding-left:20px; margin:0 0 8px;">
      <li><strong>5.B.1</strong> — Regulator determines fee is due</li>
      <li><strong>5.B.3</strong> — Company posts proof of payment (<code>Binary</code> → <code>DocumentReference</code> → added as Task <strong>output</strong>)</li>
      <li><strong>5.B.4</strong> — Regulator verifies proof → Payment Task <strong>Completed</strong></li>
    </ol>
    <div style="font-size:.8em; color:#6b7280;">📎 <a href="Task-scenario1-04-finance-payment.json" target="_blank" style="color:#1d4ed8;">JSON</a> · <a href="Task-scenario1-04-finance-payment.html" target="_blank" style="color:#1d4ed8;">HTML View</a></div>
  </div>

  <div style="background:#fff; border:1px solid #e5e7eb; border-radius:8px; padding:16px 20px;">
    <div style="font-weight:700; color:#111827; font-size:.92em; margin-bottom:10px;">Step 5.3 — Issue Resolution Loop</div>

    <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:6px; padding:12px 16px; margin-bottom:10px;">
      <div style="font-weight:700; color:#374151; font-size:.85em;">5.3.1 — Regulator Posts Questionnaire</div>
      <p style="font-size:.82em; color:#4b5563; margin:4px 0 6px;">POST <code>Questionnaire</code> → <code>DocumentReference</code> → <strong>Question Task</strong> (input: DocRef)</p>
      <div style="font-size:.78em;">📎 <a href="Task-scenario1-05-technical-question.json" target="_blank" style="color:#1d4ed8;">JSON</a> · <a href="Task-scenario1-05-technical-question.html" target="_blank" style="color:#1d4ed8;">HTML</a></div>
    </div>
    <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:6px; padding:12px 16px; margin-bottom:10px;">
      <div style="font-weight:700; color:#374151; font-size:.85em;">5.3.2 — Company Posts Response</div>
      <p style="font-size:.82em; color:#4b5563; margin:4px 0 6px;">POST <code>QuestionnaireResponse</code> → <code>DocumentReference</code> → added as Task <strong>output</strong></p>
      <div style="font-size:.78em;">📎 <a href="Task-scenario1-06-technical-response.json" target="_blank" style="color:#1d4ed8;">JSON</a> · <a href="Task-scenario1-06-technical-response.html" target="_blank" style="color:#1d4ed8;">HTML</a></div>
    </div>
    <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:6px; padding:12px 16px;">
      <div style="font-weight:700; color:#374151; font-size:.85em;">5.3.3 — Regulator Reviews Response</div>
      <p style="font-size:.82em; color:#4b5563; margin:4px 0 0;">If satisfactory → Question Task <strong>Completed</strong> → review continues.</p>
    </div>
  </div>
</div>

<!-- PHASE 3 -->
<div style="background:linear-gradient(135deg,#fff7ed,#fffbeb); border:1px solid #fed7aa; border-radius:12px; padding:24px 28px; margin-bottom:36px;">
  <div style="display:flex; align-items:center; gap:10px; margin-bottom:16px;">
    <span style="display:inline-flex; align-items:center; justify-content:center; width:36px; height:36px; border-radius:50%; background:#c2410c; color:#fff; font-weight:800; font-size:.85em;">3</span>
    <span style="font-size:1.15em; font-weight:700; color:#c2410c;">Final Decision</span>
  </div>
  <div style="background:#fff; border:1px solid #e5e7eb; border-radius:8px; padding:16px 20px;">
    <div style="font-weight:700; color:#111827; font-size:.92em; margin-bottom:6px;">Step 6.0 — Final Decision</div>
    <p style="font-size:.85em; color:#4b5563; line-height:1.65; margin-bottom:8px;">Regulator updates <code>Task.status</code> to <strong>completed</strong> and attaches decision documents to <code>Task.output</code>.</p>
    <div style="font-size:.82em; color:#6b7280;">📎 <a href="Task-scenario1-07-final-decision.json" target="_blank" style="color:#1d4ed8;">JSON</a> · <a href="Task-scenario1-07-final-decision.html" target="_blank" style="color:#1d4ed8;">HTML View</a></div>
  </div>
</div>

<hr style="border:none; border-top:1px solid #e5e7eb; margin:0 0 36px;"/>

### Workflow Diagram

```mermaid
sequenceDiagram
    participant C as Company
    participant R as Regulator
    
    %% Phase 0: Registration
    Note over C,R: Phase 0: Registration & Connection
    C->>R: 0.1 Register with Regulator Portal
    R-->>C: Client Credentials & Org ID
    C->>R: 0.2 OAuth2 Authentication
    
    %% Phase 1: Submission
    Note over C,R: Phase 1: Submission & Validation
    par Upload Binaries/Bundles
        C->>R: 1.1 POST PDFs (Binary)
        C->>R: 1.1 POST Labels (Document Bundles)
        C->>R: 1.1 POST CMC (Transaction Bundles)
    end
    C->>R: 1.2 POST DocumentReferences (IDs/Links)
    C->>R: 1.3 POST Task (Orchestrator Index)
    
    activate R
    R->>R: 2.0 Validate Application
    
    alt Validation Passes
        R-->>C: 3.1 Ack Receipt & Validation Results
    else Validation Fails
        R->>C: 4.1 Request Missing Documents
        C->>R: 4.2.1 Submit Missing Documents
        R->>R: 4.2.2 Re-validate
    end
    
    %% Phase 2: Review
    Note over C,R: Phase 2: Review Cycles
    
    par Parallel Checks
        rect rgb(240, 248, 255)
            Note right of R: Technical Review
            R->>R: 5.2.1 Check Compliance
        end
        
        rect rgb(255, 250, 240)
            Note right of R: Financial Review
            R->>R: Review Financials
            Note over R: 5.B.2 Invoice Sequence
            R->>R: POST Invoice (Binary/Resource)
            R->>R: POST DocumentReference
            R->>C: POST Payment Task (Input: DocRef)
            activate C
            Note over C: 5.B.3 Payment Sequence
            C->>C: POST Proof of Payment (Binary)
            C->>C: POST DocumentReference
            C-->>R: Update Task (Add Output DocRef)
            deactivate C
            R->>R: 5.B.4 Verify Proof & Set Task: completed
        end
    end
    
    loop Issue Resolution
        alt Issue Found
            Note over R: 5.3.1 Question Sequence
            R->>R: POST Questionnaire
            R->>R: POST DocumentReference
            R->>C: POST Question Task (Input: DocRef)
            activate C
            Note over C: 5.3.2 Response Sequence
            C->>C: POST QuestionnaireResponse
            C->>C: POST DocumentReference
            C-->>R: Update Task (Add Output DocRef)
            deactivate C
            R->>R: 5.3.3 Review & Set Task: completed
        else No Issues
            R->>R: Proceed to Decision
        end
    end
    
    %% Phase 3: Decision
    Note over C,R: Phase 3: Final Decision
    
    alt Approved
        R-->>C: 6.1 Notify Approval (Decision Letter)
    else Rejected
        R-->>C: 7.1 Notify Rejection
    end
    deactivate R
```
