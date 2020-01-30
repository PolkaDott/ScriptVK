import datetime
import colorama
import requests
import vk
import os
from colorama import Fore
colorama.init()
print(Fore.LIGHTYELLOW_EX + 'Open this site:')
print(Fore.BLUE + 'https://oauth.vk.com/authorize?client_id=7289997&scope=photos&response_type=token&v=5.103')
print(Fore.LIGHTYELLOW_EX + 'Input your token: ', end='')
token = input()
session = vk.Session(access_token=token)
api = vk.API(session, v=5.103)

#check auth
try:
    user_id = api.users.get()[0].get('id')
except vk.exceptions.VkAPIError:
    print(Fore.RED + 'Authentication is failed')
    exit(0)

print("Input a page id of the person whose saves you want to get: ", end='')
page_id = input()
try:
    int(page_id)
except: 
    print(Fore.RED + 'Id must include only digits')
    exit(0)

keks = api.photos.get(album_id='saved', count=1000, owner_id=page_id)
print('\nCount images: ' + str(keks.get('count')))
counter = 0
dir_path = './saves'+datetime.datetime.today().strftime("-%d-%H-%M-%S/")
dir = os.path.dirname(dir_path)
if not os.path.exists(dir):
    os.makedirs(dir)
for item in keks.get('items'):
    img = item.get('sizes')[-1].get('url')
    p = requests.get(img)
    counter += 1
    name = str(counter).zfill(3)+'_'+str(item.get('id'))+".jpg"
    out = open(dir_path+name, 'wb')
    out.write(p.content)
    out.close()
    print(Fore.LIGHTGREEN_EX + name + ' - saved' + Fore.RESET)
    