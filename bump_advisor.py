import os
import re

for root, _, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # bump storage-advisor.min.js version to v=5.2 just to be safe
            new_content = re.sub(r'storage-advisor\.min\.js\?v=5\.[0-9]+', 'storage-advisor.min.js?v=5.2', content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)

print("Bumped storage-advisor version.")
