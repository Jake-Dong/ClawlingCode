from selenium import webdriver
import re
from bs4 import BeautifulSoup
import csv
from selenium.webdriver.common.keys import Keys
import time


def get_list(base_url):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome(r'C:\Users\Home\PycharmProjects\pythonProject1\chromedriver.exe', options=options)
    driver.implicitly_wait(4)
    driver.get(base_url)
    click = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[4]/p/a')

    while True:
        try:
            time.sleep(2)
            click.click()
        except:
            break
    r = driver.find_elements_by_css_selector('#prodList > li > a')
    img_a_href = []
    for i in r:
        data_style = i.get_attribute('data-style')
        img_a_href.append(data_style)
    return img_a_href

def name_list(base_url):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

    chrome = webdriver.Chrome(r'C:\Users\Home\PycharmProjects\pythonProject1\chromedriver.exe', chrome_options=options)
    chrome.get(base_url)
    html = chrome.page_source
    soup = BeautifulSoup(html, 'html.parser')
    shosname = soup.select('#prodList > li > a > p')
    shosname_list = []
    for i in shosname:
        madetext = i.get_text()
        shosname_list.append(str(madetext))
    return shosname_list

def cate_list(base_url):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

    chrome = webdriver.Chrome(r'C:\Users\Home\PycharmProjects\pythonProject1\chromedriver.exe', chrome_options=options)
    chrome.get(base_url)
    html = chrome.page_source
    soup = BeautifulSoup(html, 'html.parser')
    kate = soup.select('#frmDetail > div.plp-grid.clfix > div > div > div > div.info_wrapper > a > div.info_category')
    kate_list = []
    for i in kate:
        katetext = i.get_text()
        kate_list.append(str(katetext))
    return kate_list

base_url = 'https://www.nbkorea.com/product/productList.action?cateGrpCode=250110&cIdx=1287'
allsearchlist = []
medel_name = get_list(base_url)
shoes_name = name_list(base_url)


for q,w in zip(medel_name,shoes_name):
    allsearchlist.append(q,w)

print(allsearchlist)
# f = open('NewbalanceMen.csv', 'w', encoding='utf-8', newline='')
# csvWriter = csv.writer(f)
# for i in allsearchlist:
#     csvWriter.writerow(i)
#
# f.close()
# print('완료')