"""
1.接收客户端发来的username和pwd， 进行登录确认. 成功登录则返回选择菜单 ---- 下载or上传
2.下载：返回下载目录，逐行传输
3.上传：准备接收文件，server创建空文件

"""

import socket
import struct
import json

from homework.ftp_homework.conf import conf

def connect():
    skt = socket.socket()
    skt.bind(conf.ip_port)

    skt.listen()  # 监听

    conn, addr = skt.accept()

    ret = conn.recv(1024).decode('utf-8')
    print(ret)

    with open(conf.userinfo_file, 'r', encoding='utf-8') as f1:
        for line in f1:
            # 确认登录信息
            if ret == line.strip():
                login_state = \
    """login success!
    1.下载
    2.上传"""
                conn.send(bytes(login_state, encoding='utf-8'))
            else:
                # 登录失败
                conn.send(b'fail')

                conn.close()
                skt.close()
                exit(0)

    while True:
        choose_operate = conn.recv(1024).decode('utf-8')
        if choose_operate == '1':
            conn.send('赞不提供 下载 服务'.encode('utf-8'))
            break
        elif choose_operate == '2':
            conn.send('你选择了 上传'.encode('utf-8'))
            head_len = conn.recv(4)
            head_len = struct.unpack('i', head_len)
            # json格式的报头
            print(head_len[0], head_len)
            head_json = conn.recv(head_len[0]).decode()
            head = json.loads(head_json)
            filesize = head['filesize']
            with open(head['filename'], 'wb') as f1:
                while filesize:
                    if filesize >= conf.buffer:
                        content = conn.recv(conf.buffer)
                        f1.write(content)
                        filesize -= conf.buffer
                    else:
                        content = conn.recv(conf.buffer)
                        f1.write(content)
                        conn.close()
                        skt.close()
                        exit(0)

            # break
        elif choose_operate.lower() == 'q':
            conn.send(b'q')
            break
        else:
            conn.send(b'meaningless choose')


    conn.close()
    skt.close()

if __name__ == '__main__':
    connect()
# connect()