import requests;

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

f = open('./data/all_sets.txt');
sets = f.readlines()
f.close();
f = open('./data/all_sets_details.json', 'w');
f.write('[\n');
for setid in sets:
    r = requests.get('https://us.api.battle.net/wow/item/set/%s?locale=en_US&apikey=nqc2bm6wcuyv8ux499rcrhrahp952waw' % setid.strip())
    f.write(r.text)
    # f.write('"https://us.api.battle.net/wow/item/set/%s?locale=en_US&apikey=nqc2bm6wcuyv8ux499rcrhrahp952waw",\n' % setid.strip())
    f.write(',\n');
f.write(']\n');
f.close()

print('done')
