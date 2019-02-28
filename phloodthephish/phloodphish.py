# Inspired by the Engineer Man on Youtube. Code modified from his original video on how to create a quick python script to
# send garbage data to scammer
# His link: https://www.youtube.com/channel/UCrUL8K81R4VBzm-KOYwrcxQ
# The video in question: https://www.youtube.com/watch?v=UtNYzv8gLbs
# Password and Name dictionaries sourced from https://github.com/danielmiessler/SecLists

import requests
import os
import random
import string
import json
import time
import argparse

chars1 = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

parser = argparse.ArgumentParser(
    prog='phlood',
    description='phlood.py generates random emails and passwords and allows you to send to specific phishing site.',
)

parser.add_argument(
    '-u',
    '--url',
    type=str,
    help='The URL of the phishing site. If not used, will just generate username/password pairs to std_out.',
)

parser.add_argument(
    '-i',
    '--interval',
    type=int,
    help='The number of iterations to run through the script',
    default=10000,
)

parser.add_argument(
    '-t',
    '--time',
    type=int,
    help='The delay between sending the data in seconds. Default is 600 seconds or 10 minutes.',
    default=600,
)

parser.add_argument(
    '-d',
    '--domain',
    type=str,
    help='Specifiy a domain to use for email addresses.',
)

parser.add_argument(
    '--uvar',
    type=str,
    help='Set the form name for the username.',
    default='username',
)

parser.add_argument(
    '--pvar',
    type=str,
    help='Set the form name for the password.',
    default='password',
)

a = parser.parse_args()

# Open names, words, and domains dictionaries
names = json.loads(open('names.json').read())
words = json.loads(open('words.json').read())
surnames = json.loads(open('surnames.json').read())
pswds = json.loads(open('passwords.json').read())
useragents = json.loads(open('useragents.json').read())

for i in range(a.interval):
    # Sleep random number of seconds as to not DDOS the site and make it harder for them to ignore blocks of flooded fake
    # based on time stamps.
    time.sleep(a.time)

    # Grab a random domain from the domains.json list
    if a.domain:
        domain = a.domain
    else:
        domains = json.loads(open('domains.json').read())
        domain = random.choice(domains)

    # USER NAME CREATION
    if random.getrandbits(1):

        name = random.choice(names)

        if random.randint(1, 10) == 1:
            name += '.' + random.choice(surnames)

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
        password = ''.join(random.choice(chars1) for i in range(random.randint(8, 12)))

    elif random.getrandbits(1):
        pass_words = random.sample(words, 2)
        pass_extra = ''.join(random.choice(string.digits) for i in range(random.randint(0, 2)))
        password = "".join(pass_words) + pass_extra
    else:
        password = random.choice(pswds)

    user_agent = random.choice(useragents)

    data = {
        a.uvar: username,
        a.pvar: password
    }

    header = {
        'User-Agent': user_agent
    }

    # The following commented lines of code are what will be needed from running DevTools in chrome and seeing the format
    # of the form data being sent to the scamming site. Feel ree to add more variables if there is a hash token that needs to be
    # passed as well but the majorite seem to have some variation of #username and #password. Replace the hashed names with the
    # correct variables called by the form and set the URL to the URL shown in the forn data.

    if a.url:

        requests.post(a.url, allow_redirects=False, data=data)

    print("sending username {} and password {} \n headers {}".format(username, password, header))
