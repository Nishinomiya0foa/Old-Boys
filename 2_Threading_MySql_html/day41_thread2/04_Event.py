"""事件 Event
默认False
    wait() 阻塞
True
    wait()  非阻塞

# 修改状态
    clear     设置为默认值False, 阻塞
    set:     设置为True 非阻塞

"""

# 连接数据库 检测数据库的连接情况
"""
#起两个线程
#第一个线程：连接数据库
    #等待一个信号告诉我我们之间的网络是通的
    #连接数据库
#第二个线程：检测与数据库之间的网络是否连通
    #time.sleep（0.2）2
    #将事件的进态设置为Trud"""

import time
import random
from threading import Thread, Event


def conn_db(e):
    count = 0
    while count < 3:
        if e.wait(0.8):
            print('成功连接.')
            break
        else:
            count+=1
            print('{} 次超时'.format(count))
    else:
        print('超时')

def check_net(e):
    time.sleep(random.randint(0,3))
    e.set()


if __name__ == '__main__':
    e = Event()
    t_check = Thread(target=check_net, args=(e,))
    t_conn = Thread(target=conn_db, args=(e,))
    t_check.start()
    t_conn.start()

# while   else   -> while正常执行完,则走else; 如果被break,则不走else
