import os
import re

SKIP_DIRS = {'.git', 'assets', 'node_modules'}

def inject():
    files_modified = 0
    
    old_token1 = "ab90d9124bda14347cdea243b8cd62234c61df6ed89b9d37ec7a8b5ecd033eaa"
    new_token1 = "c6eb63f6236417682faed4a4b1e543deb24e980554474aadc6154b75e0dfdcb5"
    old_token2 = "6aa318a3320f1b0607908f79e477e5b26120ae8a8442240da64c1bb2942bd6ab212b9a280ddf65cf2dbed3a61f3cfb83"
    new_token2 = "1c727e96dbfbb6c6d7b69df02c0bf8c3d062a16f4b987fb5d78cf4d6426d299bc5fad13f2c784a33a9182cc807619d30"

    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                original_content = content
                
                # Replace tokens
                content = content.replace(old_token1, new_token1)
                content = content.replace(old_token2, new_token2)
                
                # Add reCAPTCHA script to head if not present
                if "recaptcha/api.js" not in content:
                    content = content.replace('</head>', '<script src="https://www.google.com/recaptcha/api.js" async defer></script>\n</head>')
                
                # Add reCAPTCHA widget if not present
                if "g-recaptcha" not in content and '<div class="lf-submit-wrap">' in content:
                    recap_html = '<div class="g-recaptcha" data-sitekey="6LdjRN8tAAAAACdUt3PAzY7zYd1s2RIKSpZ_i8WJ" style="margin-bottom:15px;display:flex;justify-content:center;"></div>\n                    <div class="lf-submit-wrap">'
                    content = content.replace('<div class="lf-submit-wrap">', recap_html)
                
                if content != original_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    files_modified += 1
                    
    print(f"Updated tokens and added reCAPTCHA to {files_modified} HTML files.")

if __name__ == '__main__':
    inject()
