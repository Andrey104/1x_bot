import datetime
import urllib.request

from flask import json


# Парсим линию
def parse_line():
    url = "https://1xstavka.ru/LineFeed/Get1x2_VZip?sports=1&count=500&tf=1430&tz=3&mode=4&country=1&partner=51&getEmpty=true"
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


# Парсим лайв
def parse_live():
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


def parse_basket():
    url = 'https://1xstavka.ru/LineFeed/Get1x2_VZip?sports=3&count=500&tf=2200000&tz=3&mode=4&country=1&partner=51&getEmpty=true'
    contents = urllib.request.urlopen(url).read()
    contents_dict = json.loads(contents)
    value = contents_dict.get('Value')
    res = ''
    k = 0
    for i in value:
        e = i.get('E')
        for j in e:
            if j.get('T') == 9:
                k = k + 1
                res += str(k) + '\n'
                res += i.get('L') + '\n'
                res += i.get('O1') + '\n'
                res += i.get('O2') + '\n'
                res += 'ТОТАЛ: ' + str(j.get('P')) + '\n'
                if i.get('S'):
                    res += datetime.datetime.fromtimestamp(int(i.get('S'))).strftime('%Y-%m-%d %H:%M:%S') + '\n'
    return res


def parse_handball():
    url = 'https://1xstavka.ru/LineFeed/Get1x2_VZip?sports=8&count=500&tf=2200000&tz=3&mode=4&country=1&partner=51&getEmpty=true'
    contents = urllib.request.urlopen(url).read()
    contents_dict = json.loads(contents)
    value = contents_dict.get('Value')
    res = ''
    k = 0
    for i in value:
        e = i.get('E')
        for j in e:
            if j.get('T') == 9:
                k = k + 1
                res += str(k) + '\n'
                res += i.get('L') + '\n'
                res += i.get('O1') + '\n'
                res += i.get('O2') + '\n'
                res += 'ТОТАЛ: ' + str(j.get('P')) + '\n'
                if i.get('S'):
                    res += datetime.datetime.fromtimestamp(int(i.get('S'))).strftime('%Y-%m-%d %H:%M:%S') + '\n'
    return res


def parse_handball_html():
    url = 'https://1xstavka.ru/LineFeed/Get1x2_VZip?sports=8&count=500&tf=2200000&tz=3&mode=4&country=1&partner=51&getEmpty=true'
    contents = urllib.request.urlopen(url).read()
    contents_dict = json.loads(contents)
    value = contents_dict.get('Value')
    res = 'ГАНДБОЛ <br>'
    k = 0
    for i in value:
        e = i.get('E')
        for j in e:
            if j.get('T') == 9:
                k = k + 1
                res += str(k) + '<br>'
                res += i.get('L') + '<br>'
                res += i.get('O1') + '<br>'
                res += i.get('O2') + '<br>'
                res += 'ТОТАЛ: ' + str(j.get('P')) + '<br>'
                if i.get('S'):
                    res += datetime.datetime.fromtimestamp(int(i.get('S'))).strftime('%Y-%m-%d %H:%M:%S') + '<br>'
    return res


def parse_basket_html():
    url = 'https://1xstavka.ru/LineFeed/Get1x2_VZip?sports=3&count=500&tf=2200000&tz=3&mode=4&country=1&partner=51&getEmpty=true'
    contents = urllib.request.urlopen(url).read()
    contents_dict = json.loads(contents)
    value = contents_dict.get('Value')
    res = 'БАСКЕТБОЛ <br>'
    k = 0
    for i in value:
        e = i.get('E')
        for j in e:
            if j.get('T') == 9:
                k = k + 1
                res += str(k) + '<br>'
                res += i.get('L') + '<br>'
                res += i.get('O1') + '<br>'
                res += i.get('O2') + '<br>'
                res += 'ТОТАЛ: ' + str(j.get('P')) + '<br>'
                if i.get('S'):
                    res += datetime.datetime.fromtimestamp(int(i.get('S'))).strftime('%Y-%m-%d %H:%M:%S') + '<br>'
    return res
