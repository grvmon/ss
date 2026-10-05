import os, datetime
timestamp = datetime.datetime.now().strftime("%a %b %d %H:%M:%S IST %Y")
count = 0
for root, _, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'a', encoding='utf-8') as f:
                f.write(f"\n<!-- Cache Bust 26: {timestamp} -->")
            count += 1
print(f"Flushed {count} files")
