import requests

https_proxy = "https://37.61.224.234:8195"

proxyDict = {
    "https": https_proxy,
}


def get_msg():
    url = 'https://api.telegram.org/'
    r = requests.get(url, proxies=proxyDict)
    print(r)

get_msg()
