with open('storage-advisor.js', 'r') as f:
    content = f.read()

search = """      } catch (crmErr) {
        console.warn("[Storage Advisor Zoho warning]", crmErr);
        var tempForm = document.createElement('form');
        tempForm.method = 'POST';
        tempForm.action = ZOHO_WEB_TO_LEAD.action;
        tempForm.style.display = 'none';
        
        for (var pair of formData.entries()) {
          var input = document.createElement('input');
          input.type = 'hidden';
          input.name = pair[0];
          input.value = pair[1];
          tempForm.appendChild(input);
        }
        document.body.appendChild(tempForm);
        tempForm.submit();
        return;
      }"""

replace = """      } catch (crmErr) {
        console.warn("[Storage Advisor Zoho warning]", crmErr);
        var f = document.getElementById("advisorForm");
        if (f && typeof f.submit === 'function') {
           var nInp = document.getElementById("advName"); if (nInp) nInp.name = "Last Name";
           var pInp = document.getElementById("advPhone"); if (pInp) pInp.name = "Phone";
           var eInp = document.getElementById("advEmail"); if (eInp) eInp.name = "Email";
           
           var h1 = document.createElement('input'); h1.type = 'hidden'; h1.name = 'xnQsjsdp'; h1.value = ZOHO_WEB_TO_LEAD.xnQsjsdp;
           var h2 = document.createElement('input'); h2.type = 'hidden'; h2.name = 'xmIwtLD'; h2.value = ZOHO_WEB_TO_LEAD.xmIwtLD;
           var h3 = document.createElement('input'); h3.type = 'hidden'; h3.name = 'actionType'; h3.value = ZOHO_WEB_TO_LEAD.actionType;
           var h4 = document.createElement('input'); h4.type = 'hidden'; h4.name = 'returnURL'; h4.value = REDIRECT_URL;
           
           f.appendChild(h1); f.appendChild(h2); f.appendChild(h3); f.appendChild(h4);
           f.action = ZOHO_WEB_TO_LEAD.action;
           f.method = 'POST';
           f.submit();
           return;
        }
      }"""

if search in content:
    with open('storage-advisor.js', 'w') as f:
        f.write(content.replace(search, replace))
    print("storage-advisor.js native form fixed")
else:
    print("Could not find search string in storage-advisor.js")
