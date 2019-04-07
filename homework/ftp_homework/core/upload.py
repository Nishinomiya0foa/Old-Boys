import os
import struct
import json

from core import message_head

def upload():
    head = message_head.head()
    filelist = os.listdir(head['path'])
    # print(filelist)
    dic = {}
    print("文件列表如下：请选择想要上传的文件。")
    for i in range(len(filelist)):
        dic[i] = filelist[i]
        print((i,dic[i]))
    choose_file = input('>')
    try:
        choose_file = int(choose_file)
    except:
        print("找不到你选中的文件")
    filename = dic[choose_file]
    full_filename = os.path.join(head['path'],filename)
    filesize = os.path.getsize(full_filename)
    head['filename'] = filename
    head['filesize'] = filesize

    filesize_pack = struct.pack('i',filesize)
    return head, filesize_pack

if __name__ == '__main__':
    upload()