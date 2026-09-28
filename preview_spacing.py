import os

artifact_path = "/Users/gauravmongia/.gemini/antigravity/brain/fdb9c666-32ab-4e7e-8945-08dec56eb7de/preset_spacing_preview.html"

html_content = """<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet" />
  <style>
    :root {
      --primary: #186CEC;
      --text: #1e293b;
      --border: #e2e8f0;
      --surface: #f8fafc;
      --radius-pill: 20px;
    }
    body {
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background: #f1f5f9;
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 40px;
    }
    .wrapper-demo {
      width: 100%;
      max-width: 800px;
    }

    /* THE FIXES APPLIED */
    .calc-preset-wrapper {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 10px 14px; /* Perfectly even top and bottom padding */
      box-shadow: 0 1px 4px rgba(0, 0, 0, 0.02);
      display: flex;
      align-items: center;
      flex-wrap: nowrap;
      overflow-x: auto;
      overflow-y: hidden;
      gap: 12px;
    }
    .calc-preset-wrapper::-webkit-scrollbar { display: none; }
    
    .calc-preset-title {
      font-size: 0.9rem;
      font-weight: 700;
      color: var(--text);
      display: flex;
      align-items: center;
      gap: 6px;
      flex-shrink: 0;
      margin-top: 0;
      margin-bottom: 0;
      line-height: 1;
    }
    .calc-preset-title .material-symbols-rounded {
      font-size: 18px;
      color: var(--primary);
    }
    
    .calc-preset-pill {
      appearance: none;
      border: 1px solid var(--border);
      background: var(--surface);
      color: var(--text);
      padding: 6px 12px;
      border-radius: var(--radius-pill);
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      white-space: nowrap;
    }
    .calc-preset-pill .material-symbols-rounded { font-size: 16px; }
    
  </style>
</head>
<body>
  <div class="wrapper-demo">
    <div class="calc-preset-wrapper">
      <span class="calc-preset-title">
          <span class="material-symbols-rounded">auto_fix_high</span>
          1-Click Presets:
      </span>
      <button class="calc-preset-pill">
          <span class="material-symbols-rounded">home</span> 1 BHK (45–68 sq ft)
      </button>
      <button class="calc-preset-pill">
          <span class="material-symbols-rounded">business</span> 2 BHK (72–98 sq ft)
      </button>
    </div>
  </div>
</body>
</html>
"""

with open(artifact_path, "w") as f:
    f.write(html_content)

print(f"Generated calc spacing preview artifact at {artifact_path}")
