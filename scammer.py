import requests
import os
import random
import string
import json
import pdb

chars1 = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'http://battle-azeroth.net/login.asp?a=ok'

names = json.loads(open('names.json').read())

for name in names:
    name_extra = ''.join(random.choice(string.digits))

    username = name.lower() + name_extra + "@yahoo.com"

    password = ''.join(random.choice(chars1) for i in range(8))

    requests.post(url, allow_redirects=False, data={
        'accountName': username,
        'password': password
    })

    print "sending username %s and password %s" % (username, password)
