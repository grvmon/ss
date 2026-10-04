import os
import re

SKIP_DIRS = {'.git', 'assets', 'node_modules'}

def add_geo_tags():
    files_modified = 0
    
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                original_content = content
                
                # 1. Change html lang
                content = re.sub(r'<html\s+lang=["\']en(-US)?["\']>', '<html lang="en-IN">', content, flags=re.IGNORECASE)
                
                # If it didn't have lang="en", try to just match <html>
                if '<html lang="en-IN">' not in content:
                    content = re.sub(r'<html>', '<html lang="en-IN">', content, flags=re.IGNORECASE)
                
                # 2. Check if we already added it
                if 'name="geo.region"' in content:
                    continue
                
                # 3. Extract canonical URL to use in hreflang
                canonical_match = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\']([^"\']+)["\']', content, re.IGNORECASE)
                if not canonical_match:
                    # fallback to generating it based on path if missing
                    rel_path = os.path.relpath(filepath, '.')
                    if rel_path == 'index.html':
                        canonical_url = "https://selfstorageindia.com/"
                    else:
                        clean_path = rel_path.replace('/index.html', '/').replace('index.html', '')
                        canonical_url = f"https://selfstorageindia.com/{clean_path}"
                else:
                    canonical_url = canonical_match.group(1)
                
                # 4. Construct the tags
                tags_to_inject = f"""
    <!-- Geo-Targeting & Regional SEO -->
    <link rel="alternate" hreflang="en-IN" href="{canonical_url}" />
    <link rel="alternate" hreflang="x-default" href="{canonical_url}" />
    <meta name="geo.region" content="IN-DL" />
    <meta name="geo.placename" content="Delhi NCR" />
"""
                # Insert right before </head>
                content = re.sub(r'</head>', f'{tags_to_inject}</head>', content, flags=re.IGNORECASE)
                
                if content != original_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    files_modified += 1
                    
    print(f"Successfully added Geo-SEO tags to {files_modified} HTML files.")

if __name__ == '__main__':
    add_geo_tags()
