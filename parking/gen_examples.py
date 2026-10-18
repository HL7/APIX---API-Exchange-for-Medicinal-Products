# Generates the ICSR (scenario2) and clinical trial application (scenario3) examples:
#   input/fsh/workflowExamples/scenario2-icsr.fsh, scenario3-cta.fsh   (Tasks + DocumentReferences)
#   input/fsh/exampleBinaries/scenario2-icsr-binaries.fsh, scenario3-cta-binaries.fsh
#   parking/example-source/*  (readable copies of the sample ICSR XML and CTA PDFs)
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
            ('Business status', f'{x(t["bs"][1])} (<code>{t["bs"][0]}</code>)'), ('Requester', x(req[1])), ('Owner', x(own[1])),
            ('Group identifier', t['group']), ('Authored', t['authored']), ('Last modified', t['modified'])]
    if t.get('proc'): rows.insert(1, ('Procedure number', x(t['proc'][1])))
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
    L += [f'* status = #{t["status"]}', f'* businessStatus = {BS}#{t["bs"][0]} "{q(t["bs"][1])}"', '* intent = #proposal', f'* priority = #{t.get("priority","routine")}',
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
       'icsr-message': 'ICSR Message', 'icsr-acknowledgment': 'ICSR Acknowledgment'}

def docref(d, content):
    sha1 = base64.b64encode(hashlib.sha1(content).digest()).decode()
    a = ORG[d['author']]
    L = [f'Instance: {d["id"]}', 'InstanceOf: DocumentReference', f'Title: "{q(d["title"])}"', f'Description: "{q(d["desc"])}"', 'Usage: #example',
         '* meta.profile = "http://hl7.org/fhir/uv/apix/StructureDefinition/apix-documentreference"',
         f'* identifier[0].type = {DEMO}#docsetid "Document Set Identifier"', f'* identifier[0].system = "{d["sys"]}/document-set-id"', f'* identifier[0].value = "{u(d["id"]+"-set")}"',
         f'* identifier[1].type = {DEMO}#docverid "Document Version Number Identifier"', f'* identifier[1].system = "{d["sys"]}/document-version-id"', f'* identifier[1].value = "{u(d["id"]+"-v1")}"',
         '* status = #current', '* docStatus = #final', '* version = "1"', f'* type = {IO}#{d["type"]} "{q(IOD[d["type"]])}"',
         f'* date = "{d["date"]}"', f'* author = Reference({a[0]}) "{q(a[1])}"', f'* description = "{q(d["desc"])}"',
         f'* content.attachment.contentType = #{d["mime"]}', f'* content.attachment.url = "Binary/{d["binary"]}"',
         f'* content.attachment.title = "{q(d["file"])}"', f'* content.attachment.size = {len(content)}',
         f'* content.attachment.hash = "{sha1}"', f'* content.attachment.creation = "{d["date"]}"']
    return '\n'.join(L) + '\n'

def binary(bid, mime, content, desc):
    return (f'Instance: {bid}\nInstanceOf: Binary\nDescription: "{q(desc)}"\nUsage: #example\n* contentType = #{mime}\n'
            f'* data = "{base64.b64encode(content).decode()}"\n')

# ================================================================ ICSR (scenario2)
HDR = '<?xml version="1.0" encoding="UTF-8"?>\n<!-- FICTIONAL EXAMPLE for the RWI-pharma IG. Abbreviated ICH E2B(R3) message: the structure follows the\n     E2B(R3) HL7 v3 schema (MCCI_IN200100UV01 batch / PORR_IN049016UV message) but only key data elements are\n     shown, and it has not been validated against the ICH schemas. Data element numbers are given in comments. -->\n'
def icsr_xml(batch, msg, created, most_recent, followup):
    outcome = ('1', 'recovered/resolved') if followup else ('3', 'not recovered/not resolved')
    narrative = ('54-year-old female patient started WonderDrug 50 mg tablets once daily on 20-Sep-2026. On 26-Sep-2026 she developed nausea. '
                 'The reporting physician considered the event non-serious and possibly related.')
    if followup: narrative += ' Follow-up 08-Oct-2026: WonderDrug was withdrawn on 30-Sep-2026 and the nausea resolved on 05-Oct-2026 (positive dechallenge).'
    action = '\n                        <!-- G.k.8 action taken with drug: drug withdrawn -->\n                        <inboundRelationship typeCode="CAUS"><act classCode="ACT" moodCode="EVN"><code code="1" codeSystem="2.16.840.1.113883.3.989.2.1.1.15" displayName="drug withdrawn"/></act></inboundRelationship>' if followup else ''
    return (HDR + f'''<MCCI_IN200100UV01 xmlns="urn:hl7-org:v3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" ITSVersion="XML_1.0">
  <id root="2.16.840.1.113883.3.989.2.1.3.22" extension="{batch}"/>                 <!-- N.1.2 batch number -->
  <creationTime value="{created}"/>                                                   <!-- N.1.5 date of batch transmission -->
  <responseModeCode code="D"/>
  <interactionId root="2.16.840.1.113883.1.6" extension="MCCI_IN200100UV01"/>
  <name code="1" codeSystem="2.16.840.1.113883.3.989.2.1.1.1" displayName="ichicsr"/>  <!-- N.1.1 type of messages in batch -->
  <PORR_IN049016UV>
    <id root="2.16.840.1.113883.3.989.2.1.3.1" extension="{msg}"/>                   <!-- N.2.r.1 message identifier -->
    <creationTime value="{created}"/>                                                 <!-- N.2.r.4 date of message creation -->
    <interactionId root="2.16.840.1.113883.1.6" extension="PORR_IN049016UV"/>
    <processingCode code="P"/>
    <processingModeCode code="T"/>
    <acceptAckCode code="AL"/>
    <receiver typeCode="RCV"><device classCode="DEV" determinerCode="INSTANCE"><id root="2.16.840.1.113883.3.989.2.1.3.12" extension="HA-PHARMACOVIGILANCE"/></device></receiver>  <!-- N.2.r.3 -->
    <sender typeCode="SND"><device classCode="DEV" determinerCode="INSTANCE"><id root="2.16.840.1.113883.3.989.2.1.3.11" extension="SYNTHPHARMA-AG"/></device></sender>             <!-- N.2.r.2 -->
    <controlActProcess classCode="CACT" moodCode="EVN">
      <code code="PORR_TE049016UV" codeSystem="2.16.840.1.113883.1.18"/>
      <effectiveTime value="{created}"/>                                              <!-- C.1.2 date of creation -->
      <subject typeCode="SUBJ">
        <investigationEvent classCode="INVSTG" moodCode="EVN">
          <id root="2.16.840.1.113883.3.989.2.1.3.1" extension="CH-SYNTHPHARMA-2026-000456"/>   <!-- C.1.1 sender's safety report unique identifier -->
          <id root="2.16.840.1.113883.3.989.2.1.3.2" extension="CH-SYNTHPHARMA-2026-000456"/>   <!-- C.1.8.1 worldwide unique case identification number -->
          <code code="PAT_ADV_EVNT" codeSystem="2.16.840.1.113883.5.4"/>
          <text>{narrative}</text>                                                     <!-- H.1 case narrative -->
          <statusCode code="active"/>
          <effectiveTime><low value="20260928"/></effectiveTime>                         <!-- C.1.4 date report was first received from source -->
          <availabilityTime value="{most_recent}"/>                                      <!-- C.1.5 date of most recent information -->
          <component typeCode="COMP">
            <adverseEventAssessment classCode="INVSTG" moodCode="EVN">
              <subject1 typeCode="SBJ">
                <primaryRole classCode="INVSBJ">
                  <player1 classCode="PSN" determinerCode="INSTANCE">
                    <name>JD</name>                                                       <!-- D.1 patient (initials) -->
                    <administrativeGenderCode code="2" codeSystem="1.0.5218" displayName="female"/>  <!-- D.5 sex -->
                  </player1>
                  <subjectOf2 typeCode="SBJ">
                    <observation classCode="OBS" moodCode="EVN">
                      <code code="3" codeSystem="2.16.840.1.113883.3.989.2.1.1.19" displayName="age"/>
                      <value xsi:type="PQ" value="54" unit="a"/>                          <!-- D.2.2 age at time of onset -->
                    </observation>
                  </subjectOf2>
                  <subjectOf2 typeCode="SBJ">
                    <observation classCode="OBS" moodCode="EVN">
                      <id root="2.16.840.1.113883.3.989.2.1.3.8" extension="R1"/>
                      <code code="29" codeSystem="2.16.840.1.113883.3.989.2.1.1.19" displayName="reaction"/>
                      <effectiveTime xsi:type="IVL_TS"><low value="20260926"/>{'<high value="20261005"/>' if followup else ''}</effectiveTime>  <!-- E.i.4 / E.i.5 -->
                      <value xsi:type="CE" code="10028813" codeSystem="2.16.840.1.113883.6.163" codeSystemVersion="29.0" displayName="Nausea"/>  <!-- E.i.2.1b MedDRA PT -->
                      <outboundRelationship2 typeCode="PERT">
                        <observation classCode="OBS" moodCode="EVN">
                          <code code="27" codeSystem="2.16.840.1.113883.3.989.2.1.1.19" displayName="outcome"/>
                          <value xsi:type="CE" code="{outcome[0]}" codeSystem="2.16.840.1.113883.3.989.2.1.1.11" displayName="{outcome[1]}"/>  <!-- E.i.7 outcome -->
                        </observation>
                      </outboundRelationship2>
                    </observation>
                  </subjectOf2>
                  <subjectOf2 typeCode="SBJ">
                    <organizer classCode="CATEGORY" moodCode="EVN">
                      <code code="4" codeSystem="2.16.840.1.113883.3.989.2.1.1.20" displayName="drugInformation"/>
                      <component typeCode="COMP">
                        <substanceAdministration classCode="SBADM" moodCode="EVN">
                          <id root="2.16.840.1.113883.3.989.2.1.3.5" extension="D1"/>
                          <consumable typeCode="CSM"><instanceOfKind classCode="INST"><kindOfProduct classCode="MMAT" determinerCode="KIND">
                            <name>WonderDrug 50 mg tablets</name>                         <!-- G.k.2.2 medicinal product name as reported -->
                          </kindOfProduct></instanceOfKind></consumable>
                          <outboundRelationship2 typeCode="COMP"><substanceAdministration classCode="SBADM" moodCode="EVN">
                            <effectiveTime xsi:type="IVL_TS"><low value="20260920"/>{'<high value="20260930"/>' if followup else ''}</effectiveTime>  <!-- G.k.4.r.4 / G.k.4.r.5 -->
                            <doseQuantity value="50" unit="mg"/>                          <!-- G.k.4.r.1 dose -->
                          </substanceAdministration></outboundRelationship2>{action}
                        </substanceAdministration>
                      </component>
                    </organizer>
                  </subjectOf2>
                </primaryRole>
              </subject1>
            </adverseEventAssessment>
          </component>
          <outboundRelationship typeCode="SPRT">
            <relatedInvestigation classCode="INVSTG" moodCode="EVN">
              <code code="2" codeSystem="2.16.840.1.113883.3.989.2.1.1.22" displayName="sourceReport"/>
              <subjectOf2 typeCode="SUBJ"><controlActEvent classCode="CACT" moodCode="EVN"><author typeCode="AUT"><assignedEntity classCode="ASSIGNED">
                <code code="1" codeSystem="2.16.840.1.113883.3.989.2.1.1.6" displayName="physician"/>  <!-- C.2.r.4 qualification -->
              </assignedEntity></author></controlActEvent></subjectOf2>
            </relatedInvestigation>
          </outboundRelationship>
          <subjectOf2 typeCode="SUBJ">
            <investigationCharacteristic classCode="OBS" moodCode="EVN">
              <code code="1" codeSystem="2.16.840.1.113883.3.989.2.1.1.23" displayName="ichReportType"/>
              <value xsi:type="CE" code="1" codeSystem="2.16.840.1.113883.3.989.2.1.1.2" displayName="Spontaneous report"/>  <!-- C.1.3 type of report -->
            </investigationCharacteristic>
          </subjectOf2>
        </investigationEvent>
      </subject>
    </controlActProcess>
  </PORR_IN049016UV>
</MCCI_IN200100UV01>
''').encode()

def ack_xml(ack_batch, batch, msg, created):
    return (HDR.replace('(MCCI_IN200100UV01 batch / PORR_IN049016UV message)', '(MCCI_IN200101UV01 acknowledgment)') + f'''<MCCI_IN200101UV01 xmlns="urn:hl7-org:v3" ITSVersion="XML_1.0">
  <id root="2.16.840.1.113883.3.989.2.1.3.20" extension="{ack_batch}"/>
  <creationTime value="{created}"/>
  <interactionId root="2.16.840.1.113883.1.6" extension="MCCI_IN200101UV01"/>
  <MCCI_IN000002UV01>
    <id root="2.16.840.1.113883.3.989.2.1.3.24" extension="{ack_batch}-1"/>
    <creationTime value="{created}"/>
    <interactionId root="2.16.840.1.113883.1.6" extension="MCCI_IN000002UV01"/>
    <processingCode code="P"/>
    <processingModeCode code="T"/>
    <acceptAckCode code="NE"/>
    <receiver typeCode="RCV"><device classCode="DEV" determinerCode="INSTANCE"><id root="2.16.840.1.113883.3.989.2.1.3.18" extension="SYNTHPHARMA-AG"/></device></receiver>
    <sender typeCode="SND"><device classCode="DEV" determinerCode="INSTANCE"><id root="2.16.840.1.113883.3.989.2.1.3.17" extension="HA-PHARMACOVIGILANCE"/></device></sender>
    <acknowledgement typeCode="CA">                                                   <!-- ACK.B.r.6 report acknowledgment code: CA = commit accept -->
      <targetMessage><id root="2.16.840.1.113883.3.989.2.1.3.1" extension="{msg}"/></targetMessage>  <!-- the ICSR message being acknowledged -->
    </acknowledgement>
  </MCCI_IN000002UV01>
  <acknowledgement typeCode="AA">                                                     <!-- ACK.A.4 transmission acknowledgment code: AA = all reports loaded -->
    <targetBatch><id root="2.16.840.1.113883.3.989.2.1.3.22" extension="{batch}"/></targetBatch>  <!-- the batch being acknowledged -->
  </acknowledgement>
</MCCI_IN200101UV01>
''').encode()

files = {}
files['icsr-initial.xml'] = icsr_xml('SYNTH-BATCH-2026-000123', 'SYNTH-MSG-2026-000456-1', '20261002093000+0200', '20260928', False)
files['icsr-initial-ack.xml'] = ack_xml('HA-ACK-2026-778001', 'SYNTH-BATCH-2026-000123', 'SYNTH-MSG-2026-000456-1', '20261002094512+0200')
files['icsr-follow-up.xml'] = icsr_xml('SYNTH-BATCH-2026-000131', 'SYNTH-MSG-2026-000456-2', '20261009101500+0200', '20261008', True)
files['icsr-follow-up-ack.xml'] = ack_xml('HA-ACK-2026-779340', 'SYNTH-BATCH-2026-000131', 'SYNTH-MSG-2026-000456-2', '20261009103002+0200')

G2 = u('scenario2-icsr-group')
PH, HAs = 'http://example.org/synthpharma', 'http://example.org/health-authority'
icsr_docs = [
 dict(id='docref-icsr-initial', title='Initial ICSR — case CH-SYNTHPHARMA-2026-000456', desc='Initial ICH E2B(R3) ICSR for case CH-SYNTHPHARMA-2026-000456 (nausea with WonderDrug 50 mg).', type='icsr-message', mime='application/xml', binary='binary-icsr-initial', file='icsr-initial.xml', date='2026-10-02T09:30:00+02:00', author='pharma', sys=PH),
 dict(id='docref-icsr-initial-ack', title='Acknowledgment of initial ICSR', desc='ICH E2B(R3) acknowledgment: transmission AA, report CA.', type='icsr-acknowledgment', mime='application/xml', binary='binary-icsr-initial-ack', file='icsr-initial-ack.xml', date='2026-10-02T09:45:12+02:00', author='ha', sys=HAs),
 dict(id='docref-icsr-follow-up', title='Follow-up ICSR — case CH-SYNTHPHARMA-2026-000456', desc='Follow-up ICH E2B(R3) ICSR: drug withdrawn, reaction resolved (positive dechallenge).', type='icsr-message', mime='application/xml', binary='binary-icsr-follow-up', file='icsr-follow-up.xml', date='2026-10-09T10:15:00+02:00', author='pharma', sys=PH),
 dict(id='docref-icsr-follow-up-ack', title='Acknowledgment of follow-up ICSR', desc='ICH E2B(R3) acknowledgment: transmission AA, report CA.', type='icsr-acknowledgment', mime='application/xml', binary='binary-icsr-follow-up-ack', file='icsr-follow-up-ack.xml', date='2026-10-09T10:30:02+02:00', author='ha', sys=HAs),
]
I1, I2 = ('icsr-message', 'Initial ICSR', 'docref-icsr-initial'), ('icsr-message', 'Follow-up ICSR', 'docref-icsr-follow-up')
A1, A2 = ('icsr-acknowledgment', 'Acknowledgment of initial ICSR', 'docref-icsr-initial-ack'), ('icsr-acknowledgment', 'Acknowledgment of follow-up ICSR', 'docref-icsr-follow-up-ack')
icsr_tasks = [
 dict(id='scenario2-01-icsr-initial', title='scenario2 01 initial ICSR submitted', desc='The marketing authorization holder posts an initial ICSR Task; the E2B(R3) message is the input.',
      heading='Initial ICSR submitted', ver='1', uuid=u('s2-task-initial'), group=G2, status='requested', bs=('submitted', 'Submitted'), code=('icsr-initial', 'Initial ICSR'),
      authored='2026-10-02T09:30:00+02:00', modified='2026-10-02T09:30:00+02:00', requester='pharma', owner='ha', inputs=[I1]),
 dict(id='scenario2-02-icsr-initial-acknowledged', title='scenario2 02 initial ICSR acknowledged', desc='Version 2 of the initial ICSR Task (in production, the same Task as scenario2-01). The regulator completes it and returns the E2B(R3) acknowledgment as the output.',
      heading='Initial ICSR acknowledged (AA / CA)', ver='2', uuid=u('s2-task-initial'), group=G2, status='completed', bs=('icsr-accepted', 'Report Accepted (CA)'), code=('icsr-initial', 'Initial ICSR'),
      authored='2026-10-02T09:30:00+02:00', modified='2026-10-02T09:45:12+02:00', requester='pharma', owner='ha', inputs=[I1], outputs=[A1], exec=('2026-10-02T09:30:05+02:00', '2026-10-02T09:45:12+02:00')),
 dict(id='scenario2-03-icsr-follow-up', title='scenario2 03 follow-up ICSR submitted', desc='The marketing authorization holder posts a follow-up ICSR Task for the same case, with the same group identifier.',
      heading='Follow-up ICSR submitted', ver='1', uuid=u('s2-task-follow-up'), group=G2, status='requested', bs=('submitted', 'Submitted'), code=('icsr-follow-up', 'Follow-up ICSR'),
      authored='2026-10-09T10:15:00+02:00', modified='2026-10-09T10:15:00+02:00', requester='pharma', owner='ha', inputs=[I2], basedOn='scenario2-01-icsr-initial'),
 dict(id='scenario2-04-icsr-follow-up-acknowledged', title='scenario2 04 follow-up ICSR acknowledged', desc='Version 2 of the follow-up ICSR Task (in production, the same Task as scenario2-03). The regulator completes it and returns the acknowledgment.',
      heading='Follow-up ICSR acknowledged (AA / CA)', ver='2', uuid=u('s2-task-follow-up'), group=G2, status='completed', bs=('icsr-accepted', 'Report Accepted (CA)'), code=('icsr-follow-up', 'Follow-up ICSR'),
      authored='2026-10-09T10:15:00+02:00', modified='2026-10-09T10:30:02+02:00', requester='pharma', owner='ha', inputs=[I2], outputs=[A2], basedOn='scenario2-01-icsr-initial', exec=('2026-10-09T10:15:04+02:00', '2026-10-09T10:30:02+02:00')),
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

def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8').write(text)

for name, docs, tasks, intro in [
    ('scenario2-icsr', icsr_docs, icsr_tasks, 'Scenario 2 — ICSR: initial report, acknowledgment, follow-up report, acknowledgment.'),
    ('scenario3-cta', cta_docs, cta_tasks, 'Scenario 3 — Clinical trial application: submission, validation, request for information, response, authorisation.')]:
    body = [f'// {intro}\n// Generated by parking/gen_examples.py — edit the script, not this file.\n']
    body += [task(t) for t in tasks] + [docref(d, files[d['file']]) for d in docs]
    write(f'{OUT}/input/fsh/workflowExamples/{name}.fsh', '\n'.join(body))
    bins = [f'// {intro} Binaries (fictional sample content). Generated by parking/gen_examples.py.\n'] + [binary(d['binary'], d['mime'], files[d['file']], d['file']) for d in docs]
    write(f'{OUT}/input/fsh/exampleBinaries/{name}-binaries.fsh', '\n'.join(bins))
for fname, content in files.items():
    os.makedirs(f'{OUT}/parking/example-source', exist_ok=True)
    open(f'{OUT}/parking/example-source/{fname}', 'wb').write(content)
print('ok', {k: len(v) for k, v in files.items()})
