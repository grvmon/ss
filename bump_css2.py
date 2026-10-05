import os
import re

for root, _, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = re.sub(r'styles\.min\.css\?v=[0-9\.]+', 'styles.min.css?v=10.2', content)
            new_content = re.sub(r'styles\.css\?v=[0-9\.]+', 'styles.css?v=10.2', new_content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)

print("Bumped CSS cache to v=10.2")
