import os

artifact_path = "/Users/gauravmongia/.gemini/antigravity/brain/fdb9c666-32ab-4e7e-8945-08dec56eb7de/mobile_calc_preview.html"

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
      --space-sm: 12px;
      --space-md: 24px;
    }
    body {
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background: transparent;
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 20px;
    }
    .mobile-simulator {
      width: 375px;
      height: 600px;
      background: #f8fafc;
      border: 12px solid #0f172a;
      border-radius: 40px;
      overflow-y: auto;
      position: relative;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
    }
    /* Scrollbar hide for sleekness */
    .mobile-simulator::-webkit-scrollbar { display: none; }
    
    .navbar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 12px 16px;
      border-bottom: 1px solid var(--border);
      background: #ffffff;
      position: sticky;
      top: 0;
      z-index: 10;
    }
    .brand-logo-img { height: 32px; width: auto; }
    .nav-actions { display: flex; align-items: center; gap: 12px; }
    .hamburger { font-size: 24px; color: #0f172a; }
    
    /* Filter Pills */
    .filter-pills {
      display: flex;
      gap: 8px;
      padding: 16px;
      overflow-x: auto;
      background: #ffffff;
      border-bottom: 1px solid var(--border);
    }
    .filter-pills::-webkit-scrollbar { display: none; }
    .pill {
      white-space: nowrap;
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 0.85rem;
      font-weight: 600;
      border: 1px solid var(--border);
      color: var(--text);
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .pill.active {
      background: var(--primary);
      color: #fff;
      border-color: var(--primary);
    }
    .pill span { font-size: 16px; }

    /* The New Sleek Calculator Cards */
    .calc-items-grid {
      padding: 16px;
      display: grid;
      grid-template-columns: 1fr;
      gap: 14px;
    }
    .calc-inv-card {
      background-color: #ffffff;
      border: 1px solid var(--border);
      border-radius: 14px;
      display: flex;
      flex-direction: row;
      align-items: center;
      padding: 12px 14px;
      gap: 12px;
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.02);
    }
    .inv-card-header {
      display: flex;
      align-items: center;
      gap: 10px;
      width: auto;
      flex: 1;
    }
    .inv-card-icon {
      font-size: 1.35rem;
      background: rgba(37, 99, 235, 0.08);
      color: #3b82f6;
      border-radius: 8px;
      padding: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      width: 34px;
      height: 34px;
    }
    .inv-card-name {
      font-size: 0.9rem;
      font-weight: 700;
      color: var(--text);
      line-height: 1.3;
      white-space: normal;
    }
    
    /* New Controls Pill */
    .inv-card-controls {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-radius: 20px;
      width: auto;
      gap: 12px;
      padding: 4px 8px;
      background: #f8fbff;
      border: 1px solid rgba(37, 99, 235, 0.1);
    }
    .inv-btn-dec, .inv-btn-inc {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      border: none;
      background: #ffffff;
      color: var(--text);
      font-size: 1rem;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }
    .inv-qty-display {
      font-weight: 700;
      font-size: 0.95rem;
      color: var(--text);
      min-width: 14px;
      text-align: center;
    }
  </style>
</head>
<body>
  <div class="mobile-simulator">
    <!-- Mock Header -->
    <header class="navbar">
        <img src="https://grvmon.github.io/ss/assets/self-storage-india-logo.webp" alt="Logo" class="brand-logo-img">
        <div class="nav-actions">
            <span class="material-symbols-rounded hamburger" style="color:var(--primary)">call</span>
            <span class="material-symbols-rounded hamburger">menu</span>
        </div>
    </header>

    <!-- Filters -->
    <div class="filter-pills">
      <div class="pill active"><span class="material-symbols-rounded">category</span> All Items</div>
      <div class="pill"><span class="material-symbols-rounded">chair</span> Living Room</div>
      <div class="pill"><span class="material-symbols-rounded">bed</span> Bedroom</div>
    </div>

    <!-- The New Calculator Grid -->
    <div class="calc-items-grid">
      
      <!-- Card 1 -->
      <div class="calc-inv-card">
        <div class="inv-card-header">
          <span class="material-symbols-rounded inv-card-icon">chair</span>
          <div class="inv-card-info">
            <span class="inv-card-name">3-Seater Living Sofa</span>
          </div>
        </div>
        <div class="inv-card-controls">
          <button class="inv-btn-dec">—</button>
          <span class="inv-qty-display">0</span>
          <button class="inv-btn-inc">+</button>
        </div>
      </div>

      <!-- Card 2 -->
      <div class="calc-inv-card" style="border-color: var(--primary); background: #f8fbff;">
        <div class="inv-card-header">
          <span class="material-symbols-rounded inv-card-icon">chair</span>
          <div class="inv-card-info">
            <span class="inv-card-name">2-Seater Sofa</span>
          </div>
        </div>
        <div class="inv-card-controls" style="background: rgba(37,99,235,0.12); border-color:transparent;">
          <button class="inv-btn-dec">—</button>
          <span class="inv-qty-display">1</span>
          <button class="inv-btn-inc">+</button>
        </div>
      </div>

      <!-- Card 3 -->
      <div class="calc-inv-card">
        <div class="inv-card-header">
          <span class="material-symbols-rounded inv-card-icon">chair</span>
          <div class="inv-card-info">
            <span class="inv-card-name">Recliner / Armchair</span>
          </div>
        </div>
        <div class="inv-card-controls">
          <button class="inv-btn-dec">—</button>
          <span class="inv-qty-display">0</span>
          <button class="inv-btn-inc">+</button>
        </div>
      </div>

      <!-- Card 4 -->
      <div class="calc-inv-card">
        <div class="inv-card-header">
          <span class="material-symbols-rounded inv-card-icon">chair</span>
          <div class="inv-card-info">
            <span class="inv-card-name">L-Shaped Sectional Sofa</span>
          </div>
        </div>
        <div class="inv-card-controls">
          <button class="inv-btn-dec">—</button>
          <span class="inv-qty-display">0</span>
          <button class="inv-btn-inc">+</button>
        </div>
      </div>

    </div>
  </div>
</body>
</html>
"""

with open(artifact_path, "w") as f:
    f.write(html_content)

print(f"Generated calc preview artifact at {artifact_path}")
