from bs4 import BeautifulSoup
import requests
import webbrowser
import os
import random
from time import  sleep
import pandas as pd



data_url = 'https://item.fril.jp/bc643a0594ab8b489ba3e0dfd590d930?_gl=1*1rk01pr*_ga*MTI4MjE1NjkzLjE2NDI0OTUxNzI.*_ga_7KV9PBS698*MTY0MjQ5NTE3Mi4xLjEuMTY0MjQ5NTE3Ny41NQ..'


data_url = 'https://fril.jp/category/10001' 
data_url2 = 'https://fril.jp/category/682'
url_list = []
def mercari_url(url):


    user_agents = [ 
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36', 
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36', 
        'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148', 
        'Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36' 
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    ] 
    user_agent = random.choice(user_agents) 
    headers = {'User-Agent': user_agent} 

    page = requests.get(url, headers = headers)
    sleep(random.randint(0, 3)/2)
    soup = BeautifulSoup(page.content, 'html.parser')
    sleep(random.randint(0, 3)/3)


    # name_tag = soup.find_all('h1',{'class': 'item__name'}) 
    # pic_tag = soup.find_all('img', {'class': 'sp-image'})
    # price_tag = soup.find_all('span', {'class': 'item__value'})
    a_tag = soup.find_all('a', {'class': 'link_category_image'})
    for a in a_tag:
        if a:
            href = a.get('href')
            url_list.append(href)


    sleep(random.randint(0, 3)/3)

    # pics = len(pic_tag)
    # name = name_tag[0].text
    # price = price_tag[0].text

    # url = "https://notify-api.line.me/api/notify"
    # access_token = '1jBTn8eMfxeX6SdkgcWZNv6ZzHqpwTdjkvO3cyfluMQ'
    # headers = {'Authorization': 'Bearer ' + access_token}

    # message = name + 'is' + price + 'now<br/>' + data_url
    # payload = {'message': message}
    # r = requests.post(url, headers= headers, params=payload)


    # print(r)

    return url_list

lists = [data_url, data_url2]
# for 
# mercari_url()

target = []
for url in lists:
    res = mercari_url(url)
    target = target + res

    df = pd.DataFrame(target, columns=['URL'])
    writer = pd.ExcelWriter('rakuma_url.xlsx')
    df.to_excel(writer, sheet_name='sheet1')
    writer.save()

# print(len(url_list))