import colorama, time, vk
from colorama import Fore
colorama.init()
print(Fore.LIGHTYELLOW_EX + 'Open this site:')
print(Fore.BLUE + 'https://oauth.vk.com/authorize?client_id=7289997&scope=photos,wall&response_type=token&v=5.103')
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
counter = 0
for item in keks.get('items')[::-1]:
    time.sleep(4)
    api.likes.add(type='photo', owner_id=page_id, item_id=item.get('id'))
    counter += 1
    print(Fore.LIGHTGREEN_EX + '\r' + 'Liked - ' + str(counter) + '/' + str(keks.get('count')), end='')
print('\n' + Fore.LIGHTCYAN_EX + "Successfully")