import re
import glob

def fix_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Fix schema relative URLs
    html = html.replace('"../assets/self-storage-india-logo.webp"', '"https://selfstorageindia.com/assets/self-storage-india-logo.webp"')
    html = html.replace('"assets/self-storage-india-logo.webp"', '"https://selfstorageindia.com/assets/self-storage-india-logo.webp"')

    # 2. Fix malformed ALT tags (strip <a href="..."> and </a> from within alt="..."
    # We need a function to clean the alt content
    def clean_alt(match):
        full_tag = match.group(0)
        alt_content = match.group(1)
        # Strip all HTML tags from the alt string
        cleaned_alt = re.sub(r'<[^>]+>', '', alt_content)
        return full_tag.replace(alt_content, cleaned_alt)

    html = re.sub(r'alt="([^"]*<a[^"]*)"', clean_alt, html)

    # 3. Add titles to images that have alt but no title
    def add_title(match):
        img_tag = match.group(0)
        if 'title=' not in img_tag:
            alt_match = re.search(r'alt="([^"]+)"', img_tag)
            if alt_match:
                alt_text = alt_match.group(1)
                return img_tag.replace('alt="', f'title="{alt_text}" alt="')
        return img_tag

    html = re.sub(r'<img[^>]+>', add_title, html)
    
    # Bump cache
    html = re.sub(r'href="(\.\./)?styles\.min\.css\?v=[0-9.]+"', r'href="\1styles.min.css?v=8.2"', html)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Fixed SEO issues in {filepath}")

# Fix all HTML files
for file in glob.glob("**/*.html", recursive=True):
    fix_file(file)

