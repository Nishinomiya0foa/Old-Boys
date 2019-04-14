import os
import hashlib

from homework.ftp_finally.conf import conf


def check_continue_md5(server_filepath, continue_dic:dict):
    server_file_fullname = os.path.join(server_filepath, continue_dic['chosen_file'])
    continue_filesize = continue_dic['continue_filesize']
    filesize = 0
    md5 = hashlib.md5()
    with open(server_file_fullname, 'rb') as f1:
        while filesize < continue_filesize:
            content = f1.read(conf.buffer)
            md5.update(content)
            filesize += conf.buffer
        return md5.hexdigest()

def continue_download():
    pass

if __name__ == '__main__':
    check_continue_md5(r'F:\python old boys\linux 部分\day4',{'chosen_file': '01上节作业.mp4', 'chosen_downup': '2b', 'continue_filesize': 47833088, 'continue_file_md5': 'a02a9be8b5b86664544d4173fa122d45'})