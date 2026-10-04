import os
import re

SKIP_DIRS = {'.git', 'assets', 'node_modules'}

def revert():
    files_modified = 0
    
    old_token1 = "c6eb63f6236417682faed4a4b1e543deb24e980554474aadc6154b75e0dfdcb5"
    new_token1 = "3719eaafdcaf84c2c122c957b23371a7ed8c735cc2fc4dc3c4234898eab5058e"
    old_token2 = "1c727e96dbfbb6c6d7b69df02c0bf8c3d062a16f4b987fb5d78cf4d6426d299bc5fad13f2c784a33a9182cc807619d30"
    new_token2 = "79d3731cf6d5263fe25ca7b3f44f6c0d42399f0924164df81f6e37141a5c3a7a99d60f9e5782124ac0715631e04021ff"

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
                
                # Remove reCAPTCHA script
                content = content.replace('<script src="https://www.google.com/recaptcha/api.js" async defer></script>', '')
                
                # Remove reCAPTCHA widget
                content = content.replace('<div class="g-recaptcha" data-sitekey="6LdjRN8tAAAAACdUt3PAzY7zYd1s2RIKSpZ_i8WJ" style="margin-bottom:15px;display:flex;justify-content:center;"></div>\n                    <div class="lf-submit-wrap">', '<div class="lf-submit-wrap">')
                
                if content != original_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    files_modified += 1
                    
    print(f"Updated tokens and removed reCAPTCHA from {files_modified} HTML files.")

if __name__ == '__main__':
    revert()
