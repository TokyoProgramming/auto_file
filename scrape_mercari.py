from selenium import webdriver
import time
import pandas
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



options = Options()
options.add_argument('--headless')

CHROMEDRIVER = Service("C:/Users/tokyo/Downloads/softwares/chromedriver_win32/chromedriver.exe")

driver = webdriver.Chrome(service= CHROMEDRIVER)
driver.get('https://jp.mercari.com/item/m84680014499')
time.sleep(8)

time.sleep(5)
driver.close()

