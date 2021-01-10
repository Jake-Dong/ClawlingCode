import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
import csv
#  abc 운동화
# 운동화,스포츠,구두,센들,부츠
cate =['1000000245','1000000249','1000000254','1000000260','1000000266']


for i in cate:
    name_list = []    
    for page in range(1,17):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        url = 'https://abcmart.a-rt.com/display/search-word/result/list?searchPageType=category&ctgrNo='+str(i)+'&brand=000003&brand=000074&brand=000125&brand=000032&brand=000050&brand=000081&brand=000048&brand=000054&brand=000058&brand=000072&chnnlNo=10001&ctgrLevel=1&leafCtgrYn=N&pageColumn=4&sort=latest&perPage=100&rdoProdGridModule=col4&resultExistSmartFilter=Y&page='+str(page)+'&_=1600341975816'
        driver = webdriver.Chrome(r'D:\big11\tools\chromedriver.exe',options=options)
        driver.get(url)
        time.sleep(5)
        brand_name = driver.find_elements_by_class_name('prod-brand')
        momal_name = driver.find_elements_by_class_name('prod-name')
        shoes_price = driver.find_elements_by_class_name('price-cost')
        for q,w,e in zip(brand_name,momal_name,shoes_price):
            name_list.append([q.text,w.text,e.text,'{}'.format(i)])
        driver.close()
    f = open('{}.csv'.format(i), 'w', encoding='utf-8', newline='')
    csvWriter = csv.writer(f)
    csvWriter.writerow(['brand','prod-name','price-cost','category'])
    for i in name_list:
        csvWriter.writerow(i)
    f.close()
    print('완료')