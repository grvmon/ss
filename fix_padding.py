import re

with open("assets/css/storage-calculator.css", "r", encoding="utf-8") as f:
    css = f.read()

# I will append new styles to the end to ensure they override earlier ones.
new_styles = """
/* Fix for Vertical Spacing inside Preset Wrapper */
.calc-preset-wrapper {
  padding: 10px 14px !important;
  display: flex !important;
  align-items: center !important;
  flex-wrap: nowrap !important;
  overflow-x: auto !important;
  overflow-y: hidden !important;
}
.calc-preset-wrapper::-webkit-scrollbar {
  display: none;
}
.calc-preset-title {
  height: auto !important;
  margin-top: 0 !important;
  margin-bottom: 0 !important;
  line-height: 1 !important;
}
"""

with open("assets/css/storage-calculator.css", "a", encoding="utf-8") as f:
    f.write(new_styles)

print("Patched calc-preset-wrapper padding.")
