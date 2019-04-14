import socketserver
import json
import os
import hashlib
import struct

from homework.ftp_finally.conf import conf
from homework.ftp_finally.core.client import signup,signin_client, header
from homework.ftp_finally.conf import log_conf
from homework.ftp_finally.core import server_continue

class MySocket(socketserver.BaseRequestHandler):
    def handle(self):
        print('{} 连接...'.format(self.client_address))
        # 第一步，接收传递的选择（登录|注册）  接收传递的user？pwd
        chosen = self.request.recv(1024).decode('utf-8')
        # 第二步，接收传递的user/pwd
        user = self.request.recv(1024).decode('utf-8')
        pwd = self.request.recv(1024)
        # 登录
        if chosen == '1':
            # 登录成功
            if signin_client.check_signin(user, pwd):
                # 发送返回值
                self.request.send(b'0')
                print('用户：{}'.format(user))
                # head_json = self.request.recv(1024).decode('utf-8')
                # # 报头字典
                # head_dic = json.loads(head_json)
                # # 文件大小
                # filesize = head_dic['filesize']
                # while filesize:
                #     if filesize >= conf.buffer:
                #         self.request.recv(conf.buffer)
                #         filesize -= conf.buffer
                #     else:
                #         self.request.recv(filesize)
                #         break
                # 接收客户端发来的选择（上传/下载）
                chosen_downup = self.request.recv(1024).decode('utf-8')
                if chosen_downup == '1':
                    """上传"""
                    pass
                elif chosen_downup == '2':
                    """下载
                    1. 发送报头，包含 文件目录 文件名  文件大小
                    2. 发送文件"""
                    # 接收客户端发来的想下载的文件名
                    downfile = self.request.recv(1024).decode('utf-8')
                    # 报头
                    head_json_encode = header.head(conf.server_download_path,downfile)
                    self.request.send(head_json_encode)
                    head_json = head_json_encode.decode('utf-8')
                    head_dic = json.loads(head_json)
                    file_full_path = os.path.join(head_dic['filepath'], head_dic['filename'])
                    filesize = head_dic['filesize']
                    md5 = hashlib.md5()
                    with open(file_full_path, 'rb') as f1:
                        while filesize:
                            if filesize >= conf.buffer:
                                content = f1.read(conf.buffer)
                                md5.update(content)
                                self.request.send(content)
                                filesize -= conf.buffer
                            else:
                                content = f1.read(filesize)
                                md5.update(content)
                                self.request.send(content)
                                # 接收客户端发来的md5值， 进行比对
                                server_md5 = md5.hexdigest()
                                client_md5 = self.request.recv(1024).decode('utf-8')
                                if server_md5 == client_md5:
                                    self.request.send(b'0')
                                else:
                                    self.request.send(b'-1')
                                    break

                elif chosen_downup == '2b':
                    continue_dic_json_encode = self.request.recv(1024)
                    continue_dic = json.loads(continue_dic_json_encode)
                    server_md5_value = server_continue.check_continue_md5(conf.server_download_path, continue_dic)
                    if server_md5_value == continue_dic['continue_file_md5']:
                        """是可续传的文件"""
                        self.request.send(b'0')
                        # server_continue.continue_download()
                        file_full_path = os.path.join(conf.server_download_path, continue_dic['chosen_file'])
                        file_full_filesize = os.path.getsize(file_full_path)
                        # 需要续传的剩余文件大小
                        file_continue_size = file_full_filesize - continue_dic['continue_filesize']
                        file_continue_size_encode = struct.pack('i', file_continue_size)
                        self.request.send(file_continue_size_encode)

                        md5 = hashlib.md5()
                        with open(file_full_path, 'rb') as f1:
                            # 文件指针移到 续传位置
                            f1.seek(continue_dic['continue_filesize'])
                            while file_continue_size:
                                if file_continue_size >= conf.buffer:
                                    content = f1.read(conf.buffer)
                                    self.request.send(content)
                                    file_continue_size -= conf.buffer
                                    md5.update(content)
                                else:
                                    content = f1.read(file_continue_size)
                                    self.request.send(content)
                                    md5.update(content)
                                    break
                            server_md5_full = md5.hexdigest()
                            ret = self.request.recv(1024).decode('utf-8')
                            if server_md5_full == ret:
                                self.request.send(b'0')
                            else:
                                self.request.send(b'-1')
                    else:
                        """文件不同，不可续传"""


            # 登录失败
            else:
                self.request.send(b'-1')

        # 注册
        elif chosen == '2':
            # 调用signup.check_user()方法。 判断user是否已存在
            if signup.check_user(user):
                signup.signup(user, pwd)
                self.request.send(b'0')
            else:
                self.request.send(b'-1')



if __name__ == '__main__':
    skt_s = socketserver.ThreadingTCPServer(conf.ip_port, MySocket)
    skt_s.serve_forever()