<!-- WORKFLOW OVERVIEW -->

<div style="margin-bottom:32px;">
  <h2 style="font-size:1.7em; font-weight:800; color:#111827; margin-bottom:10px;">Workflow Overview</h2>
  <p style="font-size:.95em; color:#6b7280; line-height:1.6; max-width:640px;">A business-friendly walkthrough of how APIX orchestrates the regulatory lifecycle — from initial submission to final decision.</p>
</div>

<hr style="border:none; border-top:1px solid #e5e7eb; margin:0 0 32px;"/>

<!-- HOW IT WORKS -->
<div style="background:linear-gradient(135deg,#eff6ff,#faf5ff); border:1px solid #bfdbfe; border-radius:12px; padding:28px 32px; margin-bottom:32px;">
  <div style="font-weight:700; color:#111827; font-size:1.05em; margin-bottom:10px;">How APIX Works — The Big Picture</div>
  <p style="font-size:.88em; color:#374151; line-height:1.7; margin:0;">APIX uses a <strong>Task-based</strong> workflow model. Every regulatory interaction — submissions, questions, decisions, payments — is represented as a FHIR <strong>Task</strong> resource. The lifecycle of a regulatory procedure is a series of Tasks, each with a status that progresses from <em>draft → requested → received → accepted → in-progress → completed</em>. Both parties subscribe to real-time notifications so they instantly know when something changes.</p>
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
<p style="font-size:.88em; color:#6b7280; margin-bottom:16px;">The following diagram shows the complete lifecycle of a regulatory procedure through APIX — illustrating the back-and-forth exchange between Company and Regulator across all four phases.</p>

<div style="text-align:center; margin:20px 0 16px;">
  <img src="workflow-overview-diagram.png" alt="APIX Workflow Overview — Ping-Pong Diagram showing the four-phase exchange between Company and Regulator" style="max-width:680px; width:100%; border-radius:10px; border:1px solid #e5e7eb;">
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

<!-- EXAMPLE TASK LIFECYCLE -->
<h2 style="font-size:1.3em; font-weight:700; color:#111827; margin-bottom:12px;">Example: Shelf-Life Update</h2>

<div style="display:grid; grid-template-columns:repeat(4,1fr); gap:10px; margin-bottom:16px;">
  <a href="Task-scenario1-01-initial-submission.html" style="text-decoration:none; background:#eff6ff; border:1px solid #bfdbfe; border-radius:6px; padding:10px 12px; text-align:center; font-size:.82em; font-weight:600; color:#1d4ed8;">📤 Initial Submission</a>
  <a href="Task-scenario1-02-validation.html" style="text-decoration:none; background:#ecfdf5; border:1px solid #a7f3d0; border-radius:6px; padding:10px 12px; text-align:center; font-size:.82em; font-weight:600; color:#047857;">✅ Validation</a>
  <a href="Task-scenario1-05-technical-question.html" style="text-decoration:none; background:#fff7ed; border:1px solid #fed7aa; border-radius:6px; padding:10px 12px; text-align:center; font-size:.82em; font-weight:600; color:#c2410c;">❓ Question</a>
  <a href="Task-scenario1-07-final-decision.html" style="text-decoration:none; background:#faf5ff; border:1px solid #e9d5ff; border-radius:6px; padding:10px 12px; text-align:center; font-size:.82em; font-weight:600; color:#7e22ce;">📩 Decision</a>
</div>

<div style="background:#f9fafb; border:1px solid #e5e7eb; border-radius:8px; padding:14px 18px; font-size:.85em; color:#374151; display:flex; gap:10px; align-items:flex-start;">
  <span style="flex-shrink:0;">🔍</span>
  <span><strong>Technical Deep-Dive:</strong> For the full step-by-step technical detail of this workflow including FHIR resource examples, see the <a href="workflow.html" style="color:#2563eb; font-weight:600;">Workflow Deep-Dive</a>.</span>
</div>
