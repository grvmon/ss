import re

with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# I will append new styles to the end to ensure they override earlier ones.
new_styles = """
/* Fix for Editorial Headings Accent Colors */
.ncr-blog-layout h2 {
    color: var(--text) !important;
}
.ncr-blog-layout h2 .accent-word {
    color: var(--primary) !important;
}
"""

with open("styles.css", "a", encoding="utf-8") as f:
    f.write(new_styles)

print("Patched headings.")
