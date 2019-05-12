"""根据uid表中的uid, 更新用户的视频"""
import requests
import json
from threading import Thread
from multiprocessing import Pool


def get_uid_from_file(file):
    """从ups_uid.csv 中, 获取其中所有uid"""
    uid_list = []
    with open(file, 'r', encoding='gbk') as f1:
        for line in f1:
            uid_list.append(line[line.index(',')+1:].strip())
    return uid_list


def update_thread(url):
    """子线程中爬取视频信息: 网址 视频标题
    """
    pass


def update_process(url):
    """多进程爬取数据"""
    response = requests.get(url)
    page_dict = json.loads(response.content.decode('utf-8'))
    return page_dict['data']['vlist']  # 列表


def deal_data(data:list):
    """回调函数
    将数据写入到日志表 和 更新表
    """
    with open('F:\Old Boys\practice\spider_bilibili\\used_aid.csv', 'a+') as f2, \
            open('F:\Old Boys\practice\spider_bilibili\\bilibili_update.csv', 'a', encoding='gbk') as f1:
        for i in range(5):
            flag = True
            f2.seek(0)
            for line in f2:
                if str(data[i]['aid']) in line.strip():
                    flag = False
                    break
            if flag:
                f1.write('https://www.bilibili.com/video/av{aid},{author},{title}\n'.format(aid=data[i]['aid'], author=data[i]['author'], title=data[i]['title'],))
                f2.write('{aid},{author},{title}\n'.format(aid=data[i]['aid'], author=data[i]['author'], title=data[i]['title'],))
                # print('更新成功')
        print('用户 {} 更新完成.'.format(data[0]['author']))


if __name__ == '__main__':
    with open('F:\Old Boys\practice\spider_bilibili\\bilibili_update.csv', 'w'):
        pass
    uid_file = r'F:\Old Boys\practice\spider_bilibili\ups_uid.csv'
    url_json_video_list = 'https://space.bilibili.com/ajax/member/getSubmitVideos?mid={}&page=1&pagesize=25'
    uid_list = get_uid_from_file(uid_file)
    with Pool(5) as p:
        for uid in uid_list:
            # 多进程 回调函数用于写入文件
            p.apply_async(update_process, args=(url_json_video_list.format(uid),), callback=deal_data)
        p.close()
        p.join()