#coding:utf8
import re
import time
from selenium import webdriver
from jrtt03 import InsertNews
from jrtt06 import JianCa
from jrtt05 import getcomment

#url = 'http://www.toutiao.com/group/6448824826043793677/'
def getmessage(url):
    print(url,'开始抓取')
    driver = webdriver.PhantomJS()
    #driver = webdriver.Firefox(executable_path=r'C:\Python27\geckodriver.exe') 
    driver.get(url)
    driver.implicitly_wait(5) 
    #time.sleep(3)
    #文章网址
    wen_zhang_url = url
    #文章标题,遇到视频跳出
    try:
        title = driver.find_element_by_xpath('//h1[@class="article-title"]').text
    except:
        print(url,'视频，跳过')
        driver.close()
        exit(0)
    #发布时间
    try:
        fa_bu_shi_jian = driver.find_elements_by_xpath('//div[@class="articleInfo"]/span')[2].text
    except:
        try:
            fa_bu_shi_jian = driver.find_elements_by_xpath('//div[@class="article-sub"]/span')[2].text
        except:
            try:
                fa_bu_shi_jian = driver.find_elements_by_xpath('//div[@class="article-sub"]/span')[1].text
            except:
                fa_bu_shi_jian = driver.find_elements_by_xpath('//div[@class="articleInfo"]/span')[1].text
    #评论数量
    #print fa_bu_shi_jian
    if JianCa(fa_bu_shi_jian):
        print(url,'日期不符，跳过')
        exit(0)
    try:
        submit_button = driver.find_element_by_class_name('c-load-more')
        submit_button.click()
    except:
        pass
    time.sleep(2)
    page = driver.page_source
    #getcomment(url,page)
    pin_lun_shu_liang = driver.find_element_by_xpath('//a[@class="share-count"]//span').text
    if int(pin_lun_shu_liang) :
        try:
            getcomment(url,page)
        except:
            pass
    else:
        print(url,'无评论')
    #文章来源
    try:
        wen_zhang_source = driver.find_elements_by_xpath('//div[@class="articleInfo"]/span')[0].text
    except:
        wen_zhang_source = driver.find_elements_by_xpath('//div[@class="article-sub"]/span')[0].text
    #文章正文
    wen_zhang_zheng_wen = ''
    wen_zhang = driver.find_elements_by_xpath('//div[@class="article-content"]//p')
    for i in wen_zhang:
        wen_zhang_zheng_wen += i.text
    #抓取时间
    #now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    now = time.time()
    #抓取网站
    zhan_dian = '今日头条'
    #图片链接
    imgs = ''
    try:
        img = driver.find_elements_by_xpath('//div[@class="article-content"]//p/img')
        for i in img:
            i = i.get_attribute('src')
            imgs = imgs + i + ' '
    except:
        imgs = ''
    #文章栏目
    wen_zhang_lan_mu = wen_zhang = driver.find_element_by_xpath('//a[@ga_event="click_channel"]').text
    #文章作者
    author = None
    #关键词
    guan_jian_ci = []
    try:
        cis = driver.find_elements_by_xpath('//a[@class="label-link"]')
    except:
        cis = driver.find_elements_by_xpath('//a[@class="tag-item"]')
    for i in cis:
        guan_jian_ci.append(i.text)
    #阅读数量
    readers = None
    #主键     
    driver.close()
    data = {'wen_zhang_wang_zhi':wen_zhang_url,\
            'wen_zhang_biao_ti':title,\
            'fa_bu_shi_jian':fa_bu_shi_jian,\
            'ping_lun_shu_liang':pin_lun_shu_liang,\
            'wen_zhang_lai_yuan':wen_zhang_source,\
            'wen_zhang_zheng_wen':wen_zhang_zheng_wen,\
            'do_time':now,\
            'zhan_dian':zhan_dian,\
            'tu_pian_lian_jie':imgs,\
            'wen_zhang_lan_mu':wen_zhang_lan_mu,\
            'wen_zhang_zuo_zhe':author,\
            'xiang_guan_biao_qian':guan_jian_ci,\
            'guan_jian_ci':None,\
            'yue_du_shu':readers,\
            '_id':wen_zhang_url}
    try:
        InsertNews(data)
    except:
        print(url,'该文章已存在')
        exit(0)
    print(url,'文章获取成功')
#getmessage(url)   