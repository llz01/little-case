#coding:utf-8
'''
Created on 2017��7��6��

@author: Administrator
'''
from bs4 import BeautifulSoup
import requests
import time
import os

#url = 'http://www.mzitu.com/96934'
def download_img(url):
    referer = url
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
    cookie = 'Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1499159355,1499409628; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1499413222'
    headers = {'Referer':referer,'User-Agent':user_agent,'Cookie':cookie}
    rsp = requests.get(url,headers=headers).content
    soup = BeautifulSoup(rsp,'html.parser').find('div',class_='pagenavi').find_all('a')
    #print len(soup)
    page_max = soup[4].find('span').get_text()
    #print page_max
    Q = True
    index = 1
    while Q:
        url_ = url+'/%d' % index
        index = index + 1
        if index > int(page_max):
            Q = False
        rsp = requests.get(url_,headers=headers)
        code = url_+' '+ str(rsp.status_code)
        print code
        if rsp.status_code == 200:
            soup = BeautifulSoup(rsp.content,'html.parser').find('div',class_='main-image').find('p').find('a').find('img')
            #print soup.get('alt'),soup.get('src')
            miaoshu = soup.get('alt')
            src = soup.get('src')
        img = requests.get(src,headers).content
        path = 'D:/img/%s' % miaoshu
        if not os.path.isdir(path):
            path = os.mkdir(path)
        f = open('D:/img/%s/%d.jpg'%(miaoshu,index-1),'wb')
        f.write(img)
        f.close()
        #time.sleep(1)
        
#download_img(url)
#print 'Over'