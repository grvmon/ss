import re

with open('storage-advisor.min.js', 'r') as f:
    content = f.read()

# match catch(e){console.warn("[Storage Advisor Zoho warning]",e)}
pattern = re.compile(r'catch\(([a-zA-Z0-9_]+)\)\{console\.warn\("\[Storage Advisor Zoho warning\]",\1\)\}')

# we need to replace it with:
# catch(e){console.warn("[Storage Advisor Zoho warning]",e);var tF=document.createElement("form");tF.method="POST";tF.action=ZOHO_WEB_TO_LEAD.action;tF.style.display="none";for(var p of formData.entries()){var i=document.createElement("input");i.type="hidden";i.name=p[0];i.value=p[1];tF.appendChild(i)}document.body.appendChild(tF);tF.submit();return}
# wait, ZOHO_WEB_TO_LEAD and formData might be minified!
# Let's search for how they are named in the minified file.
