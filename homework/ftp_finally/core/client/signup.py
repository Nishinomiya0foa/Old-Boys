"""注册"""

import hashlib

from homework.ftp_finally.conf import conf
from homework.ftp_finally.conf import log_conf

def signup(user, pwd):
    """注册，对密码进行md5加密。"""
    md5 = hashlib.md5('陈文波'.encode('utf-8'))
    with open(conf.user_table, 'a', encoding='utf-8') as f1:
        msg = user+'|'
        md5.update(pwd)
        secret_pwd = md5.hexdigest()
        msg = msg + secret_pwd
        # print(md5.hexdigest())
        # log_conf.pr_log().info('{}'.format(md5.hexdigest()))
        f1.write('{}\n'.format(msg))

def check_user(user):
    """判断user是否为已注册用户
    :return True?False
    """
    with open(conf.user_table, 'r', encoding='utf-8') as f1:
        flag = True
        for line in f1:
            if user != line[:line.index('|')]:  # 直接in不好
                # log_conf.pr_log().debug(user+'|')
                # self.request.send(b'0')
                # signup.signup(user, pwd)
                pass
            else:
                flag = False
        if flag:  # user 不存在
            return True
        else:# 已经存在同名user
            return False

if __name__ == '__main__':
    # signup('xiaochen', '123123')
    print(check_user('chen123'))