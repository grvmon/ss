import re

def fix_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Find the overlay
    overlay_str = '    <!-- Mobile Drawer Overlay -->\n    <div class="mobile-nav-overlay" id="mobileNavOverlay" onclick="closeMobileMenu()"></div>\n'
    
    if overlay_str in html:
        # Remove it from its current position
        html = html.replace(overlay_str, '')
        
        # Inject it right before </header>
        html = html.replace('    </header>', '        <!-- Mobile Drawer Overlay -->\n        <div class="mobile-nav-overlay" id="mobileNavOverlay" onclick="closeMobileMenu()"></div>\n    </header>')
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Fixed {filepath}")
    else:
        print(f"Overlay not found precisely in {filepath}")

import glob
for f in glob.glob("**/*.html", recursive=True):
    fix_file(f)
