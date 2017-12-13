#coding:utf-8
import requests
from bs4 import BeautifulSoup
import re
import time
import traceback
from craw_scnews2 import download


user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
headers = {'User-Agent':user_agent}
urls = ['http://scnews.newssc.org/2009scxw/',
        'http://china.newssc.org/shxw/',
        'http://china.newssc.org/zxbd/',
        'http://china.newssc.org/gat/']
today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
links = []
for url in urls:
    rsp = requests.get(url,headers=headers).content.decode('gb2312','ignore')
    #print rsp
    items = re.findall('<a href="(.*?)"\s*title=.*?target="_blank"  >.*?</a>\s*&nbsp;&nbsp;\s*(.*?)\s*</td>',rsp)
    for url,time_ in items:
        if time_ == today:
            links.append(url)
while range(len(links)):            
    url = links.pop()
    try:
        download(url)
    except:
        f = open('scnews.log','a+')
        error = traceback.format_exc()
        error = now +'\n'+ error
        f.write('\n'+error+'\n')
        f.close()
    #time.sleep(2)