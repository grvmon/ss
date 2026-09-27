import re
import glob

def fix_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Check if the overlay is already inside the header
    if re.search(r'<div class="mobile-nav-overlay".*?</div>\s*</header>', html):
        return # Already fixed
        
    # Remove the overlay from anywhere
    overlay_pattern = r'\n?\s*(<!--.*?Mobile.*?Overlay.*?-->)?\s*<div class="mobile-nav-overlay" id="mobileNavOverlay" onclick="closeMobileMenu\(\)"></div>\n?'
    
    # If the overlay exists outside
    if re.search(overlay_pattern, html):
        html = re.sub(overlay_pattern, '', html)
        
        # Inject it into the header
        html = html.replace('</header>', '    <div class="mobile-nav-overlay" id="mobileNavOverlay" onclick="closeMobileMenu()"></div>\n    </header>')
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Fixed {filepath}")

for f in glob.glob("**/*.html", recursive=True):
    fix_file(f)
