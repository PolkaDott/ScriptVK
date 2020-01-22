import vk
token = 'c352d7dc22e17b26305c7261764455d677b07891fcbaf2354201db987eb5a39a773ba10c9cb4380a1a71a'
session = vk.Session(access_token=token)
api = vk.API(session, v=5.103)
req = api.groups.get(user_id=179995182)
ids = req.get('items')
groups = api.groups.getById(group_ids=ids)
names = [x.get('name') for x in groups]
print(str(len(names))+'GROUPS:')
for i in range(len(names)):
    print("{0}: vk.com/club{1}".format(names[i], ids[i]))
print("\n\n\n\nLEAVE THESE GROUPS???(Y/N)\n->", end='')
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