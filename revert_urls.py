import re
import glob

for filepath in glob.glob("**/*.html", recursive=True):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Revert my previous mistake: links that I changed to /self-storage-calculator/ should go back to /store
    html = html.replace('href="/self-storage-calculator/#locations"', 'href="/store#locations"')
    html = html.replace('href="/self-storage-calculator/"', 'href="/store/"')
    # Be careful not to mess up anything else, but /self-storage-calculator/ was entirely my creation.
    
    # Now correctly rename links to the ACTUAL calculator page
    html = html.replace('href="/storage-calculator"', 'href="/self-storage-calculator"')
    html = html.replace('href="/storage-calculator/"', 'href="/self-storage-calculator/"')

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
        
print("Reverted URL mistake and applied correct calculator links.")
