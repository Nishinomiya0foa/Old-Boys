"""进程之间的数据共享
    Manager 模块中的很多数据类型,会有数据不安全. 因为多个进程争夺同一资源.  同样使用进程锁来限制
"""

from multiprocessing import Manager

if __name__ == '__main__':

    m = Manager()
    dic = m.dict({'student': 45})  # 这是字典是进程间共享的数据
