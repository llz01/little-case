#coding:utf-8
'''
Created on 2017��7��1��

@author: Administrator
'''
import requests
import traceback
from bs4 import BeautifulSoup
from craw_mzitu2 import download_img

referer = 'http://www.mzitu.com/'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
cookie = 'Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1499159355,1499409628; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1499409628'
headers = {'Referer':referer,'User-Agent':user_agent,'Cookie':cookie}
link = []

rsp = requests.get('http://www.mzitu.com/page/4',headers=headers)
print 'http://www.mzitu.com/',rsp.status_code
soup = BeautifulSoup(rsp.content,'html.parser')
links = soup.find('ul',id='pins').find_all('li')
for i in links:
    i = i.find('span').find('a').get('href')
    print i
    link.append(i)
print len(link)
for url in link:
    try:
        download_img(url)
    except:
        traceback.print_exc()
print 'Over'