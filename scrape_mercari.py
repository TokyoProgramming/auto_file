from selenium import webdriver
import time
import pandas
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service




options = Options()
options.add_argument('--headless')

CHROMEDRIVER = Service("C:/Users/tokyo/Downloads/softwares/chromedriver_win32/chromedriver.exe")

driver = webdriver.Chrome(service= CHROMEDRIVER)
driver.get('https://jp.mercari.com/item/m84680014499')
time.sleep(10)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


name_tag = soup.find_all(attrs={'data-testid' : 'name'})
price_tag = soup.find_all(attrs={'data-testid' : 'price'})
heart_tag = soup.find_all(attrs={'data-testid' : 'icon-heart-button'})

status_tag = soup.find_all(attrs={'data-testid': 'checkout-button'})



name = name_tag[0]['title-label']
price = price_tag[0]['value']
heart = heart_tag[0]['label']
status = status_tag[0].text

print(name)
print(price)
print(heart)
print(status)







time.sleep(5)
driver.close()

