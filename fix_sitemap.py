with open("sitemap.xml", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("<loc>https://selfstorageindia.com/storage-calculator</loc>", "<loc>https://selfstorageindia.com/self-storage-calculator/</loc>")

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(text)

print("Fixed sitemap.")
