with open('styles.css', 'r') as f:
    content = f.read()

content = content.replace("""    .phone-link span {
        display: none;
        font-size: 1.2rem;
        color: var(--primary);
    }""", """    .phone-link span {
        font-size: 22px;
        color: #ffffff;
        margin: 0;
    }""")

content = content.replace("""    .phone-link span {
        display: flex;
        align-items: center;
        justify-content: center;
        line-height: 0;
        font-size: 22px;
        color: #ffffff;
        margin: 0;
    }""", """    .phone-link span {
        font-size: 22px;
        color: #ffffff;
        margin: 0;
    }""")

with open('styles.css', 'w') as f:
    f.write(content)

with open('styles.min.css', 'r') as f:
    min_content = f.read()

import re
min_content = re.sub(r'\.phone-link span\{display:none;font-size: 1\.2rem; color: var\(--primary\);\}', r'.phone-link span{font-size: 22px; color: #ffffff; margin: 0;}', min_content)
min_content = re.sub(r'\.phone-link span\{display: flex; align-items: center; justify-content: center; line-height: 0; font-size: 22px; color: #ffffff; margin: 0;\}', r'.phone-link span{font-size: 22px; color: #ffffff; margin: 0;}', min_content)

with open('styles.min.css', 'w') as f:
    f.write(min_content)

print("Fixed phone-link span.")
