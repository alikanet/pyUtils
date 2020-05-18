import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))
providers = ['@yahoo.com', '@gmail.com', '@aol.com', '@tmobile.net', '@verizion.net', '@outlook.com']
print(random.choice(providers))

url = 'http://craigslist.pottsfam.com/index872dijasydu2iuad27aysdu2yytaus6d2ajsdhasdasd2.php'

names = json.loads(open('names.json').read())

for name in names:
    name_extra = random.choice(range(1939, 2012))
    username = f'{name.lower()}_{random.choice(string.ascii_letters)}{name_extra}{random.choice(providers)}'
    password = ''.join(random.choice(chars) for i in range(8))
    print(f'sending username {username} and password {password}')
    requests.post(url, allow_redirects=False, data={'auid2yjauysd2uasdasdasd': username,'kjauysd6sAJSDhyui2yasd': password})

print('All Done!')