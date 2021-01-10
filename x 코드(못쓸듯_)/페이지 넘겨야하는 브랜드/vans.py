from selenium import webdriver
import re
from bs4 import BeautifulSoup
import csv


def get_link(url):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome(r'C:\Users\Home\PycharmProjects\pythonProject1\chromedriver.exe', options=options)
    driver.get(url)

    r = driver.find_elements_by_tag_name('div>a')
    img_a_href = []
    for i in r:
        href = i.get_attribute('href')
        img_a_href.append(href)
    return img_a_href


url = 'https://shop.vans.co.kr/category/men/classic'
aaa = get_link(url)

searchlist = []

for i in aaa:
    temp = []
    try:
        test = i.split('/')
        ss = test[4]
        temp.append(ss)
    except:
        pass
    searchlist.append(temp)

print(searchlist)
f = open('classic.csv', 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)
for i in searchlist:
    csvWriter.writerow(i)

f.close()
print('완료')