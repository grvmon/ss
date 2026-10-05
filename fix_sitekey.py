import os

SKIP_DIRS = {'.git', 'assets', 'node_modules'}

def inject():
    files_modified = 0
    
    old_token1 = "ab2c0d137452c6e44d4ab49aaf9d107d0881349743d2338ac3e06be64f6329b8"
    new_token1 = "bd195846afb64011ff79f94b8dbc5c0afdc7e2650c20303bd3d18ad6d50a58c4"
    old_token2 = "91ea25b27e38c66119c317f8814dd4df415a342fbb82279dc17fac58adca3bd871658a8b2696c9081e5b822911055b5b"
    new_token2 = "731726f5f4ffa32876e2a1cc06f4d0ec6d1f5e0a5f916e1b90092cc89a47e2538f742d3154220199982b03b394318917"
    
    old_sitekey = "6Ld1zd8tAAAAAGOMVDrGqo7XZHSeGkDZHfAFa1Sy"
    new_sitekey = "6Le3zt8tAAAAAIjt9FtWdfrGKz4i2zWYCKsAskqR"

    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for file in files:
            if file.endswith('.html') or file == "lead-form.min.js":
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                original_content = content
                
                # Replace tokens & sitekey
                content = content.replace(old_token1, new_token1)
                content = content.replace(old_token2, new_token2)
                content = content.replace(old_sitekey, new_sitekey)
                
                if content != original_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    files_modified += 1
                    
    print(f"Updated tokens and sitekey in {files_modified} files.")

if __name__ == '__main__':
    inject()
