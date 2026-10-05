with open('styles.css', 'r') as f:
    content = f.read()

search = """.phone-link span {
    display: none;
    font-size: 1.2rem;
    color: var(--primary);
}"""

replace = """.phone-link span {
    display: inline-block;
    font-size: 1.2rem;
    color: var(--primary);
}"""

if search in content:
    with open('styles.css', 'w') as f:
        f.write(content.replace(search, replace))
    print("styles.css patched")
else:
    print("Could not find search string in styles.css")
