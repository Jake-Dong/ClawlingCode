from selenium import webdriver
import csv
import re
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
base_url =  'https://www.lsnmall.com/display.do?cmd=categoryMain&CAT_GB=10002&TCAT_CD=2361&MCAT_CD=2368'
driver = webdriver.Chrome(r'C:\Users\Home\PycharmProjects\pythonProject1\Modelname\chromedriver.exe')
driver.implicitly_wait(4)
driver.get(base_url)


html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
r = soup.select('#listBox > li > p.tit > span')

body = driver.find_element_by_css_selector('body')
driver.implicitly_wait(5)
allsearchlist = []
for i in range(20):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    for i in r:

        allsearchlist.append(i)

print(allsearchlist)

f = open('Prospecs.csv', 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)
for i in allsearchlist:
    csvWriter.writerow(i)

f.close()
print('완료')