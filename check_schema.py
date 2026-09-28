import json
import re

with open("business-storage/index.html", "r", encoding="utf-8") as f:
    html = f.read()

for match in re.finditer(r'<script\s+type="application/ld\+json">([\s\S]*?)</script>', html):
    try:
        data = json.loads(match.group(1))
        print(f"Valid Schema: {data.get('@type')}")
        if data.get('@type') == 'Service':
             print(json.dumps(data, indent=2))
    except Exception as e:
        print(f"Error parsing schema: {e}")
