import os

old_xn = "7546ce5237fb71a5aec0c5ef5c56c4a8660ef9e244b3113358fe7964b5f28eb5"
new_xn = "fedbdee437014154ed2bb16453017bf1804b43155bb724c59474e33ae8f3d9ed"

old_xm = "fca10274295c5074a3d86ccea7a46cf2b85f39e880b5a44293827267958b1c2d7ac70e90da677cefd7a7ce1ae0627bf1"
new_xm = "5b244f2d61e9bc1a1dd7c8178a8cb743242ac4d88a14ea9a5ea5f84e811f0e0d3d3885fbd8ccbbc43c019981f23d6ba8"

files_updated = 0

for root, _, files in os.walk("."):
    for file in files:
        if file.endswith(".html") or file.endswith(".js"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            
            if old_xn in content or old_xm in content:
                new_content = content.replace(old_xn, new_xn).replace(old_xm, new_xm)
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                files_updated += 1

print(f"Updated {files_updated} files with brand new Zoho form keys.")
