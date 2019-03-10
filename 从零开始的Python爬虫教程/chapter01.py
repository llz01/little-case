import requests

headers = {
    'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}
response = requests.get('https://baike.baidu.com/item/网络爬虫/5162711', headers=headers)
print(response.content.decode('UTF8'))

if __name__ == '__main__':
    pass
