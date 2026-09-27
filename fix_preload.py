with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

preload_css = """
.preload * {
    -webkit-transition: none !important;
    -moz-transition: none !important;
    -ms-transition: none !important;
    -o-transition: none !important;
    transition: none !important;
}
"""

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(preload_css + css)
print("Added preload CSS.")
