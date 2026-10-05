import re

with open('storage-advisor.js', 'r') as f:
    content = f.read()

search = """      } catch (crmErr) {
        console.warn("[Storage Advisor Zoho warning]", crmErr);
      }"""

replace = """      } catch (crmErr) {
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

if search in content:
    with open('storage-advisor.js', 'w') as f:
        f.write(content.replace(search, replace))
    print("storage-advisor.js patched")
else:
    print("Could not find search string in storage-advisor.js")
