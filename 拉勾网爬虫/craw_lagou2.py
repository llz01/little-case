#coding:utf-8
'''
Created on 2017��7��5��

@author: Administrator
'''
import requests,time
import traceback
from bs4 import BeautifulSoup
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
referer = 'https://www.lagou.com/zhaopin/'
cookie = 'user_trace_token=20170705135310-5b09be00-212e-447d-99f7-d4f5649e5c69; LGUID=20170705135311-3ab13de6-6146-11e7-9824-525400f775ce; ab_test_random_num=0; JSESSIONID=ABAAABAACDBAAIAD91248A517A79B094A419CB95B166F2E; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DKTwpsh2cLAxgZmyQBp6D38PU33OvagwYtuCqaJgTj-3%26wd%3D%26eqid%3Db760c5660004b56900000002595f1a9f; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; _putrc=475433F4CB2C8F1A; login=true; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B70190; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; SEARCH_ID=80b862586d5b4445aeb0f4baa0bcf4d0; index_location_city=%E5%85%A8%E5%9B%BD; _gid=GA1.2.1648604578.1499233990; _gat=1; _ga=GA1.2.1136791278.1499233990; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1499241450,1499241456,1499319615,1499404965; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1499405170; LGSID=20170707132247-502684ad-62d4-11e7-a50b-5254005c3644; LGRID=20170707132612-ca4992df-62d4-11e7-a50b-5254005c3644'
headers = {'User-Agent':user_agent,"Cookie":cookie,"Referer":referer}
def download(url):
    response = requests.get(url,headers=headers)
    #print response.content
    time.sleep(10)
    print url,' ',response.status_code

    soup = BeautifulSoup(response.content,'html5lib')
    try:
        job_name = soup.find('div',class_='job-name').get_text()
        job_req = soup.find('dd',class_='job_request').get_text()
        job_adv = soup.find('dd',class_='job-advantage').get_text()
        job_des = soup.find('dd',class_='job_bt').get_text()
        work_addr = soup.find('dd',class_='job-address clearfix').get_text()
        now = soup.find('ul',class_='c_feature').get_text()
    except:
        traceback.print_exc()
    f = open('craw.html','a')
    f.write('<html><meta charset="utf-8"><body>')
    f.write('<h3>')
    f.write(job_name.encode('utf8'))
    f.write('</h3>')
    f.write('<p>工资及要求：')
    f.write(job_req.encode('utf-8'))#编码
    f.write('</p>')
    f.write('<br>')
    f.write('<p>')
    f.write(job_adv.encode('utf8'))
    f.write('</p>')
    f.write('<br>')
    f.write('<p>')
    f.write(job_des.encode('utf8'))
    f.write('</p>')
    f.write('<br>')
    f.write('<p>')
    f.write(work_addr.encode('utf8'))
    f.write('<br>')
    f.write('<p>')
    f.write(now.encode('utf8'))
    f.write('</p>')
    f.write('<hr/></body></html>')
    f.close()
'''url = 'https://www.lagou.com/jobs/3316291.html'
download(url)'''