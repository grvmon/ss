import re

# 1. Add 'page-home' to body in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<body class="light-theme preload">', '<body class="light-theme preload page-home">')

# 2. Add the CTA button back to nav-actions
btn_html = """
                <button class="btn btn-primary" onclick="openLeadModal('Header CTA')" aria-label="Talk to an Advisor">Talk to an Advisor</button>"""

# Insert right before the mobile-nav-toggle
content = content.replace('                <button class="mobile-nav-toggle"', btn_html + '\n                <button class="mobile-nav-toggle"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("index.html updated (added page-home and btn)")

# 3. Add CSS to hide the button on mobile for .page-home
css_append = """
@media (max-width: 1024px) {
    .page-home .nav-actions .btn-primary {
        display: none !important;
    }
}
@media (max-width: 768px) {
    .page-home .nav-actions .btn-primary {
        display: none !important;
    }
}
"""

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write(css_append)

with open('styles.min.css', 'a', encoding='utf-8') as f:
    f.write(css_append)
    
print("CSS updated.")
