import os, re
count = 0
for root, _, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new = re.sub(r'styles\.min\.css\?v=[0-9\.]+', 'styles.min.css?v=10.6', content)
            new = re.sub(r'styles\.css\?v=[0-9\.]+', 'styles.css?v=10.6', new)
            new = re.sub(r'lead-form\.min\.js\?v=[0-9\.]+', 'lead-form.min.js?v=5.4', new)
            new = re.sub(r'storage-advisor\.min\.js\?v=[0-9\.]+', 'storage-advisor.min.js?v=5.4', new)
            new += "\n<!-- Cache Bust 28 -->"
            
            if new != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new)
                count += 1
print(f"Bumped cache on {count} files")
