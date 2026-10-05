with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old = """<button class="btn btn-primary" onclick="openLeadModal('Header CTA')" aria-label="Talk to an Advisor">Talk to an Advisor</button>"""
new = """<button class="btn btn-primary" onclick="if (window.openAdvisorModal) { window.openAdvisorModal(); } else { openQuoteModal('Header Navigation'); }">Talk to an Advisor</button>"""

content = content.replace(old, new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Button click handler fixed.")
