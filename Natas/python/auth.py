import base64

def genHeader(level,nataspass):
    url = "http://"+ level +'.natas.labs.overthewire.org'
    user = level
    password = nataspass
    authcred = user+":"+password
    auth64 = base64.b64encode(authcred.encode('ascii'))
    authstring="Basic "+auth64.decode('ascii')
    natasRequest={
        "Authorization": authstring,
        "URL": url
        }
    return natasRequest
