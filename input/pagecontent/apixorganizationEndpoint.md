<!-- ORGANIZATION & ENDPOINT PAGE -->
<div style="margin-bottom:16px;">
  <h2 style="font-size:1.7em; font-weight:800; color:#111827; margin-bottom:10px;">Organization & Endpoint</h2>
  <p style="font-size:.95em; color:#6b7280; line-height:1.6; max-width:640px;">Organizations represent the parties in regulatory exchange (Applicants and Regulators), while Endpoints define the technical channels for receiving notifications.</p>
</div>

<div style="background:linear-gradient(135deg,#ecfdf5,#eff6ff); border:1px solid #a7f3d0; border-radius:12px; padding:20px 24px; margin-bottom:24px;">
  <div style="font-weight:700; color:#003087; font-size:.92em; margin-bottom:6px;">For Business Readers</div>
  <p style="font-size:.85em; color:#374151; line-height:1.6; margin:0;">Think of Organization as your <strong>digital business card</strong> on the FHIR server — it identifies who you are. The Endpoint is your <strong>mailbox address</strong> — where the server delivers webhook notifications. Together they form the identity and communication layer of APIX.</p>
</div>

In APIX, **Organization** and **Endpoint** work together to represent the parties involved in regulatory exchange and the technical channels used for communication. An **Organization** represents either an Applicant or a Regulator on the FHIR server and includes the contact and identification details needed throughout a regulatory procedure. Organizations may reference one or more **Endpoints**, which define the technical connection details for receiving notifications or other machine‑to‑machine interactions.

The **Endpoint.managingOrganization** element is especially important: it identifies which Organization owns or controls the Endpoint, ensuring that only the appropriate party can modify or maintain the connection details. Together, Organization and Endpoint form the identity and communication layer of the APIX ecosystem.

[Example Organization](Organization-1002.html)

[Example Endpoint](Endpoint-1003.html)

[Example Endpoint with header element](Endpoint-1005.html)

---

### Organization

<style>
.apix-table { border-collapse: collapse; width: 100%; margin: 1.5em 0; }
.apix-table th, .apix-table td { border: 1px solid #d3d3d3; padding: 10px; text-align: left; vertical-align: top; }
.apix-table th { background-color: #f0f0f0; font-weight: bold; }
.apix-table tr:nth-child(even) { background-color: #f9f9f9; }
</style>

<table class="apix-table">
<thead>
<tr>
<th>Element</th>
<th>Cardinality (APIX)</th>
<th>Value / Example</th>
<th>Purpose / Notes</th>
</tr>
</thead>
<tbody>

<tr>
<td><code>Organization.identifier</code></td>
<td>1..*</td>
<td>Globally unique identifier</td>
<td>Primary identity for Applicants and Regulators within APIX</td>
</tr>

<tr>
<td><code>Organization.endpoint</code></td>
<td>1..*</td>
<td>Reference to <code>Endpoint</code></td>
<td>Links the Organization to the technical endpoint used for receiving notifications or other automated interactions</td>
</tr>

</tbody>
</table>

---

### Endpoint

<style>
.apix-table { border-collapse: collapse; width: 100%; margin: 1.5em 0; }
.apix-table th, .apix-table td { border: 1px solid #d3d3d3; padding: 10px; text-align: left; vertical-align: top; }
.apix-table th { background-color: #f0f0f0; font-weight: bold; }
.apix-table tr:nth-child(even) { background-color: #f9f9f9; }
</style>

<table class="apix-table">
<thead>
<tr>
<th>Element</th>
<th>Cardinality (APIX)</th>
<th>Value / Example</th>
<th>Purpose / Notes</th>
</tr>
</thead>
<tbody>

<tr>
<td><code>Endpoint.identifier</code></td>
<td>0..*</td>
<td>Globally unique identifier</td>
<td>Enables reuse across multiple FHIR servers and ensures stable cross‑system identity</td>
</tr>

<tr>
<td><code>Endpoint.connectionType</code></td>
<td>1..1</td>
<td><code>hl7-fhir-subscription-notify</code><br>(or temporary IG code)</td>
<td>Indicates that the Endpoint is used for receiving FHIR Subscription notifications</td>
</tr>

<tr>
<td><code>Endpoint.name</code></td>
<td>0..1</td>
<td>Human‑readable label</td>
<td>Useful for UI display and administrative clarity</td>
</tr>

<tr>
<td><code>Endpoint.address</code></td>
<td>1..1</td>
<td>URL<br>e.g. <code>https://example.org/fhir-notify</code></td>
<td>Where notifications or other machine‑to‑machine messages are delivered</td>
</tr>

<tr>
<td><code>Endpoint.payload</code> and <code>Endpoint.header</code></td>
<td>0..*</td>
<td>Machine‑readable connection details</td>
<td>May include authentication headers or content‑type declarations; carries security implications</td>
</tr>

<tr>
<td><code>Endpoint.managingOrganization</code></td>
<td>0..1</td>
<td>Reference to <code>Organization</code></td>
<td>Indicates which Organization owns and controls the Endpoint configuration</td>
</tr>

</tbody>
</table>