#coding:utf8
import re
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import time
from lxml.html import fromstring
from bs4 import BeautifulSoup
from clientDb import InsertComments,InsertNews
import logging


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s:[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='JRTT.log',
                    filemode='w')


class Toutiao():

    links = []
        
    def getLinks(self,url):
        driver = webdriver.Firefox(executable_path=r'C:\Python27\geckodriver.exe')
        ua = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.3 Safari/537.36"
        cap = webdriver.DesiredCapabilities.PHANTOMJS
        cap["phantomjs.page.settings.resourceTimeout"] = 200000
        cap["phantomjs.page.settings.loadImages"] = False
        cap["phantomjs.page.settings.disk-cache"] = False
        cap["phantomjs.page.settings.userAgent"] = ua
        cap["phantomjs.page.customHeaders.User-Agent"] =ua
        cap["phantomjs.page.customHeaders.Referer"] = "https://www.toutiao.com/"
        #driver = webdriver.PhantomJS(desired_capabilities=cap, service_args=['--ignore-ssl-errors=true'])  
        driver.get(url)
        driver.refresh()
        time.sleep(2)
        #driver.implicitly_wait(5) 
        for i in range(7):
            driver.execute_script("window.scrollBy(0,700)")
            time.sleep(2)
        html = driver.page_source
        print html
        driver.close()
        tree = fromstring(html)
        list = tree.xpath('//a[@class="link"]/@href')
        print(0,list)
        if not list:
            list = tree.xpath('//a[@class="link title"]/@href')
            #print(1,list)
        if not list:
            list = tree.xpath('//a[@class="news-link"]/@href')
            #print(2,list)
        if not list:
            logging.warning('Can\'t get the news url')
            #print("Can't find any url!")
            exit(0)
        for i in list:
            link = 'https://www.toutiao.com' + i
            #print 'Get link:', link
            logging.info('Get link:%s' % link)
            self.links.append(link)
  
    def getNews(self,url):
        #print url,'��ʼץȡ'
        logging.info('%s ��ʼ��ȡ' % url)
        driver = webdriver.PhantomJS()
        #driver = webdriver.Firefox(executable_path=r'C:\Python27\geckodriver.exe') 
        driver.get(url)
        driver.implicitly_wait(5) 
        #������ַ
        wen_zhang_url = url
        #���±���,������Ƶ����
        try:
            title = driver.find_element_by_xpath('//h1[@class="article-title"]').text
        except:
            #print url,'��������������'
            logging.info('%s ��������������' % url)
            driver.close()
            exit(0)
        #����ʱ��
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
        #��������
        if self.isToday(fa_bu_shi_jian):
            #print url,'���ڲ���������'
            logging.info('%s ���ڲ���������' % url)
            driver.close()
            exit(0)
        try:
            submit_button = driver.find_element_by_class_name('c-load-more')
            submit_button.click()
        except:
            pass
        time.sleep(2)
        page = driver.page_source
        pin_lun_shu_liang = driver.find_element_by_xpath('//a[@class="share-count"]//span').text
        if int(pin_lun_shu_liang) :
            try:
                self.getCommen(url,page)
            except:
                pass
        else:
            #print(url,'������')
            logging.info('%s ������' % url)
        #������Դ
        try:
            wen_zhang_source = driver.find_elements_by_xpath('//div[@class="articleInfo"]/span')[0].text
        except:
            wen_zhang_source = driver.find_elements_by_xpath('//div[@class="article-sub"]/span')[0].text
        #��������
        wen_zhang_zheng_wen = ''
        wen_zhang = driver.find_elements_by_xpath('//div[@class="article-content"]//p')
        for i in wen_zhang:
            wen_zhang_zheng_wen += i.text
        #ץȡʱ��
        #now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        now = time.time()
        #ץȡ��վ
        zhan_dian = u'����ͷ��'
        #ͼƬ����
        imgs = ''
        try:
            img = driver.find_elements_by_xpath('//div[@class="article-content"]//p/img')
            for i in img:
                i = i.get_attribute('src')
                imgs = imgs + i + ' '
        except:
            imgs = ''
        #������Ŀ
        wen_zhang_lan_mu = wen_zhang = driver.find_element_by_xpath('//a[@ga_event="click_channel"]').text
        #��������
        author = None
        #�ؼ���
        guan_jian_ci = []
        try:
            cis = driver.find_elements_by_xpath('//a[@class="label-link"]')
        except:
            cis = driver.find_elements_by_xpath('//a[@class="tag-item"]')
        for i in cis:
            guan_jian_ci.append(i.text)
        #�Ķ�����
        readers = None
        #����     
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
            #print url,'�������Ѵ���'
            logging.info('{} �Ѵ���'.format(url))
            exit(0)
        #print url,'���»�ȡ�ɹ�'
        logging.info('%s ���»�ȡ�ɹ�' % url)
    
    def getCommen(self,url,page):
        soup = BeautifulSoup(page,'html.parser')
        all = soup.find_all('div',class_='c-content')
        comments = []
        for i in all:
            id = 'http://www.toutiao.com'+i.find('a').get('href')
            name = i.find('a').get_text()
            c_content =  i.find('p').get_text()
            c_time = i.find('span',class_='c-create-time').get_text()
            if c_time[1] == u'\u5206':
                c_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            else:
                now = time.strftime('%H',time.localtime(time.time()))
                time1 = int(now) - int(c_time[0])
                if time1<10:
                    time1 = '0'+str(time1)+':'
                else:
                    time1 = str(time1)+':'
                now = now+':'
                c_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                c_time = c_time.replace(now,time1)
            try:
                r_count =  i.find('span',class_='c-reply-count').get_text()
            except:
                r_count = None
            z_count = i.find('span',title='����').get_text()
            #z_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            z_time = time.time()
            c_url = u'����ͷ��'
            comment = {}
            #comment['news_url'] = url
            comment['ping_lun_id'] = id
            comment['yong_hu_ming'] = name
            comment['xing_bie'] = None
            comment['yong_hu_deng_ji'] = None
            comment['yong_hu_sheng_fen'] = None
            comment['ping_lun_nei_rong'] = c_content
            comment['hui_fu_shu'] = r_count
            comment['ping_lun_shi_jian'] = c_time
            #print comment['ping_lun_shi_jian']
            comment['do_time'] = z_time
            comment['dian_zan_shu'] = z_count
            comment['zhan_dian'] = c_url
            comment['_id'] = id+url
            comments.append(comment)
        try:
            InsertComments(comments)
        except:
            #print url,'�������Ѵ���'
            logging.info('%s �����Ѵ���' % url)
            exit(0)
        #print(url,'���ۻ�ȡ�ɹ�')
        logging.info('%s ���ۻ�ȡ�ɹ�' % url)
        
    def isToday(self,fb_time):  
            today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
            fb_time = re.findall('(.*?) .*?',fb_time)[0]
            if fb_time != today:
                return True
            else:
                return False   

def main():
    logging.info('���ο�ʼ')
    urls = ['https://www.toutiao.com/',
    'https://www.toutiao.com/ch/news_society/',\
    'https://www.toutiao.com/ch/news_entertainment/',\
    'https://www.toutiao.com/ch/news_finance/',\
    'https://www.toutiao.com/ch/news_world/']
    for i in urls:
        test = Toutiao()
        test.getLinks(i)
        count = len(test.links)
        #print '%s��%d' % i,count
        while len(test.links):
            url = test.links.pop()
            try:
                test.getNews(url)
            except:
                pass
            count -= 1
            #print '��%d' % count
if __name__=='__main__':
    #main()
    test = Toutiao()
    test.getLinks('https://www.toutiao.com/')
    #print(test.links)
    #test.getNews('https://www.toutiao.com/a6496631827619381774/')