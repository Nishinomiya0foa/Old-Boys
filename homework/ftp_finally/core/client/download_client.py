import os

from homework.ftp_finally.core import show_path
from homework.ftp_finally.conf import conf

# 如果登录成功
def choose_operate():
    print("""选择您要执行的操作：
    1.上传文件
    2.下载文件""")

    chosen = input('>')
    if chosen:
        if chosen == '1':
            print('你选择了1.上传文件')
        elif chosen == '2':
            print('你选择了2.下载文件')
            server_download_path, chosen_file, continue_filesize, contine_file_md5 = show_path.show_path()
            return server_download_path, chosen_file, continue_filesize, contine_file_md5, chosen

    else:
        exit(0)

