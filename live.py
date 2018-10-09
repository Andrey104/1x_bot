import json
import urllib.request


url = "https://1xstavka.ru/LiveFeed/Get1x2_VZip?count=500&mode=4&country=1&partner=51"
contents = urllib.request.urlopen(url).read()
contents_dict = json.loads(contents)
value = contents_dict.get('Value')
k = 0
for i in value:
    e = i.get('E')
    for j in e:
        if j.get('T') == 9 and j.get('P') == 2.5 and j.get('C') > 2:
            k = k + 1
            print(k)
            print(i.get('L'))
            print(i.get('O1'))
            print(i.get('O2'))
            print('ТОТАЛ: ' + str(j.get('P')))
            print('Коэффицент: ' + str(j.get('C')))
            # print(i)