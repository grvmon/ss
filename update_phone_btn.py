import re

with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace the mobile phone-link styles
old_mobile = """    .phone-link {
        font-size: 0;
        width: 40px;
        height: 40px;
        border-radius: var(--radius-sm, 8px);
        background: transparent;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
    }
    .phone-link span {
        font-size: 26px;
        color: var(--primary);
        margin: 0;
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
        flex-shrink: 0;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .phone-link span {
        font-size: 22px;
        color: #ffffff;
        margin: 0;
    }
    .phone-link:active {
        transform: scale(0.95);
    }"""

css = css.replace(old_mobile, new_mobile)

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Updated phone link CSS.")
