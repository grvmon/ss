with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Fix the broken selector
css = css.replace(".business-need__card-html, body {", ".business-need__card-body {")

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)
print("Fixed!")
