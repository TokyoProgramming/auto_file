import requests

proxy = '140.227.238.217'
try:
    r = requests.get('https://httpbin.org/ip', proxies={'http':proxy, 'https':proxy}, timeout= 3)
except:
    print('failed')
    pass
    


# print(r.status_code)