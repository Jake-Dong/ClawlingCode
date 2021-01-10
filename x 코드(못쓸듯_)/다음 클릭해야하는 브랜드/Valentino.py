from selenium import webdriver
import csv
import re
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time

base_url =  'https://www.valentino.com/ko-kr/%EB%82%A8%EC%9E%90/%EC%8A%88%EC%A6%88/%EC%8A%A4%EB%8B%88%EC%BB%A4%EC%A6%88'
driver = webdriver.Chrome(r'C:\Users\Home\PycharmProjects\pythonProject1\chromedriver.exe')
driver.implicitly_wait(4)
driver.get(base_url)
click = driver.find_element_by_xpath('//*[@id="wrapper-product-lists"]/button/span[3]')

while True:
    try:
        time.sleep(3)
        click.click()
    except:
        break
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
r = soup.select('#wrapper-product-lists > ul > li > div > div > a > span')
for i in r:
    print(i)

allsearchlist = []
f = open('Prospecs.csv', 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)
for i in allsearchlist:
    csvWriter.writerow(i)

f.close()
print('완료')