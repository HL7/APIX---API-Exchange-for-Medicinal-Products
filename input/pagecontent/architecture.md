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

### Architecture Diagram
(INSERT diagram)