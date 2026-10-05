import re
with open('styles.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace flex-wrap: nowrap with flex-wrap: wrap for loc-chips
old_css = """    flex-wrap: nowrap; /* Force all chips onto a single line */"""
new_css = """    flex-wrap: wrap; /* Allow wrapping on small screens */"""

if old_css in content:
    content = content.replace(old_css, new_css)
    with open('styles.css', 'w', encoding='utf-8') as f:
        f.write(content)
    print("styles.css fixed")
else:
    print("Could not find exact match in styles.css")

# Fix in styles.min.css
with open('styles.min.css', 'r', encoding='utf-8') as f:
    min_content = f.read()

min_old = ".loc-chips{display: flex; flex-wrap: nowrap;"
min_new = ".loc-chips{display: flex; flex-wrap: wrap;"

if min_old in min_content:
    min_content = min_content.replace(min_old, min_new)
    with open('styles.min.css', 'w', encoding='utf-8') as f:
        f.write(min_content)
    print("styles.min.css fixed")
else:
    min_content = min_content.replace("flex-wrap: nowrap;", "flex-wrap: wrap;")
    with open('styles.min.css', 'w', encoding='utf-8') as f:
        f.write(min_content)
    print("styles.min.css attempted blind replacement")
