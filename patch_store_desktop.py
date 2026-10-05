import os

files = ['app.js', 'app.min.js']
for file in files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # We need to append the JS check before document.head.appendChild(style);
        # Let's use simple string replacement.
        search_str1 = "document.head.appendChild(style);"
        replace_str1 = "if(window.location.pathname.indexOf('/store') !== -1) { style.innerHTML += ' .floating-call-btn{ display: flex !important; }'; } document.head.appendChild(style);"
        
        search_str2 = "document.head.appendChild(t),"
        replace_str2 = "window.location.pathname.indexOf('/store')!==-1&&(t.innerHTML+=' .floating-call-btn{ display: flex !important; }'),document.head.appendChild(t),"
        
        if search_str1 in content:
            content = content.replace(search_str1, replace_str1)
        elif search_str2 in content:
            content = content.replace(search_str2, replace_str2)
            
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Patched {file}")
