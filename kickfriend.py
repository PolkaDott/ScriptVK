import colorama, time, vk_api
from colorama import Fore
colorama.init()
print(Fore.LIGHTYELLOW_EX + 'Open this site:')
print(Fore.BLUE + 'https://oauth.vk.com/authorize?client_id=7289997&scope=friends&response_type=token&v=5.103')
print(Fore.LIGHTYELLOW_EX + 'Input your token: ', end='')
token = input()
session = vk_api.VkApi(token=token)
api = session.get_api()

#check auth
try:
    user_id = api.users.get()[0].get('id')
except vk.exceptions.VkAPIError:
    print(Fore.RED + 'Authentication is failed')
    exit(0)

while(True):
    print(Fore.LIGHTWHITE_EX + "\nInput friend's id you want to delete: ", end='')
    page_id = input()
    if page_id[-1] == '/':
        page_id = page_id[:-1]
    page_id = page_id.split('/')[-1]
    try:
        page_id = api.users.get(user_ids=page_id)[0].get('id') 
    except:
        print("This id is not correct")
        exit(0)
    api.account.ban(owner_id=page_id)
    try:
        api.account.ban(owner_id=page_id)
    except:
        pass
    api.account.unban(owner_id=page_id)
    print(Fore.LIGHTGREEN_EX + 'It deleted!')
    print(Fore.WHITE + 'To close program press CTRL+C...')
