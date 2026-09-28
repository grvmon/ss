with open(".htaccess", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("/storage-calculator", "/self-storage-calculator/")
text = text.replace("/self-storage-calculator//", "/self-storage-calculator/")

with open(".htaccess", "w", encoding="utf-8") as f:
    f.write(text)

print("Fixed htaccess.")
