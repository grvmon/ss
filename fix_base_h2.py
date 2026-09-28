with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Enforce base h2 rule to exactly match FAQ section standard
old = """h2 {
    font-family: var(--font-heading);
    font-weight: 600;
    font-size: clamp(1.3rem, 2vw, 1.7rem);
    line-height: 1.25;
    letter-spacing: -0.01em;
    color: var(--text);
}"""

new = """h2 {
    font-family: var(--font-heading);
    font-weight: 600;
    font-size: clamp(1.3rem, 2vw, 1.7rem);
    line-height: 1.2;
    letter-spacing: -0.02em;
    color: var(--text);
}"""

css = css.replace(old, new)

# Also fix the base h3 to use consistent sizing
old3 = """h3 {
    font-family: var(--font-heading);
    font-weight: 600;
    font-size: 1.35rem;
    line-height: 1.25;
    letter-spacing: -0.01em;
    color: var(--text);
}"""
new3 = """h3 {
    font-family: var(--font-heading);
    font-weight: 600;
    font-size: 1.15rem;
    line-height: 1.3;
    letter-spacing: -0.01em;
    color: var(--text);
}"""
css = css.replace(old3, new3)

with open("styles.css", "w") as f:
    f.write(css)
print("Base h2 and h3 standardized.")
