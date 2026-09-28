import urllib.request
import urllib.parse
import time

url = "https://crm.zoho.in/crm/WebToLeadForm"

base_data = {
    'xnQsjsdp': 'fedbdee437014154ed2bb16453017bf1804b43155bb724c59474e33ae8f3d9ed',
    'xmIwtLD': '5b244f2d61e9bc1a1dd7c8178a8cb743242ac4d88a14ea9a5ea5f84e811f0e0d3d3885fbd8ccbbc43c019981f23d6ba8',
    'actionType': 'TGVhZHM=',
    'returnURL': 'https://selfstorageindia.com/thank-you/',
    'aG9uZXlwb3Q': '',
    'zc_gad': 'GCLID_NEW_FORM_001',
    'ldeskuid': '',
    'LDTuvid': '',
    'Description': 'Automated submission using brand new form ID'
}

test_cases = [
    {"Last Name": "Test Lead Supernova", "Email": "supernova@selfstorageindia.com", "Phone": "+919000000001"}
]

for tc in test_cases:
    data = base_data.copy()
    data.update(tc)
    
    encoded_data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, data=encoded_data, method='POST')
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)')
    req.add_header('Referer', 'https://selfstorageindia.com/')
    
    try:
        with urllib.request.urlopen(req) as response:
            status = response.getcode()
            print(f"Submitted '{tc['Last Name']}' | Status: {status}")
    except Exception as e:
        print(f"Failed to submit '{tc['Last Name']}': {e}")
