with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Final clean state: html=#F8FAFC, body=white, html+body share just resets
old = """html {
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
    background-color: #F8FAFC;
    color: var(--text);
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
    overflow-x: hidden;
}"""

new = """html {
    margin: 0;
    padding: 0;
    width: 100%;
    background-color: #F8FAFC;
    overflow-x: hidden;
}

body {
    margin: 0;
    padding: 0;
    width: 100%;
    background-color: #FFFFFF;
    font-family: var(--font-body);
    color: var(--text);
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
    overflow-x: hidden;
}"""

css = css.replace(old, new)

with open("styles.css", "w") as f:
    f.write(css)
print("Clean HTML/body rules applied")
