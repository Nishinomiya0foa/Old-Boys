"""进程池"""

import os

# apply
import time
from multiprocessing import Pool

def func(n):
    print('start func {}, port: {}'.format(n, os.getpid()))
    time.sleep(1)
    print('end func {}, port: {}'.format(n, os.getpid()))

if __name__ == '__main__':
    p = Pool(5)
    for i in range(15):
        p.apply_async(func, args=(i,))  # p.apply_async()  异步
                                        # p.apply() 同步

    p.close()   # 结束进程池接收任务
    p.join()  # 感知进程池中的任务执行结束