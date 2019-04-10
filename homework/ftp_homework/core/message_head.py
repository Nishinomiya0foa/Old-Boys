import os

from homework.ftp_homework.conf import conf

# path = 'F:\软件质量与测试\期末报告'
# print(os.listdir(path))
# print(os.path.isfile(path))


def head():
    head = {
        'filename': None,
        'path': conf.path,
        'filesize': None,
    }
    return head