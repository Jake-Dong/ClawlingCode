from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
import csv
import re
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
base_url =  'https://www.zara.com/kr/ko/man-shoes-sneakers-l797.html?v1=1546897'
driver = webdriver.Chrome(r'D:\big11\[90]tools\chromedriver.exe', options=options)
driver.implicitly_wait(4)
driver.get(base_url)
body = driver.find_element_by_css_selector('body')
for i in range(100):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
r = soup.select('div > div.product-info-item.product-info-item-name > a')
allsearchlist = []
for i in r:
   tt= i.get_text() 
   print(tt)
    allsearchlist.append(tt)

f = open('zara1.csv', 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)
for i in allsearchlist:
    csvWriter.writerow(i)

f.close()
print('완료')