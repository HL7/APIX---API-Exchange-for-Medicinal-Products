# Generates the ICSR (scenario2a/2b), clinical trial application (scenario3) and label negotiation (scenario4) examples:
#   input/fsh/workflowExamples/scenario2-icsr.fsh, scenario3-cta.fsh, scenario4-label-negotiation.fsh   (Tasks + DocumentReferences)
#   input/fsh/exampleBinaries/scenario2-icsr-binaries.fsh, scenario3-cta-binaries.fsh, scenario4-label-negotiation-binaries.fsh
#   parking/example-source/*  (readable copies of the sample E2B(R2) ICSR and acklog XML, ICSR validation report, CTA PDFs, and label negotiation ePIs and PDFs)
# Usage (from repo root): python3 parking/gen_examples.py   — needs reportlab (pip install reportlab)
import base64, hashlib, uuid, os, html, io
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors

OUT = os.environ.get('OUT', '.')
NS = uuid.UUID('6f1d1c2e-3a4b-4c5d-8e9f-0a1b2c3d4e5f')
def u(name): return 'urn:uuid:' + str(uuid.uuid5(NS, name))
APIX = 'http://hl7.org/fhir/uv/apix/CodeSystem/'
TC, BS, IO, DEMO = APIX+'apix-task-code', APIX+'apix-business-status', APIX+'apix-task-input-output-type', APIX+'apix-demo'
ORG = {'pharma': ('org-synthpharma-ag', 'SynthPharma AG'), 'ha': ('org-ema-srm-hmed', 'Health Authority – Regulatory Review Division')}

def q(s): return s.replace('\\', '\\\\').replace('"', '\\"')
def x(s): return html.escape(s, quote=True)

# ---------------------------------------------------------------- PDFs
def pdf(title, subtitle, blocks):
    buf = io.BytesIO()
    st = getSampleStyleSheet()
    doc = SimpleDocTemplate(buf, pagesize=A4, leftMargin=20*mm, rightMargin=20*mm, topMargin=18*mm, bottomMargin=18*mm,
                            title=title, author='RWI-pharma example (fictional)', invariant=1)
    flow = [Paragraph('<font color="#b45309">FICTIONAL EXAMPLE — RWI-pharma Implementation Guide</font>', st['Normal']), Spacer(1, 4),
            Paragraph(title, st['Title']), Paragraph(subtitle, st['Italic']), Spacer(1, 8)]
    for b in blocks:
        if isinstance(b, tuple) and b[0] == 'h': flow += [Spacer(1, 6), Paragraph(b[1], st['Heading3'])]
        elif isinstance(b, tuple) and b[0] == 'table':
            t = Table([[Paragraph(f'<b>{k}</b>', st['Normal']), Paragraph(v, st['Normal'])] for k, v in b[1]], colWidths=[55*mm, 115*mm])
            t.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), .5, colors.HexColor('#d1d5db')), ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#f3f4f6')), ('VALIGN', (0, 0), (-1, -1), 'TOP')]))
            flow.append(t)
        else: flow += [Paragraph(b, st['BodyText'])]
    doc.build(flow)
    return buf.getvalue()

# ---------------------------------------------------------------- FSH builders
def narrative(heading, rows, inputs, outputs):
    r = ''.join(f'<tr><th>{x(k)}</th><td>{v}</td></tr>' for k, v in rows)
    def docs(lst): return '<ul>' + ''.join(f'<li><a href="DocumentReference-{d}.html">{x(t)}</a> <code>{c}</code></li>' for c, t, d in lst) + '</ul>' if lst else '<p>None</p>'
    return (f'<div xmlns="http://www.w3.org/1999/xhtml"><p><b>{x(heading)}</b></p><table class="grid">{r}</table>'
            f'<p><b>Inputs (from the requester)</b></p>{docs(inputs)}<p><b>Outputs (from the owner)</b></p>{docs(outputs)}</div>')

def task(t):
    L = [f'Instance: {t["id"]}', 'InstanceOf: Task', f'Title: "{q(t["title"])}"', f'Description: "{q(t["desc"])}"', 'Usage: #example',
         f'* meta.versionId = "{t["ver"]}"', f'* meta.lastUpdated = "{t["modified"]}"', '* meta.profile = "http://hl7.org/fhir/uv/apix/StructureDefinition/apix-task"']
    req, own = ORG[t['requester']], ORG[t['owner']]
    rows = [('Task', f'{x(t["code"][1])} (<code>{t["code"][0]}</code>)'), ('Version', t['ver']), ('Status', t['status']),
            ('Business status', f'{x(t["bs"][1])} (<code>{t["bs"][0]}</code>)' if t.get('bs') else 'Not set'), ('Requester', x(req[1])), ('Owner', x(own[1])),
            ('Group identifier', t['group']), ('Authored', t['authored']), ('Last modified', t['modified'])]
    if t.get('proc'): rows.insert(1, ('Procedure number', x(t['proc'][1])))
    if t.get('reason'): rows.insert(3, ('Status reason', x(t['reason'])))
    if t.get('basedOn'): rows.append(('Based on', f'<a href="Task-{t["basedOn"]}.html">{t["basedOn"]}</a>'))
    if t.get('period'): rows.append(('Response due', t['period'][1]))
    L += ['* text.status = #generated', f'* text.div = "{q(narrative(t["heading"], rows, t.get("inputs", []), t.get("outputs", [])))}"']
    L += ['* identifier[0].use = #official', '* identifier[=].system = "http://example.org/health-authority/task-id"',
          f'* identifier[=].value = "{t["uuid"]}"', f'* identifier[=].type = {DEMO}#apixtaskinstance "APIX Task Instance ID"']
    if t.get('proc'):
        L += ['* identifier[+].use = #official', f'* identifier[=].system = "{t["proc"][0]}"', f'* identifier[=].value = "{t["proc"][1]}"',
              f'* identifier[=].type = {DEMO}#apixregulatorprocedureno "APIX Regulator Procedure Number"']
    L += ['* groupIdentifier.use = #official', '* groupIdentifier.system = "http://example.org/health-authority/work-flow-group-id"', f'* groupIdentifier.value = "{t["group"]}"']
    if t.get('basedOn'): L.append(f'* basedOn = Reference({t["basedOn"]})')
    L += [f'* status = #{t["status"]}'] + ([f'* statusReason.concept.text = "{q(t["reason"])}"'] if t.get('reason') else [])
    L += ([f'* businessStatus = {BS}#{t["bs"][0]} "{q(t["bs"][1])}"'] if t.get('bs') else []) + ['* intent = #proposal', f'* priority = #{t.get("priority","routine")}',
          f'* code = {TC}#{t["code"][0]} "{q(t["code"][1])}"', f'* authoredOn = "{t["authored"]}"', f'* lastModified = "{t["modified"]}"',
          f'* requester = Reference({req[0]}) "{q(req[1])}"', f'* owner = Reference({own[0]}) "{q(own[1])}"']
    if t.get('period'): L += [f'* requestedPeriod.start = "{t["period"][0]}"', f'* requestedPeriod.end = "{t["period"][1]}"']
    if t.get('exec'): L += [f'* executionPeriod.start = "{t["exec"][0]}"'] + ([f'* executionPeriod.end = "{t["exec"][1]}"'] if t['exec'][1] else [])
    for k, (c, title, d) in enumerate(t.get('inputs', [])):
        L += [f'* input[{k}].type = {IO}#{c} "{q(IOD[c])}"', f'* input[{k}].valueReference = Reference({d}) "{q(title)}"']
    for k, (c, title, d) in enumerate(t.get('outputs', [])):
        L += [f'* output[{k}].type = {IO}#{c} "{q(IOD[c])}"', f'* output[{k}].valueReference = Reference({d}) "{q(title)}"']
    return '\n'.join(L) + '\n'

IOD = {'cover-letter': 'Cover Letter', 'application-form': 'Application Form', 'validation-report': 'Validation Report', 'protocol': 'Protocol',
       'request-for-information': 'Request for Information', 'response-to-questions': 'Response to Questions', 'authorisation-decision': 'Authorisation Decision',
       'icsr-e2b-r2': 'ICSR (E2B(R2))', 'icsr-e2b-r3': 'ICSR (E2B(R3))', 'susar-e2b-r2': 'SUSAR (E2B(R2))', 'susar-e2b-r3': 'SUSAR (E2B(R3))',
       'icsr-e2b-r2-acklog': 'ICSR E2B(R2) Acknowledgment Log', 'icsr-e2b-r3-acklog': 'ICSR E2B(R3) Acknowledgment Log',
       'susar-e2b-r2-acklog': 'SUSAR E2B(R2) Acknowledgment Log', 'susar-e2b-r3-acklog': 'SUSAR E2B(R3) Acknowledgment Log',
       'change-description': 'Change Description and Justification', 'epi-bundle': 'ePI Bundle', 'proposed-labelling': 'Proposed Labelling',
       'labelling-comments': 'Labelling Comments', 'approved-labelling': 'Approved Labelling', 'approval-letter': 'Approval Letter'}

def docref(d, content):
    sha1 = base64.b64encode(hashlib.sha1(content).digest()).decode()
    a = ORG[d['author']]
    L = [f'Instance: {d["id"]}', 'InstanceOf: DocumentReference', f'Title: "{q(d["title"])}"', f'Description: "{q(d["desc"])}"', 'Usage: #example',
         '* meta.profile = "http://hl7.org/fhir/uv/apix/StructureDefinition/apix-documentreference"',
         f'* identifier[0].type = {DEMO}#docsetid "Document Set Identifier"', f'* identifier[0].system = "{d.get("setsys", d["sys"])}/document-set-id"', f'* identifier[0].value = "{u(d.get("set", d["id"]+"-set"))}"',
         f'* identifier[1].type = {DEMO}#docverid "Document Version Number Identifier"', f'* identifier[1].system = "{d["sys"]}/document-version-id"', f'* identifier[1].value = "{u(d["id"]+"-v1")}"',
         '* status = #current', '* docStatus = #final', f'* version = "{d.get("ver", "1")}"']
    if d.get('replaces'):
        L += ['* relatesTo[0].code = http://hl7.org/fhir/document-relationship-type#replaces "Replaces"', f'* relatesTo[0].target = Reference({d["replaces"]})']
    L += [f'* type = {IO}#{d["type"]} "{q(IOD[d["type"]])}"',
         f'* date = "{d["date"]}"', f'* author = Reference({a[0]}) "{q(a[1])}"', f'* description = "{q(d["desc"])}"',
         f'* content.attachment.contentType = #{d["mime"]}', f'* content.attachment.url = "Binary/{d["binary"]}"',
         f'* content.attachment.title = "{q(d["file"])}"', f'* content.attachment.size = {len(content)}',
         f'* content.attachment.hash = "{sha1}"', f'* content.attachment.creation = "{d["date"]}"']
    return '\n'.join(L) + '\n'

def binary(bid, mime, content, desc):
    return (f'Instance: {bid}\nInstanceOf: Binary\nDescription: "{q(desc)}"\nUsage: #example\n* contentType = #{mime}\n'
            f'* data = "{base64.b64encode(content).decode()}"\n')

files = {}
# ================================================================ ICSR (scenario2a: accepted; scenario2b: rejected, resubmitted, accepted)
HDR2 = ('<?xml version="1.0" encoding="UTF-8"?>\n<!-- FICTIONAL EXAMPLE for the RWI-pharma IG. Abbreviated ICH E2B(R2) {what}: the structure follows the\n'
        '     ICH {dtd} DTD but only key data elements are shown, and it has not been validated against the DTD.\n'
        '     Data element numbers are given in comments. -->\n')

def icsr_r2(msgnum, msgdate, case, received, initials, age, sex, term, llt, meddra, onset, narrative):
    ver = (f'<reactionmeddraversionllt>{meddra}</reactionmeddraversionllt>                 <!-- B.2.i.1a MedDRA version for reaction -->' if meddra
           else '<!-- B.2.i.1a reactionmeddraversionllt is missing in this message: the error that causes the rejection -->')
    return (HDR2.format(what='ICSR message (one report per message)', dtd='E2B(R2) ICSR (ich-icsr-v2.1)') + f'''<!DOCTYPE ichicsr SYSTEM "ich-icsr-v2.1.dtd">
<ichicsr lang="en">
  <ichicsrmessageheader>
    <messagetype>ichicsr</messagetype>
    <messageformatversion>2.1</messageformatversion>
    <messageformatrelease>2.0</messageformatrelease>
    <messagenumb>{msgnum}</messagenumb>                                       <!-- M.1.4 message number -->
    <messagesenderidentifier>SYNTHPHARMA-AG</messagesenderidentifier>           <!-- M.1.5 -->
    <messagereceiveridentifier>HA-PHARMACOVIGILANCE</messagereceiveridentifier> <!-- M.1.6 -->
    <messagedateformat>204</messagedateformat>
    <messagedate>{msgdate}</messagedate>                                      <!-- M.1.7 message date -->
  </ichicsrmessageheader>
  <safetyreport>
    <safetyreportversion>1</safetyreportversion>
    <safetyreportid>{case}</safetyreportid>                <!-- A.1.0.1 sender's (case) safety report unique identifier -->
    <primarysourcecountry>CH</primarysourcecountry>                             <!-- A.1.1 -->
    <occurcountry>CH</occurcountry>                                             <!-- A.1.2 -->
    <transmissiondateformat>102</transmissiondateformat>
    <transmissiondate>{msgdate[:8]}</transmissiondate>                                   <!-- A.1.3 date of this transmission -->
    <reporttype>1</reporttype>                                                  <!-- A.1.4 type of report: 1 = spontaneous -->
    <serious>2</serious>                                                        <!-- A.1.5.1 serious: 2 = no -->
    <receivedateformat>102</receivedateformat>
    <receivedate>{received}</receivedate>                                           <!-- A.1.6 date report was first received from source -->
    <receiptdateformat>102</receiptdateformat>
    <receiptdate>{received}</receiptdate>                                           <!-- A.1.7 date of receipt of most recent information -->
    <fulfillexpeditecriteria>2</fulfillexpeditecriteria>                        <!-- A.1.9 fulfils expedited criteria: 2 = no -->
    <companynumb>{case}</companynumb>                      <!-- A.1.10.2 company number -->
    <primarysource>
      <qualification>1</qualification>                                          <!-- A.2.1.4 qualification: 1 = physician -->
    </primarysource>
    <sender>
      <sendertype>1</sendertype>                                                <!-- A.3.1.1 sender type: 1 = pharmaceutical company -->
      <senderorganization>SynthPharma AG</senderorganization>                   <!-- A.3.1.2 -->
    </sender>
    <receiver>
      <receivertype>2</receivertype>                                            <!-- A.3.2.1 receiver type: 2 = regulatory authority -->
      <receiverorganization>Health Authority</receiverorganization>             <!-- A.3.2.2 -->
    </receiver>
    <patient>
      <patientinitial>{initials}</patientinitial>                                       <!-- B.1.1 patient initials -->
      <patientonsetage>{age}</patientonsetage>                                      <!-- B.1.2.2a age at onset -->
      <patientonsetageunit>801</patientonsetageunit>                            <!-- B.1.2.2b unit: 801 = year -->
      <patientsex>{sex}</patientsex>                                              <!-- B.1.5 sex: 1 = male, 2 = female -->
      <reaction>
        <primarysourcereaction>{term}</primarysourcereaction>                  <!-- B.2.i.0 reaction as reported -->
        {ver}
        <reactionmeddrallt>{llt}</reactionmeddrallt>                           <!-- B.2.i.1b MedDRA LLT -->
        <reactionstartdateformat>102</reactionstartdateformat>
        <reactionstartdate>{onset}</reactionstartdate>                         <!-- B.2.i.4 start date -->
        <reactionoutcome>3</reactionoutcome>                                    <!-- B.2.i.8 outcome: 3 = not recovered/not resolved -->
      </reaction>
      <drug>
        <drugcharacterization>1</drugcharacterization>                          <!-- B.4.k.1 characterisation: 1 = suspect -->
        <medicinalproduct>WonderDrug 50 mg tablets</medicinalproduct>           <!-- B.4.k.2.1 proprietary medicinal product name -->
        <drugstructuredosagenumb>50</drugstructuredosagenumb>                   <!-- B.4.k.5.1 dose -->
        <drugstructuredosageunit>003</drugstructuredosageunit>                  <!-- B.4.k.5.2 unit: 003 = mg -->
        <drugstartdateformat>102</drugstartdateformat>
        <drugstartdate>20260920</drugstartdate>                                 <!-- B.4.k.12 start date -->
        <actiondrug>4</actiondrug>                                              <!-- B.4.k.16 action taken: 4 = dose not changed -->
      </drug>
      <summary>
        <narrativeincludeclinical>{narrative}</narrativeincludeclinical>  <!-- B.5.1 case narrative -->
      </summary>
    </patient>
  </safetyreport>
</ichicsr>
''').encode()

def ack_r2(acknum, ackdate, msgnum, msgdate, case, loaded, localrep=None, err=None):
    code = '01' if loaded else '02'
    extra = (f'\n      <localreportnumb>{localrep}</localreportnumb>                    <!-- receiver\'s local report number -->' if localrep else '')
    errel = (f'\n      <errormessagecomment>{x(err)}</errormessagecomment>' if err else '')
    return (HDR2.format(what='acknowledgment message (acklog)', dtd='E2B(R2) / M2 ICSR acknowledgment (ich-icsrack-v1.1)') + f'''<!DOCTYPE ichicsrack SYSTEM "ich-icsrack-v1.1.dtd">
<ichicsrack lang="en">
  <ichicsrmessageheader>
    <messagetype>ichicsrack</messagetype>
    <messageformatversion>1.1</messageformatversion>
    <messageformatrelease>1.0</messageformatrelease>
    <messagenumb>{acknum}</messagenumb>
    <messagesenderidentifier>HA-PHARMACOVIGILANCE</messagesenderidentifier>
    <messagereceiveridentifier>SYNTHPHARMA-AG</messagereceiveridentifier>
    <messagedateformat>204</messagedateformat>
    <messagedate>{ackdate}</messagedate>
  </ichicsrmessageheader>
  <acknowledgment>
    <messageacknowledgment>
      <icsrmessagenumb>{msgnum}</icsrmessagenumb>                          <!-- the ICSR message being acknowledged -->
      <icsrmessagesenderidentifier>SYNTHPHARMA-AG</icsrmessagesenderidentifier>
      <icsrmessagereceiveridentifier>HA-PHARMACOVIGILANCE</icsrmessagereceiveridentifier>
      <icsrmessagedateformat>204</icsrmessagedateformat>
      <icsrmessagedate>{msgdate}</icsrmessagedate>
      <transmissionacknowledgmentcode>{code}</transmissionacknowledgmentcode>  <!-- 01 = all reports loaded; 02 = not all reports loaded; 03 = message not parsed -->
    </messageacknowledgment>
    <reportacknowledgment>
      <safetyreportid>{case}</safetyreportid>
      <safetyreportversion>1</safetyreportversion>{extra}
      <companynumb>{case}</companynumb>
      <receiptdateformat>102</receiptdateformat>
      <receiptdate>{ackdate[:8]}</receiptdate>
      <reportacknowledgmentcode>{code}</reportacknowledgmentcode>             <!-- 01 = report loaded; 02 = report not loaded -->{errel}
    </reportacknowledgment>
  </acknowledgment>
</ichicsrack>
''').encode()

# --- 2a: nausea case, accepted first time
C2A, C2B = 'CH-SYNTHPHARMA-2026-000456', 'CH-SYNTHPHARMA-2026-000512'
files['icsr-2a-e2b-r2.xml'] = icsr_r2('SYNTH-MSG-2026-000456-1', '20261002093000', C2A, '20260928', 'JD', 54, 2, 'feeling sick', '10028813', '29.0', '20260926',
    '54-year-old female patient started WonderDrug 50 mg tablets once daily on 20-Sep-2026. On 26-Sep-2026 she developed nausea. The reporting physician considered the event non-serious and possibly related.')
files['icsr-2a-e2b-r2-acklog.xml'] = ack_r2('HA-ACK-2026-778001', '20261002094512', 'SYNTH-MSG-2026-000456-1', '20261002093000', C2A, True, 'HA-ICSR-2026-104233')
# --- 2b: dizziness case, rejected (MedDRA version missing), corrected and resubmitted
ERR = 'B.2.i.1a reactionmeddraversionllt is mandatory when B.2.i.1b reactionmeddrallt is given (rule R2-0214). Report not loaded.'
NARR_B = '61-year-old male patient started WonderDrug 50 mg tablets once daily on 20-Sep-2026. On 08-Oct-2026 he reported dizziness on standing. The reporting physician considered the event non-serious and possibly related.'
files['icsr-2b-e2b-r2.xml'] = icsr_r2('SYNTH-MSG-2026-000512-1', '20261014110000', C2B, '20261009', 'MK', 61, 1, 'dizzy when standing up', '10013573', None, '20261008', NARR_B)
files['icsr-2b-e2b-r2-acklog.xml'] = ack_r2('HA-ACK-2026-781455', '20261014111230', 'SYNTH-MSG-2026-000512-1', '20261014110000', C2B, False, err=ERR)
files['icsr-2b-validation-report.pdf'] = pdf('Validation Report — ICSR', f'Case {C2B} · 14 October 2026', [
 'The ICSR message below failed validation. The report was not loaded into the safety database.',
 ('table', [('Message number', 'SYNTH-MSG-2026-000512-1'), ('Safety report ID', C2B), ('Format', 'ICH E2B(R2)'), ('Outcome', 'Rejected — report not loaded (acknowledgment code 02)')]),
 ('h', 'Errors'),
 ('table', [('R2-0214 (error)', 'B.2.i.1a <i>reactionmeddraversionllt</i> is missing. The MedDRA version is mandatory when a MedDRA code is given in B.2.i.1b (here LLT 10013573, Dizziness).')]),
 ('h', 'Action required'),
 'Add the MedDRA version to the reaction and resubmit the report. Because this report was not loaded, resubmit it as safety report version 1 with a new message number.'])
files['icsr-2b-resubmission-e2b-r2.xml'] = icsr_r2('SYNTH-MSG-2026-000512-2', '20261014154000', C2B, '20261009', 'MK', 61, 1, 'dizzy when standing up', '10013573', '29.0', '20261008', NARR_B)
files['icsr-2b-resubmission-e2b-r2-acklog.xml'] = ack_r2('HA-ACK-2026-781602', '20261014155208', 'SYNTH-MSG-2026-000512-2', '20261014154000', C2B, True, 'HA-ICSR-2026-104871')

PH, HAs = 'http://example.org/synthpharma', 'http://example.org/health-authority'
def icsr_doc(id_, title, desc, type_, file, date, author):
    return dict(id=id_, title=title, desc=desc, type=type_, mime='application/pdf' if file.endswith('.pdf') else 'application/xml',
                binary='binary-' + file.rsplit('.', 1)[0], file=file, date=date, author=author, sys=PH if author == 'pharma' else HAs)
icsr_docs = [
 icsr_doc('docref-icsr-2a', f'ICSR — case {C2A}', f'ICH E2B(R2) ICSR for case {C2A} (nausea with WonderDrug 50 mg).', 'icsr-e2b-r2', 'icsr-2a-e2b-r2.xml', '2026-10-02T09:30:00+02:00', 'pharma'),
 icsr_doc('docref-icsr-2a-acklog', 'ICSR acknowledgment log', 'ICH E2B(R2) acknowledgment: transmission 01 (all reports loaded), report 01 (report loaded).', 'icsr-e2b-r2-acklog', 'icsr-2a-e2b-r2-acklog.xml', '2026-10-02T09:45:12+02:00', 'ha'),
 icsr_doc('docref-icsr-2b', f'ICSR — case {C2B}', f'ICH E2B(R2) ICSR for case {C2B} (dizziness with WonderDrug 50 mg). The MedDRA version is missing.', 'icsr-e2b-r2', 'icsr-2b-e2b-r2.xml', '2026-10-14T11:00:00+02:00', 'pharma'),
 icsr_doc('docref-icsr-2b-acklog', 'ICSR acknowledgment log (rejected)', 'ICH E2B(R2) acknowledgment: transmission 02 (not all reports loaded), report 02 (report not loaded), with the error.', 'icsr-e2b-r2-acklog', 'icsr-2b-e2b-r2-acklog.xml', '2026-10-14T11:12:30+02:00', 'ha'),
 icsr_doc('docref-icsr-2b-validation-report', 'ICSR validation report', 'Validation report listing the error that caused the rejection.', 'validation-report', 'icsr-2b-validation-report.pdf', '2026-10-14T11:12:30+02:00', 'ha'),
 icsr_doc('docref-icsr-2b-resubmission', f'ICSR resubmission — case {C2B}', f'Corrected ICH E2B(R2) ICSR for case {C2B}, with the MedDRA version added.', 'icsr-e2b-r2', 'icsr-2b-resubmission-e2b-r2.xml', '2026-10-14T15:40:00+02:00', 'pharma'),
 icsr_doc('docref-icsr-2b-resubmission-acklog', 'ICSR acknowledgment log (resubmission)', 'ICH E2B(R2) acknowledgment: transmission 01 (all reports loaded), report 01 (report loaded).', 'icsr-e2b-r2-acklog', 'icsr-2b-resubmission-e2b-r2-acklog.xml', '2026-10-14T15:52:08+02:00', 'ha'),
]
ICSR = ('icsr', 'Individual Case Safety Report')
ACC, CMP, REJ = ('accepted', 'Accepted'), ('complete', 'Complete'), ('rejected', 'Rejected')
IA, AA = ('icsr-e2b-r2', f'ICSR — case {C2A}', 'docref-icsr-2a'), ('icsr-e2b-r2-acklog', 'ICSR acknowledgment log', 'docref-icsr-2a-acklog')
IB, AB, VB = ('icsr-e2b-r2', f'ICSR — case {C2B}', 'docref-icsr-2b'), ('icsr-e2b-r2-acklog', 'ICSR acknowledgment log (rejected)', 'docref-icsr-2b-acklog'), ('validation-report', 'ICSR validation report', 'docref-icsr-2b-validation-report')
IR, AR = ('icsr-e2b-r2', f'ICSR resubmission — case {C2B}', 'docref-icsr-2b-resubmission'), ('icsr-e2b-r2-acklog', 'ICSR acknowledgment log (resubmission)', 'docref-icsr-2b-resubmission-acklog')
G2A, G2B = u('scenario2a-icsr-group'), u('scenario2b-icsr-group')
P = dict(code=ICSR, requester='pharma', owner='ha')
icsr_a_tasks = [
 dict(P, id='scenario2a-01-icsr-submitted', title='scenario2a 01 ICSR submitted', desc='The marketing authorization holder posts an ICSR Task; the E2B(R2) message is the input.',
      heading='ICSR submitted', ver='1', uuid=u('s2a-task'), group=G2A, status='requested', bs=('submitted', 'Submitted'), authored='2026-10-02T09:30:00+02:00', modified='2026-10-02T09:30:00+02:00', inputs=[IA]),
 dict(P, id='scenario2a-02-icsr-accepted', title='scenario2a 02 ICSR accepted', desc='Version 2 of the ICSR Task (in production, the same Task as scenario2a-01). The report passed validation and was loaded; the regulator returns the E2B(R2) acknowledgment log.',
      heading='ICSR accepted', ver='2', uuid=u('s2a-task'), group=G2A, status='accepted', bs=ACC, authored='2026-10-02T09:30:00+02:00', modified='2026-10-02T09:45:12+02:00',
      inputs=[IA], outputs=[AA], exec=('2026-10-02T09:30:05+02:00', None)),
 dict(P, id='scenario2a-03-icsr-complete', title='scenario2a 03 ICSR complete', desc='Version 3 of the ICSR Task (in production, the same Task as scenario2a-01). Processing is complete and the Task is closed.',
      heading='ICSR complete', ver='3', uuid=u('s2a-task'), group=G2A, status='completed', bs=CMP, authored='2026-10-02T09:30:00+02:00', modified='2026-10-02T10:02:40+02:00',
      inputs=[IA], outputs=[AA], exec=('2026-10-02T09:30:05+02:00', '2026-10-02T10:02:40+02:00')),
]
REASON = 'The ICSR failed validation (rule R2-0214: MedDRA version missing in B.2.i.1a) and was not loaded. See the acknowledgment log and validation report.'
icsr_b_tasks = [
 dict(P, id='scenario2b-01-icsr-submitted', title='scenario2b 01 ICSR submitted', desc='The marketing authorization holder posts an ICSR Task; the E2B(R2) message is the input. The message has an error.',
      heading='ICSR submitted', ver='1', uuid=u('s2b-task-1'), group=G2B, status='requested', bs=('submitted', 'Submitted'), authored='2026-10-14T11:00:00+02:00', modified='2026-10-14T11:00:00+02:00', inputs=[IB]),
 dict(P, id='scenario2b-02-icsr-rejected', title='scenario2b 02 ICSR rejected', desc='Version 2 of the ICSR Task (in production, the same Task as scenario2b-01). The report failed validation; the regulator rejects the Task and returns the acknowledgment log and a validation report.',
      heading='ICSR rejected', ver='2', uuid=u('s2b-task-1'), group=G2B, status='rejected', reason=REASON, bs=REJ, authored='2026-10-14T11:00:00+02:00', modified='2026-10-14T11:12:30+02:00',
      inputs=[IB], outputs=[AB, VB], exec=('2026-10-14T11:00:04+02:00', '2026-10-14T11:12:30+02:00')),
 dict(P, id='scenario2b-03-icsr-resubmitted', title='scenario2b 03 ICSR resubmitted', desc='The marketing authorization holder posts a new ICSR Task with the corrected E2B(R2) message. It has the same group identifier and is basedOn the rejected Task.',
      heading='ICSR resubmitted', ver='1', uuid=u('s2b-task-2'), group=G2B, status='requested', bs=('submitted', 'Submitted'), authored='2026-10-14T15:40:00+02:00', modified='2026-10-14T15:40:00+02:00', inputs=[IR], basedOn='scenario2b-01-icsr-submitted'),
 dict(P, id='scenario2b-04-icsr-accepted', title='scenario2b 04 ICSR resubmission accepted', desc='Version 2 of the resubmission Task (in production, the same Task as scenario2b-03). The corrected report passed validation and was loaded; the regulator returns the acknowledgment log.',
      heading='ICSR resubmission accepted', ver='2', uuid=u('s2b-task-2'), group=G2B, status='accepted', bs=ACC, authored='2026-10-14T15:40:00+02:00', modified='2026-10-14T15:52:08+02:00',
      inputs=[IR], outputs=[AR], basedOn='scenario2b-01-icsr-submitted', exec=('2026-10-14T15:40:03+02:00', None)),
 dict(P, id='scenario2b-05-icsr-complete', title='scenario2b 05 ICSR resubmission complete', desc='Version 3 of the resubmission Task (in production, the same Task as scenario2b-03). Processing is complete and the Task is closed.',
      heading='ICSR resubmission complete', ver='3', uuid=u('s2b-task-2'), group=G2B, status='completed', bs=CMP, authored='2026-10-14T15:40:00+02:00', modified='2026-10-14T16:10:21+02:00',
      inputs=[IR], outputs=[AR], basedOn='scenario2b-01-icsr-submitted', exec=('2026-10-14T15:40:03+02:00', '2026-10-14T16:10:21+02:00')),
]

# ================================================================ CTA (scenario3)
TRIAL = 'CT-2026-000789'
TT = 'A Phase 2, randomised, double-blind, placebo-controlled study of WonderDrug 50 mg tablets in adults with chronic migraine (WD-201)'
files['cta-cover-letter.pdf'] = pdf('Cover Letter — Clinical Trial Application', 'SynthPharma AG · 01 September 2026', [
 'To: Health Authority – Regulatory Review Division', f'Re: Initial clinical trial application for study WD-201 — {x(TT)}',
 'Dear Sir or Madam,', 'SynthPharma AG submits an initial clinical trial application for study WD-201. The application contains the application form and the clinical trial protocol (version 1.0). The investigator\'s brochure and investigational medicinal product dossier are available on request in this example.',
 'We request authorisation to conduct the trial at 12 sites, with first participant planned for January 2027.', 'Yours faithfully,', 'Dr. John Doe, Head of Regulatory Affairs, SynthPharma AG'])
files['cta-application-form.pdf'] = pdf('Clinical Trial Application Form', 'Initial application · sample content', [
 ('h', 'A. Trial identification'), ('table', [('Sponsor protocol code', 'WD-201'), ('Full title', x(TT)), ('Phase', 'Phase 2'), ('Trial category', 'Therapeutic exploratory')]),
 ('h', 'B. Sponsor'), ('table', [('Sponsor', 'SynthPharma AG, 123 Synthetic Research Blvd, 4000 Basel, Switzerland'), ('Contact', 'Dr. John Doe — john.doe@synthpharma.example')]),
 ('h', 'C. Investigational medicinal product'), ('table', [('Product', 'WonderDrug 50 mg film-coated tablets'), ('Comparator', 'Matching placebo'), ('Route / dose', 'Oral, 50 mg once daily for 12 weeks')]),
 ('h', 'D. Population and sites'), ('table', [('Condition', 'Chronic migraine (adults 18–65 years)'), ('Planned participants', '240 (1:1 randomisation)'), ('Planned sites', '12'), ('Planned start', 'January 2027')])])
files['cta-protocol.pdf'] = pdf('Clinical Trial Protocol WD-201 (Synopsis)', 'Version 1.0 · 15 August 2026', [
 ('table', [('Title', x(TT)), ('Objectives', 'Primary: change from baseline in monthly migraine days at week 12. Secondary: responder rate (at least 50% reduction), safety and tolerability.'),
            ('Design', 'Randomised, double-blind, placebo-controlled, parallel-group'), ('Population', 'Adults 18–65 with chronic migraine for at least 12 months'),
            ('Treatment', 'WonderDrug 50 mg or placebo, orally once daily for 12 weeks'), ('Safety monitoring', 'Adverse events at every visit; liver function tests at screening, week 4, week 8 and week 12'),
            ('Sample size', '240 participants (120 per arm), 90% power to detect a 2-day difference'), ('Duration', '12-week treatment plus 4-week follow-up')])])
files['cta-validation-report.pdf'] = pdf('Validation Report', f'Trial {TRIAL} · 12 September 2026', [
 'The application for study WD-201 has been validated.', ('table', [('Outcome', 'Validation successful — application complete'), ('Trial number assigned', TRIAL), ('Assessment start', '15 September 2026')])])
files['cta-request-for-information.pdf'] = pdf('Request for Information', f'Trial {TRIAL} · 01 October 2026', [
 'During assessment of the application, the following questions were raised. Please respond by 15 October 2026. The assessment clock is stopped until a response is received.',
 '<b>Q1.</b> Justify the selection of the 50 mg dose, with reference to the Phase 1 exposure data.', '<b>Q2.</b> Clarify the stopping rules for elevated liver enzymes.',
 '<b>Q3.</b> Provide stability data supporting the proposed 24-month shelf life of the investigational product.'])
files['cta-response-to-questions.pdf'] = pdf('Response to Request for Information', f'Trial {TRIAL} · SynthPharma AG · 12 October 2026', [
 '<b>R1.</b> The 50 mg dose gives exposure within the range that was well tolerated in Phase 1 (study WD-101) and is predicted to achieve target receptor occupancy.',
 '<b>R2.</b> Treatment will be stopped if ALT or AST exceeds 3 times the upper limit of normal; the protocol has been amended accordingly (version 1.1).',
 '<b>R3.</b> 18-month real-time and 6-month accelerated stability data are provided and support the proposed 24-month shelf life.'])
files['cta-authorisation-decision.pdf'] = pdf('Authorisation Decision', f'Trial {TRIAL} · 03 November 2026', [
 f'The Health Authority authorises the conduct of clinical trial {TRIAL} (WD-201), sponsored by SynthPharma AG, as described in protocol version 1.1.',
 ('table', [('Decision', 'Authorised'), ('Conditions', 'None'), ('Date of decision', '03 November 2026')])])

G3 = u('scenario3-cta-group')
PROC = ('http://example.org/health-authority/clinical-trial-number', TRIAL)
cta_docs = [
 dict(id='docref-cta-cover-letter', title='CTA cover letter', desc='Cover letter for the initial clinical trial application for study WD-201.', type='cover-letter', file='cta-cover-letter.pdf', date='2026-09-01T10:00:00+02:00', author='pharma'),
 dict(id='docref-cta-application-form', title='CTA application form', desc='Completed clinical trial application form for study WD-201.', type='application-form', file='cta-application-form.pdf', date='2026-09-01T10:00:00+02:00', author='pharma'),
 dict(id='docref-cta-protocol', title='Protocol WD-201 v1.0', desc='Clinical trial protocol WD-201, version 1.0 (synopsis).', type='protocol', file='cta-protocol.pdf', date='2026-09-01T10:00:00+02:00', author='pharma'),
 dict(id='docref-cta-validation-report', title='CTA validation report', desc='Validation report: application complete; trial number assigned.', type='validation-report', file='cta-validation-report.pdf', date='2026-09-12T15:00:00+02:00', author='ha'),
 dict(id='docref-cta-rfi', title='Request for information', desc='Request for information raised during assessment (three questions).', type='request-for-information', file='cta-request-for-information.pdf', date='2026-10-01T11:00:00+02:00', author='ha'),
 dict(id='docref-cta-rfi-response', title='Response to request for information', desc='Sponsor response to the three questions.', type='response-to-questions', file='cta-response-to-questions.pdf', date='2026-10-12T16:00:00+02:00', author='pharma'),
 dict(id='docref-cta-decision', title='Authorisation decision', desc='Decision authorising clinical trial CT-2026-000789.', type='authorisation-decision', file='cta-authorisation-decision.pdf', date='2026-11-03T09:00:00+01:00', author='ha'),
]
for d in cta_docs:
    d.update(mime='application/pdf', binary='binary-' + d['id'][len('docref-'):], sys=PH if d['author'] == 'pharma' else HAs)
CI = [('cover-letter', 'CTA cover letter', 'docref-cta-cover-letter'), ('application-form', 'CTA application form', 'docref-cta-application-form'), ('protocol', 'Protocol WD-201 v1.0', 'docref-cta-protocol')]
VR = ('validation-report', 'CTA validation report', 'docref-cta-validation-report')
DEC = ('authorisation-decision', 'Authorisation decision', 'docref-cta-decision')
RFI = ('request-for-information', 'Request for information', 'docref-cta-rfi')
RSP = ('response-to-questions', 'Response to request for information', 'docref-cta-rfi-response')
P = 'scenario3-01-cta-submission'
cta_tasks = [
 dict(id=P, title='scenario3 01 clinical trial application submitted', desc='The sponsor posts the clinical trial application Task with the cover letter, application form and protocol as inputs.',
      heading='Clinical trial application submitted', ver='1', uuid=u('s3-task-cta'), group=G3, status='requested', bs=('submitted', 'Submitted'), code=('clinical-trial-application', 'Clinical Trial Application'),
      authored='2026-09-01T10:00:00+02:00', modified='2026-09-01T10:00:00+02:00', requester='pharma', owner='ha', inputs=CI),
 dict(id='scenario3-02-cta-validated', title='scenario3 02 clinical trial application validated', desc='Version 2 of the application Task (in production, the same Task as scenario3-01). The regulator accepts it, assigns the trial number and returns the validation report.',
      heading='Clinical trial application validated', ver='2', uuid=u('s3-task-cta'), proc=PROC, group=G3, status='accepted', bs=('validation-successful', 'Validation Successful'), code=('clinical-trial-application', 'Clinical Trial Application'),
      authored='2026-09-01T10:00:00+02:00', modified='2026-09-12T15:00:00+02:00', requester='pharma', owner='ha', inputs=CI, outputs=[VR], exec=('2026-09-02T08:00:00+02:00', None)),
 dict(id='scenario3-03-cta-rfi', title='scenario3 03 request for information issued', desc='The regulator posts a request-for-information Task, based on the application Task. The regulator is the requester here, so the questions are the input and the sponsor owns the response.',
      heading='Request for information issued', ver='1', uuid=u('s3-task-rfi'), proc=PROC, group=G3, status='requested', bs=('request-for-information-issued', 'Request for Information Issued'), code=('information-request', 'List of Questions / Information Request'),
      authored='2026-10-01T11:00:00+02:00', modified='2026-10-01T11:00:00+02:00', requester='ha', owner='pharma', inputs=[RFI], basedOn=P, period=('2026-10-01T11:00:00+02:00', '2026-10-15T23:59:59+02:00')),
 dict(id='scenario3-04-cta-rfi-response', title='scenario3 04 request for information answered', desc='Version 2 of the request-for-information Task (in production, the same Task as scenario3-03). The sponsor completes it with the response as the output; the clock restarts.',
      heading='Request for information answered', ver='2', uuid=u('s3-task-rfi'), proc=PROC, group=G3, status='completed', bs=('clock-restart', 'Clock Restart'), code=('information-request', 'List of Questions / Information Request'),
      authored='2026-10-01T11:00:00+02:00', modified='2026-10-12T16:00:00+02:00', requester='ha', owner='pharma', inputs=[RFI], outputs=[RSP], basedOn=P, period=('2026-10-01T11:00:00+02:00', '2026-10-15T23:59:59+02:00'), exec=('2026-10-01T11:05:00+02:00', '2026-10-12T16:00:00+02:00')),
 dict(id='scenario3-05-cta-authorised', title='scenario3 05 clinical trial authorised', desc='Version 3 of the application Task (in production, the same Task as scenario3-01). The regulator completes it and returns the authorisation decision.',
      heading='Clinical trial authorised', ver='3', uuid=u('s3-task-cta'), proc=PROC, group=G3, status='completed', bs=('authorised', 'Authorised'), code=('clinical-trial-application', 'Clinical Trial Application'),
      authored='2026-09-01T10:00:00+02:00', modified='2026-11-03T09:00:00+01:00', requester='pharma', owner='ha', inputs=CI, outputs=[VR, DEC], exec=('2026-09-02T08:00:00+02:00', '2026-11-03T09:00:00+01:00')),
]

# ================================================================ Label negotiation (scenario4)
# A Type II variation adds nausea to the WonderDrug 50 mg product information. The label is exchanged as FHIR ePI Bundles:
# an ANNOTATED ePI shows every change against the approved text with XHTML <ins>/<del> (class = who made the change,
# title = why), and a CLEAN ePI has the same structure without markup. Two rounds of labelling comments, then agreement.
PROD = 'WonderDrug 50 mg film-coated tablets'
SECT = 'http://example.org/epi-section'   # placeholder section code system (fictional)
def ins(who, why, t): return f'<ins class="rwi-{who}" title="{x(why)}">{x(t)}</ins>'
def dele(who, why, t): return f'<del class="rwi-{who}" title="{x(why)}">{x(t)}</del>'
APPROVED = {  # currently approved text (before this variation)
 'smpc-4.2': 'The recommended dose is one 50 mg tablet once daily. The tablet can be taken with or without food.',
 'smpc-4.8': 'Gastrointestinal disorders. Common: abdominal pain. Uncommon: dyspepsia.',
 'pil-3': 'Take one tablet once a day. You can take it with or without food.',
 'pil-4': 'Common (may affect up to 1 in 10 people): stomach pain. Uncommon (may affect up to 1 in 100 people): indigestion.'}
WHY1 = 'Applicant: add nausea following the signal evaluation'
WHYF = 'HA round 1: clinical data support the frequency "common"'
WHYFOOD = 'HA round 1: advise intake with food to reduce nausea'
WHYC = 'Applicant counter-proposal: food-effect study WD-105 shows no loss of exposure when taken fasted'
WHYLAY = 'HA round 2: plain-language wording for patients'
S42 = 'The recommended dose is one 50 mg tablet once daily. '
S48C, S48U = 'Gastrointestinal disorders. Common: abdominal pain', '. Uncommon: dyspepsia'
P3 = 'Take one tablet once a day. '
P4C, P4U = 'Common (may affect up to 1 in 10 people): stomach pain', '. Uncommon (may affect up to 1 in 100 people): indigestion'
# EPI[version][section] = (annotated XHTML or None, clean text or None). Annotations are cumulative against the approved text.
EPI = {
 1: {'smpc-4.2': (x(APPROVED['smpc-4.2']), APPROVED['smpc-4.2']),
     'smpc-4.8': (x(S48C + S48U) + ins('mah', WHY1, ', nausea') + '.', S48C + S48U + ', nausea.'),
     'pil-3': (x(APPROVED['pil-3']), APPROVED['pil-3']),
     'pil-4': (x(P4C + P4U) + ins('mah', WHY1, ', nausea') + '.', P4C + P4U + ', nausea.')},
 2: {'smpc-4.2': (x(S42) + dele('ha', WHYFOOD, 'The tablet can be taken with or without food.') + ins('ha', WHYFOOD, 'WonderDrug should be taken with food.'), None),
     'smpc-4.8': (x(S48C) + ins('ha', WHYF, ', nausea') + x(S48U) + '.', None),
     'pil-3': (x(P3) + dele('ha', WHYFOOD, 'You can take it with or without food.') + ins('ha', WHYFOOD, 'Take WonderDrug with food.'), None),
     'pil-4': (x(P4C) + ins('ha', WHYF, ', nausea') + x(P4U) + '.', None)},
 3: {'smpc-4.2': (x(S42) + dele('ha', WHYFOOD, 'The tablet can be taken with or without food.') + ins('mah', WHYC, 'WonderDrug may be taken with food to reduce nausea.'), S42 + 'WonderDrug may be taken with food to reduce nausea.'),
     'smpc-4.8': (x(S48C) + ins('ha', WHYF, ', nausea') + x(S48U) + '.', S48C + ', nausea' + S48U + '.'),
     'pil-3': (x(P3) + dele('ha', WHYFOOD, 'You can take it with or without food.') + ins('mah', WHYC, 'Taking WonderDrug with food may help to reduce nausea.'), P3 + 'Taking WonderDrug with food may help to reduce nausea.'),
     'pil-4': (x(P4C) + ins('ha', WHYF, ', nausea') + x(P4U) + '.', P4C + ', nausea' + P4U + '.')},
 4: {'smpc-4.2': (x(S42) + dele('ha', WHYFOOD, 'The tablet can be taken with or without food.') + ins('mah', WHYC, 'WonderDrug may be taken with food to reduce nausea.'), None),
     'smpc-4.8': (x(S48C) + ins('ha', WHYF, ', nausea') + x(S48U) + '.', None),
     'pil-3': (x(P3) + dele('ha', WHYFOOD, 'You can take it with or without food.') + ins('ha', WHYLAY, 'Taking WonderDrug with food may help you feel less sick.'), None),
     'pil-4': (x(P4C) + ins('ha', WHYLAY, ', feeling sick (nausea)') + x(P4U) + '.', None)},
}
EPI[5] = {'smpc-4.2': (None, EPI[3]['smpc-4.2'][1]), 'smpc-4.8': (None, EPI[3]['smpc-4.8'][1]),
          'pil-3': (None, P3 + 'Taking WonderDrug with food may help you feel less sick.'),
          'pil-4': (None, P4C + ', feeling sick (nausea)' + P4U + '.')}
SECTIONS = [('smpc', 'Summary of Product Characteristics', [('smpc-4.2', '4.2 Posology and method of administration'), ('smpc-4.8', '4.8 Undesirable effects')]),
            ('pil', 'Package Leaflet', [('pil-3', '3. How to take WonderDrug'), ('pil-4', '4. Possible side effects')])]

def epi_xml(ver, annotated, who, date):
    org = ORG[who][1]
    kind = 'annotated' if annotated else 'clean'
    def sec(code, title, div, p):
        return (f'{p}<section>\n{p}  <title value="{x(title)}"/>\n{p}  <code><coding><system value="{SECT}"/><code value="{code}"/><display value="{x(title)}"/></coding></code>\n'
                f'{p}  <text><status value="additional"/><div xmlns="http://www.w3.org/1999/xhtml"><p>{div}</p></div></text>\n{p}</section>\n')
    body = ''
    for code, title, subs in SECTIONS:
        inner = ''.join(sec(c, t, EPI[ver][c][0] if annotated else x(EPI[ver][c][1]), ' ' * 10) for c, t in subs)
        body += (f'        <section>\n          <title value="{x(title)}"/>\n          <code><coding><system value="{SECT}"/><code value="{code}"/><display value="{x(title)}"/></coding></code>\n'
                 f'{inner}        </section>\n')
    legend = ('\n<!-- Annotated ePI: changes against the currently approved text are marked with XHTML <ins>/<del> in each section narrative.\n'
              '     class="rwi-mah" = change made by the marketing authorisation holder; class="rwi-ha" = change made by the health authority;\n'
              '     title = reason for the change. The clean ePI of the same version has the same structure without markup. -->') if annotated else ''
    return (f'''<?xml version="1.0" encoding="UTF-8"?>
<!-- FICTIONAL EXAMPLE for the RWI-pharma IG. Abbreviated FHIR ePI document Bundle (product information for {PROD}),
     showing only the sections changed by this variation. Section and document type codes use a placeholder code system. -->{legend}
<Bundle xmlns="http://hl7.org/fhir">
  <identifier><system value="http://example.org/synthpharma/epi"/><value value="{u('s4-epi-' + kind + '-v' + str(ver))}"/></identifier>
  <type value="document"/>
  <timestamp value="{date}"/>
  <entry>
    <fullUrl value="{u('s4-epi-composition-' + kind + '-v' + str(ver))}"/>
    <resource>
      <Composition>
        <status value="{'final' if ver == 5 else 'preliminary'}"/>
        <type><coding><system value="{SECT}"/><code value="product-information"/><display value="Product information (SmPC and package leaflet)"/></coding></type>
        <date value="{date}"/>
        <author><reference value="{u('s4-epi-org-' + who)}"/><display value="{x(org)}"/></author>
        <title value="{x(PROD)} — product information, version {ver} ({kind})"/>
{body}      </Composition>
    </resource>
  </entry>
  <entry>
    <fullUrl value="{u('s4-epi-org-' + who)}"/>
    <resource>
      <Organization><name value="{x(org)}"/></Organization>
    </resource>
  </entry>
</Bundle>
''').encode()

PROCNO = 'VAR-II-2027-0012'
D = {'sub': '2027-01-11T10:00:00+01:00', 'val': '2027-01-15T14:00:00+01:00', 'ass': '2027-01-18T09:00:00+01:00',
     'r1': '2027-02-22T10:00:00+01:00', 'r1due': '2027-03-04T23:59:59+01:00', 'r1resp': '2027-03-01T16:30:00+01:00',
     'r2': '2027-03-08T10:00:00+01:00', 'r2due': '2027-03-18T23:59:59+01:00', 'r2resp': '2027-03-10T11:15:00+01:00',
     'agr': '2027-03-11T09:00:00+01:00', 'agrresp': '2027-03-11T15:40:00+01:00', 'dec': '2027-03-17T09:00:00+01:00'}
files['epi-annotated-v1.xml'] = epi_xml(1, True, 'pharma', D['sub'])
files['epi-clean-v1.xml'] = epi_xml(1, False, 'pharma', D['sub'])
files['epi-annotated-v2.xml'] = epi_xml(2, True, 'ha', D['r1'])
files['epi-annotated-v3.xml'] = epi_xml(3, True, 'pharma', D['r1resp'])
files['epi-clean-v3.xml'] = epi_xml(3, False, 'pharma', D['r1resp'])
files['epi-annotated-v4.xml'] = epi_xml(4, True, 'ha', D['r2'])
files['epi-clean-v5.xml'] = epi_xml(5, False, 'pharma', D['r2resp'])
files['var-cover-letter.pdf'] = pdf('Cover Letter — Type II Variation', 'SynthPharma AG · 11 January 2027', [
 'To: Health Authority – Regulatory Review Division', f'Re: Type II variation for {PROD} — addition of nausea to SmPC section 4.8 and package leaflet section 4',
 'Dear Sir or Madam,', 'Following the evaluation of a signal of nausea, SynthPharma AG submits a Type II variation to add nausea as an undesirable effect. '
 'The proposed product information is provided as FHIR ePI, both annotated (changes against the approved text) and clean.', 'Yours faithfully,', 'Dr. John Doe, Head of Regulatory Affairs, SynthPharma AG'])
files['var-application-form.pdf'] = pdf('Variation Application Form', 'Type II variation · sample content', [
 ('table', [('Product', PROD), ('Marketing authorisation holder', 'SynthPharma AG'), ('Variation type', 'Type II — safety-related change to the product information'),
            ('Sections affected', 'SmPC 4.8; package leaflet section 4'), ('Proposed implementation', 'On approval')])])
files['var-change-description.pdf'] = pdf('Change Description and Justification', f'{PROD} · 11 January 2027', [
 ('table', [('Current', 'Nausea is not listed as an undesirable effect.'), ('Proposed', 'Add nausea to SmPC section 4.8 (frequency: uncommon) and to package leaflet section 4.'),
            ('Justification', 'Cumulative review of spontaneous reports (including case CH-SYNTHPHARMA-2026-000456, positive dechallenge) and clinical trial data supports a causal association.')])])
files['var-validation-report.pdf'] = pdf('Validation Report', f'Procedure {PROCNO} · 15 January 2027', [
 'The Type II variation has been validated.', ('table', [('Outcome', 'Validation successful'), ('Procedure number assigned', PROCNO), ('Assessment start', '18 January 2027')])])
files['var-approval-letter.pdf'] = pdf('Approval Letter', f'Procedure {PROCNO} · 17 March 2027', [
 f'The Health Authority approves the Type II variation for {PROD}. The approved product information is the agreed ePI returned with this decision.',
 ('table', [('Decision', 'Approved'), ('Sections changed', 'SmPC 4.2 and 4.8; package leaflet sections 3 and 4'), ('Implementation', 'Within 6 months of this decision')])])

G4 = u('scenario4-label-negotiation-group')
PROC4 = ('http://example.org/health-authority/procedure-number', PROCNO)
def ed(id, title, desc, type, file, date, author, **k):
    return dict(id=id, title=title, desc=desc, type=type, file=file, date=date, author=author, **k)
ln_docs = [
 ed('docref-var-cover-letter', 'Variation cover letter', 'Cover letter for the Type II variation adding nausea to the WonderDrug product information.', 'cover-letter', 'var-cover-letter.pdf', D['sub'], 'pharma'),
 ed('docref-var-application-form', 'Variation application form', 'Completed Type II variation application form.', 'application-form', 'var-application-form.pdf', D['sub'], 'pharma'),
 ed('docref-var-change-description', 'Change description and justification', 'Current versus proposed product information, with justification.', 'change-description', 'var-change-description.pdf', D['sub'], 'pharma'),
 ed('docref-epi-annotated-v1', 'Annotated ePI v1 (proposal)', 'Proposed product information as annotated ePI, version 1: adds nausea (uncommon) to SmPC 4.8 and leaflet section 4.', 'proposed-labelling', 'epi-annotated-v1.xml', D['sub'], 'pharma', set='s4-epi-annotated', ver='1'),
 ed('docref-epi-clean-v1', 'Clean ePI v1 (proposal)', 'Proposed product information as clean ePI, version 1.', 'epi-bundle', 'epi-clean-v1.xml', D['sub'], 'pharma', set='s4-epi-clean', ver='1'),
 ed('docref-var-validation-report', 'Variation validation report', 'Validation report: variation valid; procedure number assigned.', 'validation-report', 'var-validation-report.pdf', D['val'], 'ha'),
 ed('docref-epi-annotated-v2', 'Annotated ePI v2 (regulator comments, round 1)', "Regulator's tracked changes on v1: nausea frequency raised to common; intake with food required (SmPC 4.2, leaflet section 3).", 'labelling-comments', 'epi-annotated-v2.xml', D['r1'], 'ha', set='s4-epi-annotated', ver='2', replaces='docref-epi-annotated-v1'),
 ed('docref-epi-annotated-v3', 'Annotated ePI v3 (counter-proposal, round 1)', 'Applicant accepts the frequency change and counter-proposes "may be taken with food to reduce nausea" (SmPC 4.2, leaflet section 3).', 'proposed-labelling', 'epi-annotated-v3.xml', D['r1resp'], 'pharma', set='s4-epi-annotated', ver='3', replaces='docref-epi-annotated-v2'),
 ed('docref-epi-clean-v3', 'Clean ePI v3 (counter-proposal, round 1)', 'Clean ePI matching annotated v3.', 'epi-bundle', 'epi-clean-v3.xml', D['r1resp'], 'pharma', set='s4-epi-clean', ver='3', replaces='docref-epi-clean-v1'),
 ed('docref-epi-annotated-v4', 'Annotated ePI v4 (regulator comments, round 2)', 'Regulator accepts the counter-proposal and changes the leaflet wording to "feeling sick".', 'labelling-comments', 'epi-annotated-v4.xml', D['r2'], 'ha', set='s4-epi-annotated', ver='4', replaces='docref-epi-annotated-v3'),
 ed('docref-epi-clean-v5', 'Clean ePI v5 (agreed text)', 'Clean ePI with all round 2 changes accepted: the agreed product information.', 'epi-bundle', 'epi-clean-v5.xml', D['r2resp'], 'pharma', set='s4-epi-clean', ver='5', replaces='docref-epi-clean-v3'),
 ed('docref-var-approval-letter', 'Variation approval letter', f'Approval of Type II variation {PROCNO}.', 'approval-letter', 'var-approval-letter.pdf', D['dec'], 'ha'),
 ed('docref-epi-approved', 'Approved ePI', 'Approved product information. Points to the same Binary as the agreed clean ePI v5, so the approved text is identical to the agreed text.', 'approved-labelling', 'epi-clean-v5.xml', D['dec'], 'ha', binary='binary-epi-clean-v5', reuse=True),
]
for d in ln_docs:
    d.setdefault('binary', 'binary-' + d['file'].rsplit('.', 1)[0])
    d.update(mime='application/pdf' if d['file'].endswith('.pdf') else 'application/fhir+xml', sys=PH if d['author'] == 'pharma' else HAs)
    if 'set' in d: d['setsys'] = PH   # one ePI version chain = one document set, whoever authored the version
def ref(id):
    d = next(d for d in ln_docs if d['id'] == id)
    return (d['type'], d['title'], d['id'])
VI = [ref('docref-var-cover-letter'), ref('docref-var-application-form'), ref('docref-var-change-description'), ref('docref-epi-annotated-v1'), ref('docref-epi-clean-v1')]
VVR = ref('docref-var-validation-report')
V = 'scenario4-01-variation-submitted'
VAR = ('variation-type-ii', 'Type II Variation')
LC, LA = ('labelling-comments', 'Labelling Comments'), ('labelling-agreement', 'Labelling Agreement')
ln_tasks = [
 dict(id=V, title='scenario4 01 Type II variation submitted', desc='The marketing authorisation holder posts a Type II variation adding nausea to the product information. The proposed label is an annotated ePI plus a clean ePI.',
      heading='Type II variation submitted', ver='1', uuid=u('s4-task-variation'), group=G4, status='requested', bs=('submitted', 'Submitted'), code=VAR,
      authored=D['sub'], modified=D['sub'], requester='pharma', owner='ha', inputs=VI),
 dict(id='scenario4-02-variation-validated', title='scenario4 02 Type II variation validated', desc='Version 2 of the variation Task (in production, the same Task as scenario4-01). The regulator validates it, assigns the procedure number and returns the validation report.',
      heading='Type II variation validated', ver='2', uuid=u('s4-task-variation'), proc=PROC4, group=G4, status='accepted', bs=('validation-successful', 'Validation Successful'), code=VAR,
      authored=D['sub'], modified=D['val'], requester='pharma', owner='ha', inputs=VI, outputs=[VVR], exec=(D['val'], None)),
 dict(id='scenario4-03-variation-under-assessment', title='scenario4 03 Type II variation under assessment', desc='Version 3 of the variation Task (in production, the same Task as scenario4-01). Scientific assessment, including the proposed product information, has started.',
      heading='Type II variation under assessment', ver='3', uuid=u('s4-task-variation'), proc=PROC4, group=G4, status='in-progress', bs=('under-assessment', 'Under Assessment'), code=VAR,
      authored=D['sub'], modified=D['ass'], requester='pharma', owner='ha', inputs=VI, outputs=[VVR], exec=(D['val'], None)),
 dict(id='scenario4-04-labelling-comments-round1', title='scenario4 04 labelling comments round 1 issued', desc='The regulator posts round 1 of the label negotiation, based on the variation Task. Its tracked changes to the proposed ePI (annotated v2) are the input; the applicant owns the response.',
      heading='Labelling comments issued (round 1)', ver='1', uuid=u('s4-task-lc1'), proc=PROC4, group=G4, status='requested', bs=('labelling-comments-issued', 'Labelling Comments Issued'), code=LC,
      authored=D['r1'], modified=D['r1'], requester='ha', owner='pharma', inputs=[ref('docref-epi-annotated-v2')], basedOn=V, period=(D['r1'], D['r1due'])),
 dict(id='scenario4-05-labelling-comments-round1-response', title='scenario4 05 labelling comments round 1 answered with a counter-proposal', desc='Version 2 of the round 1 Task (in production, the same Task as scenario4-04). The applicant accepts the frequency change and counter-proposes the food wording, returning annotated and clean ePI v3.',
      heading='Counter-proposal received (round 1)', ver='2', uuid=u('s4-task-lc1'), proc=PROC4, group=G4, status='completed', bs=('counter-proposal-received', 'Counter-Proposal Received'), code=LC,
      authored=D['r1'], modified=D['r1resp'], requester='ha', owner='pharma', inputs=[ref('docref-epi-annotated-v2')], outputs=[ref('docref-epi-annotated-v3'), ref('docref-epi-clean-v3')], basedOn=V, period=(D['r1'], D['r1due']), exec=('2027-02-22T10:20:00+01:00', D['r1resp'])),
 dict(id='scenario4-06-labelling-comments-round2', title='scenario4 06 labelling comments round 2 issued', desc='The regulator posts round 2: it accepts the counter-proposal and makes one plain-language change to the leaflet (annotated v4).',
      heading='Labelling comments issued (round 2)', ver='1', uuid=u('s4-task-lc2'), proc=PROC4, group=G4, status='requested', bs=('labelling-comments-issued', 'Labelling Comments Issued'), code=LC,
      authored=D['r2'], modified=D['r2'], requester='ha', owner='pharma', inputs=[ref('docref-epi-annotated-v4')], basedOn=V, period=(D['r2'], D['r2due'])),
 dict(id='scenario4-07-labelling-comments-round2-response', title='scenario4 07 labelling comments round 2 accepted', desc='Version 2 of the round 2 Task (in production, the same Task as scenario4-06). The applicant accepts all changes and returns clean ePI v5.',
      heading='Response received (round 2)', ver='2', uuid=u('s4-task-lc2'), proc=PROC4, group=G4, status='completed', bs=('response-received', 'Response Received'), code=LC,
      authored=D['r2'], modified=D['r2resp'], requester='ha', owner='pharma', inputs=[ref('docref-epi-annotated-v4')], outputs=[ref('docref-epi-clean-v5')], basedOn=V, period=(D['r2'], D['r2due']), exec=('2027-03-08T10:05:00+01:00', D['r2resp'])),
 dict(id='scenario4-08-labelling-agreement', title='scenario4 08 labelling agreement requested', desc='The regulator asks the applicant to confirm that clean ePI v5 is the final agreed product information.',
      heading='Labelling agreement requested', ver='1', uuid=u('s4-task-la'), proc=PROC4, group=G4, status='requested', bs=('awaiting-applicant-response', 'Awaiting Applicant Response'), code=LA,
      authored=D['agr'], modified=D['agr'], requester='ha', owner='pharma', inputs=[ref('docref-epi-clean-v5')], basedOn=V),
 dict(id='scenario4-09-labelling-agreed', title='scenario4 09 labelling agreed', desc='Version 2 of the agreement Task (in production, the same Task as scenario4-08). The applicant confirms; completing the Task is the confirmation, so there is no output document.',
      heading='Labelling agreed', ver='2', uuid=u('s4-task-la'), proc=PROC4, group=G4, status='completed', bs=('labelling-agreed', 'Labelling Agreed'), code=LA,
      authored=D['agr'], modified=D['agrresp'], requester='ha', owner='pharma', inputs=[ref('docref-epi-clean-v5')], basedOn=V, exec=('2027-03-11T09:10:00+01:00', D['agrresp'])),
 dict(id='scenario4-10-variation-approved', title='scenario4 10 Type II variation approved', desc='Version 4 of the variation Task (in production, the same Task as scenario4-01). The regulator approves it and returns the approval letter and the approved ePI.',
      heading='Type II variation approved', ver='4', uuid=u('s4-task-variation'), proc=PROC4, group=G4, status='completed', bs=('approved', 'Approved'), code=VAR,
      authored=D['sub'], modified=D['dec'], requester='pharma', owner='ha', inputs=VI, outputs=[VVR, ref('docref-var-approval-letter'), ref('docref-epi-approved')], exec=(D['val'], D['dec'])),
]

def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8').write(text)

for name, docs, tasks, intro in [
    ('scenario2-icsr', icsr_docs, icsr_a_tasks + icsr_b_tasks, 'Scenario 2 — ICSR (E2B(R2)): 2a submitted, accepted, complete; 2b submitted, rejected, resubmitted, accepted, complete.'),
    ('scenario3-cta', cta_docs, cta_tasks, 'Scenario 3 — Clinical trial application: submission, validation, request for information, response, authorisation.'),
    ('scenario4-label-negotiation', ln_docs, ln_tasks, 'Scenario 4 — Label negotiation: Type II variation, two rounds of labelling comments on an annotated ePI, agreement, approval.')]:
    body = [f'// {intro}\n// Generated by parking/gen_examples.py — edit the script, not this file.\n']
    body += [task(t) for t in tasks] + [docref(d, files[d['file']]) for d in docs]
    write(f'{OUT}/input/fsh/workflowExamples/{name}.fsh', '\n'.join(body))
    bins = [f'// {intro} Binaries (fictional sample content). Generated by parking/gen_examples.py.\n'] + [binary(d['binary'], d['mime'], files[d['file']], d['file']) for d in docs if not d.get('reuse')]
    write(f'{OUT}/input/fsh/exampleBinaries/{name}-binaries.fsh', '\n'.join(bins))
for fname, content in files.items():
    os.makedirs(f'{OUT}/parking/example-source', exist_ok=True)
    open(f'{OUT}/parking/example-source/{fname}', 'wb').write(content)
print('ok', {k: len(v) for k, v in files.items()})
