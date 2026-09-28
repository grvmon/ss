import os
import re

logo_mappings = {
    "Self-Storage-India-Logo-300x63.png": "self-storage-india-logo.png",
    "Self-Storage-India-Logo.png": "self-storage-india-logo.png",
    "ss_warehouse_white_bg_449_60-1-300x40.webp": "self-storage-warehouse-logo.webp",
    "Logo_SSAMember-Reflex_kiztzz-300x198.webp": "self-storage-association-member.webp",
    "ptinews.jpeg": "TOI-Logo-300x300.webp",
    "The-Week-Logo-300x300.png": "The-Week-Logo-300x300.webp",
    "TOI-Logo-300x300.png": "TOI-Logo-300x300.webp",
    "Radiusplus-Logo.png": "Radiusplus-Logo.webp",
    "ET-Logo.png": "ET-Logo.webp",
    "ISS-Logo.png": "ISS-Logo.webp"
}

def get_depth(file_path):
    parts = file_path.split("/")
    if len(parts) == 1:
        return ""
    else:
        return "../" * (len(parts) - 1)

# Match any occurrence of https://selfstorageindia.com/... with an image extension
url_pattern = re.compile(r'https://selfstorageindia\.com/[^"]+\.(?:jpg|jpeg|png|webp)')

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            depth_prefix = get_depth(path[2:]) 
            
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            
            original_content = content
            
            matches = url_pattern.findall(content)
            # Remove duplicates to process each unique URL once
            for url in set(matches):
                filename = url.split("/")[-1]
                
                if filename in logo_mappings:
                    local_path = f"{depth_prefix}assets/{logo_mappings[filename]}"
                else:
                    # It's a blog or general image
                    local_path = f"{depth_prefix}assets/blog/{filename}"
                
                content = content.replace(url, local_path)
            
            if content != original_content:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)

print("Finished replacing all remaining absolute image URLs.")
