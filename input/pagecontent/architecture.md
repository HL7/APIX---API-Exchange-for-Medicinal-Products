The following architecture components are illustrative suggestions only. Implementers are free to select any technologies or platforms (including on-premises, cloud-based, or hybrid solutions) that meet the specified functional requirements.

<table style="width:100%; border-collapse: collapse; border: 1px solid #d0d0d0;">
  <thead>
    <tr style="background-color: #f5f5f5; text-align: left;">
      <th style="padding: 12px; border: 1px solid #d0d0d0;">Component</th>
      <th style="padding: 12px; border: 1px solid #d0d0d0;">Minimum Requirement</th>
      <th style="padding: 12px; border: 1px solid #d0d0d0;">Recommendation / Examples</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 12px; border: 1px solid #d0d0d0; vertical-align: top;"><strong>FHIR Server<br>(Regulatory Authority and Submitting Company)</strong></td>
      <td style="padding: 12px; border: 1px solid #d0d0d0; vertical-align: top;">FHIR R5, conditional create/update, Subscriptions, SMART Backend Services</td>
      <td style="padding: 12px; border: 1px solid #d0d0d0; vertical-align: top;">Open-source or commercial servers such as HAPI FHIR, Smile CDR, Microsoft Azure API for FHIR, AWS HealthLake, Google Cloud Healthcare API, or any other compliant FHIR server</td>
    </tr>
    <tr>
      <td style="padding: 12px; border: 1px solid #d0d0d0; vertical-align: top;"><strong>Authentication</strong></td>
      <td style="padding: 12px; border: 1px solid #d0d0d0; vertical-align: top;">SMART Backend Services (system-level scopes, JWT bearer tokens)</td>
      <td style="padding: 12px; border: 1px solid #d0d0d0; vertical-align: top;">Mandatory for production use</td>
    </tr>
    <tr>
      <td style="padding: 12px; border: 1px solid #d0d0d0; vertical-align: top;"><strong>Subscriptions</strong></td>
      <td style="padding: 12px; border: 1px solid #d0d0d0; vertical-align: top;">R5-native or R5 backport, rest-hook channel with signed webhook delivery</td>
      <td style="padding: 12px; border: 1px solid #d0d0d0; vertical-align: top;">Mandatory for production environments</td>
    </tr>
    <tr>
      <td style="padding: 12px; border: 1px solid #d0d0d0; vertical-align: top;"><strong>Validation Engine</strong></td>
      <td style="padding: 12px; border: 1px solid #d0d0d0; vertical-align: top;">Support for <code>$validate</code> operation + custom regulatory rules Operation</td>
      <td style="padding: 12px; border: 1px solid #d0d0d0; vertical-align: top;">May be implemented as part of the FHIR server, an API gateway, or a dedicated validation service</td>
    </tr>
    <tr>
      <td style="padding: 12px; border: 1px solid #d0d0d0; vertical-align: top;"><strong>Audit</strong></td>
      <td style="padding: 12px; border: 1px solid #d0d0d0; vertical-align: top;">Provenance resource created/updated on every relevant Task change</td>
      <td style="padding: 12px; border: 1px solid #d0d0d0; vertical-align: top;">Mandatory</td>
    </tr>
    <tr>
      <td style="padding: 12px; border: 1px solid #d0d0d0; vertical-align: top;"><strong>Search / Grouping</strong></td>
      <td style="padding: 12px; border: 1px solid #d0d0d0; vertical-align: top;">Support for <code>groupIdentifier</code>, <code>partOf</code>, chaining, and reverse chaining as required by the profiles</td>
      <td style="padding: 12px; border: 1px solid #d0d0d0; vertical-align: top;">Essential for workflow navigation and reporting</td>
    </tr>
  </tbody>
</table>

### System Landscape

The following interaction diagram illustrates how these components work together in a production environment:

<pre class="mermaid">
sequenceDiagram
    autonumber
    participant App as Applicant (RIM System)
    participant Auth as Auth Server (OAuth2)
    participant APIX as APIX FHIR Server
    participant Val as Validation Engine

    note over App, Val: Phase 1: Authentication & Submission
    
    App->>Auth: 1. Request Access Token
    Auth-->>App: 2. Return JWT (Scope: system/Task.cruds)
    
    App->>APIX: 3. POST /Task (Submission Bundle)
    APIX->>Val: 4. $validate Bundle
    Val-->>APIX: 5. Validation Outcome (Pass)
    APIX-->>App: 6. 201 Created (Task.status = received)

    note over App, Val: Phase 2: Asynchronous Processing & Notification

    APIX->>APIX: 7. Regulator Review (Status Change)
    
    par Real-Time Notification
        APIX->>App: 8. POST Subscription Notification (Task.status = in-progress)
    and Audit Logging
        APIX->>APIX: 9. Create Provenance Record
    end

</pre>

### Data Governance and Security

The APIX "Index Pattern" relies on a **logical separation** of data rather than physical silos. This approach ensures scalability while maintaining strict intellectual property (IP) protection.

#### Logical Data Separation (Multi-Tenancy)
In a shared regulatory environment, data for different medicinal products (e.g., Drug A vs. Drug B) sits in a common storage layer but is differentiated by FHIR metadata:

*   **Subject Linking**: Every `DocumentReference` is linked to a specific `MedicinalProductDefinition` via the `subject` field, ensuring documents are contextually tied to the correct product lifecycle.
*   **Metadata Categorization**: The `category` and `type` fields (using CTD Module and Section codes) provide the structural hierarchy needed to organize large submissions within the product context.
*   **Shared Infrastructure**: While physical separation (e.g., dedicated database instances per company) is an implementation choice, the APIX standard is designed to work in a multi-tenant environment where metadata-driven filters provide the necessary isolation.

#### IP Protection and Access Control
To protect company trade secrets and clinical data, the following security principles are applied:

1.  **SMART on FHIR & OAuth2**: All access is authenticated via system-level or user-level JWT tokens. These tokens carry claims about the user's organizational affiliation (e.g., `Org: SynthPharma`).
2.  **Attribute-Based Access Control (ABAC)**: The regulator's FHIR server acts as a Policy Enforcement Point. Every query is intercepted to ensure that a company can only search for or retrieve resources that "belong" to their organizational compartment.
3.  **Security Labels**: The `DocumentReference.securityLabel` field allows for granular confidentiality tagging (e.g., `R` for Restricted). Access is denied unless the requester’s security clearance matches the document's label.
4.  **Provenance & Integrity**: Every upload is tracked via a `Provenance` resource, providing a cryptographic audit trail that proves the origin and integrity of the submission, ensuring no unauthorized party has modified or accessed the index.

### Binary Upload Guide (Post-then-Link)

To handle large documents (e.g., 20MB PDFs) or massive data packages (e.g., 50GB stability datasets) without impacting API performance, APIX utilizes a two-step **"Post-then-Link"** mechanism.

#### Step 1: Upload Raw Binary
The submittor posts the file as a raw octet-stream directly to the `/Binary` endpoint. This avoids the overhead of Base64 encoding.

*   **Request**: `POST [base]/Binary`
*   **Header**: `Content-Type: application/pdf` (or appropriate MIME type)
*   **Body**: Raw binary bytes.
*   **Response**: `201 Created` with a `Location` header (e.g., `Location: Binary/123`).

#### Step 2: Create Metadata Link (`DocumentReference`)
The submittor creates a `DocumentReference` resource that "claims" the binary and provides regulatory context (CTD section, title, etc.).

*   **Content URL**: Set `DocumentReference.content.attachment.url` to the ID received in Step 1 (`Binary/123`).
*   **Metadata**: Add `category` (e.g., Module 3) and `type` (e.g., Stability Report) to allow for indexing and search.

#### Step 3: Orchestrate via Task
The `DocumentReference` ID is added to the `Task.input` or `Task.output` array. The regulator can now discover the file through the Task and only retrieve the binary payload if needed.

#### Technical Benefits
*   **Memory Efficiency**: The server can stream the binary directly to storage without loading the entire file into memory.
*   **Scalability**: Supports massive files that would otherwise exceed JSON size limits.
*   **Resume-ability**: If an upload is interrupted, only the specific Binary needs to be retried, not the entire submission package.