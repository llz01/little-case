#coding:utf-8
'''
Created on 2017年7月5日

@author: Administrator
'''
import requests
import traceback
import time
from bs4 import BeautifulSoup
from craw_lagou2 import download

user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
referer = 'https://www.lagou.com/zhaopin/'
cookie = 'user_trace_token=20170705135310-5b09be00-212e-447d-99f7-d4f5649e5c69; LGUID=20170705135311-3ab13de6-6146-11e7-9824-525400f775ce; ab_test_random_num=0; JSESSIONID=ABAAABAACDBAAIAD91248A517A79B094A419CB95B166F2E; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DKTwpsh2cLAxgZmyQBp6D38PU33OvagwYtuCqaJgTj-3%26wd%3D%26eqid%3Db760c5660004b56900000002595f1a9f; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; _putrc=475433F4CB2C8F1A; login=true; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B70190; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; SEARCH_ID=80b862586d5b4445aeb0f4baa0bcf4d0; index_location_city=%E5%85%A8%E5%9B%BD; _gid=GA1.2.1648604578.1499233990; _gat=1; _ga=GA1.2.1136791278.1499233990; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1499241450,1499241456,1499319615,1499404965; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1499405170; LGSID=20170707132247-502684ad-62d4-11e7-a50b-5254005c3644; LGRID=20170707132612-ca4992df-62d4-11e7-a50b-5254005c3644'
headers = {'User-Agent':user_agent,"Cookie":cookie,"Referer":referer}
indexs = []
links = []
def get_page():
    for page in range(1,31):
        url_page = 'https://www.lagou.com/zhaopin/%d/?filterOption=3' % page
        indexs.append(url_page)
        
def download_link():
    for html in indexs:
        html_ = requests.get(html,headers=headers)
        print 'Download  links from the  page:',html,' ',html_.status_code
        soup = BeautifulSoup(html_.content,'html.parser')
        zhiwei = soup.find_all('a',class_ ='position_link')
        for i in zhiwei:
            i = i.get('href')
            print i
            links.append(i)
        time.sleep(5)
            
get_page()
download_link()
print len(links)
'''for url in links:
    try:
        download(url)
        #time.sleep(5)
    except:
        traceback.print_exc()
'''
print 'Over!'


    
    
    
    