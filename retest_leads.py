import urllib.request
import urllib.parse
import time

url = "https://crm.zoho.in/crm/WebToLeadForm"

base_data = {
    'xnQsjsdp': '7546ce5237fb71a5aec0c5ef5c56c4a8660ef9e244b3113358fe7964b5f28eb5',
    'xmIwtLD': 'fca10274295c5074a3d86ccea7a46cf2b85f39e880b5a44293827267958b1c2d7ac70e90da677cefd7a7ce1ae0627bf1',
    'actionType': 'TGVhZHM=',
    'returnURL': 'https://selfstorageindia.com/thank-you/',
    'wFaTrisJS': 'true',
    'aG9uZXlwb3Q': '',
    'zc_gad': 'GCLID_RETEST_001',
    'ldeskuid': '',
    'LDTuvid': '',
    'Description': 'Automated Retest submission'
}

test_cases = [
    {"Last Name": "Test Lead Omega", "Email": "omega.retest@selfstorageindia.com", "Phone": "+919999900001"},
    {"Last Name": "Test Lead Sigma", "Email": "sigma.retest@selfstorageindia.com", "Phone": "+919999900002"},
    {"Last Name": "Test Lead Zeta",  "Email": "zeta.retest@selfstorageindia.com",  "Phone": "+919999900003"}
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
            print(f"Submitted '{tc['Last Name']}' | Email: {tc['Email']} | Status: {status}")
    except Exception as e:
        print(f"Failed to submit '{tc['Last Name']}': {e}")
    
    time.sleep(2)
