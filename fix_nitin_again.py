import re
import glob

def fix_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Exact replace for the currently broken Nitin tag
    broken = r'<img src="\.\./assets/client_nitin\.webp" title="Nitin Gupta - Verified  alt="Nitin Gupta - Verified Business Storage Customer Review Noida" class="profile-img" loading="lazy" width="200" height="200" decoding="async">'
    fixed = r'<img src="../assets/client_nitin.webp" title="Nitin Gupta - Verified Business Storage Customer Review Noida" alt="Nitin Gupta - Verified Business Storage Customer Review Noida" class="profile-img" loading="lazy" width="200" height="200" decoding="async">'
    
    html = re.sub(broken, fixed, html)
    
    # Check facility_1, etc just in case they are also missing quotes
    html = re.sub(r'title="([^"]*)"? alt=', r'title="\1" alt=', html)

    # Cache bust
    html = re.sub(r'href="(\.\./)?styles\.min\.css\?v=[0-9.]+"', r'href="\1styles.min.css?v=8.3"', html)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

for file in glob.glob("**/*.html", recursive=True):
    fix_file(file)

