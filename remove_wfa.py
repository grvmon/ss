import os
import re

for root, _, files in os.walk("."):
    for file in files:
        if file.endswith(".js"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            
            if "wFaTrisJS" in content:
                # Remove wFaTrisJS from ZOHO_WEB_TO_LEAD object
                content = re.sub(r"wFaTrisJS:\s*'true'[,]?", "", content)
                # Remove formData.append('wFaTrisJS', ...)
                content = re.sub(r"formData\.append\('wFaTrisJS'[^;]+;", "", content)
                
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Removed wFaTrisJS from {path}")
