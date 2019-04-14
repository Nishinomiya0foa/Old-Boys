import os

from homework.ftp_finally.conf import conf
from homework.ftp_finally.core.client import continue_down

def show_path():
    """打印 server_download_path 中的所有文件，用户选择下载"""
    file_list = os.listdir(conf.server_download_path)
    file_dic = {}
    for i in range(len(file_list)):
        file_dic[i+1] = file_list[i]
        print('{}、{}'.format(i+1, file_list[i]))
    chosen  = input('输入你想下载的文件编号:')
    try:
        chosen = int(chosen)
    except ValueError:
        print('请输入正确的文件编号')
        exit(-1)
    if file_dic.get(chosen):
        print('你选择了{}'.format(file_dic.get(chosen)))
        user1_path_listdir = os.listdir(conf.user1_selfpath)
        # 目标文件夹中没有该文件
        if file_dic.get(chosen) not in user1_path_listdir:
            # return   server端下载路径，       选择的文件名
            return conf.server_download_path, file_dic.get(chosen), None, None  # 返回server端
        else:
            print('存在同名文件,是否需要覆盖？输入1？0')
            choose_continue = input('>')
            if choose_continue == '1':
                filesize, md5_continue_file = continue_down.continue_down(conf.user1_selfpath, file_dic.get(chosen))
                return conf.server_download_path, file_dic.get(chosen), filesize, md5_continue_file
            else:
                print('你选择了不进行覆盖，程序结束。')
                exit(0)
    else:
        print('无此文件')
        exit(-1)


if __name__ == '__main__':

    show_path()