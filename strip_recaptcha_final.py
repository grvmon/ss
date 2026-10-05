import os
import re

SKIP_DIRS = {'.git', 'assets', 'node_modules'}

def process():
    files_modified = 0
    
    old_token1 = "bd195846afb64011ff79f94b8dbc5c0afdc7e2650c20303bd3d18ad6d50a58c4"
    new_token1 = "f16e947a58c920d3d9bbb4b80e92c047ca04ed4d68bb240204297c44c42d8001"
    
    old_token2 = "731726f5f4ffa32876e2a1cc06f4d0ec6d1f5e0a5f916e1b90092cc89a47e2538f742d3154220199982b03b394318917"
    new_token2 = "e9726bf6b19e499bf582aa195c8e5d128958792568633ff8fe046537f9cb109d26d208f333e4ee6aef5c1bebc25b1097"

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
                content = content.replace('<script src="https://www.google.com/recaptcha/api.js" async defer></script>\n', '')
                content = content.replace('<script src="https://www.google.com/recaptcha/api.js" async defer></script>', '')
                
                # Remove reCAPTCHA widget
                content = re.sub(r'<div class="g-recaptcha"[^>]+></div>\n\s*<div class="lf-submit-wrap">', '<div class="lf-submit-wrap">', content)
                
                if content != original_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    files_modified += 1
                    
            elif file == 'lead-form.min.js':
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                original_content = content
                
                # Replace tokens
                content = content.replace(old_token1, new_token1)
                content = content.replace(old_token2, new_token2)
                
                # Remove reCAPTCHA check logic
                search_str = 'L.append("fclid",uf);var _gr=document.getElementById("g-recaptcha-response");if(_gr&&_gr.value){L.append("g-recaptcha-response",_gr.value)}else{b&&(b.classList.add("lf-show"),b.textContent="Please complete the robot check.");M&&(M.disabled=!1,M.classList.remove("lf-loading"));D&&(D.textContent="Request Callback");clearTimeout(X);H=!1;return}try{'
                replace_str = 'L.append("fclid",uf);try{'
                content = content.replace(search_str, replace_str)
                
                if content != original_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print("Updated lead-form.min.js")

    print(f"Updated tokens and removed reCAPTCHA in {files_modified} HTML files.")

if __name__ == '__main__':
    process()
