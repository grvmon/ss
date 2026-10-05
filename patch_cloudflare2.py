import os
import re

js_files = ['lead-form.min.js', 'lead-form.js', 'storage-advisor.js', 'storage-advisor.min.js', 'app.js', 'app.min.js']
for file in js_files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = re.sub(r'[A-Za-z0-9_]+\.append\([\"\']xnQsjsdp[\"\'][^)]*\)[,;]?', '', content)
        content = re.sub(r'[A-Za-z0-9_]+\.append\([\"\']xmIwtLD[\"\'][^)]*\)[,;]?', '', content)
        content = re.sub(r'[A-Za-z0-9_]+\.append\([\"\']actionType[\"\'][^)]*\)[,;]?', '', content)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
