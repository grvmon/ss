with open('lead-form.min.js', 'r') as f:
    content = f.read()

search = "ye&&(ye.value=R),T.action=q.action,T.submit()"
replace = 'ye&&(ye.value=R),T.action=q.action,function(){var h1=document.createElement("input");h1.type="hidden";h1.name="xnQsjsdp";h1.value=q.xnQsjsdp;T.appendChild(h1);var h2=document.createElement("input");h2.type="hidden";h2.name="xmIwtLD";h2.value=q.xmIwtLD;T.appendChild(h2);var h3=document.createElement("input");h3.type="hidden";h3.name="actionType";h3.value=q.actionType;T.appendChild(h3)}(),T.submit()'

if search in content:
    with open('lead-form.min.js', 'w') as f:
        f.write(content.replace(search, replace))
    print("lead-form.min.js patched")
else:
    print("Not found in lead-form.min.js")
