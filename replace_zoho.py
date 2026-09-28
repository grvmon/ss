import os

old_xn = "a979ecd831c0e0cc3021561407927e41ccad53ba7f9728c54ff061b222e0eb6c"
new_xn = "7546ce5237fb71a5aec0c5ef5c56c4a8660ef9e244b3113358fe7964b5f28eb5"

old_xm = "0554b4515d63426b46b3bc2afad2cbd7fb8d66685ba40768b173c282051a2e9df93658768a3fc0ab3706c8f4d36586b4"
new_xm = "fca10274295c5074a3d86ccea7a46cf2b85f39e880b5a44293827267958b1c2d7ac70e90da677cefd7a7ce1ae0627bf1"

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

print(f"Updated {files_updated} files with new Zoho keys.")
