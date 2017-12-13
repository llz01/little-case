#coding:utf-8
import time,re

def JianCa(fb_time):
    today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    fb_time = re.findall('(.*?) .*?',fb_time)[0]
    if fb_time != today:
        return True
    else:
        return False