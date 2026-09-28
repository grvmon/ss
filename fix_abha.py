import re

with open("storage-advisor.js", "r", encoding="utf-8") as f:
    js = f.read()

# 1. Remove the Speech Bubble completely
js = re.sub(
    r"'<div class=\"advisor-speech-bubble\" id=\"advisorSpeechBubble\".*?</svg>' \+\n\s*'(</div>' \+\n\s*'<div class=\"advisor-card\")",
    r"'\1",
    js,
    flags=re.DOTALL
)

# Wait, let me just replace the exact lines:
bubble_regex = r"'<div class=\"advisor-speech-bubble\" id=\"advisorSpeechBubble\".*?</div>' \+"
js = re.sub(bubble_regex, "", js, flags=re.DOTALL)

# Let me use an explicit string replacement instead of regex to be safe
# The original code has:
#         '<div class="advisor-speech-bubble" id="advisorSpeechBubble" role="status" aria-live="polite" title="Chat with Abha">' +
#           '<div class="advisor-speech-title">Hi! I\\'m Abha</div>' +
#           '<div class="advisor-speech-desc">Need help calculating storage space?</div>' +
#           '<div class="advisor-bubble-tail" aria-hidden="true">' +
#             '<svg width="16" height="9" viewBox="0 0 16 9" fill="none">' +
#               '<path d="M0 0H16L8.8 7.6C8.4 8 7.6 8 7.2 7.6L0 0Z" fill="#FFFFFF"></path>' +
#               '<path d="M0 0L7.2 7.6C7.6 8 8.4 8 8.8 7.6L16 0" stroke="rgba(0, 43, 73, 0.12)" stroke-width="1" fill="none"></path>' +
#             '</svg>' +
#           '</div>' +
#         '</div>' +

target_bubble = """        '<div class="advisor-speech-bubble" id="advisorSpeechBubble" role="status" aria-live="polite" title="Chat with Abha">' +
          '<div class="advisor-speech-title">Hi! I\\'m Abha</div>' +
          '<div class="advisor-speech-desc">Need help calculating storage space?</div>' +
          '<div class="advisor-bubble-tail" aria-hidden="true">' +
            '<svg width="16" height="9" viewBox="0 0 16 9" fill="none">' +
              '<path d="M0 0H16L8.8 7.6C8.4 8 7.6 8 7.2 7.6L0 0Z" fill="#FFFFFF"></path>' +
              '<path d="M0 0L7.2 7.6C7.6 8 8.4 8 8.8 7.6L16 0" stroke="rgba(0, 43, 73, 0.12)" stroke-width="1" fill="none"></path>' +
            '</svg>' +
          '</div>' +
        '</div>' +
"""
js = js.replace(target_bubble, "")

# 2. Remove mobile minification logic
target_minimized = """    var startMinimized = (typeof window.advisorStartMinimized !== 'undefined') ?
      Boolean(window.advisorStartMinimized) :
      (window.location.pathname.indexOf('storage-calculator') !== -1 ||
       !!document.querySelector('.storage-calculator-section') ||
       !!document.getElementById('ssiCalcApp') ||
       document.body.classList.contains('page-storage-calculator') ||
       window.innerWidth <= 768);"""

replacement_minimized = """    var startMinimized = (typeof window.advisorStartMinimized !== 'undefined') ?
      Boolean(window.advisorStartMinimized) :
      (window.location.pathname.indexOf('storage-calculator') !== -1 ||
       !!document.querySelector('.storage-calculator-section') ||
       !!document.getElementById('ssiCalcApp') ||
       document.body.classList.contains('page-storage-calculator'));"""
       
js = js.replace(target_minimized, replacement_minimized)

with open("storage-advisor.js", "w", encoding="utf-8") as f:
    f.write(js)

print("Patched storage-advisor.js")
