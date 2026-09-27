import re

with open("household-goods-storage/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 4. Link size calculator
html = html.replace('size calculator', '<a href="/storage-calculator/">size calculator</a>')
# Ensure we didn't accidentally double-link
html = html.replace('href="/storage-calculator/">size calculator</a></a>', 'href="/storage-calculator/">size calculator</a>')
html = html.replace('<a href="/storage-calculator/"><a href="/storage-calculator/">', '<a href="/storage-calculator/">')

# 5, 6, 7. Link relocation, renovation, downsizing inside the household-need__cards
html = re.sub(
    r'(<h3 class="household-need__card-title">Relocation</h3>\s*<p class="household-need__card-desc">.*?)</p>',
    r'\1</p>\n                            <a href="/storage-during-relocation/" class="explore-link" style="margin-top: 12px; display: inline-flex; align-items: center; gap: 4px; color: var(--primary); font-weight: 600;">Learn More <span class="material-symbols-rounded" style="font-size: 1.2rem;">arrow_forward</span></a>',
    html, flags=re.DOTALL
)

html = re.sub(
    r'(<h3 class="household-need__card-title">Home Renovation</h3>\s*<p class="household-need__card-desc">.*?)</p>',
    r'\1</p>\n                            <a href="/storage-during-renovation/" class="explore-link" style="margin-top: 12px; display: inline-flex; align-items: center; gap: 4px; color: var(--primary); font-weight: 600;">Learn More <span class="material-symbols-rounded" style="font-size: 1.2rem;">arrow_forward</span></a>',
    html, flags=re.DOTALL
)

html = re.sub(
    r'(<h3 class="household-need__card-title">Downsizing</h3>\s*<p class="household-need__card-desc">.*?)</p>',
    r'\1</p>\n                            <a href="/storage-for-downsizing/" class="explore-link" style="margin-top: 12px; display: inline-flex; align-items: center; gap: 4px; color: var(--primary); font-weight: 600;">Learn More <span class="material-symbols-rounded" style="font-size: 1.2rem;">arrow_forward</span></a>',
    html, flags=re.DOTALL
)

# 8. Link Private Storage Rooms
# Find "private storage rooms" text and link it to /offering-private-rooms/
html = re.sub(r'(?i)\b(private lockable storage rooms)\b', r'<a href="/offering-private-rooms/">\1</a>', html)
html = re.sub(r'(?i)\b(private storage rooms)\b', r'<a href="/offering-private-rooms/">\1</a>', html)

# 9. Link Business Storage
html = re.sub(r'(?i)\b(business storage)\b', r'<a href="/business-storage/">\1</a>', html)
# Fix overlapping link issues (like in href="/business-storage/")
html = re.sub(r'href="<a href="/business-storage/">Business Storage</a>"', r'href="/business-storage/"', html)
html = re.sub(r'<a href="/business-storage/">business storage</a> units', r'<a href="/business-storage/">business storage</a> units', html)

with open("household-goods-storage/index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Links updated.")
