from selenium import webdriver
import re
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
import csv
# 어글리슈즈
shoesname_list = []
model_list = []

allshos_list = []
for i in range(1):
    url ='https://www.drmartens.co.kr/items/womens-footwear-sandals?page='+ str(i+1)
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome(r'C:\Users\Home\PycharmProjects\pythonProject1\chromedriver.exe', chrome_options=options)
    driver.get(url)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    shoes_name = soup.select('#vue-body > div > div.ProductListContainer__body > div > ul > li > div > div.contents-column.left > h2 > a')
    model_name = driver.find_elements_by_xpath('/html/body/div[1]/main/div[2]/div/div[2]/div/ul/li/a')
    for i in shoes_name:
        zz = i.get_text().strip()
        shoesname_list.append(zz)
    for j in model_name:
        xx = j.get_attribute('href')
        ss = xx.split('/')[4]
        model_list.append(ss)

    for q,w in zip(model_list,shoesname_list):
        zz = [q,w,'샌들']
        allshos_list.append(zz)



f = open('DrmartensWomen3.csv', 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)
for i in allshos_list:
    csvWriter.writerow(i)

f.close()
print('완료')
