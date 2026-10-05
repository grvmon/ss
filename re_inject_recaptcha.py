import os

SKIP_DIRS = {'.git', 'assets', 'node_modules'}

def inject():
    files_modified = 0
    
    old_token1 = "3719eaafdcaf84c2c122c957b23371a7ed8c735cc2fc4dc3c4234898eab5058e"
    new_token1 = "ab2c0d137452c6e44d4ab49aaf9d107d0881349743d2338ac3e06be64f6329b8"
    old_token2 = "79d3731cf6d5263fe25ca7b3f44f6c0d42399f0924164df81f6e37141a5c3a7a99d60f9e5782124ac0715631e04021ff"
    new_token2 = "91ea25b27e38c66119c317f8814dd4df415a342fbb82279dc17fac58adca3bd871658a8b2696c9081e5b822911055b5b"
    new_sitekey = "6Ld1zd8tAAAAAGOMVDrGqo7XZHSeGkDZHfAFa1Sy"

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
                    recap_html = f'<div class="g-recaptcha" data-sitekey="{new_sitekey}" style="margin-bottom:15px;display:flex;justify-content:center;"></div>\n                    <div class="lf-submit-wrap">'
                    content = content.replace('<div class="lf-submit-wrap">', recap_html)
                
                if content != original_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    files_modified += 1
                    
    print(f"Updated tokens and added reCAPTCHA to {files_modified} HTML files.")

if __name__ == '__main__':
    inject()
