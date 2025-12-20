import json
import os
import sys
from datetime import datetime

# File paths
JSON_FILE = '/Users/a001/Documents/GitHub/APIX---API-Exchange-for-Medicinal-Products/input/examples/example-apix-task-shelf-life-original.json'
OUTPUT_DIR = '/Users/a001/Documents/GitHub/APIX---API-Exchange-for-Medicinal-Products/output'

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def get_contained_resource(resource, ref_id):
    if ref_id.startswith('#'):
        ref_id = ref_id[1:]
    
    for item in resource.get('contained', []):
        if item.get('id') == ref_id:
            return item
    return None

def format_date(date_str):
    if not date_str:
        return "N/A"
    try:
        dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        return dt.strftime('%Y-%m-%d %H:%M:%S %Z')
    except:
        return date_str

def get_address_html(org):
    lines = []
    if not org:
        return "N/A"
    
    addr = org.get('address', {})
    if 'text' in addr:
        lines.append(addr['text'])
    else:
        line = " ".join(addr.get('line', []))
        city = addr.get('city', '')
        postal = addr.get('postalCode', '')
        country = addr.get('country', '')
        if line or city or country:
            lines.append(f"{line}, {postal} {city}, {country}")
        
    return "<br>".join(lines) if lines else "N/A"

def get_contact_html(org):
    if not org:
        return ""
    
    contacts = org.get('contact', [])
    html = ""
    for c in contacts:
        name = c.get('name', {}).get('text', 'Contact')
        phone = ""
        email = ""
        for t in c.get('telecom', []):
            if t.get('system') == 'phone':
                phone = t.get('value')
            elif t.get('system') == 'email':
                email = t.get('value')
        
        html += f"<strong>{name}</strong><br>"
        if phone:
            html += f"<strong>Phone:</strong> {phone}<br>"
        if email:
            html += f"<strong>Email:</strong> {email}<br>"
            
    return html

def categorize_docs(docs):
    modules = {
        'Module 1': [],
        'Module 2': [],
        'Module 3': [],
        'Module 4': [],
        'Module 5': [],
        'Other': []
    }
    
    for doc in docs:
        doc_type_coding = doc.get('type', {}).get('coding', [{}])[0]
        code = doc_type_coding.get('code', '')
        
        attachment = None
        if 'content' in doc and len(doc['content']) > 0:
            attachment = doc['content'][0].get('attachment')
        if not attachment:
            attachment = doc.get('valueAttachment')
            
        if not attachment:
            continue
            
        title = attachment.get('title', 'Untitled')
        
        item = {
            'code': code,
            'title': title,
            'display': doc_type_coding.get('display', code),
            'url': attachment.get('url'),
            'size': attachment.get('size'),
            'type': attachment.get('contentType')
        }
        
        if code.startswith('1') or code in ['cover-letter', 'application-form']:
            modules['Module 1'].append(item)
        elif code.startswith('2'):
            modules['Module 2'].append(item)
        elif code.startswith('3') or code.startswith('cmc'):
            modules['Module 3'].append(item)
        elif code.startswith('4'):
            modules['Module 4'].append(item)
        elif code.startswith('5'):
            modules['Module 5'].append(item)
        else:
            modules['Other'].append(item)
            
    return modules

def main():
    json_path = JSON_FILE
    template_path = None
    
    if len(sys.argv) > 1:
        json_path = sys.argv[1]
    if len(sys.argv) > 2:
        template_path = sys.argv[2]
    
    if not os.path.exists(json_path):
        print(f"Error: File {json_path} not found.")
        return

    base_name = os.path.basename(json_path).replace('.json', '')
    instance_output_file = os.path.join(OUTPUT_DIR, f"{base_name}-render.html")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    data = load_json(json_path)
    
    task_id = data.get('id', 'N/A')
    status = data.get('status', 'N/A')
    priority = data.get('priority', 'N/A')
    
    task_coding = data.get('code', {}).get('coding', [{}])[0]
    task_type_display = task_coding.get('display', 'Task')
    task_type_code = task_coding.get('code', '')
    
    authored_on = data.get('authoredOn', '')
    last_modified = data.get('lastModified', authored_on)
    
    requester_ref = data.get('requester', {}).get('reference', '')
    requester = get_contained_resource(data, requester_ref)
    
    performer_ref = (data.get('owner', {}) or data.get('requesterPerformer', {})).get('reference', '')
    performer = get_contained_resource(data, performer_ref)
    
    inputs = data.get('input', [])
    doc_resources = []
    for inp in inputs:
        ref = inp.get('valueReference', {}).get('reference', '')
        if ref.startswith('#'):
            res = get_contained_resource(data, ref)
            if res:
                doc_resources.append(res)
    
    modules = categorize_docs(doc_resources)
    
    docs_html = ""
    for mod_name, items in modules.items():
        if not items:
            continue
            
        docs_html += f'<div class="module"><h3>{mod_name}</h3>'
        for item in items:
            size_str = ""
            if item.get('size'):
                if item['size'] >= 1024*1024*1024:
                    size_str = f" • {item['size'] / 1024 / 1024 / 1024:.2f} GB"
                else:
                    size_str = f" • {item['size'] / 1024 / 1024:.2f} MB"
            
            link_html = ""
            if item.get('url'):
                link_html = f'<a href="{item["url"]}" style="color:#007aff; text-decoration:none; font-weight:600;">View External</a>'
            else:
                link_html = '<span style="color:#666;">Embedded Data</span>'
            
            docs_html += f"""
            <div class="doc-item">
                <div style="display:flex; justify-content:space-between; align-items:flex-start;">
                    <div>
                        <div class="doc-type">{item['display'] or item['code']}</div>
                        <span class="doc-code">{item['code']}</span>{size_str}<br>
                        {item['title']}
                    </div>
                    <div>
                        {link_html}
                    </div>
                </div>
            </div>
            """
        docs_html += "</div>"

    html_template = None
    if template_path and os.path.exists(template_path):
        with open(template_path, 'r') as f:
            html_template = f.read()
    
    is_external_template = (html_template is not None)

    if not html_template:
        html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>APIX Task – {task_title}</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background: linear-gradient(to bottom, #f2f6fa, #e8eef5); color: #1d1d1f; margin: 0; padding: 40px 20px; line-height: 1.5; }
        .container { max-width: 1000px; margin: 0 auto; }
        header { background: linear-gradient(135deg, #007aff, #5ac8fa); color: white; padding: 40px 24px; border-radius: 18px; text-align: center; box-shadow: 0 10px 30px rgba(0, 122, 255, 0.3); margin-bottom: 36px; }
        header h1 { margin: 0 0 8px; font-size: 32px; font-weight: 600; }
        header p { margin: 0; opacity: 0.95; font-size: 17px; }
        .card { background: white; border-radius: 18px; padding: 32px; margin-bottom: 32px; box-shadow: 0 8px 28px rgba(0,0,0,0.08), 0 2px 10px rgba(0,0,0,0.06); transition: all 0.25s ease; }
        .card:hover { transform: translateY(-6px); box-shadow: 0 20px 40px rgba(0,0,0,0.12); }
        .card-title { font-size: 24px; font-weight: 600; color: #007aff; margin: 0 0 24px 0; padding-bottom: 12px; border-bottom: 1px solid #e5e5ea; display: flex; justify-content: space-between; align-items: center; }
        .count-badge { background: #007aff; color: white; font-size: 14px; font-weight: 600; padding: 6px 14px; border-radius: 20px; }
        .module { margin: 24px 0; padding: 20px; background: #f8fbff; border-radius: 14px; border-left: 5px solid #007aff; }
        .module h3 { margin: 0 0 16px 0; font-size: 18px; color: #007aff; font-weight: 600; }
        .doc-item { background: white; border: 1px solid #d1e4ff; border-radius: 12px; padding: 16px; margin-bottom: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); }
        .doc-type { font-weight: 600; color: #007aff; font-size: 15px; }
        .doc-code { font-family: Menlo, Monaco, Consolas, monospace; background: #e5f2ff; padding: 2px 8px; border-radius: 6px; font-size: 13px; }
        footer { text-align: center; padding: 50px; color: #666; font-size: 14px; }
        .field-label { font-weight: 600; color: #555; }
    </style>
</head>
<body>
<div class="container">
<header>
    <h1>Task: {task_title}</h1>
    <p>HL7 FHIR R5 – APIX Implementation Guide</p>
</header>
<div class="card">
    <h2 class="card-title">Core Task Information</h2>
    <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 20px;">
        <div>
            <span class="field-label">ID</span><br>{task_id}<br><br>
            <span class="field-label">Status</span><br><span style="background:#007aff;color:white;padding:4px 10px;border-radius:8px;">{status}</span><br><br>
            <span class="field-label">Priority</span><br>{priority}
        </div>
        <div>
            <span class="field-label">Code</span><br>{task_type_display} ({task_type_code})<br><br>
            <span class="field-label">Authored</span><br>{authored_on}<br><br>
            <span class="field-label">Last Updated</span><br>{last_modified}
        </div>
    </div>
</div>
<div class="card">
    <h2 class="card-title">Parties Involved</h2>
    <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 40px;">
        <div class="party-info">
            <span style="font-weight:600; color:#007aff;">Requester</span><br>
            <div style="font-size:16px; font-weight:500; margin:8px 0;">{requester_name}</div>
            <div style="font-size:14px; color:#555;">{requester_address}</div>
            {requester_contact}
        </div>
        <div class="party-info">
            <span style="font-weight:600; color:#007aff;">Performer/Owner</span><br>
            <div style="font-size:16px; font-weight:500; margin:8px 0;">{performer_name}</div>
            <div style="font-size:14px; color:#555;">{performer_address}</div>
            {performer_contact}
        </div>
    </div>
</div>
<div class="card">
    <div class="card-title">
        Input Documents
        <span class="count-badge">{doc_count} total</span>
    </div>
    {input_docs_html}
</div>
</div>
<footer>
    HL7 FHIR R5 – API Exchange for Medicinal Products (APIX)<br>
    Render Generated on {render_date}
</footer>
</body>
</html>
"""

    replacements = {
        "{task_title}": task_type_display,
        "{task_id}": task_id,
        "{status}": status,
        "{priority}": priority,
        "{task_type_display}": task_type_display,
        "{task_type_code}": task_type_code,
        "{authored_on}": format_date(authored_on),
        "{last_modified}": format_date(last_modified),
        "{requester_name}": requester.get('name', 'Unknown') if requester else 'Unknown',
        "{requester_address}": get_address_html(requester),
        "{requester_contact}": get_contact_html(requester),
        "{performer_name}": performer.get('name', 'Unknown') if performer else 'Unknown',
        "{performer_address}": get_address_html(performer),
        "{performer_contact}": get_contact_html(performer),
        "{doc_count}": str(len(inputs)),
        "{input_docs_html}": docs_html,
        "{render_date}": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    html_content = html_template
    for key, val in replacements.items():
        html_content = html_content.replace(key, val)
    
    with open(instance_output_file, 'w') as f:
        f.write(html_content)
    
    print(f"Successfully generated {instance_output_file}")

if __name__ == "__main__":
    main()
