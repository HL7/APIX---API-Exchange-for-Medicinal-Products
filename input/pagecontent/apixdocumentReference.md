## DocumentReference

In APIX, the **DocumentReference** resource provides the metadata wrapper for regulatory documents submitted as part of a procedure. It links descriptive information (title, category, CTD section, author) with the actual payload stored separately on the FHIR server. E.g. A binary file is uploaded first as a raw `Binary` resource, and the DocumentReference then “claims” that binary by referencing it through `DocumentReference.content.attachment.url`.

The `DocumentReference.author` element identifies the creator of both the metadata and the associated binary content, ensuring clear provenance for regulatory submissions. DocumentReferences are then attached to Tasks via `Task.input` or `Task.output`, allowing the regulator to discover and retrieve documents only when needed.

Note: To keep the server healthy, buisness rules should be determined at what frequency unattached binaries and unused DocumentReferences be expunged. 

---

### Key Elements of the APIX DocumentReference Resource

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
<td><code>DocumentReference.content.attachment.url</code></td>
<td>1..1</td>
<td><code>Binary/123</code></td>
<td>Main link to the raw binary mentioned in the [Architecture](architecture.html#binary-upload-guide-post-then-link) page; the most important element for retrieval of the binary</td>
</tr>

<tr>
<td><code>DocumentReference.category</code></td>
<td>0..*</td>
<td>e.g. Module 3, Quality, Clinical</td>
<td>Used for indexing, grouping, and regulatory classification</td>
</tr>

<tr>
<td><code>DocumentReference.type</code></td>
<td>1..1</td>
<td>e.g. Stability Report, Study Protocol</td>
<td>Describes the document’s regulatory purpose</td>
</tr>

<tr>
<td><code>DocumentReference.author</code></td>
<td>0..*</td>
<td>Reference to <code>Organization</code> or <code>Practitioner</code></td>
<td>Identifies the creator of both the DocumentReference metadata and the associated binary content</td>
</tr>

<tr>
<td><code>DocumentReference.date</code></td>
<td>1..1</td>
<td>Date/time of creation</td>
<td>Useful for audit trails and version tracking</td>
</tr>

<tr>
<td><code>DocumentReference.status</code></td>
<td>1..1</td>
<td><code>current</code></td>
<td>Indicates that the document is active and available for use</td>
</tr>

<tr>
<td><code>DocumentReference.description</code></td>
<td>0..1</td>
<td>Human‑readable title or summary</td>
<td>Improves usability and searchability</td>
</tr>

<tr>
<td><code>DocumentReference.subject</code></td>
<td>0..1</td>
<td>Indicates what is the subject of the document</td>
<td>Used to link to specific products, such as a `MedicinalProductDefinition`</td>
</tr>

<tr>
<td><code>DocumentReference.securityLabel</code></td>
<td>0..1</td>
<td>Field for tagging confidentiality</td>
<td>Used to restrict access</td>
</tr>

</tbody>
</table>
