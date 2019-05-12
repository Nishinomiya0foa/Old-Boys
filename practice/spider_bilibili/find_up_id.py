"""搜索用户id, 并加入浏览树"""
import requests
import re
import time
from bs4 import BeautifulSoup


def get_id(url):
    headers = {
        'Host': 'search.bilibili.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    if response.__dict__['status_code'] == 200:
        cont = response.content.decode('utf-8')
        soup = BeautifulSoup(cont, 'html.parser')
        try:
            up = soup.find(name='li', attrs={'class': 'up-item'}).find(name='a', attrs={'class': 'title'}).get('href')
        except AttributeError:
            print('AttributeError, soup解析异常, 用户可能不存在')
            exit(-1)
        uid = re.findall('com/(.*?)\?from=', up)
        if uid[0].isdigit():
            return uid[0]
        else:
            print('没能解析出uid')
    else:
        print('网页访问失败!')


def write_in(file, up=None, uid=None, is_write=True):
    """
    查询和新增. 写在了同一个方法内
    """
    with open(file, 'a+', encoding='gbk') as f1:
        if is_write:
            f1.write('{},{}\n'.format(up, uid))
            print('写入成功')
        else:
            f1.seek(0)
            for line in f1:
                print(line.strip())


def check_is_exist(uid, file):
    """检查想要查询的用户uid是否已存在"""
    with open(file, 'r') as f1:
        for line in f1:
            if uid in line:
                return True  # 已存在
        return False  # 不存在


if __name__ == '__main__':
    search_url_part = 'https://search.bilibili.com/upuser?keyword={}'
    uid_file = r'F:\Old Boys\practice\spider_bilibili\ups_uid.csv'
    chosen = input(
        """输入你要进行的操作:
1.查看uid表
2.新增uid
输入其他以退出
>""")
    # 查询
    if chosen == '1':
        write_in(uid_file, is_write=False)

    # 新增
    elif chosen == '2':
        search_name = input('>')
        # 拼出完整 url
        search_url_full = search_url_part.format(search_name)
        # 获得用户的uid
        uid = get_id(search_url_full)
        if uid:
            # 判断该uid是否已存在
            uid_is_exist = check_is_exist(search_name, uid_file)
            # 不存在, 写入
            if not uid_is_exist:
                print('成功解析出 {} 的uid: {}, 正在写入到文件.'.format(search_name, uid))
                write_in(uid_file, search_name, uid)
            # 存在
            else:
                print('该用户已存在uid表中,不能重复添加')

    else:
        print('正在结束..')
        time.sleep(0.5)