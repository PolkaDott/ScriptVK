import vk
import time
import colorama
from colorama import Fore
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
print('Input name of file with ')
filename = input()
file = open('groups.txt', 'r')
groups = file.read().split('\n')
ids = [group[group.rfind('/')+5:] for group in groups]
i = 0
privates = []
while i < len(ids):
    time.sleep(4)
    try:
        req = api.groups.getById(group_id=ids[i], fields='is_closed')
        if req[0].get('is_closed') != 0:
            privates.append(int(ids[i]))
        else:
            api.groups.join(group_id=ids[i])
    except vk.exceptions.VkAPIError as error:
        print(error)
        i = i - 1
    i = i + 1
    print(str(i))
if len(privates) > 0:
    for id in privates:
        print(f"{api.groups.getById(group_id=id)[0].get('name')}: {id}")
    print("\n\n\nThere're private groups. Join them too?(Y/N)", end='')
    inp = input()
    if inp == 'y' or inp == 'Y':
        i = 0
        while i < len(privates):
            try:
                api.groups.join(group_id=privates[i])
            except vk.exceptions.VkAPIError:
                i = i - 1
            i = i + 1
            

exit(0)


req = api.groups.get(user_id=179995182)
ids = req.get('items')
groups = api.groups.getById(group_ids=ids)
names = [x.get('name') for x in groups]
print(str(len(names))+'GROUPS:')
for i in range(len(names)):
    print("{0}: vk.com/club{1}".format(names[i], ids[i]))
print("\n\n\n\nLEAVE THESE GROUPS???(Y/N)", end='')
inp = input()
if inp != 'y' and inp != 'Y':
    print('\nREJECTED')
    exit(0)
isAccess = True
for id in ids:
    try:
        if api.groups.leave(group_id=id) != 1:
            isAccess = False
    except vk.exceptions.VkAPIError:
        print('yeee')
print(isAccess)
input()
for id in ids:
    api.groups.join(group_id=id)