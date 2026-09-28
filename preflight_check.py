import os, glob, re
from collections import defaultdict

html_files = glob.glob("**/*.html", recursive=True)

broken_links = defaultdict(list)
bad_canonicals = []
missing_canonicals = []
multiple_h1s = []
zero_h1s = []
missing_meta_desc = []
http_links = []

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Canonical Check
    canonical = re.search(r'<link[^>]*rel="canonical"[^>]*href="([^"]*)"', content, re.IGNORECASE)
    if canonical:
        url = canonical.group(1)
        if not url.startswith("https://selfstorageindia.com"):
            bad_canonicals.append((filepath, url))
    else:
        missing_canonicals.append(filepath)

    # 2. H1 Check
    h1s = re.findall(r'<h1[^>]*>.*?</h1>', content, re.IGNORECASE | re.DOTALL)
    if len(h1s) == 0:
        zero_h1s.append(filepath)
    elif len(h1s) > 1:
        multiple_h1s.append(filepath)

    # 3. Meta Description Check
    desc = re.search(r'<meta[^>]*name="description"[^>]*content="([^"]*)"', content, re.IGNORECASE)
    if not desc or not desc.group(1).strip():
        missing_meta_desc.append(filepath)

    # 4. Insecure HTTP links Check (Should be HTTPS)
    insecure = re.findall(r'(?:href|src)="http://([^"]+)"', content, re.IGNORECASE)
    for link in insecure:
        if "w3.org" not in link and "schema.org" not in link:
            http_links.append((filepath, "http://" + link))

    # 5. Internal Link & Asset Resolution Check
    links = re.findall(r'(?:href|src)="([^"]+)"', content, re.IGNORECASE)
    dir_path = os.path.dirname(filepath)
    
    for link in links:
        if link.startswith(('http://', 'https://', 'mailto:', 'tel:', 'javascript:', '#', 'data:')):
            continue
            
        clean_link = link.split('?')[0].split('#')[0]
        if not clean_link:
            continue

        # Handle root-relative vs document-relative
        if clean_link.startswith('/'):
            target_path = os.path.join(".", clean_link.lstrip('/'))
        else:
            target_path = os.path.normpath(os.path.join(dir_path, clean_link))

        # Verification logic
        exists = False
        if os.path.exists(target_path):
            exists = True
        elif os.path.isdir(target_path) and os.path.exists(os.path.join(target_path, 'index.html')):
            exists = True
        elif os.path.exists(target_path.rstrip('/') + '.html'):
             # fallback if someone linked to /about instead of /about.html without a directory
             exists = True
        elif os.path.isdir(target_path.rstrip('/')):
             # directory exists
             exists = True

        if not exists:
            broken_links[link].append(filepath)

print("=== PRE-FLIGHT QC REPORT ===")
print(f"Total HTML files scanned: {len(html_files)}")
print(f"Zero H1s: {len(zero_h1s)} files")
print(f"Multiple H1s: {len(multiple_h1s)} files")
print(f"Missing Meta Desc: {len(missing_meta_desc)} files")
print(f"Missing Canonicals: {len(missing_canonicals)} files")
print(f"Bad Canonicals (not selfstorageindia.com): {len(bad_canonicals)} files")
print(f"Insecure HTTP links: {len(http_links)}")

print("\n--- BROKEN INTERNAL LINKS & ASSETS ---")
broken_count = 0
for link, files in broken_links.items():
    broken_count += 1
    if broken_count <= 15:
        print(f"Broken Link: '{link}' found in {len(files)} files (e.g., {files[0]})")

if broken_count > 15:
    print(f"...and {broken_count - 15} more unique broken links.")
elif broken_count == 0:
    print("Zero broken internal links found! Excellent.")

