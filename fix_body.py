import re

with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# We need to find the `html, body {` block and add margin: 0; padding: 0;
# Make sure we only replace the FIRST occurrence which is the main block
css = css.replace('html, body {\n    overflow-x: hidden !important;', 'html, body {\n    margin: 0;\n    padding: 0;\n    overflow-x: hidden !important;', 1)

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

