import requests
import base64
import re
from auth import *

user = "natas3"
password = "sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14"

requestData = genHeader(user,password)

headerData ={"Authorization":requestData["Authorization"]}

def newReq("directory"):
    fileURL = requestData["URL"]+"/robots.txt"
    x = requests.post(url=fileURL,headers=headerData)
    return x.text




print(newReq("/robots.txt"))
#nextcode = re.findall('[a-zA-Z0-9]{32}',x.text)
#print(f'The code for the next level is: {nextcode[0]}' )

