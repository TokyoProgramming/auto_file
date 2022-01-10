import requests
from selenium import webdriver
from bs4 import BeautifulSoup

page = requests.get('https://mainichi.jp/oshosen-kifu/220109.html')
soup = BeautifulSoup(page.content, 'html.parser')

# url = 'https://mainichi.jp/oshosen-kifu/220109.html'

# driver = webdriver.Chrome()
# driver.get(url)
# stages = driver.find_element_by_class_name('tesu-list')
# driver.close()

# soup = BeautifulSoup(driver.page_source, 'html.parser')

a_tag = soup.find_all('div', {'class': 'unit-save button'})
print(a_tag)
for a in soup.find_all('a', href=True):
    print("Found the URL:", a['href'])

a_href = 'https://cdn.mainichi.jp/vol1/shougi/kif/ousho202201090101.kif'
