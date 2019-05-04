"""使用回调函数实现的爬虫"""

import requests
from multiprocessing import Pool


def spider_web(url):
    res = requests.get(url)
    if res.status_code == 200:
        return url, res.content.decode('utf-8')
    else:
        print('{} 爬取失败.'.format(url))
        return url, None

def analyse_data(args):
    # url, res = args
    if args[1]:
        print(args[0], len(args[1]))

# res = requests.get('http://www.baidu.com')
# print(res.__dict__)
if __name__ == '__main__':
    url_list = [
        'http://www.baidu.com',
        'https://zhuanlan.zhihu.com/p/54430650',
        'https://blog.csdn.net/qq_38950316/article/details/81087809',
        'https://www.cnblogs.com/venicid/p/8878970.html',
        'https://python3-cookbook.readthedocs.io/zh_CN/latest/preface.html',
        'https://github.com/Yixiaohan/show-me-the-code',
        'http://www.baidu.com',
        'https://zhuanlan.zhihu.com/p/54430650',
    ]
    p = Pool(5)
    for url in url_list:
        p.apply_async(func=spider_web, args=(url,), callback=analyse_data)
        # s = spider_web(url)
        # print(len(s))
    p.close()
    p.join()