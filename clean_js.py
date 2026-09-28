with open("storage-advisor.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
skip = False
for i, line in enumerate(lines):
    if "advisor-speech-desc" in line:
        continue
    if "advisor-bubble-tail" in line:
        skip = True
        continue
    
    if skip:
        if "</div>' +" in line and "advisorMainCard" not in lines[i+1]:
            # This is the closing div of the bubble
            skip = False
            continue
        if "</div>' +" in line and "advisorMainCard" in lines[i+1]:
            # wait, let me just hardcode the removal of these precise strings instead of logic
            pass
            
# Let's just do text replace again
with open("storage-advisor.js", "r", encoding="utf-8") as f:
    js = f.read()

import re
# Remove the broken leftover bubble fragment
broken_fragment = r"\s*'<div class=\"advisor-speech-desc\">Need help calculating storage space\?</div>' \+\n\s*'<div class=\"advisor-bubble-tail\" aria-hidden=\"true\">' \+\n\s*'<svg width=\"16\" height=\"9\" viewBox=\"0 0 16 9\" fill=\"none\">' \+\n\s*'<path d=\"M0 0H16L8\.8 7\.6C8\.4 8 7\.6 8 7\.2 7\.6L0 0Z\" fill=\"#FFFFFF\"></path>' \+\n\s*'<path d=\"M0 0L7\.2 7\.6C7\.6 8 8\.4 8 8\.8 7\.6L16 0\" stroke=\"rgba\(0, 43, 73, 0\.12\)\" stroke-width=\"1\" fill=\"none\"></path>' \+\n\s*'</svg>' \+\n\s*'</div>' \+\n\s*'</div>' \+"

js = re.sub(broken_fragment, "", js)

with open("storage-advisor.js", "w", encoding="utf-8") as f:
    f.write(js)

print("Cleaned up fragmented bubble.")
