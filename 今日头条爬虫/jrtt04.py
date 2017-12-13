#coding:utf-8
from selenium import webdriver
import time
from jrtt03 import InsertComments

def getcomment(url):
    #driver = webdriver.PhantomJS()
    driver = webdriver.Firefox(executable_path=r'C:\Python27\geckodriver.exe')
    driver.get(url)
    driver.implicitly_wait(10)
    #time.sleep(3)
    submit_button = driver.find_element_by_class_name('c-load-more')
    submit_button.click()
    time.sleep(2)
    comments = []
    url = url
    try:
        alls = driver.find_element_by_xpath('//div[@id="comment"]')
        all = alls.find_elements_by_xpath('//div[@class="c-content"]')
    except:
        print(url,'视频')
        driver.close()
        exit(0)
    print all[2].find_element_by_xpath('//div[@class="c-user-info"]/a').text
    #��������
    '''for i in all:
        id = i.find_element_by_xpath('//div[@class="c-user-info"]/a').get_attribute('href')
        name = i.find_element_by_xpath('//div[@class="c-user-info"]/a').text
        comment_ = i.find_element_by_xpath('//div[@class="c-content"]/p').text
        print comment_
        qi_ta_xin_xi = None
        comment_time = i.find_element_by_xpath('//div[@class="c-user-info"]/span').text
        now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        comment = {}
        comment['url'] = url
        comment['id'] = id
        comment['name'] = name
        comment['comment'] = comment_
        comment['qi_ta_xin_xi'] = None
        comment['pin_lun_time'] = comment_time
        comment['zhua_qu_time'] = now
        #print comment
        comments.append(comment)
    #driver.close()
    #InsertComments(comments)'''
    print url,'getcomments'
    #����ʱ��
    #�ظ�����
    #����id
    #�û��ǳ�
    #�Ա�
    #�û��ȼ�
    #�û�ʡ��
    #ץȡʱ��
    #ץȡ��վ
getcomment('http://www.toutiao.com/group/6448160898867577101/')