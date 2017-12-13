import time
from bs4 import BeautifulSoup
from jrtt03 import InsertComments
#from selenium import webdriver

def getcomment(url,page):
#def getcomment(url):
    '''driver = webdriver.PhantomJS()
    #driver = webdriver.Firefox(executable_path=r'C:\Python27\geckodriver.exe')
    driver.get(url)
    driver.implicitly_wait(10)
    #time.sleep(3)
    submit_button = driver.find_element_by_class_name('c-load-more')
    submit_button.click()
    time.sleep(3)
    page = driver.page_source
    driver.close()'''
    #————————————————————————————————————————————————
    soup = BeautifulSoup(page,'html.parser')
    all = soup.find_all('div',class_='c-content')
    comments = []
    for i in all:
        id = 'http://www.toutiao.com'+i.find('a').get('href')
        name = i.find('a').get_text()
        c_content =  i.find('p').get_text()
        c_time = i.find('span',class_='c-create-time').get_text()
        if c_time[1] == '\u5206':
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
        z_count = i.find('span',title='点赞').get_text()
        #z_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        z_time = time.time()
        c_url = '今日头条'
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
        print(url,'该评论已存在')
        exit(0)
    print(url,'评论获取成功')
#getcomment('http://www.toutiao.com/a6451854282776904205/')