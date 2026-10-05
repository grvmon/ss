import os
import re
import glob

button_pattern = re.compile(r'<button class="btn btn-primary"[^>]*>Talk to an Advisor</button>\s*')

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content, num_subs = button_pattern.subn('', content)
    
    if num_subs > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Modified {filepath} ({num_subs} replacements)")

for root, _, files in os.walk('.'):
    for file in files:
        if file.endswith('.html') or file.endswith('.txt'):
            process_file(os.path.join(root, file))
