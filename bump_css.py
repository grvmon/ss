import os
import glob
import re

for root, _, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = content.replace("styles.min.css?v=10.0", "styles.min.css?v=10.1")
            new_content = new_content.replace("styles.css?v=10.0", "styles.css?v=10.1")
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)

print("Bumped CSS version.")
