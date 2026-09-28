with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Make html and body explicitly 100% width with no margin/padding
# Also make navbar background match the hero gradient color so no contrast line visible
old = "html, body {\n    margin: 0;\n    padding: 0;\n    overflow-x: hidden !important;"
new = "html, body {\n    margin: 0;\n    padding: 0;\n    width: 100%;\n    overflow-x: hidden !important;"
css = css.replace(old, new, 1)

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)
print("Done")
