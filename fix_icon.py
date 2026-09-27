with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

icon_fix = """
/* Prevent font-loading layout shift (jerk) for material symbols */
.material-symbols-rounded {
    display: inline-block;
    width: 24px;
    height: 24px;
    line-height: 24px;
    text-transform: none;
    letter-spacing: normal;
    word-wrap: normal;
    white-space: nowrap;
    direction: ltr;
    overflow: hidden;
    font-size: 24px;
}
"""

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(icon_fix + css)
print("Added icon anti-jerk CSS.")
