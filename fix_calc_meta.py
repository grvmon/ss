import re

with open("self-storage-calculator/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Update canonical and OG URLs
html = html.replace('href="https://selfstorageindia.com/storage-calculator"', 'href="https://selfstorageindia.com/self-storage-calculator/"')
html = html.replace('content="https://selfstorageindia.com/storage-calculator"', 'content="https://selfstorageindia.com/self-storage-calculator/"')

# Cache bust
html = re.sub(r'href="\.\./styles\.css\?v=[0-9.]+"', r'href="../styles.css?v=3.8"', html)
html = re.sub(r'href="\.\./assets/css/storage-calculator\.css\?v=[0-9.]+"', r'href="../assets/css/storage-calculator.css?v=1.8"', html)

with open("self-storage-calculator/index.html", "w", encoding="utf-8") as f:
    f.write(html)

