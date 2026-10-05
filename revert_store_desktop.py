import os

with open('app.js', 'r') as f:
    content = f.read()
content = content.replace("if(window.location.pathname.indexOf('/store') !== -1) { style.innerHTML += ' .floating-call-btn{ display: flex !important; }'; } document.head.appendChild(style);", "document.head.appendChild(style);")
with open('app.js', 'w') as f:
    f.write(content)

with open('app.min.js', 'r') as f:
    content = f.read()
content = content.replace("window.location.pathname.indexOf('/store')!==-1&&(t.innerHTML+=' .floating-call-btn{ display: flex !important; }'),document.head.appendChild(t),", "document.head.appendChild(t),")
with open('app.min.js', 'w') as f:
    f.write(content)

print("Reverted exceptions")
