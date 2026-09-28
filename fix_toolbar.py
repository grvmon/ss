import re

with open("assets/css/storage-calculator.css", "r", encoding="utf-8") as f:
    css = f.read()

# Make calc-preset-bar stretch
if "flex: 1;" not in css and "calc-preset-bar {" in css:
    css = re.sub(r'(\.calc-preset-bar\s*\{[^}]*?)(?=\})', r'\1  flex: 1;\n', css)

# Push .btn-reset to the right
if "margin-left: auto;" not in css and ".btn-reset {" in css:
    css = re.sub(r'(\.btn-reset\s*\{[^}]*?)(?=\})', r'\1  margin-left: auto;\n', css)
elif ".btn-reset {" not in css:
    css += "\n.calc-preset-pill.btn-reset {\n  margin-left: auto;\n}\n"

with open("assets/css/storage-calculator.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Fixed toolbar layout in storage-calculator.css")
