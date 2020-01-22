import vk
import colorama
from colorama import Fore, Style
colorama.init()
token = '12074ed1388c45383ab0751cb5e70ff6978413ea80ded624cbbd7796b30228697bbe66a2c9c88e68d2303'
session = vk.Session(access_token=token)
api = vk.API(session, v=5.103)
user_id = api.users.get()[0].get('id')
req = api.groups.get(user_id=user_id)
ids = req.get('items')
groups = api.groups.getById(group_ids=ids)
names = [x.get('name') for x in groups]
print(Fore.CYAN + Style.BRIGHT + str(len(names)) + ' GROUPS:')
for i in range(len(names)):
    print(Fore.GREEN + f"{names[i]}: vk.com/club{ids[i]}")
print(Fore.YELLOW + "\n\n\n\nLEAVE THESE GROUPS???(Y/N)\n->", end='')
inp = input()
if inp != 'y' and inp != 'Y':
    print('\nREJECTED')
    exit(0)
isAccess = True
i = 0
while i < len(ids):
	try:
		api.groups.leave(group_id=ids[i])
	except:
		print('yeee')
		i = i - 1
	i = i + 1
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