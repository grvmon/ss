import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Change SEO title
html = re.sub(r"<title>.*?</title>", "<title>Secure Self Storage Solutions in Delhi NCR | Self Storage India</title>", html, count=1)

# 2. Meta description uniqueness - just ensure it's there.
# Let's check if it exists.
if 'name="description"' in html:
    html = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="Rent secure private self-storage rooms in Delhi, Gurugram & Noida with 24/7 CCTV security, partner transport support & flexible monthly storage plans.">', html, count=1)

# 3. Keep only one H1. Let's find all h1s.
h1_count = len(re.findall(r"<h1", html, flags=re.IGNORECASE))
if h1_count > 1:
    # Demote subsequent H1s to H2s
    parts = html.split('<h1')
    new_html = parts[0] + '<h1' + parts[1]
    for i in range(2, len(parts)):
        new_html += '<h2' + parts[i].replace('</h1>', '</h2>', 1)
    html = new_html

# 4. Links fixes
# Delhi
html = html.replace('href="/self-storage-in-delhi/"', 'href="/self-storage-delhi/"')
# Gurugram
html = html.replace('href="/self-storage-in-gurugram/"', 'href="/self-storage-gurugram/"')
# Noida
html = html.replace('href="/self-storage-in-noida/"', 'href="/self-storage-noida/"')

# Dedicated Locations page link in footer
html = html.replace('href="#locations">Locations', 'href="/locations/">Locations')

# Contact Us clickable -> change from modal to actual URL if they meant that, but let's just make sure it points to /contact-us/
# Actually I'll leave the modal but also provide a fallback href
html = html.replace('href="javascript:void(0)" onclick="openQuoteModal(\'Footer Contact Us\')">Contact Us</a>', 'href="/contact-us/" onclick="openQuoteModal(\'Footer Contact Us\'); return false;">Contact Us</a>')

# Remove staging robots / meta indexing.
# Insert noindex if it doesn't exist
if 'name="robots" content="noindex' not in html:
    html = html.replace('<meta name="robots" content="index, follow', '<meta name="robots" content="noindex, nofollow')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print(f"H1 count was {h1_count}. HTML updated.")
