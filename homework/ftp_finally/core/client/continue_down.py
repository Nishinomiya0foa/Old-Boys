import os
import hashlib

from homework.ftp_finally.conf import conf


def continue_down(filepath, filename):
    file_full_name = os.path.join(filepath,filename)
    print(file_full_name)
    filesize = os.path.getsize(file_full_name)  # 客户端待续传
    filesize_ret = os.path.getsize(file_full_name)
    # filesize = 0
    print(filesize)
    md5 = hashlib.md5()
    with open(file_full_name, 'rb') as f1:
        while filesize:
            if filesize >= conf.buffer:
                content = f1.read(conf.buffer)
                md5.update(content)
                filesize -= conf.buffer
            else:
                content = f1.read(filesize)
                md5.update(content)
                filesize -= conf.buffer
        # while filesize < 43073536:
        #     content = f1.read(conf.buffer)
        #     md5.update(content)
        #     filesize += conf.buffer
        return filesize_ret, md5.hexdigest()
    # print(filesize)

if __name__ == '__main__':
    # filepath = r'F:\python old boys\linux 部分\day4'  # server端
    filepath = r'F:\python old boys\testFile'  # client端
    filename = r'01上节作业.mp4'
    continue_down(filepath, filename)