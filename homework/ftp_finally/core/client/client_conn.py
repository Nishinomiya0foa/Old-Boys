import socket
import json
import os
import hashlib
import struct

from homework.ftp_finally.conf import conf, log_conf
from homework.ftp_finally.core.client import signup_client,download_client,header
from homework.ftp_finally.core import show_path


def client_conn(ip_port):
    skt = socket.socket()
    skt.connect(ip_port)

    # islogin = False
    print("""请选择操作：
    1.登录
    2.注册""")
    chosen = input('>')
    if chosen:
        # 发送server端 客户端的选择
        skt.send(chosen.encode('utf-8'))

        if chosen == '1':
            user, pwd = signup_client.signup_client()  # 输入用户名，密码
            skt.send(user.encode('utf-8'))
            skt.send(pwd.encode('utf-8'))
            # 接收返回值
            ret = skt.recv(1024).decode('utf-8')
            if ret == '0':
                print('登录成功，欢迎你, {}'.format(user))
                # 调用 选择操作 方法
                # 接受文件目录 文件名 选择（上传/下载）
                """
                server_download_path:服务器下载路径
                chosen_file:下载的文件名
                continue_filesize:待续传文件已经下载部分的大小，没有则None
                continue_file_md5：待续传文件的已经下载部分的md5值,没有则None
                chosen_downup：用户的选择， 1---上传；2----下载"""
                server_download_path, chosen_file,continue_filesize, continue_file_md5,\
                    chosen_downup = download_client.choose_operate()
                if chosen_downup == '1':
                    skt.send(chosen_downup.encode('utf-8'))
                    """上传"""
                    pass

                # 下载全新文件
                elif chosen_downup == '2' and continue_filesize is None:
                    """下载
                    1.接收报头， 解析出文件大小
                    2.根据文件大小，设置接收
                    """
                    skt.send(chosen_downup.encode('utf-8'))
                    skt.send(chosen_file.encode('utf-8'))
                    head_json = skt.recv(1024).decode('utf-8')
                    head_dic = json.loads(head_json)
                    filesize = head_dic['filesize']
                    user_self_path = os.path.join(conf.user1_selfpath, chosen_file)
                    # 实例md5
                    md5 = hashlib.md5()

                    with open(user_self_path, 'wb') as f1:
                        while filesize:
                            if filesize >= conf.buffer:
                                content = skt.recv(conf.buffer)
                                md5.update(content)
                                f1.write(content)
                                filesize -= conf.buffer
                            else:
                                content = skt.recv(filesize)
                                md5.update(content)
                                f1.write(content)
                                break
                        client_md5 = md5.hexdigest()
                        print('文件下载完成，正在校验...')
                        skt.send(client_md5.encode('utf-8'))
                        ret = skt.recv(1024).decode('utf-8')

                        if ret == '0':
                            log_conf.pr_log().info('用户 {} 成功下载文件 {}'.format(user, user_self_path))
                            print('文件校验完成！')
                        else:
                            log_conf.pr_log().error('用户 {} 失败下载文件 {}'.format(user, user_self_path))
                            print('文件校验失败！')

                # 下载 续传文件
                elif chosen_downup == '2' and continue_filesize:
                    chosen_downup = chosen_downup + 'b'
                    # 发送 chose_downup  --- 2b  , 指选择续传
                    skt.send(chosen_downup.encode('utf-8'))
                    # skt.send(str(continue_filesize).encode('utf-8'))
                    continue_dic = {}
                    continue_dic['chosen_file'] = chosen_file
                    continue_dic['continue_filesize'] = continue_filesize
                    continue_dic['continue_file_md5'] = continue_file_md5
                    continue_dic_json_encode = json.dumps(continue_dic)
                    # 发送 字典
                    skt.send(continue_dic_json_encode.encode('utf-8'))
                    reply = skt.recv(1024).decode('utf-8')
                    continue_file_path = os.path.join(conf.user1_selfpath, chosen_file)
                    if reply == '0':
                        left_filesize_encode = skt.recv(4)
                        # 剩余待下载文件大小
                        left_filesize = struct.unpack('i', left_filesize_encode)[0]
                        print('正在续传中...')


                        md5 = hashlib.md5()
                        with open(continue_file_path, 'ab') as f1:
                            while left_filesize:
                                if left_filesize >= conf.buffer:
                                    content = skt.recv(conf.buffer)
                                    f1.write(content)
                                    md5.update(content)
                                    left_filesize -= conf.buffer

                                else:
                                    content = skt.recv(left_filesize)
                                    f1.write(content)
                                    md5.update(content)
                                    break
                            skt.send(md5.hexdigest().encode('utf-8'))
                    res = skt.recv(1024).decode('utf-8')
                    if res == '0':
                        print('续传文件成功。')
                        log_conf.pr_log().info('用户 {} 续传文件 {}'.format(user, continue_file_path))
                    else:
                        print('续传文件失败')

            elif ret == '-1':
                print('登录失败！')
                exit(0)

        elif chosen == '2':
            user,pwd = signup_client.signup_client()
            skt.send(user.encode('utf-8'))
            skt.send(pwd.encode('utf-8'))
            ret = skt.recv(1024)
            if ret == b'-1':
                print('用户名已存在。')
                exit(0)
            elif ret == b'0':
                print('注册成功，欢迎你， {}'.format(user))
                exit(0)

    skt.close()
    # return登录状态
    # return islogin

if __name__ == '__main__':
    client_conn(conf.ip_port)

