import requests
import base64
import re

url = 'http://natas0.natas.labs.overthewire.org'
username='natas0'
password='natas0'
auth1=username+':'+password
auth2=base64.b64encode(auth1.encode("ascii"))
auth = 'Basic ' + auth2.decode('ascii')
header={'Authorization': auth}

x = requests.post(url,headers=header)

nextcode = re.findall('[a-zA-Z0-9]{32}',x.text)
print(f'The code for the next level is: {nextcode}' )
