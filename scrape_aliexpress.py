import requests
import json
import re

target = ["title", "itemDetailUrl", "imagePath"]


def main(url):
    r = requests.get(url)
    match = re.search(r'data: ({.+})', r.text).group(1)
    data = json.loads(match)
    goal = [data['pageModule'][x] for x in target] + \
        [data['priceModule']['formatedActivityPrice']]
    return goal


res = main("https://ja.aliexpress.com/item/32867673917.html?gatewayAdapt=glo2jpn")
 

for item in res:
    print(item)
