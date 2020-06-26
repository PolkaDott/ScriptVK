import vk, datetime, colorama
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
req = api.groups.get(user_id=user_id)
ids = req.get('items')
if len(ids) == 0:
    print(Fore.LIGHTRED_EX + "There're no groups")
    exit(0)
file = open('groups-' + datetime.datetime.today().strftime("%d-%H-%M-%S") + '.txt', 'w', encoding='utf-8')
groups = api.groups.getById(group_ids=ids)
names = [x.get('name') for x in groups]
print(Fore.LIGHTRED_EX + '\n' + str(len(names)) + ' GROUPS:')
for i in range(len(names)):
    print(Fore.LIGHTBLUE_EX + f"{names[i]}: vk.com/club{ids[i]}")
    file.write(f"{names[i]}: vk.com/club{ids[i]}\n")
file.close()
print(Fore.RED + "\nLEAVE THESE GROUPS???(Y/N)", end='')
inp = input()
if inp != 'y' and inp != 'Y':
    print(Fore.RED + '\nREJECTED')
    exit(0)

privates = []
i = 0
while i < len(ids):
    try:
        if api.groups.getById(group_id=ids[i], fields='is_closed')[0].get('is_closed') != 0:
            privates.append(ids[i])
        elif api.groups.leave(group_id=ids[i]) == 1:
            print(Fore.GREEN + names[i] + ' vk.com/club' + str(ids[i]) + ' - Successfully!')
        else:
            print(Fore.RED + names[i] + ' vk.com/club' + str(ids[i]) + ' - Error!')
    except vk.exceptions.VkAPIError as error:
        i = i - 1
    i = i + 1

if len(privates) > 0:
    print(Fore.LIGHTRED_EX + "\nThere're privates groups:")
    for id in privates:
        print(Fore.LIGHTBLUE_EX + f"{api.groups.getById(group_id=id)[0].get('name')}: vk.com/club{id}")
    print(Fore.RED + "Leave their too(Y/N)?", end='')
    inp = input()
    if inp != 'y' and inp != 'Y':
        exit(0)
else:
    exit(0)

i = 0
while i < len(privates):
    try:
        if api.groups.leave(group_id=privates[i]) == 1:
            print(Fore.GREEN + names[i] + ': vk.com/club' + str(privates[i]) + ' - Successfully!')
        else:
            print(Fore.RED + names[i] + ': vk.com/club' + str(privates[i]) + ' - Error!')
    except vk.exceptions.VkAPIError as error:
        i = i - 1
    i = i + 1