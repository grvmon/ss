import re

with open("assets/js/storage-calculator.js", "r", encoding="utf-8") as f:
    js = f.read()

# Replace the text
js = js.replace(
    "Get Free Quote for ${result.unit.area} sq ft Unit",
    "Free Quote: ${result.unit.area} sq ft Unit"
)
js = js.replace(
    "Unit sized for your ${totalItems} items. Zero obligation quotation.",
    "Fits ${totalItems} items. Zero obligation quote."
)

with open("assets/js/storage-calculator.js", "w", encoding="utf-8") as f:
    f.write(js)

print("Patched calculator JS.")
