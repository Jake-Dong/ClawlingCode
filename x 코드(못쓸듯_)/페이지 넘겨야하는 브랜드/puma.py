from selenium import webdriver
import re
from bs4 import BeautifulSoup
import csv

# 푸마 카테고리 페이지 별 자동화.

def get_link(base_url):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome(r'C:\Users\Home\PycharmProjects\pythonProject1\chromedriver.exe', options=options)
    driver.implicitly_wait(4)
    driver.get(base_url)

    r = driver.find_elements_by_tag_name('li>div>a')
    img_a_href = []
    for i in r:
        href = i.get_attribute('href')
        img_a_href.append(href)
    return img_a_href

allsearchlist = []
for i in range(16):
    searchlist = []
    base_url = 'https://kr.puma.com/men/shoes/sneakers.html?category=11&color=&dir=&limit=&order=&p='+ str(i+1)
    aaa = get_link(base_url)
    for i in aaa:
        temp = []
        searchlist.append(temp)
        try:
            test = i.split('/')
            ss = test[3]
            bb = ss[:-5]
            temp.append(bb)
            print(bb)
        except:
            pass
            print('오류')
    print('다음')

    allsearchlist.append(searchlist)

f = open('pumatest2.csv', 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)
for i in allsearchlist:
    csvWriter.writerow(i)

f.close()
print('완료')