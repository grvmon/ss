with open('styles.css', 'r') as f:
    content = f.read()

# Let's replace the base `.phone-link span` block
search = """.phone-link span {
    display: inline-block;
    font-size: 1.2rem;
    color: var(--primary);
}"""

replace = """.phone-link span {
    display: inline-flex;
    align-items: center;
    font-size: 1.2rem;
    color: var(--text-secondary); /* Same color as the text */
}"""

if search in content:
    with open('styles.css', 'w') as f:
        f.write(content.replace(search, replace))
    print("styles.css patched base span")
else:
    print("Base span not found")
