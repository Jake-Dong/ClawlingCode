import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
import csv

url = "https://www.nike.com/kr/ko_kr/w/women/fw"

allshos_list =[]


for i in range(9):

    params = {
        'page': i,
        'pageSize': 25,
        'lineSize': 4,
        '_': 1599310375345
    }
    headers = {
        'referer': url,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }

    res = requests.get(url, params=params, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    lis = soup.find_all('li', {'class': 'ncss-col-sm-6 ncss-col-md-6 ncss-col-lg-4 grid-wall-list-item'})
    for li in lis:
      item_title = li.find('span', {'class': 'item-title'}).text
      product_kate = li.find('span',{'class':'text-color-secondary'}).text
      productId = li.find('input', {'name': 'productId'})['value']
      aaa = [ productId,item_title,product_kate]

      allshos_list.append(aaa)

print(allshos_list)

f = open('NikeWomen.csv', 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)
for i in allshos_list:
    csvWriter.writerow(i)

f.close()
print('완료')


