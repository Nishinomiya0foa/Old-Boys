"""
协程
    :爬虫的例子
    :socket的例子

"""

# 爬虫
import requests


url = 'https://www.baidu.com'
response = requests.get(url).content.decode('utf-8')

print(response)