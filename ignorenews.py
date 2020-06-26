import colorama, time, vk_api
from colorama import Fore
colorama.init()
print(Fore.LIGHTYELLOW_EX + 'Open this site:')
print(Fore.BLUE + 'https://oauth.vk.com/authorize?client_id=7289997&scope=wall&response_type=token&v=5.103')
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

friends = api.friends.get().get('items')
friends = ','.join([str(x) for x in friends])
api.newsfeed.addBan(user_ids=friends)
print(Fore.GREEN + 'Successfully!')
