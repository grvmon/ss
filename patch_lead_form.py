with open('lead-form.js', 'r') as f:
    content = f.read()

search = """      console.warn("Direct fetch submission issue, submitting native form...", err);
      if (form && typeof form.submit === 'function') {
        var retInput = document.getElementById("zoho_return_url");
        if (retInput) retInput.value = returnUrl;
        form.submit();"""

replace = """      console.warn("Direct fetch submission issue, submitting native form...", err);
      if (form && typeof form.submit === 'function') {
        var retInput = document.getElementById("zoho_return_url");
        if (retInput) retInput.value = returnUrl;
        
        // Inject required Zoho hidden fields before native submit
        var h1 = document.createElement('input'); h1.type = 'hidden'; h1.name = 'xnQsjsdp'; h1.value = ZOHO_WEB_TO_LEAD.xnQsjsdp;
        var h2 = document.createElement('input'); h2.type = 'hidden'; h2.name = 'xmIwtLD'; h2.value = ZOHO_WEB_TO_LEAD.xmIwtLD;
        var h3 = document.createElement('input'); h3.type = 'hidden'; h3.name = 'actionType'; h3.value = ZOHO_WEB_TO_LEAD.actionType;
        form.appendChild(h1); form.appendChild(h2); form.appendChild(h3);
        
        // Ensure action is set
        form.action = ZOHO_WEB_TO_LEAD.action;
        form.method = 'POST';
        
        form.submit();"""

if search in content:
    with open('lead-form.js', 'w') as f:
        f.write(content.replace(search, replace))
    print("lead-form.js patched")
else:
    print("Could not find string in lead-form.js")
