import requests
from lxml.html import fromstring

import requests

headers = {
    'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
                    Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}
response = requests.get('https://baike.baidu.com/item/网络爬虫/5162711', headers=headers)
html = response.content.decode('UTF8')
tree = fromstring(html)
result = tree.xpath('//div[@class="para" and @label-module="para"]/text()')
print(result)


if __name__ == '__main__':
    pass
