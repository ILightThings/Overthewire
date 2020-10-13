import requests
import re
import os

s = requests.Session()
s.auth = ("natas12","EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3")
game = s.get("http://natas12.natas.labs.overthewire.org")

print(game.text)
