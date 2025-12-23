import json
import os
import sys
import shutil
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

def get_all_task_docs():
    """Scans all JSON tasks in the examples directory to build a logical document history."""
    examples_dir = '/Users/a001/Documents/GitHub/APIX---API-Exchange-for-Medicinal-Products/input/examples'
    all_docs = []
    for filename in os.listdir(examples_dir):
        if filename.endswith('.json'):
            path = os.path.join(examples_dir, filename)
            try:
                data = load_json(path)
                if data.get('resourceType') == 'Task':
                    # Extract all DocumentReferences (contained or linked)
                    for res in data.get('contained', []):
                        if res.get('resourceType') == 'DocumentReference':
                            res['_source_task'] = data.get('id', 'Unknown')
                            res['_source_date'] = data.get('lastModified', '')
                            all_docs.append(res)
            except:
                continue
    return all_docs

def generate_dossier_rows(current_docs, all_history):
    if not current_docs:
        return '<tr><td colspan="4" style="text-align:center; padding:20px;">No documents found.</td></tr>'
    
    # Group history by Doc Type Code for the sidebar simulation
    history_by_type = {}
    for doc in all_history:
        code = doc.get('type', {}).get('coding', [{}])[0].get('code', 'unknown')
        if code not in history_by_type:
            history_by_type[code] = []
        history_by_type[code].append(doc)
    
    # Sort history items by date/version descending
    for code in history_by_type:
        history_by_type[code].sort(key=lambda x: (x.get('version', '0'), x.get('_source_date', '')), reverse=True)

    html = ""
    for doc in current_docs:
        doc_type_coding = doc.get('type', {}).get('coding', [{}])[0]
        category_coding = (doc.get('category') or [{}])[0].get('coding', [{}])[0]
        
        module = category_coding.get('display', category_coding.get('code', 'Other'))
        code = doc_type_coding.get('code', 'unknown')
        doc_name = doc_type_coding.get('display', doc_type_coding.get('code', 'Untitled'))
        version = doc.get('version', '1.0')
        status = doc.get('status', 'current')
        
        status_color = "#10b981" if status == 'current' else "#64748b"
        
        # Build the history HTML for this specific doc to be injected via JS
        history_html = ""
        items = history_by_type.get(code, [doc])
        for item in items:
            iv = item.get('version', '1.0')
            idate = format_date(item.get('_source_date', ''))
            is_current = (iv == version)
            dot_color = "#6366f1" if is_current else "#cbd5e1"
            
            history_html += f"""
            <div class='timeline-item'>
                <div class='dot' style='background:{dot_color}'></div>
                <div class='time-label'>{idate} (VERSION {iv})</div>
                <div class='his-title'>{item.get('_source_task')}</div>
                <div class='his-meta'>ID: {item.get('id')} | Status: {item.get('status')}</div>
            </div>
            """
        
        # Escape single quotes in history_html for the JS call
        safe_history = history_html.replace("'", "\\'").replace("\n", "")
        
        html += f"""
        <tr onclick="updateSidebar('{doc_name}', '{safe_history}')">
            <td><span class="module-badge">{module}</span></td>
            <td><strong>{doc_name}</strong></td>
            <td>v{version}</td>
            <td style="color:{status_color}">{status.capitalize()}</td>
        </tr>
        """
    return html

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
    
    # Calculate Lifecycle History
    all_history = get_all_task_docs()
    dossier_rows = generate_dossier_rows(input_resources + output_resources, all_history)
    
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
        "{dossier_title}": f"Dossier Index: {task_id}",
        "{dossier_rows}": dossier_rows,
        "{lifecycle_sidebar_content}": "Select a row to view version history.",
        "{render_date}": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    html_content = html_template
    for key, val in replacements.items():
        html_content = html_content.replace(key, val)
    
    with open(instance_output_file, 'w') as f:
        f.write(html_content)
    
    print(f"Successfully generated {instance_output_file}")
    
    # Copy supporting JS for IG compatibility
    js_src = os.path.join(os.path.dirname(template_path), 'lifecycle.js')
    js_dest = os.path.join(os.path.dirname(instance_output_file), 'lifecycle.js')
    if os.path.exists(js_src):
        shutil.copy(js_src, js_dest)
        print(f"Copied {js_src} to {js_dest}")

if __name__ == "__main__":
    main()
