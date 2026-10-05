import re

with open('store/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add phone-link back to nav-actions in store/index.html
phone_html = """<a href="tel:+919090206090" class="phone-link"><span class="material-symbols-rounded">call</span>+91-9090206090</a>
                """

if '<a href="tel:+919090206090" class="phone-link">' not in content.split('<div class="nav-actions">')[1]:
    pattern = re.compile(r'(<div class="nav-actions">\s*)')
    new_content = pattern.sub(r'\1' + phone_html, content, count=1)
    with open('store/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Added phone-link to store/index.html")
else:
    print("phone-link already in store/index.html")
