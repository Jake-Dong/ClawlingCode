import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
import csv

url = "https://shop.vans.co.kr/category/women/allshoes"

allshos_list =[]


for i in range(11):

    params = {
        'page': i,
        'pageSize': 20,
        'lineSize': 5,

    }
    headers = {
        'referer': url,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }

    res = requests.get(url, params=params, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    lis = soup.select('#wrapper > main > section > div.plp-container.flex > section > div.plp-grid.row.item-list-wrap > div')
    for li in lis:
        item_title = li.find('a').text
        productId = li.find('p', {'data-id': 'name'})['data-id']
        aaa = [item_title]
        allshos_list.append(aaa)

print(allshos_list)
#
# f = open('VansWomen.csv', 'w', encoding='utf-8', newline='')
# csvWriter = csv.writer(f)
# for i in allshos_list:
#     csvWriter.writerow(i)
#
# f.close()
# print('완료')

