import re
with open('styles.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace flex-wrap: nowrap with flex-wrap: wrap for calc-banner-features
old_css = """    .calc-banner-features {
        flex-wrap: nowrap !important;"""
new_css = """    .calc-banner-features {
        flex-wrap: wrap !important;"""

if old_css in content:
    content = content.replace(old_css, new_css)
    with open('styles.css', 'w', encoding='utf-8') as f:
        f.write(content)
    print("styles.css fixed")
else:
    print("Could not find exact match in styles.css")

# Also need to fix in styles.min.css if it exists
with open('styles.min.css', 'r', encoding='utf-8') as f:
    min_content = f.read()

min_old = ".calc-banner-features{flex-wrap: nowrap !important;"
min_new = ".calc-banner-features{flex-wrap: wrap !important;"
if min_old in min_content:
    min_content = min_content.replace(min_old, min_new)
    with open('styles.min.css', 'w', encoding='utf-8') as f:
        f.write(min_content)
    print("styles.min.css fixed")
else:
    # try space variation
    min_content = min_content.replace("flex-wrap: nowrap !important", "flex-wrap: wrap !important")
    with open('styles.min.css', 'w', encoding='utf-8') as f:
        f.write(min_content)
    print("styles.min.css attempted replace all nowrap to wrap (will just do a regex)")
