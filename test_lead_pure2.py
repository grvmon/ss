import urllib.request
import urllib.parse
import json

url = "https://crm.zoho.in/crm/WebToLeadForm"

data = {
    'xnQsjsdp': '7546ce5237fb71a5aec0c5ef5c56c4a8660ef9e244b3113358fe7964b5f28eb5',
    'xmIwtLD': 'fca10274295c5074a3d86ccea7a46cf2b85f39e880b5a44293827267958b1c2d7ac70e90da677cefd7a7ce1ae0627bf1',
    'actionType': 'TGVhZHM=',
    'returnURL': 'https://selfstorageindia.com/thank-you/',
    'ldeskuid': '',
    'LDTuvid': '',
    'aG9uZXlwb3Q': '',
    'Last Name': 'Test Lead Pure 2 (Referer: selfstorageindia.com)',
    'Phone': '9090206090',
    'Email': 'testpure2@selfstorageindia.com',
    'zc_gad': ''
}

encoded_data = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request(url, data=encoded_data, method='POST')
req.add_header('User-Agent', 'Mozilla/5.0')
req.add_header('Referer', 'https://selfstorageindia.com/')

try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        print(f"Status: {response.getcode()}")
except Exception as e:
    print(f"Failed: {e}")
