import os
import re

button_html = """
                <button class="btn btn-primary" onclick="if (window.openAdvisorModal) { window.openAdvisorModal(); } else { openQuoteModal('Header Navigation'); }">Talk to an Advisor</button>"""

modified_count = 0

for root, _, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Look for nav-actions where the button is missing
            # It usually looks like:
            # <div class="nav-actions">
            #     <a href="tel:+919090206090" class="phone-link">
            #         <span class="material-symbols-rounded">call</span>
            #         +91-9090206090
            #     </a>
            #     <button class="mobile-nav-toggle"
            
            # Check if button is already there
            if ">Talk to an Advisor</button>" in content:
                continue
                
            # Regex to find the spot right before mobile-nav-toggle in nav-actions
            # We want to insert the button right before <button class="mobile-nav-toggle"
            pattern = re.compile(r'(<a href="tel:\+919090206090"[^>]*>.*?</a>\s*)(<button class="mobile-nav-toggle")', re.DOTALL)
            
            if pattern.search(content):
                new_content = pattern.sub(r'\1' + button_html + r'\n                \2', content)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                modified_count += 1
                
print(f"Added CTA back to {modified_count} files")
