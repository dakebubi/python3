import requests


def do_request():
    # r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
    r = requests.get('https://www.baidu.com')
    print(r.status_code)
    print(r.headers['content-type'])
    print(r.encoding)
    print(r.text)
    print(r.cookies.__len__())
    d = r.cookies;
    for (d, x) in d.items():
        print("key: " + d + ", value: " + x)
