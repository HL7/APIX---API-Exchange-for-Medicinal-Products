import json
import os
from datetime import datetime

# File paths
JSON_FILE = '/Users/a001/Documents/GitHub/APIX---API-Exchange-for-Medicinal-Products/input/examples/example-apix-task-shelf-life-original.json'
OUTPUT_FILE = '/Users/a001/Documents/GitHub/APIX---API-Exchange-for-Medicinal-Products/output/apix-task-shelf-life-render.html'

# Ensure output directory exists
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

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
    try:
        # Simplistic parsing for the example format "2025-11-15T09:00:00+01:00"
        dt = datetime.fromisoformat(date_str)
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
        # Fallback to parts
        line = " ".join(addr.get('line', []))
        city = addr.get('city', '')
        postal = addr.get('postalCode', '')
        country = addr.get('country', '')
        lines.append(f"{line}, {postal} {city}, {country}")
        
    return "<br>".join(lines)

def get_contact_html(org):
    if not org:
        return ""
    
    contacts = org.get('contact', [])
    html = ""
    for c in contacts:
        name = c.get('name', {}).get('text', 'Contact')
        # Extract phone and email
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
    # Mapping based on CTD structure
    modules = {
        'Module 1': [],
        'Module 2': [],
        'Module 3': [],
        'Module 4': [],
        'Module 5': [],
        'Regional': [],
        'Other': []
    }
    
    for doc in docs:
        doc_type_coding = doc.get('type', {}).get('coding', [{}])[0]
        code = doc_type_coding.get('code', '')
        title = doc.get('valueAttachment', {}).get('title', 'Untitled')
        
        item = {
            'code': code,
            'title': title,
            'display': doc_type_coding.get('display', code) # Fallback to code if display missing
        }
        
        # Simple categorization logic
        if code in ['cover-letter', 'application-form', 'annotated-label', 'clean-label', 'pack-mockup']:
            modules['Module 1'].append(item)
        elif code.startswith('cmc-stability'):
            modules['Module 3'].append(item)
        else:
            modules['Other'].append(item)
            
    return modules

def main():
    data = load_json(JSON_FILE)
    
    # Extract Header Info
    task_id = data.get('id', 'N/A')
    status = data.get('status', 'N/A')
    priority = data.get('priority', 'N/A')
    
    # Task Code/Type
    task_coding = data.get('code', {}).get('coding', [{}])[0]
    task_type_display = task_coding.get('display', 'Task')
    task_type_code = task_coding.get('code', '')
    
    authored_on = data.get('authoredOn', '')
    last_modified = data.get('lastModified', '')
    
    # Parties
    requester_ref = data.get('requester', {}).get('reference', '')
    requester = get_contained_resource(data, requester_ref)
    
    performer_ref = data.get('requesterPerformer', {}).get('reference', '')
    performer = get_contained_resource(data, performer_ref) # Assuming 'requesterPerformer' maps to the "Owner/MAH" role in the visual, or vice versa? 
    # In the HTML example:
    # Requester = EMA (Regulator)
    # Owner = PharmaCorp (MAH) - usually the performer of the submission *preparation*, but in a "Task" context, usually the requester asks for work. 
    # However, for a Regulatory Task:
    # Requester is usually the MAH asking for review OR the Regulator asking for info. 
    # Let's look at the JSON:
    # "requester": reference: "#org-synthpharma-ag" (The Pharma company)
    # "requesterPerformer": reference: "#org-ema-srm-hmed" (The EMA)
    # So SynthPharma (MAH) is requesting the task, EMA is the performer (Regulator).
    
    # HTML Layout
    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>APIX Task – {task_title}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background: linear-gradient(to bottom, #f2f6fa, #e8eef5);
            color: #1d1d1f;
            margin: 0;
            padding: 40px 20px;
            line-height: 1.5;
        }}
        .container {{ max-width: 1000px; margin: 0 auto; }}
        header {{
            background: linear-gradient(135deg, #007aff, #5ac8fa);
            color: white;
            padding: 40px 24px;
            border-radius: 18px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0, 122, 255, 0.3);
            margin-bottom: 36px;
        }}
        header h1 {{ margin: 0 0 8px; font-size: 32px; font-weight: 600; }}
        header p {{ margin: 0; opacity: 0.95; font-size: 17px; }}

        .card {{
            background: white;
            border-radius: 18px;
            padding: 32px;
            margin-bottom: 32px;
            box-shadow: 0 8px 28px rgba(0,0,0,0.08), 0 2px 10px rgba(0,0,0,0.06);
            transition: all 0.25s ease;
        }}
        .card:hover {{ transform: translateY(-6px); box-shadow: 0 20px 40px rgba(0,0,0,0.12); }}
        .card-title {{
            font-size: 24px;
            font-weight: 600;
            color: #007aff;
            margin: 0 0 24px 0;
            padding-bottom: 12px;
            border-bottom: 1px solid #e5e5ea;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .count-badge {{
            background: #007aff;
            color: white;
            font-size: 14px;
            font-weight: 600;
            padding: 6px 14px;
            border-radius: 20px;
        }}
        .module {{
            margin: 24px 0;
            padding: 20px;
            background: #f8fbff;
            border-radius: 14px;
            border-left: 5px solid #007aff;
        }}
        .module h3 {{
            margin: 0 0 16px 0;
            font-size: 18px;
            color: #007aff;
            font-weight: 600;
        }}
        .doc-item {{
            background: white;
            border: 1px solid #d1e4ff;
            border-radius: 12px;
            padding: 16px;
            margin-bottom: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }}
        .doc-type {{
            font-weight: 600;
            color: #007aff;
            font-size: 15px;
        }}
        .doc-code {{
            font-family: Menlo, Monaco, Consolas, monospace;
            background: #e5f2ff;
            padding: 2px 8px;
            border-radius: 6px;
            font-size: 13px;
        }}
        .empty {{ color: #888; font-style: italic; margin: 12px 0; }}
        footer {{ text-align: center; padding: 50px; color: #666; font-size: 14px; }}
    </style>
</head>
<body>
<div class="container">

<!-- 1. Header -->
<header>
    <h1>Task: {task_title}</h1>
    <p>HL7 FHIR R5 – APIX Implementation Guide</p>
</header>

<!-- 2. Core Task Information -->
<div class="card">
    <h2 class="card-title">Core Task Information</h2>
    <strong>ID</strong><br>{task_id}<br><br>
    <strong>Status</strong><br><span style="background:#007aff;color:white;padding:4px 10px;border-radius:8px;">{status}</span><br><br>
    <strong>Priority</strong><br>{priority}<br><br>
    <strong>Code</strong><br>{task_type_display} ({task_type_code})<br><br>
    <strong>Authored</strong><br>{authored_on}<br><br>
    <strong>Last Updated</strong><br>{last_modified}
</div>

<!-- 3. Parties Involved -->
<div class="card">
    <h2 class="card-title">Parties Involved</h2>
    
    <div style="margin-bottom:28px;">
        <strong>Requester</strong><br>
        {requester_name}<br>
        <strong>Address:</strong><br> {requester_address}<br>
        {requester_contact}
    </div>

    <div>
        <strong>Performer</strong><br>
        {performer_name}<br>
        <strong>Address:</strong><br> {performer_address}<br>
        {performer_contact}
    </div>
</div>

<!-- 4. Input Documents -->
<div class="card">
    <div class="card-title">
        Input Documents
        <span class="count-badge">{doc_count} documents</span>
    </div>

    {input_docs_html}

</div>

<!-- 5. Expected Output -->
<div class="card">
    <div class="card-title">Expected Output</div>
    <div style="text-align:center;padding:40px 20px;color:#888;background:#f9f9f9;border-radius:14px;">
        No output content defined in this render script.
    </div>
</div>

</div>

<footer>
    HL7 FHIR R5 – API Exchange for Medicinal Products (APIX)<br>
    Generated Render
</footer>

</body>
</html>
"""

    # Process Documents
    inputs = data.get('input', [])
    modules = categorize_docs(inputs)
    
    docs_html = ""
    for mod_name, items in modules.items():
        if not items:
            continue
            
        docs_html += f'<div class="module"><h3>{mod_name}</h3>'
        for item in items:
            docs_html += f"""
            <div class="doc-item">
                <div class="doc-type">{item['display'] or item['code']}</div>
                <span class="doc-code">{item['code']}</span><br>
                {item['title']}
            </div>
            """
        docs_html += "</div>"
        
    # Populate Template
    html_content = html_template.format(
        task_title=task_type_display,
        task_id=task_id,
        status=status,
        priority=priority,
        task_type_display=task_type_display,
        task_type_code=task_type_code,
        authored_on=format_date(authored_on),
        last_modified=format_date(last_modified),
        requester_name=requester.get('name', 'Unknown') if requester else 'Unknown',
        requester_address=get_address_html(requester),
        requester_contact=get_contact_html(requester),
        performer_name=performer.get('name', 'Unknown') if performer else 'Unknown',
        performer_address=get_address_html(performer),
        performer_contact=get_contact_html(performer),
        doc_count=len(inputs),
        input_docs_html=docs_html
    )
    
    with open(OUTPUT_FILE, 'w') as f:
        f.write(html_content)
    
    print(f"Successfully generated {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
