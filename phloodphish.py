# Inspired by the Engineer Man on Youtube. Code modified from his original video on how to create a quick python script to
# send garbage data to scammer
# His link: https://www.youtube.com/channel/UCrUL8K81R4VBzm-KOYwrcxQ
# The video in question: https://www.youtube.com/watch?v=UtNYzv8gLbs


import requests
import os
import random
import string
import json
import time

chars1 = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

# Open names, words, and domains dictionaries
names = json.loads(open('names.json').read())
words = json.loads(open('words.json').read())
domains = json.loads(open('domains.json').read())

while True:
    # Sleep random number of seconds as to not DDOS the site and make it harder for them to ignore blocks of flooded fake
    # based on time stamps.
    time.sleep(random.randint(1, 3))

    # Grab a random domain from the domains.json list
    domain = random.choice(domains)

    # USER NAME CREATION
    if random.getrandbits(1):

        name = random.choice(names)

    else:
        name_words = random.sample(words, 2)
        name = "".join(name_words)

    # Create a random number to add to the end of usernames
    name_extra = ''.join(random.choice(string.digits) for i in range(random.randint(1, 4)))

    # Create the username from the dictionary, extra digits and a domain.
    username = name.lower() + name_extra + "@" + domain

    # PASSWORD CREATION
    if random.getrandbits(1):

        # Create a random 8 character password with letters defined in chars1 variable
        password = ''.join(random.choice(chars1) for i in range(8))

    else:
        pass_words = random.sample(words, 2)
        pass_extra = ''.join(random.choice(string.digits) for i in range(random.randint(0, 2)))
        password = "".join(pass_words) + pass_extra

    # The following commented lines of code are what will be needed from running DevTools in chrome and seeing the format
    # of the form data being sent to the scamming site. Feel ree to add more variables if there is a hash token that needs to be
    # passed as well but the majorite seem to have some variation of #username and #password. Replace the hashed names with the
    # correct variables called by the form and set the URL to the URL shown in the forn data.

    # url =

    # requests.post(url, allow_redirects=False, data={
    #     '#username': username,
    #     '#password': password
    # })

    print "sending username %s and password %s" % (username, password)
