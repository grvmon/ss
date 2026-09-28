import re
import json

with open("business-storage/index.html", "r", encoding="utf-8") as f:
    html = f.read()

print("## SEO & Meta Tags")
title = re.search(r'<title>(.*?)</title>', html)
print(f"- **Title:** {title.group(1) if title else 'MISSING'}")

desc = re.search(r'<meta[^>]*name="description"[^>]*content="([^"]*)"', html)
print(f"- **Description:** {desc.group(1) if desc else 'MISSING'}")

canon = re.search(r'<link[^>]*rel="canonical"[^>]*href="([^"]*)"', html)
print(f"- **Canonical URL:** {canon.group(1) if canon else 'MISSING'}")

print("\n## Headings Structure")
for match in re.finditer(r'<h([1-6])[^>]*>(.*?)</h\1>', html, re.DOTALL):
    level = match.group(1)
    text = re.sub(r'<[^>]+>', '', match.group(2)).strip()
    text = " ".join(text.split()) # Replace newlines/multiple spaces
    print(f"- **H{level}:** {text}")

print("\n## Images (Alt & Title Tags)")
for match in re.finditer(r'<img\s+([^>]+)>', html):
    attrs = match.group(1)
    src_match = re.search(r'src="([^"]*)"', attrs)
    alt_match = re.search(r'alt="([^"]*)"', attrs)
    title_match = re.search(r'title="([^"]*)"', attrs)
    
    src = src_match.group(1) if src_match else 'MISSING SRC'
    alt = alt_match.group(1) if alt_match else 'MISSING ALT'
    title = title_match.group(1) if title_match else 'MISSING TITLE'
    
    print(f"- **Image:** {src}")
    print(f"  - Alt: {alt}")
    print(f"  - Title: {title}")

print("\n## JSON-LD Schema")
for match in re.finditer(r'<script\s+type="application/ld\+json">([\s\S]*?)</script>', html):
    try:
        data = json.loads(match.group(1))
        print(f"- Found Schema: {data.get('@type', 'Unknown Type')}")
        if 'logo' in data:
            print(f"  - Logo URL: {data['logo']}")
    except:
        print("- Found Schema, but invalid JSON format")
