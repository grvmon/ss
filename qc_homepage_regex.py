import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("--- SEO TAGS ---")
title = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
desc = re.search(r'<meta[^>]*name="description"[^>]*content="([^"]*)"', html, re.IGNORECASE)
canon = re.search(r'<link[^>]*rel="canonical"[^>]*href="([^"]*)"', html, re.IGNORECASE)
print(f"Title: {title.group(1) if title else 'MISSING'}")
print(f"Meta Desc: {desc.group(1) if desc else 'MISSING'}")
print(f"Canonical: {canon.group(1) if canon else 'MISSING'}")
schemas = len(re.findall(r'<script[^>]*type="application/ld\+json"', html, re.IGNORECASE))
print(f"Schemas Found: {schemas}")

print("\n--- HEADINGS ---")
h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.IGNORECASE | re.DOTALL)
print(f"H1 Count: {len(h1s)} (Should be exactly 1)")
for h1 in h1s:
    print(f" - H1: {re.sub(r'<[^>]+>', '', h1).strip()}")

h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', html, re.IGNORECASE | re.DOTALL)
print(f"H2 Count: {len(h2s)}")

print("\n--- IMAGES (ALT & TITLE TAGS) ---")
images = re.findall(r'<img\s+([^>]+)>', html, re.IGNORECASE)
missing_alt = 0
missing_title = 0
for img in images:
    if 'alt="' not in img:
        missing_alt += 1
        print(f"Missing alt: {img}")
    if 'title="' not in img:
        missing_title += 1

print(f"Total Images: {len(images)}")
print(f"Images missing ALT: {missing_alt}")
print(f"Images missing TITLE: {missing_title}")

