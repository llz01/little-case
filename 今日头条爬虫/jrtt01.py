import re
import time,traceback,threading
from selenium import webdriver
from bs4 import BeautifulSoup
from jrtt02 import getmessage
#from jrtt04 import getcomment

links = []
def geturls(url):
    #driver = webdriver.Firefox(executable_path=r'C:\Python27\geckodriver.exe')
    driver = webdriver.PhantomJS()  
    driver.get(url)
    driver.implicitly_wait(10) 
    for i in range(8):
        driver.execute_script("window.scrollBy(0,700)")
        driver.implicitly_wait(2)
    #time.sleep(5)
    page = driver.page_source
    driver.close()
    soup = BeautifulSoup(page,'html.parser')
    try:
        #list = driver.find_elements_by_xpath('//a[@class="link"]')
        list = soup.find_all('a',class_='link')
    except:
        #list = driver.find_elements_by_xpath('//a[@class="link title"]')
        list = soup.find_all('a',class_='link title')
    for i in list:
        #link = i.get_attribute('href')
        link = 'http://www.toutiao.com'+i.get('href')
        print('got link',link)
        links.append(link)
def main():
    urls = ['http://www.toutiao.com/',\
        'http://www.toutiao.com/ch/news_society/',\
        'http://www.toutiao.com/ch/news_entertainment/',\
        'http://www.toutiao.com/ch/news_finance/',\
        'http://www.toutiao.com/ch/news_world/']
    for url in urls:
            geturls(url)
            #Threads = []
    while len(links):
        print('本次还剩余%d条' % len(links))
        try:
            url_ = links.pop()
            getmessage(url_)

        except:
            pass
        print('Over!')
#geturls('http://www.toutiao.com/')   
#print links
if __name__=='__main__':
    main()