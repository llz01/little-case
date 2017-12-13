#coding:utf-8
import re,time
import requests
from bs4 import BeautifulSoup
from craw_scnews3 import Insert

user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
headers = {'User-Agent':user_agent}

def download(url):
    html = requests.get(url,headers=headers).content.decode('gb2312','ignore')
    soup = BeautifulSoup(html,'html.parser')
    #print soup
    #文章网址ַ
    url = url
    #文章标题
    title = re.finditer('<h1>(.*?)</h1>',html).next().group(1)
    #发布时间
    time_ = soup.find('span').get_text()
    #评论数量
    comment = None
    #文章来源
    source = re.finditer('<span id="source_baidu ".*?target="_blank">(.*?)</a></span>',html).next().group(1)
    #文章栏目
    lanmu = soup.find('div',class_='col-xs-12 col-md-8 col-lg-8').find_all('a')[1].get_text()
    #文章正文
    content = soup.find('div',class_='content').find_all('p')
    message = ''
    for i in content:
        message += i.get_text()
    #图片链接
    try:
        img = soup.find('div',class_='content').find('p').find('img').get('src')
    except:
        img = None
    #文章作者
    author = soup.find('span',id='editor_baidu').get_text()
    #关键词
    gjc = None
    #相关标签
    xgbq = None
    #阅读数
    yds = None
    now = time.time()
    data = {'wen_zhang_wang_zhi':url,
            'wen_zhang_biao_ti':title,
            'fa_bu_shi_jian':time_,
            'ping_lun_shu_liang':comment,\
            'wen_zhang_lai_yuan':source,
            'wen_zhang_lan_mu':lanmu,
            'wen_zhang_zhen_wen':message,
            'tu_pian_lian_jie':img,\
            'wen_zhang_zuo_zhe':author,
            'guan_jian_ci':gjc,
            'xiang_guan_biao_qian':xgbq,
            'yue_du_shu':yds,
            'do_time':now,
            '_id':url}
    Insert(data)
    finish = url +' ok'
    f = open('scnews.log','a+')
    f.write(finish+'\n')
    f.close()
    #print finish
    
    
#download('http://china.newssc.org/system/20170724/000800978.html')