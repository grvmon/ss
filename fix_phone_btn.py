import re

with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

old_mobile = """    .phone-link {
        font-size: 0;
        width: 42px;
        height: 42px;
        border-radius: 50%;
        background: var(--primary);
        box-shadow: 0 4px 12px rgba(24, 108, 236, 0.25);
        display: inline-flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }"""

new_mobile = """    .phone-link {
        font-size: 0;
        width: 42px;
        height: 42px;
        border-radius: 50%;
        background: var(--primary);
        box-shadow: 0 4px 12px rgba(24, 108, 236, 0.25);
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 0;
        padding: 0;
        flex-shrink: 0;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }"""

css = css.replace(old_mobile, new_mobile)

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Fixed gap on mobile phone btn.")
