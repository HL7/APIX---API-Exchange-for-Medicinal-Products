<!-- WORKFLOW (merged Workflow Overview + Workflow Deep-Dive) -->
<div style="margin-bottom:32px;">
  <h2 style="font-size:1.7em; font-weight:800; color:#111827; margin-bottom:10px;">Workflow</h2>
  <p style="font-size:.95em; color:#6b7280; line-height:1.6; max-width:640px;">How RWI-pharma orchestrates a regulatory procedure — first the big picture, then a step-by-step technical walkthrough of a shelf-life update showing every FHIR resource exchange.</p>
</div>

<hr style="border:none; border-top:1px solid #e5e7eb; margin:0 0 32px;"/>

<!-- HOW IT WORKS -->
<div style="background:linear-gradient(135deg,#eff6ff,#faf5ff); border:1px solid #bfdbfe; border-radius:12px; padding:28px 32px; margin-bottom:32px;">
  <div style="font-weight:700; color:#111827; font-size:1.05em; margin-bottom:10px;">How RWI-pharma Works — The Big Picture</div>
  <p style="font-size:.88em; color:#374151; line-height:1.7; margin:0;">RWI-pharma uses a <strong>Task-based</strong> workflow model. Every regulatory interaction — submissions, questions, decisions, payments — is represented as a FHIR <strong>Task</strong> resource. The lifecycle of a regulatory procedure is a series of Tasks, each with a status that progresses from <em>draft → requested → received → accepted → in-progress → completed</em>. Both parties subscribe to real-time notifications so they instantly know when something changes.</p>
</div>

<!-- NOTIFICATION MECHANISM -->
<div style="background:#fffbeb; border:1px solid #fde68a; border-radius:8px; padding:14px 18px; margin-bottom:32px; font-size:.85em; color:#78350f; display:flex; gap:10px; align-items:flex-start;">
  <span style="flex-shrink:0; font-size:1rem;">⚠️</span>
  <span><strong>Key Principle:</strong> The Regulator does not directly "send" messages to the Company. Instead, the Regulator updates the Task on the server. The Company, having <a href="subscriptions.html" style="color:#92400e; font-weight:600;">subscribed</a> to that Task, receives an automatic notification whenever a change occurs.</span>
</div>

<!-- FOUR PHASES -->
<h2 style="font-size:1.3em; font-weight:700; color:#111827; margin-bottom:16px;">The Four Phases</h2>

<div style="display:grid; grid-template-columns:1fr 1fr 1fr 1fr; gap:14px; margin-bottom:32px;">
  <div style="background:#fff; border:1px solid #e5e7eb; border-top:3px solid #2563eb; border-radius:8px; padding:20px;">
    <div style="font-size:.72em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#2563eb; margin-bottom:6px;">Phase 1</div>
    <div style="font-weight:700; color:#111827; margin-bottom:6px;">Submission & Validation</div>
    <ol style="font-size:.82em; color:#4b5563; line-height:1.7; padding-left:16px; margin:0;">
      <li>Company registers and authenticates</li>
      <li>Company uploads documents (PDFs, FHIR Bundles)</li>
      <li>Company creates DocumentReferences (metadata)</li>
      <li>Company posts the Task (the "orchestrator")</li>
      <li>Regulator validates the package</li>
    </ol>
  </div>
  <div style="background:#fff; border:1px solid #e5e7eb; border-top:3px solid #f59e0b; border-radius:8px; padding:20px;">
    <div style="font-size:.72em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#b45309; margin-bottom:6px;">Phase 2</div>
    <div style="font-weight:700; color:#111827; margin-bottom:6px;">Payment</div>
    <ol style="font-size:.82em; color:#4b5563; line-height:1.7; padding-left:16px; margin:0;">
      <li>Regulator issues a Payment Request (Task)</li>
      <li>Company submits Proof of Payment</li>
      <li>Regulator verifies and completes Payment Task</li>
    </ol>
  </div>
  <div style="background:#fff; border:1px solid #e5e7eb; border-top:3px solid #10b981; border-radius:8px; padding:20px;">
    <div style="font-size:.72em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#10b981; margin-bottom:6px;">Phase 3</div>
    <div style="font-weight:700; color:#111827; margin-bottom:6px;">Review & Questions</div>
    <ol style="font-size:.82em; color:#4b5563; line-height:1.7; padding-left:16px; margin:0;">
      <li>Regulator conducts technical review</li>
      <li>Regulator issues Questions (as new Tasks)</li>
      <li>Company provides Responses (in Task.output)</li>
      <li>Iterative Q&A until all issues resolved</li>
    </ol>
  </div>
  <div style="background:#fff; border:1px solid #e5e7eb; border-top:3px solid #8b5cf6; border-radius:8px; padding:20px;">
    <div style="font-size:.72em; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#8b5cf6; margin-bottom:6px;">Phase 4</div>
    <div style="font-weight:700; color:#111827; margin-bottom:6px;">Decision</div>
    <ol style="font-size:.82em; color:#4b5563; line-height:1.7; padding-left:16px; margin:0;">
      <li>Regulator completes the original Task</li>
      <li>Decision letter attached to Task.output</li>
      <li>Company receives instant notification</li>
      <li>Full audit trail preserved in Provenance</li>
    </ol>
  </div>
</div>

<hr style="border:none; border-top:1px solid #e5e7eb; margin:0 0 32px;"/>

<!-- VISUAL WORKFLOW DIAGRAM -->
<h2 style="font-size:1.3em; font-weight:700; color:#111827; margin-bottom:12px;">Workflow Diagram</h2>
<p style="font-size:.88em; color:#6b7280; margin-bottom:16px;">The following diagram shows the complete lifecycle of a regulatory procedure through RWI-pharma — illustrating the back-and-forth exchange between Company and Regulator across all four phases.</p>

<div style="text-align:center; margin:20px 0 16px;">
  <img src="workflow-overview-diagram.png" alt="RWI-pharma Workflow — Ping-Pong Diagram showing the four-phase exchange between Company and Regulator" style="max-width:680px; width:100%; border-radius:10px; border:1px solid #e5e7eb;">
</div>

<hr style="border:none; border-top:1px solid #e5e7eb; margin:16px 0 32px;"/>

<!-- KEY CONCEPTS -->
<h2 style="font-size:1.3em; font-weight:700; color:#111827; margin-bottom:16px;">Key Concepts</h2>

<div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-bottom:32px;">
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:8px; padding:18px;">
    <div style="font-weight:700; color:#003087; margin-bottom:6px; font-size:.9em;">📋 Task = Regulatory Envelope</div>
    <p style="font-size:.85em; color:#4b5563; line-height:1.6; margin:0;">Every interaction (submission, question, decision) is a Task. Tasks carry metadata (who, what, when) and reference documents via <code>Task.input</code> and <code>Task.output</code>.</p>
  </div>
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:8px; padding:18px;">
    <div style="font-weight:700; color:#003087; margin-bottom:6px; font-size:.9em;">📄 DocumentReference = Library Card</div>
    <p style="font-size:.85em; color:#4b5563; line-height:1.6; margin:0;">Each uploaded file gets a metadata wrapper (title, type, CTD section). The regulator discovers files through the Task, downloading the payload only when needed.</p>
  </div>
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:8px; padding:18px;">
    <div style="font-weight:700; color:#003087; margin-bottom:6px; font-size:.9em;">🔔 Subscription = Real-Time Alert</div>
    <p style="font-size:.85em; color:#4b5563; line-height:1.6; margin:0;">Both parties subscribe to events (status changes, new Tasks). Notifications arrive instantly at configured endpoints — no polling required.</p>
  </div>
  <div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:8px; padding:18px;">
    <div style="font-weight:700; color:#003087; margin-bottom:6px; font-size:.9em;">🔗 groupIdentifier = Procedure Thread</div>
    <p style="font-size:.85em; color:#4b5563; line-height:1.6; margin:0;">All Tasks within a single regulatory procedure share the same <code>groupIdentifier</code>, enabling portfolio-wide search and reporting.</p>
  </div>
</div>

<hr style="border:none; border-top:1px solid #e5e7eb; margin:0 0 32px;"/>

<!-- STEP-BY-STEP WALKTHROUGH -->
<h2 id="walkthrough" style="font-size:1.3em; font-weight:700; color:#111827; margin-bottom:8px;">Step-by-Step Walkthrough: Shelf-Life Update</h2>
<p style="font-size:.88em; color:#6b7280; line-height:1.6; margin-bottom:16px;">The detailed exchange for a shelf-life update, with links to the example Task resources at each step. Jump straight to a key example:</p>

<div style="display:grid; grid-template-columns:repeat(4,1fr); gap:10px; margin-bottom:16px;">
  <a href="Task-scenario1-01-initial-submission.html" style="text-decoration:none; background:#eff6ff; border:1px solid #bfdbfe; border-radius:6px; padding:10px 12px; text-align:center; font-size:.82em; font-weight:600; color:#1d4ed8;">📤 Initial Submission</a>
  <a href="Task-scenario1-02-validation.html" style="text-decoration:none; background:#ecfdf5; border:1px solid #a7f3d0; border-radius:6px; padding:10px 12px; text-align:center; font-size:.82em; font-weight:600; color:#047857;">✅ Validation</a>
  <a href="Task-scenario1-05-technical-question.html" style="text-decoration:none; background:#fff7ed; border:1px solid #fed7aa; border-radius:6px; padding:10px 12px; text-align:center; font-size:.82em; font-weight:600; color:#c2410c;">❓ Question</a>
  <a href="Task-scenario1-07-final-decision.html" style="text-decoration:none; background:#faf5ff; border:1px solid #e9d5ff; border-radius:6px; padding:10px 12px; text-align:center; font-size:.82em; font-weight:600; color:#7e22ce;">📩 Decision</a>
</div>

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

<hr style="border:none; border-top:1px solid #e5e7eb; margin:0 0 32px;"/>

<!-- SEQUENCE DIAGRAM -->
### Sequence Diagram

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
