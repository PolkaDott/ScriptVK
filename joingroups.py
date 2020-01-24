import vk
import time
import re
import colorama
from colorama import Fore
colorama.init()

print(Fore.LIGHTYELLOW_EX + 'Open this site:')
print(Fore.BLUE + 'https://oauth.vk.com/authorize?client_id=7289997&scope=groups&response_type=token&v=5.103')
print(Fore.LIGHTYELLOW_EX + 'Input your token: ', end='')
token = input()
session = vk.Session(access_token=token)
api = vk.API(session, v=5.103)
try:
    user_id = api.users.get()[0].get('id')
except vk.exceptions.VkAPIError:
    print(Fore.RED + 'Authentication is failed')
    exit(0)

print('Input file\'s name with groups: ', end='')
filename = input()
file = open(filename, 'r', encoding='utf-8')
groups = file.read().split('\n')
ids = [re.findall(r'\d+', group)[-1] for group in groups if group != [] and re.search(r'\d', group) != None]
if len(ids) == 0:
    print(Fore.RED + 'file sucks')
    exit(0)
i = 0

privates = []
while i < len(ids):
    time.sleep(4)
    try:
        req = api.groups.getById(group_id=ids[i], fields='is_closed')
        if req[0].get('is_closed') != 0:
            privates.append(int(ids[i]))
        elif api.groups.join(group_id=ids[i]) == 1:
            print(Fore.GREEN + req[0].get('name') + ': vk.com/club' + str(ids[i]) + ' - Successfully!')
        else:
            print(Fore.RED + req[0].get('name') + ': vk.com/club' + str(ids[i]) + ' - Error!')
    except vk.exceptions.VkAPIError as error:
        print(Fore.RED + error)
    i = i + 1

if len(privates) > 0:
    print(Fore.LIGHTRED_EX + "\nThere're privates groups:")
    for id in privates:
        print(Fore.LIGHTBLUE_EX + f"{api.groups.getById(group_id=id)[0].get('name')}: vk.com/club{id}")
    print(Fore.RED + "Join their too(Y/N): ", end='')
    inp = input()
    if inp != 'y' and inp != 'Y':
        exit(0)
else:
    exit(0)

i = 0
while i < len(privates):
    time.sleep(4)
    try:
        if api.groups.join(group_id=privates[i]) == 1:
            print(Fore.GREEN + api.groups.getById(group_id=privates[i])[0].get('name') + ': vk.com/club' + str(privates[i]) + ' - Successfully!')
        else:
            print(Fore.RED + api.groups.getById(group_id=privates[i])[0].get('name') + ': vk.com/club' + str(privates[i]) + ' - Error!')
    except vk.exceptions.VkAPIError as error:
        print(Fore.RED + error)
    i = i + 1