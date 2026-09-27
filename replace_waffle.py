import re

with open("household-goods-storage/index.html", "r", encoding="utf-8") as f:
    hgs = f.read()

with open("replacement.html", "r", encoding="utf-8") as f:
    rep = f.read()

# Remove the Business tab from replacement HTML
rep = re.sub(r'<button class="tab-btn" onclick="switchStorageTab\(\'business\'\)">.*?Business \&amp; Office.*?</button>', '', rep, flags=re.DOTALL)
rep = re.sub(r'<div class="storage-tab-pane" id="tab-business">.*?</div>\s*<!-- 3\. LUGGAGE -->', '<!-- 3. LUGGAGE -->', rep, flags=re.DOTALL)

# Locate the waffle in HGS
start_waffle = "<h2>Household Storage India NCR | Protect Your Valuables</h2>"
end_waffle = "find the perfect unit for your needs!</p>\n            </div>\n        </section>"

if start_waffle in hgs and end_waffle in hgs:
    prefix = hgs.split(start_waffle)[0]
    suffix = hgs.split(end_waffle)[1]
    
    # Wait, the end_waffle might not match exactly. Let's use regex.
    pattern = r'<h2>Household Storage India NCR \| Protect Your Valuables</h2>.*?</section>'
    
    new_hgs = re.sub(pattern, "</section>\n\n" + rep, hgs, flags=re.DOTALL)
    
    with open("household-goods-storage/index.html", "w", encoding="utf-8") as f:
        f.write(new_hgs)
    print("Waffle replaced.")
else:
    print("Could not find waffle markers.")
