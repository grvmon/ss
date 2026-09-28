import os

artifact_path = "/Users/gauravmongia/.gemini/antigravity/brain/fdb9c666-32ab-4e7e-8945-08dec56eb7de/mobile_header_preview.html"

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
      background: #f8fafc;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }
    .mobile-simulator {
      width: 375px;
      height: 600px;
      background: white;
      border: 12px solid #0f172a;
      border-radius: 40px;
      overflow: hidden;
      position: relative;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
    }
    .navbar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 12px 16px;
      border-bottom: 1px solid var(--border);
      background: #ffffff;
    }
    .brand-logo-img {
      height: 36px;
      width: auto;
    }
    .nav-actions {
      display: flex;
      align-items: center;
      gap: 16px;
    }
    /* Updated Mobile Phone Link CSS */
    .phone-link {
        font-size: 0;
        width: 42px;
        height: 42px;
        border-radius: 50%;
        background: var(--primary);
        box-shadow: 0 4px 12px rgba(24, 108, 236, 0.25);
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 0;
        padding: 0;
        flex-shrink: 0;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        text-decoration: none;
        cursor: pointer;
    }
    .phone-link span {
        font-size: 22px;
        color: #ffffff;
        margin: 0;
    }
    .phone-link:active {
        transform: scale(0.95);
    }
    .hamburger {
      font-size: 28px;
      color: #0f172a;
    }
    .mock-content {
      padding: 24px 16px;
    }
    .mock-text {
      height: 12px;
      background: #e2e8f0;
      border-radius: 6px;
      margin-bottom: 12px;
    }
  </style>
</head>
<body>
  <div class="mobile-simulator">
    <header class="navbar">
        <!-- Brand Logo -->
        <a href="#" class="brand-logo">
            <img src="https://grvmon.github.io/ss/assets/self-storage-india-logo.webp" alt="Logo" class="brand-logo-img">
        </a>
        <div class="nav-actions">
            <!-- Centered Phone Button -->
            <a href="#" class="phone-link">
                <span class="material-symbols-rounded">call</span>
            </a>
            <span class="material-symbols-rounded hamburger">menu</span>
        </div>
    </header>
    <div class="mock-content">
      <div class="mock-text" style="width: 80%"></div>
      <div class="mock-text" style="width: 60%"></div>
      <div class="mock-text" style="width: 90%"></div>
    </div>
  </div>
</body>
</html>
"""

with open(artifact_path, "w") as f:
    f.write(html_content)

print(f"Generated preview artifact at {artifact_path}")
