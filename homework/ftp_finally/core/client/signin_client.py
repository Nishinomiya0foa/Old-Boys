import hashlib

from homework.ftp_finally.conf import conf

def check_signin(user, pwd):
    md5 = hashlib.md5('陈文波'.encode('utf-8'))
    md5.update(pwd)
    with open(conf.user_table, 'r', encoding='utf-8') as f1:
        for line in f1:
            if user == line[:line.index('|')] and md5.hexdigest() == line[line.index('|')+1:].strip():
                return True
        return False

if __name__ == '__main__':
    print(check_signin('chen123', b'1231'))

