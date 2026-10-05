import os, re
count = 0
for root, _, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            new = re.sub(r'styles\.min\.css\?v=[0-9\.]+', 'styles.min.css?v=10.5', content)
            new = re.sub(r'styles\.css\?v=[0-9\.]+', 'styles.css?v=10.5', new)
            new += "\n<!-- Cache Bust 27 -->"
            if new != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new)
                count += 1
print(f"Bumped to v10.5 on {count} files")
