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
    driver.get(base_url)

    r = driver.find_elements_by_xpath('/html/body/div[1]/div[4]/div[3]/div[2]/div[4]/ul/li/a')

    img_a_title = []
    for i in r:
        title = i.get_attribute('title')
        img_a_title.append(title)
    return img_a_title

# base_url = 'https://www.onitsukatiger.com/kr/ko-kr/mens-shoes/c/ko20201000/?start=0'
# aaa = get_link(base_url)
# print(aaa)
allsearchlist = []
for i in range(13):
    base_url = 'https://www.onitsukatiger.com/kr/ko-kr/mens-shoes/c/ko20201000/?start='+ str(i)
    aaa = get_link(base_url)
    allsearchlist.append(aaa)

f = open('Onitsukatiger.csv', 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)
for i in allsearchlist:
    csvWriter.writerow(i)

f.close()
print('완료')