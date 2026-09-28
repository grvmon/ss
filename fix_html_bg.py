with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Remove the duplicate conflicting second html block (our earlier fix that gets overridden)
# and merge it properly into the first html block
old_second_html = """html {
    margin: 0;
    padding: 0;
    background-color: #F8FAFC;
}

html, body {
    margin: 0;
    padding: 0;
    width: 100%;
    overflow-x: hidden !important;
    font-family: var(--font-body);
    background-color: #FFFFFF;"""

new_html = """html {
    margin: 0;
    padding: 0;
    background-color: #F8FAFC;
}

body {
    margin: 0;
    padding: 0;
    width: 100%;
    background-color: #FFFFFF;
}

html, body {
    overflow-x: hidden !important;
    font-family: var(--font-body);
    background-color: #F8FAFC;"""

css = css.replace(old_second_html, new_html)

with open("styles.css", "w") as f:
    f.write(css)
print("Done")
