with open("assets/css/storage-calculator.css", "r", encoding="utf-8") as f:
    css = f.read()

# Add white-space: nowrap back to .calc-preset-pill
target = """.calc-preset-pill {
  appearance: none;
  background: #ffffff;
  border: 1px solid var(--border);
  border-radius: 99px;
  padding: 8px 16px;
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--text-secondary);
  cursor: pointer;
  transition: all 0.2s ease;
  display: inline-flex;
  align-items: center;
  gap: 5px;
}"""

replacement = """.calc-preset-pill {
  appearance: none;
  background: #ffffff;
  border: 1px solid var(--border);
  border-radius: 99px;
  padding: 8px 16px;
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--text-secondary);
  cursor: pointer;
  transition: all 0.2s ease;
  display: inline-flex;
  align-items: center;
  gap: 5px;
  white-space: nowrap;
}"""

css = css.replace(target, replacement)

with open("assets/css/storage-calculator.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Fixed calc-preset-pill css.")
