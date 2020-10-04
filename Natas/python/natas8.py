import base64
import requests
import re

secret = base64.b64decode(bytes.fromhex("3d3d516343746d4d6d6c315669563362")[::-1])
s = requests.session()
s.auth = ("natas8","DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe")

req = requests.Request("POST", "http://natas8.natas.labs.overthewire.org/", data={"secret":secret,"submit":"Submit+Query"})

game = s.send(s.prepare_request(req))

nextcode = re.findall('[a-zA-Z0-9]{32}',game.text)
print(nextcode[1])

