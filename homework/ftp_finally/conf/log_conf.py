import logging

from homework.ftp_finally.conf import conf

def pr_log():
    logger = logging.getLogger()
    # 定制日志格式
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - (%(filename)s的-%(funcName)s-%(lineno)d行)    : %(message)s')

    log_file = conf.log_file
    fh = logging.FileHandler(filename=log_file, encoding='utf-8')
    sh = logging.StreamHandler()

    # 绑定日志格式
    fh.setFormatter(formatter)
    sh.setFormatter(formatter)

    # 设置日志级别
    logger.setLevel(logging.DEBUG)
    fh.setLevel(logging.INFO)
    sh.setLevel(logging.DEBUG)

    logger.addHandler(fh)
    logger.addHandler(sh)
    return logger



if __name__ == '__main__':

    pr_log().error('thisisaeerrr')