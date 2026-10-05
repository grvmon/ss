import os
import re
import glob

# 1. Update JS files
js_files = ['app.js', 'app.min.js', 'lead-form.js', 'lead-form.min.js', 'storage-advisor.js', 'storage-advisor.min.js']
old_url = 'https://crm.zoho.in/crm/WebToLeadForm'
new_url = 'https://zoho-lead-proxy.rajeev-c18.workers.dev/'

for file in js_files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace(old_url, new_url)
        
        # We also want to remove the token appending from the JS so it doesn't conflict with the worker.
        # But to be safe and avoid breaking minified syntax, we'll just let it send the old token.
        # Wait, if we send the old token, Zoho might fail. 
        # Let's replace the old token values with empty strings. 
        # But formData.append("xnQsjsdp", "") will still send an empty string. 
        # Let's remove the .append calls using regex.
        
        content = re.sub(r'formData\.append\([\"]xnQsjsdp[\"],[^)]*\);', '', content)
        content = re.sub(r'formData\.append\([\"]xmIwtLD[\"],[^)]*\);', '', content)
        content = re.sub(r'formData\.append\([\"]actionType[\"],[^)]*\);', '', content)
        content = re.sub(r'formData\.append\([\']xnQsjsdp[\'],[^)]*\);', '', content)
        content = re.sub(r'formData\.append\([\']xmIwtLD[\'],[^)]*\);', '', content)
        content = re.sub(r'formData\.append\([\']actionType[\'],[^)]*\);', '', content)
        
        # For lead-form.min.js which uses L.append
        content = re.sub(r'[A-Za-z0-9_]+\.append\([\"\']xnQsjsdp[\"\'],[^)]*\);', '', content)
        content = re.sub(r'[A-Za-z0-9_]+\.append\([\"\']xmIwtLD[\"\'],[^)]*\);', '', content)
        content = re.sub(r'[A-Za-z0-9_]+\.append\([\"\']actionType[\"\'],[^)]*\);', '', content)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Patched JS {file}")

# 2. Update HTML files
html_files = glob.glob('**/*.html', recursive=True)
for file in html_files:
    if 'node_modules' in file or '.git' in file: continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if old_url in content or 'xnQsjsdp' in content:
        content = content.replace(old_url, new_url)
        # Wipe the hidden inputs so bots see absolutely nothing in the DOM!
        content = re.sub(r'<input type="hidden" name="xnQsjsdp" value="[^"]*">', '', content)
        content = re.sub(r'<input type="hidden" name="xmIwtLD" value="[^"]*">', '', content)
        content = re.sub(r'<input type="hidden" name="actionType" value="[^"]*">', '', content)
        
        # also match without quotes or with single quotes just in case
        content = re.sub(r'<input[^>]*name=[\'\"]?xnQsjsdp[\'\"]?[^>]*>', '', content)
        content = re.sub(r'<input[^>]*name=[\'\"]?xmIwtLD[\'\"]?[^>]*>', '', content)
        content = re.sub(r'<input[^>]*name=[\'\"]?actionType[\'\"]?[^>]*>', '', content)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        # print(f"Patched HTML {file}")

print("HTML patching complete.")

