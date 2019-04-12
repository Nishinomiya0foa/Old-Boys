"""
1.输入username 和pwd 上传至server
2,登录成功：接收菜单 下载 / 上传？
    1.下载：接收下载目录，选择文件，本地创建空文件，逐行接收文件，进行写入
    2.上传：选择上传的文件，逐行传输
3.登录失败，程序终止运行

"""

import socket
import os
import json

from homework.ftp_homework.conf import conf


def connect():
    skt = socket.socket()
    skt.connect(conf.ip_port)

    username = input('username:')
    pwd = input('pwd:')

    username_pwd = username + '|' + pwd  # xiaochen|123123
    # 发送账号密码
    skt.send(username_pwd.encode('utf-8'))
    # 接收登录状态
    login_state = skt.recv(1024).decode('utf-8')
    if login_state == 'fail':
        print('账号或密码错误，登录失败！')
        skt.close()
        exit(0)
    else:
        print(login_state)

    while True:
        choose_operate = bytes(input('>'), encoding='utf-8')
        # send 选择
        skt.send(choose_operate)

        # 接收回应
        choose_operate_reply = skt.recv(1024).decode('utf-8')
        print(choose_operate_reply)
        if choose_operate.decode('utf-8').lower() == 'q':
            skt.close()
            exit(0)
        # 下载
        elif choose_operate.decode('utf-8') == '1':
            break
        # 上传
        elif choose_operate.decode('utf-8') == '2':
            from homework.ftp_homework.core import upload

            # 得到 报头utf-8， 文件大小bytes
            head, filesize_pack = upload.upload()
            # print(head, filesize_pack)
            filesize = head['filesize']
            skt.send(filesize_pack)
            head_json = json.dumps(head)
            skt.send(head_json.encode('utf-8'))
            with open(os.path.join(head['path'], head['filename']), 'rb') as f1:
                while filesize:
                    if filesize >= conf.buffer:
                        content = f1.read(conf.buffer)
                        skt.send(content)
                        filesize -= conf.buffer
                    else:
                        content = f1.read(filesize)
                        skt.send(content)
                        print("上传文件 {} 完成".format(os.path.join(head['path'], head['filename'])))
                        skt.close()
                        exit(0)

            break
        else:
            pass
    skt.close()

if __name__ == '__main__':
    connect()
#
# connect()