import os
import re
import urllib.request
import urllib.parse

os.makedirs("assets/blog", exist_ok=True)

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

img_pattern = re.compile(r'src="(https://selfstorageindia\.com/[^"]+)"')
meta_pattern = re.compile(r'content="(https://selfstorageindia\.com/[^"]+)"')

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            depth_prefix = get_depth(path[2:]) 
            
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            
            original_content = content
            
            matches = img_pattern.findall(content)
            for url in matches:
                filename = url.split("/")[-1]
                
                if filename in logo_mappings:
                    local_path = f"{depth_prefix}assets/{logo_mappings[filename]}"
                    content = content.replace(f'src="{url}"', f'src="{local_path}"')
                else:
                    local_save_path = f"assets/blog/{filename}"
                    if not os.path.exists(local_save_path):
                        try:
                            # Safely encode the URL preserving slashes
                            parsed = urllib.parse.urlparse(url)
                            safe_path = urllib.parse.quote(parsed.path, safe='/')
                            safe_url = parsed._replace(path=safe_path).geturl()
                            
                            req = urllib.request.Request(safe_url, headers={'User-Agent': 'Mozilla/5.0'})
                            with urllib.request.urlopen(req) as response, open(local_save_path, 'wb') as out_file:
                                out_file.write(response.read())
                            print(f"Downloaded: {filename}")
                        except Exception as e:
                            print(f"Failed to download {url}: {e}")
                    
                    local_html_path = f"{depth_prefix}assets/blog/{filename}"
                    content = content.replace(f'src="{url}"', f'src="{local_html_path}"')
                    
            # For meta tags, replace the domain with the local relative path as well, so it's fully local
            meta_matches = meta_pattern.findall(content)
            for url in meta_matches:
                filename = url.split("/")[-1]
                if filename in logo_mappings:
                    local_path = f"{depth_prefix}assets/{logo_mappings[filename]}"
                    content = content.replace(f'content="{url}"', f'content="{local_path}"')
                else:
                    local_html_path = f"{depth_prefix}assets/blog/{filename}"
                    content = content.replace(f'content="{url}"', f'content="{local_html_path}"')
            
            if content != original_content:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)

print("Finished localizing images perfectly.")
