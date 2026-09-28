import re

with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

h2_clamp = "clamp(1.3rem, 2vw, 1.7rem)"

# Fix all remaining H2 sizes
css = re.sub(r'(\.article-content h2\s*\{[^}]*?)font-size:\s*1\.35rem;', r'\g<1>font-size: ' + h2_clamp + ';', css)
css = re.sub(r'(\.ceo-story-card h2\s*\{[^}]*?)font-size:\s*1\.45rem;', r'\g<1>font-size: ' + h2_clamp + ';', css)
css = re.sub(r'(\.values-section-head h2\s*\{[^}]*?)font-size:\s*clamp\([^)]+\);', r'\g<1>font-size: ' + h2_clamp + ';', css)
css = re.sub(r'(\.advisor-modal-head h2\s*\{[^}]*?)font-size:\s*27px;', r'\g<1>font-size: ' + h2_clamp + ';', css)
css = re.sub(r'(\.ssi-noida-blog h2\.article-main-title\s*\{[^}]*?)font-size:\s*clamp\([^)]+\);', r'\g<1>font-size: ' + h2_clamp + ';', css)
css = re.sub(r'(\.ssi-noida-blog h2\.article-section-title\s*\{[^}]*?)font-size:\s*17px;', r'\g<1>font-size: ' + h2_clamp + ';', css)

# Fix corresponding paragraphs
css = re.sub(r'(\.ceo-story-card p\s*\{[^}]*?)font-size:\s*0\.95rem;', r'\g<1>font-size: 17px;', css)
css = re.sub(r'(\.values-section-head p\s*\{[^}]*?)font-size:\s*1rem;', r'\g<1>font-size: 17px;', css)
css = re.sub(r'(\.advisor-modal-head p\s*\{[^}]*?)font-size:\s*15px;', r'\g<1>font-size: 17px;', css)
css = re.sub(r'(\.ssi-noida-blog p\s*\{[^}]*?)font-size:\s*15px;', r'\g<1>font-size: 17px;', css)

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)
print("Outlier H2s and Ps fixed.")
