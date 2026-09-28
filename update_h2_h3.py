import re

with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace H2 properties globally
old_h2_clamp = "clamp(1.3rem, 2vw, 1.7rem)"
new_h2_clamp = "clamp(1.2rem, 2vw, 1.6rem)"

# 1. Update font-size
css = css.replace(old_h2_clamp, new_h2_clamp)

# 2. Update weight, letter-spacing, and line-height for h2 globally
# The base h2 block looks like this:
"""
h2 {
    font-family: var(--font-heading);
    font-weight: 600;
    font-size: clamp(1.2rem, 2vw, 1.6rem);
    line-height: 1.2;
    letter-spacing: -0.02em;
    color: var(--text);
}
"""
css = re.sub(
    r'(h2\s*\{[^}]*?font-weight:\s*)600([^}]*?line-height:\s*)1\.2([^}]*?letter-spacing:\s*)-0\.02em',
    r'\g<1>500\g<2>1.18\g<3>-0.01em',
    css
)

# 3. Update the mobile override block to ensure weight/spacing/line-height matches if intended
# The mobile block currently has font-weight 600, letter-spacing -0.02em, line-height 1.2
css = re.sub(
    r'(margin-bottom:\s*8px\s*!important;\s*font-weight:\s*)600(\s*!important;\s*\})',
    r'\g<1>500\g<2>',
    css
)
css = re.sub(
    r'(line-height:\s*)1\.2(\s*!important;)',
    r'\g<1>1.18\g<2>',
    css
)
css = re.sub(
    r'(letter-spacing:\s*)-0\.02em(\s*!important;)',
    r'\g<1>-0.01em\g<2>',
    css
)

# 4. Update base H3 properties
# The base h3 block looks like this:
"""
h3 {
    font-family: var(--font-heading);
    font-weight: 600;
    font-size: 1.15rem;
    line-height: 1.3;
    letter-spacing: -0.01em;
    color: var(--text);
}
"""
css = re.sub(
    r'(h3\s*\{[^}]*?font-weight:\s*)600([^}]*?line-height:\s*)1\.3([^}]*?letter-spacing:\s*)-0\.01em',
    r'\g<1>500\g<2>1.18\g<3>-0.01em',
    css
)

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("H2 and H3 updated.")
