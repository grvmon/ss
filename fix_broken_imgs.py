import re
import glob

def fix_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # We need to target any img tag that has title="... <a href=" or alt="... <a href=" 
    # and just fix the whole string for the broken ones manually.
    
    # 1. Nitin
    broken_nitin = r'<img src="\.\./assets/client_nitin\.webp" title="Nitin Gupta - Verified <a href=" alt="Nitin Gupta - Verified <a href="/business-storage/">Business Storage</a> Customer Review Noida" class="profile-img" loading="lazy" width="200" height="200" decoding="async">'
    fixed_nitin = r'<img src="../assets/client_nitin.webp" title="Nitin Gupta - Verified Business Storage Customer Review Noida" alt="Nitin Gupta - Verified Business Storage Customer Review Noida" class="profile-img" loading="lazy" width="200" height="200" decoding="async">'
    
    html = html.replace(broken_nitin, fixed_nitin)
    
    # Also without title in case it missed it
    broken_nitin2 = r'<img src="\.\./assets/client_nitin\.webp" alt="Nitin Gupta - Verified <a href="/business-storage/">Business Storage</a> Customer Review Noida" class="profile-img" loading="lazy" width="200" height="200" decoding="async">'
    html = html.replace(broken_nitin2, fixed_nitin)
    
    # 2. facility_1
    broken_f1 = r'title="<a href=" alt="<a href="/offering-private-rooms/">Private lockable storage rooms</a> at Self Storage India Delhi"'
    fixed_f1 = r'title="Private lockable storage rooms at Self Storage India Delhi" alt="Private lockable storage rooms at Self Storage India Delhi"'
    html = html.replace(broken_f1, fixed_f1)
    
    # 3. facility_3
    broken_f3 = r'title="<a href=" alt="<a href="/offering-business-storage/">Business storage</a> facility corridors"'
    fixed_f3 = r'title="Business storage facility corridors" alt="Business storage facility corridors"'
    html = html.replace(broken_f3, fixed_f3)
    
    # 4. facility_4
    broken_f4 = r'title="pest-controlled <a href=" alt="pest-controlled <a href="/offering-luggage-storage/">luggage storage rooms</a> in NCR"'
    fixed_f4 = r'title="pest-controlled luggage storage rooms in NCR" alt="pest-controlled luggage storage rooms in NCR"'
    html = html.replace(broken_f4, fixed_f4)

    # Clean up any general `<a href=` inside title or alt that might be lingering
    # This is dangerous if we don't know the exact string, but safer to just do a strict replace
    html = re.sub(r'title="([^"]*)<a href="', r'title="\1', html)
    html = re.sub(r'alt="([^"]*)<a href="([^"]*)">([^<]*)</a>([^"]*)"', r'alt="\1\3\4"', html)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

for file in glob.glob("**/*.html", recursive=True):
    fix_file(file)

