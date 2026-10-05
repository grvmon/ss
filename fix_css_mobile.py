with open('styles.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Revert the global .nav-actions .phone-link hiding in styles.css
content = content.replace("    /* Hide phone-link circular icon in header on mobile — floating call btn handles calls */\n    .nav-actions .phone-link {\n        display: none !important;\n    }", "")
content = content.replace("    /* Hide phone-link in header on mobile — floating btn handles it */\n    .nav-actions .phone-link {\n        display: none !important;\n    }", "")

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(content)

with open('styles.min.css', 'r', encoding='utf-8') as f:
    min_content = f.read()

# Replace global hidden phone-link with page-store specific
min_content = min_content.replace(".nav-actions .phone-link { display: none !important; }", "")

with open('styles.min.css', 'w', encoding='utf-8') as f:
    f.write(min_content)

print("Restored phone-link globally on mobile, relying on .page-store specific hiding.")
