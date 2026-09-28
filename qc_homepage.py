import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

print("--- SEO TAGS ---")
title = soup.find('title')
print(f"Title: {title.string if title else 'MISSING'}")
desc = soup.find('meta', attrs={'name': 'description'})
print(f"Meta Desc: {desc['content'] if desc else 'MISSING'}")
canon = soup.find('link', attrs={'rel': 'canonical'})
print(f"Canonical: {canon['href'] if canon else 'MISSING'}")
og_title = soup.find('meta', attrs={'property': 'og:title'})
print(f"OG Title: {og_title['content'] if og_title else 'MISSING'}")
og_desc = soup.find('meta', attrs={'property': 'og:description'})
print(f"OG Desc: {og_desc['content'] if og_desc else 'MISSING'}")
schema = soup.find_all('script', attrs={'type': 'application/ld+json'})
print(f"Schemas Found: {len(schema)}")

print("\n--- HEADINGS ---")
h1s = soup.find_all('h1')
print(f"H1 Count: {len(h1s)} (Should be exactly 1)")
for h1 in h1s:
    print(f" - H1: {h1.text.strip()}")
h2s = soup.find_all('h2')
print(f"H2 Count: {len(h2s)}")
for i, h2 in enumerate(h2s[:5]):
    print(f" - H2: {h2.text.strip()}")
if len(h2s) > 5:
    print("   ...")

print("\n--- IMAGES (ALT & TITLE TAGS) ---")
images = soup.find_all('img')
missing_alt = []
missing_title = []
for img in images:
    src = img.get('src', 'unknown')
    alt = img.get('alt', '')
    title = img.get('title', '')
    if not alt:
        missing_alt.append(src)
    if not title:
        missing_title.append(src)
print(f"Total Images: {len(images)}")
print(f"Images missing ALT: {len(missing_alt)}")
for m in missing_alt:
    print(f" - {m}")
print(f"Images missing TITLE: {len(missing_title)}")

print("\n--- LAYOUT STRUCTURE ---")
# Check padding/width wrappers
sections = soup.find_all(class_=re.compile(r'(container|wrapper|layout)'))
print(f"Found {len(sections)} layout containers.")
classes_used = set()
for sec in sections:
    for cls in sec.get('class', []):
        if 'container' in cls or 'wrapper' in cls or 'layout' in cls:
            classes_used.add(cls)
print(f"Container classes in use: {', '.join(classes_used)}")

