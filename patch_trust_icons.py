import re

with open("assets/css/storage-calculator.css", "r", encoding="utf-8") as f:
    css = f.read()

new_styles = """
/* Fix for Trust Card Icons Alignment */
.calc-trust-grid .trust-card span {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  width: 44px !important;
  height: 44px !important;
  padding: 0 !important; /* Remove padding since we are using flex and fixed w/h */
  flex-shrink: 0 !important;
}
"""

with open("assets/css/storage-calculator.css", "a", encoding="utf-8") as f:
    f.write(new_styles)

print("Patched trust card icons.")
