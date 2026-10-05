import os
import re
import glob

old_token1 = "f16e947a58c920d3d9bbb4b80e92c047ca04ed4d68bb240204297c44c42d8001"
new_token1 = "ecb154d42f1b846df0927acffa26e37579f01023755e425fa43cbe26ffa05991"

old_token2 = "e9726bf6b19e499bf582aa195c8e5d128958792568633ff8fe046537f9cb109d26d208f333e4ee6aef5c1bebc25b1097"
new_token2 = "db48556d6f91a0df06bd7556cda4884937ab3db875922c176ac957abfe8e85cd89d9f1a3ea0b7faeecd867a4e8700d06"

# 1. Update JS files
js_files = ['app.js', 'app.min.js', 'lead-form.js', 'lead-form.min.js', 'storage-advisor.js', 'storage-advisor.min.js']

for file in js_files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace(old_token1, new_token1)
        content = content.replace(old_token2, new_token2)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Patched JS {file}")

# 2. Update HTML files
html_files = glob.glob('**/*.html', recursive=True)
for file in html_files:
    if 'node_modules' in file or '.git' in file: continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Wipe the hidden inputs so bots see absolutely nothing in the DOM!
    content = re.sub(r'<input type="hidden" name="xnQsjsdp" value="[^"]*">', '', content)
    content = re.sub(r'<input type="hidden" name="xmIwtLD" value="[^"]*">', '', content)
    content = re.sub(r'<input type="hidden" name="actionType" value="[^"]*">', '', content)
    
    # also match without quotes or with single quotes just in case
    content = re.sub(r'<input[^>]*name=[\'\"]?xnQsjsdp[\'\"]?[^>]*>', '', content)
    content = re.sub(r'<input[^>]*name=[\'\"]?xmIwtLD[\'\"]?[^>]*>', '', content)
    content = re.sub(r'<input[^>]*name=[\'\"]?actionType[\'\"]?[^>]*>', '', content)
    
    # replace tokens just in case we missed any regex
    content = content.replace(old_token1, new_token1)
    content = content.replace(old_token2, new_token2)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("HTML patching complete.")

