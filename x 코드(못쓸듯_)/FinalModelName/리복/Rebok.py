from selenium import webdriver
import re
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
import csv

def get_link(url):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

    chrome = webdriver.Chrome(r'C:\Users\Home\PycharmProjects\pythonProject1\chromedriver.exe', chrome_options=options)

    chrome.get(url)

    tt = chrome.find_elements_by_tag_name('a')
    img_a_href = []
    for i in tt:
        tr = i.get_attribute("href")
        qq = re.match('j', str(tr))
        if qq != None:
            img_a_href.append(str(tr))
    return img_a_href


def split_link(url):
    split_link_href = []
    t = get_link(url)

    for i in t:
        split_str = i.split(":")
        split_link_href.append(split_str)

    return split_link_href


def link_list(url):
    t = split_link(url)
    link_list = []

    for i in t:
        spl = i[1]
        qq = re.match('fn_prod', spl)
        if qq != None:
            pl = spl.split('\'')
            link_list.append(pl[1])
    return link_list


def Akate_list(url):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

    chrome = webdriver.Chrome(r'C:\Users\Home\PycharmProjects\pythonProject1\chromedriver.exe', chrome_options=options)
    chrome.get(url)
    html = chrome.page_source
    soup = BeautifulSoup(html, 'html.parser')
    kate = soup.select('#prodList > div > div.plp-products > div.productArea > div.plp-grid.clfix > div > div > div.info_wrapper > a > div.txt')
    kate_list = []
    for i in kate:
        katetext = i.get_text()
        kate_list.append(str(katetext))
    return kate_list

def name_list(url):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

    chrome = webdriver.Chrome(r'C:\Users\Home\PycharmProjects\pythonProject1\chromedriver.exe', chrome_options=options)
    chrome.get(url)
    html = chrome.page_source
    soup = BeautifulSoup(html, 'html.parser')
    shosname = soup.select('#prodList > div > div.plp-products > div.productArea > div.plp-grid.clfix > div > div > div.info_wrapper > a > div.title')
    shosname_list = []
    for i in shosname:
        madetext = i.get_text()
        shosname_list.append(str(madetext))
    return shosname_list

allshos_list=[]

passpage = []
try:
    for i in range(7):
        base_url = 'https://shop.reebok.co.kr/RPF020201.action?S_CTGR_CD=02002001&PAGE_CUR=' + str(i + 1)
        passpage.append(base_url)
    for url in passpage:
        model_list = link_list(url)
        shosname_list = name_list(url)
        kate_list = Akate_list(url)
        for q,w,e in zip(model_list,shosname_list,kate_list):
            xxx = [q,w,e]
            allshos_list.append(xxx)
except:
    pass
print(allshos_list)
f = open('RebokWomen.csv', 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)
for i in allshos_list:
    csvWriter.writerow(i)

f.close()
print('완료')


