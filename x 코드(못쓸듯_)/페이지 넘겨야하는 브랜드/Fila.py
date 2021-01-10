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


    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    r = soup.select('#productList > li > a.txt_box.txt-box__new > div.name > p:nth-child(2)')

    return r

# base_url = 'https://www.fila.co.kr/product/list.asp?no=922&gender=&page=3&sortVal=4&colorVal=0&priceVal=0&sizeVal=0'
# aaa = get_link(base_url)
# for i in aaa:
#     print(i)
allsearchlist = []
for i in range(8):
    base_url = 'https://www.fila.co.kr/product/list.asp?no=922&gender=&page='+ str(i+1)
    aaa = get_link(base_url)
    allsearchlist.append(aaa)

print(allsearchlist)
f = open('Fila.csv', 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)
for i in allsearchlist:
    csvWriter.writerow(i)

f.close()
print('완료')