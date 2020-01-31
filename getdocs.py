import datetime
import colorama
import requests
import vk
import re
import os
from colorama import Fore
colorama.init()
print(Fore.LIGHTYELLOW_EX + 'Open this site:')
print(Fore.BLUE + 'https://oauth.vk.com/authorize?client_id=7289997&scope=docs&response_type=token&v=5.103')
print(Fore.LIGHTYELLOW_EX + 'Input your token: ', end='')
token = input()
session = vk.Session(access_token=token)
api = vk.API(session, v=5.103)

#check auth
try:
    api.users.get()[0].get('id')
except vk.exceptions.VkAPIError:
    print(Fore.RED + 'Authentication is failed')
    exit(0)

keks = api.docs.get()
print('\nCount docs: ' + str(keks.get('count')))
counter = 0
dir_path = './docs'+datetime.datetime.today().strftime("-%d-%H-%M-%S/")
dir = os.path.dirname(dir_path)
if not os.path.exists(dir):
    os.makedirs(dir)
for item in keks.get('items'):
    doc = item.get('url')
    p = requests.get(doc)
    counter += 1
    name = str(counter).zfill(3)+'_'+re.sub(r'[?:<>/\\\"*|]','',str(item.get('title')))+('.'+item.get('ext') if not item.get('title').endswith(item.get('ext')) else '')
    out = open(dir_path+name, 'wb')
    out.write(p.content)
    out.close()
    print(Fore.LIGHTGREEN_EX + name + ' - saved' + Fore.RESET)
    