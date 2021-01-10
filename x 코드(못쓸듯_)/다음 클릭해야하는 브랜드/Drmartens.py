from selenium import webdriver
import re
from bs4 import BeautifulSoup
import csv
from selenium.webdriver.common.keys import Keys
import time


def get_link(base_url):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome(r'C:\Users\Home\PycharmProjects\pythonProject1\chromedriver.exe', options=options)
    driver.implicitly_wait(4)
    driver.get(base_url)
    click = driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/div/div[2]/div/div/button/span')

    while True:
        try:
            time.sleep(2)
            click.click()
        except:
            break
    r = driver.find_elements_by_tag_name('div > ul > li > div > div > h2 > a')
    img_a_href = []
    for i in r:
        href = i.get_attribute('href')
        img_a_href.append(href)
    return img_a_href

base_url = 'https://www.drmartens.co.kr/items/mens-footwear'
allsearchlist = []
aaa = get_link(base_url)

for i in aaa:
    test = i.split('/')
    ss = test[4]
    print(ss)
    allsearchlist.append(ss)


f = open('Drmartens.csv', 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)
for i in allsearchlist:
    csvWriter.writerow(i)

f.close()
print('완료')