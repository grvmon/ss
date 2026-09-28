from bs4 import BeautifulSoup
import json

with open("household-goods-storage/index.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# Headings
print("=== HEADINGS ===")
headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
for h in headings:
    print(f"{h.name.upper()}: {h.get_text(strip=True)}")

# Images
print("\n=== IMAGES ===")
images = soup.find_all('img')
for img in images:
    src = img.get('src', '')
    alt = img.get('alt', 'MISSING')
    title = img.get('title', 'MISSING')
    print(f"IMG: {src} | ALT: {alt} | TITLE: {title}")

# Schema
print("\n=== SCHEMA ===")
schemas = soup.find_all('script', type='application/ld+json')
for s in schemas:
    try:
        data = json.loads(s.string)
        print(f"Schema Type: {data.get('@type', 'Unknown')}")
    except:
        print("Invalid JSON-LD")
