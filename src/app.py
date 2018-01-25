import requests;

#=============================   Get all item sets ids =============================================================

#r = requests.get('https://us.api.battle.net/wow/item/set/1060?locale=en_US&apikey=nqc2bm6wcuyv8ux499rcrhrahp952waw')
#if r.ok:
#    print("itsok")

# for i in range(1, 100000):
#     #r = requests.get(`https://us.api.battle.net/wow/item/set/{i}?locale=en_US&apikey=nqc2bm6wcuyv8ux499rcrhrahp952waw`)
#     r = requests.get('https://us.api.battle.net/wow/item/set/%s?locale=en_US&apikey=nqc2bm6wcuyv8ux499rcrhrahp952waw' % i)
#     if r.ok:
#         print('%sth set got!' % i)
#     if i % 1000 == 0:
#         print('------ %s item sets checked --------' % i)

# print('done!');
#=============================   Get all item sets ids =============================================================




#=============================   Get all item sets contexts =============================================================
# f = open('./data/all_sets.txt');
# sets = f.readlines()
# f.close();
# f = open('./data/all_sets_details.json', 'w');
# f.write('[\n');
# for setid in sets:
#     r = requests.get('https://us.api.battle.net/wow/item/set/%s?locale=en_US&apikey=nqc2bm6wcuyv8ux499rcrhrahp952waw' % setid.strip())
#     f.write(r.text)
#     # f.write('"https://us.api.battle.net/wow/item/set/%s?locale=en_US&apikey=nqc2bm6wcuyv8ux499rcrhrahp952waw",\n' % setid.strip())
#     f.write(',\n');
# f.write(']\n');
# f.close()

# print('done')
#=============================   Get all item sets contexts =============================================================



#=============================   Get all item sets item ids =============================================================
# import json
# f = open('./data/all_sets_details.json')
# itemsets = json.loads(f.read())
# f.close()
# itemids = []
# for itemset in itemsets:
#     items = itemset['items']
#     itemids += items

# f = open('./data/all_set_items.txt', 'w')

# for item in itemids:
#     f.write(str(item) + '\n');

# f.close()

# print('done')
#=============================   Get all item sets item ids =============================================================


#=============================   Get all item set item contexts =============================================================
# f = open('./data/all_set_items.txt');
# setitems = f.readlines()
# f.close();
# f = open('./data/all_sets_item_details.json', 'w');
# f.write('[\n');
# for setitem in setitems:
#     r = requests.get('https://us.api.battle.net/wow/item/%s?locale=en_US&apikey=nqc2bm6wcuyv8ux499rcrhrahp952waw' % setitem.strip())
#     f.write(r.text)
#     # f.write('"https://us.api.battle.net/wow/item/set/%s?locale=en_US&apikey=nqc2bm6wcuyv8ux499rcrhrahp952waw",\n' % setid.strip())
#     f.write(',\n');
# f.write(']\n');
# f.close()

# print('done')
#=============================   Get all item set item contexts =============================================================
16437