import glob

# The replacement block
old_html = '<span class="mobile-drawer-title">Menu</span>'
new_html = '<img src="https://selfstorageindia.com/wp-content/uploads/2025/07/Self-Storage-India-Logo.png" alt="Self Storage India Logo" style="height: 32px; width: auto; object-fit: contain;">'

count = 0
for filepath in glob.glob("**/*.html", recursive=True):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    if old_html in content:
        content = content.replace(old_html, new_html)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        count += 1

print(f"Replaced in {count} files.")
