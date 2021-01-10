import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
import csv
#  abc 운동화
page = 0
name_list = []
for page in range(1,3):
    url = 'https://abcmart.a-rt.com/display/search-word/result/list?searchPageType=category&ctgrNo=1000000266&brand=000003&brand=000074&brand=000125&brand=000032&brand=000050&brand=000081&brand=000048&brand=000054&brand=000058&brand=000072&chnnlNo=10001&ctgrLevel=1&leafCtgrYn=N&pageColumn=4&sort=latest&perPage=100&rdoProdGridModule=col4&resultExistSmartFilter=Y&page='+str(page)+'&_=1600341975816'
    driver = webdriver.Chrome(r'C:\Users\Home\PycharmProjects\pythonProject1\chromedriver.exe')
    driver.get(url)
    time.sleep(5)
    brand_name = driver.find_elements_by_class_name('prod-brand')
    momal_name = driver.find_elements_by_class_name('prod-name')
    shoes_price = driver.find_elements_by_class_name('price-cost')
    for q,w,e in zip(brand_name,momal_name,shoes_price):
        name_list.append([q.text,w.text,e.text,'boots'])
    driver.close()

f = open('boots.csv', 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)
csvWriter.writerow(['brand','prod-name','price-cost','category'])
for i in name_list:
    csvWriter.writerow(i)
f.close()
print('완료')
