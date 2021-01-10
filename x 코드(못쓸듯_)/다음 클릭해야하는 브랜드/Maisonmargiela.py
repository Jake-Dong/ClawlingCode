from selenium import webdriver
import re
from bs4 import BeautifulSoup
import csv
import time

base_url = 'https://www.maisonmargiela.com/kr/maison-margiela/%EB%82%A8%EC%9E%90/%EC%8A%A4%EB%8B%88%EC%BB%A4%EC%A6%88'
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
driver = webdriver.Chrome(r'D:\big11\[90]tools\chromedriver.exe', options=options)
driver.implicitly_wait(5)
driver.get(base_url)


click = driver.find_element_by_xpath('/html/body/main/div/section[2]/div[2]/button[1]/span[1]')


while True:
    try:
        time.sleep(3)
        click.click()
    except:
        break

html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
r = soup.select('ul>li>div>div>span')
allsearchlist = []
for i in r:
   tt= i.get_text() 
   print(tt)
   allsearchlist.append(tt)
   
f = open('Maisonmargiela.csv', 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)
for i in allsearchlist:
    csvWriter.writerow(i)

f.close()
print('완료') 