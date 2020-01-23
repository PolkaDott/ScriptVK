import vk
import colorama
from colorama import Fore, Style
colorama.init()
token = 'b698d21d19ad8723bf0fc3362bc71b9f5c9d4a16bbad9c682e2a249650a71665f523ddcb4f2e5e51406ae'
session = vk.Session(access_token=token)
api = vk.API(session, v=5.103)
user_id = api.users.get()[0].get('id')
req = api.groups.get(user_id=user_id)
ids = req.get('items')
if len(ids) == 0:
    print(Fore.LIGHTRED_EX + "There're no groups")
    exit(0)
groups = api.groups.getById(group_ids=ids)
names = [x.get('name') for x in groups]
print(Fore.LIGHTRED_EX + str(len(names)) + ' GROUPS:')
for i in range(len(names)):
    print(Fore.LIGHTBLUE_EX + f"{names[i]}: vk.com/club{ids[i]}")
print(Fore.RED + "\nLEAVE THESE GROUPS???(Y/N)\n->", end='')
inp = input()
if inp != 'y' and inp != 'Y':
    print('\nREJECTED')
    exit(0)
i = 0
while i < len(ids):
    try:
        if api.groups.leave(group_id=ids[i]) == 1:
            print(Fore.GREEN + names[i] + ' vk.com/club' + str(ids[i]) + ' - Successfully!')
        else:
            print(Fore.RED + names[i] + ' vk.com/club' + str(ids[i]) + ' - Error!')
    except vk.exceptions.VkAPIError as error:
        i = i - 1
    i = i + 1
