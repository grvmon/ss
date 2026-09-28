with open("assets/css/storage-calculator.css", "r", encoding="utf-8") as f:
    css = f.read()

# Remove white-space: nowrap from .result-details li
import re
css = re.sub(r'(\.result-details\s*li\s*\{[^}]*)white-space:\s*nowrap;', r'\1', css)

# Or maybe just replace all instances of white-space: nowrap inside that specific block if my regex fails?
# Let's just find exactly the blocks
css = css.replace("  white-space: nowrap;\n}\n\n.result-details li .check-icon", "\n}\n\n.result-details li .check-icon")
css = css.replace("  white-space: nowrap;\n}", "}\n")

# Re-enable the calc-visual-column on mobile that I hid previously
css = css.replace("display: none !important;", "position: relative; top: 0;")

with open("assets/css/storage-calculator.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Patched css")
