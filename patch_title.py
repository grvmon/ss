import re

with open("assets/css/storage-calculator.css", "r", encoding="utf-8") as f:
    css = f.read()

# I will append new styles to the end to ensure they override earlier ones.
new_styles = """
/* Fix for Preset Title Alignment and Styling */
.calc-preset-title {
  font-size: 0.9rem !important;
  font-weight: 700 !important;
  text-transform: none !important;
  letter-spacing: normal !important;
  color: var(--text) !important;
  display: flex !important;
  align-items: center !important;
  gap: 6px !important;
  flex-shrink: 0 !important;
  margin-right: 4px !important;
  height: 100% !important;
}
.calc-preset-title .material-symbols-rounded {
  font-size: 18px !important;
}
"""

with open("assets/css/storage-calculator.css", "a", encoding="utf-8") as f:
    f.write(new_styles)

print("Patched calc-preset-title.")
