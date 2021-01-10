import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
import csv

url = "https://www.converse.co.kr/category/shoes?productSubType=MEN"

allshos_list =[]


for i in range(13):

    params = {
        'page': i,
        'pageSize': 40,
        'lineSize': 5,
        '_': 1599310375345
    }
    headers = {
        'referer': url,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }

    res = requests.get(url, params=params, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    lis = soup.find_all('div', {'class': 'plp-grid-item col-6 col-md-4 col-lg-3'})
    for li in lis:
      item_title = li.find('p').text
      # product_display_price = li.find('p', {'class': 'product-display-price'})
      # product_kate = li.find('span',{'class':'text-color-secondary'}).text
      productId = li.find('a', {'class': 'text-link'})

      aaa = [ productId,item_title,'운동화']

      allshos_list.append(aaa)

print(allshos_list)

f = open('ConverseMen.csv', 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)
for i in allshos_list:
    csvWriter.writerow(i)

f.close()
print('완료')
#
#
