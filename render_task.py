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
    if not ref_id or not isinstance(ref_id, str):
        return None
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
    if isinstance(addr, list) and len(addr) > 0:
        addr = addr[0]
        
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
        name_obj = c.get('name')
        name = "Contact"
        if isinstance(name_obj, dict):
            name = name_obj.get('text', 'Contact')
        elif isinstance(name_obj, str):
            name = name_obj
            
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
        
        if code.startswith('1') or code in ['cover-letter', 'application-form', 'invoice', 'proof-of-payment']:
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

def generate_docs_html(doc_resources):
    if not doc_resources:
        return '<div style="padding:20px; color:#6b7280; font-style:italic;">No documents in this section.</div>'
        
    modules = categorize_docs(doc_resources)
    html = ""
    for mod_name, items in modules.items():
        if not items:
            continue
            
        html += f'<div class="module-group"><div class="module-title">{mod_name}</div>'
        for item in items:
            size_str = ""
            if item.get('size'):
                if item['size'] >= 1024*1024*1024:
                    size_str = f" • {item['size'] / 1024 / 1024 / 1024:.2f} GB"
                else:
                    size_str = f" • {item['size'] / 1024 / 1024:.2f} MB"
            
            link_label = "View Document"
            if item.get('url'):
                link_label = "View External"
            
            url = item.get('url', '#')
            
            html += f"""
            <div class="doc-row">
                <div class="doc-info">
                    <div class="doc-icon">📄</div>
                    <div>
                        <div class="doc-name">{item['display'] or item['code']}</div>
                        <div class="doc-meta"><span style="font-family:monospace; background:#f1f5f9; padding:1px 4px; border-radius:4px;">{item['code']}</span>{size_str} • {item['title']}</div>
                    </div>
                </div>
                <a href="{url}" class="btn-view">{link_label}</a>
            </div>
            """
        html += "</div>"
    return html

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
    
    # Text Field (Description)
    task_description = data.get('text', {}).get('div', 'No description provided.')
    # Strip HTML tags from div if it's there
    if task_description.startswith('<div'):
        import re
        task_description = re.sub('<[^<]+?>', '', task_description)
    
    business_status_coding = data.get('businessStatus', {}).get('coding', [{}])[0]
    business_status = business_status_coding.get('display', business_status_coding.get('code', 'N/A'))
    
    task_coding = data.get('code', {}).get('coding', [{}])[0]
    task_type_display = task_coding.get('display', 'Task')
    task_type_code = task_coding.get('code', '')
    
    authored_on = data.get('authoredOn', '')
    last_modified = data.get('lastModified', authored_on)
    
    requester_ref = data.get('requester', {}).get('reference', '')
    requester = get_contained_resource(data, requester_ref)
    
    performer_ref = (data.get('owner', {}) or data.get('requesterPerformer', {})).get('reference', '')
    if not performer_ref and data.get('requestedPerformer'):
        req_perf = data.get('requestedPerformer')[0]
        if isinstance(req_perf, dict):
            performer_ref = req_perf.get('reference', {}).get('reference', '')
            
    performer = get_contained_resource(data, performer_ref)
    
    # Resolve Documents
    def resolve_refs(entries):
        resources = []
        for entry in entries:
            ref = entry.get('valueReference', {}).get('reference', '')
            if ref.startswith('#'):
                res = get_contained_resource(data, ref)
                if res:
                    resources.append(res)
        return resources

    input_resources = resolve_refs(data.get('input', []))
    output_resources = resolve_refs(data.get('output', []))
    
    input_docs_html = generate_docs_html(input_resources)
    output_docs_html = generate_docs_html(output_resources)
    
    html_template = None
    if template_path and os.path.exists(template_path):
        with open(template_path, 'r') as f:
            html_template = f.read()
    
    if not html_template:
        # Fallback to a basic internal template if external fails
        html_template = "<html><body><h1>{task_title}</h1>{input_docs_html}</body></html>"

    replacements = {
        "{task_title}": task_type_display,
        "{task_id}": task_id,
        "{status}": status,
        "{business_status}": business_status,
        "{priority}": priority,
        "{task_description}": task_description,
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
        "{doc_count}": str(len(input_resources) + len(output_resources)),
        "{input_docs_html}": input_docs_html,
        "{output_docs_html}": output_docs_html,
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
