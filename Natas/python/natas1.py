import requests
import base64
import re
from auth import *

user = "natas1"
password = "gtVrDuiDfck831PqWsLEZy5gyDz1clto"

requestData = genHeader(user,password)

headerData ={"Authorization":requestData["Authorization"]}

x = requests.post(url=requestData["URL"],headers=headerData)

nextcode = re.findall('[a-zA-Z0-9]{32}',x.text)
print(f'The code for the next level is: {nextcode[1]}' )
