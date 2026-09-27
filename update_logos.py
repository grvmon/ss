import os
from PIL import Image

names = ["ptinews.jpeg", "The-Week-Logo-300x300.png", "TOI-Logo-300x300.png", "Radiusplus-Logo.png", "ET-Logo.png", "ISS-Logo.png"]
for name in names:
    path = os.path.join("assets", name)
    try:
        if os.path.exists(path):
            img = Image.open(path).convert('RGBA')
            # For jpeg, RGB is better. Just convert to RGB if it doesn't have transparency
            if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                # webp supports RGBA natively
                pass
            webp_name = name.rsplit('.', 1)[0] + '.webp'
            webp_path = os.path.join("assets", webp_name)
            img.save(webp_path, "WEBP", quality=85)
            print(f"Converted {name} to {webp_name}")
    except Exception as e:
        print(f"Error {name}: {e}")
