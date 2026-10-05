with open('styles.css', 'r', encoding='utf-8') as f:
    content = f.read()

old = """.phone-link span {
    display: inline-flex;
    align-items: center;
    font-size: 1.2rem;
    color: var(--text-secondary); /* Same color as the text */
}"""

new = """.phone-link span {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background: var(--primary);
    box-shadow: 0 4px 12px rgba(24, 108, 236, 0.25);
    font-size: 20px;
    color: #ffffff;
    flex-shrink: 0;
}"""

if old in content:
    with open('styles.css', 'w', encoding='utf-8') as f:
        f.write(content.replace(old, new))
    print("styles.css desktop icon patched")
else:
    print("NOT FOUND")

# Append desktop override to minified CSS
append = """
@media (min-width: 769px) {
    .phone-link span {
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        width: 36px !important;
        height: 36px !important;
        border-radius: 50% !important;
        background: var(--primary) !important;
        box-shadow: 0 4px 12px rgba(24,108,236,0.25) !important;
        font-size: 20px !important;
        color: #ffffff !important;
        flex-shrink: 0 !important;
    }
}
"""
with open('styles.min.css', 'a', encoding='utf-8') as f:
    f.write(append)
print("styles.min.css appended")
