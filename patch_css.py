import re

with open('styles.css', 'r') as f:
    css = f.read()

# Replace inline-flex with flex in .phone-link media query
css = css.replace("""    .phone-link {
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
    }""", """    .phone-link {
        font-size: 0;
        width: 42px;
        height: 42px;
        border-radius: 50%;
        background: var(--primary);
        box-shadow: 0 4px 12px rgba(24, 108, 236, 0.25);
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0;
        padding: 0;
        flex-shrink: 0;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }""")

css = css.replace("""    .phone-link span {
        font-size: 22px;
        color: #ffffff;
        margin: 0;
    }""", """    .phone-link span {
        font-size: 22px;
        color: #ffffff;
        margin: 0;
        line-height: 0;
        display: flex;
        align-items: center;
        justify-content: center;
    }""")

with open('styles.css', 'w') as f:
    f.write(css)

# Also update styles.min.css if needed, but since it's just a test, we can just replace minified version using regex.
import os
os.system('npx clean-css-cli -o styles.min.css styles.css')
