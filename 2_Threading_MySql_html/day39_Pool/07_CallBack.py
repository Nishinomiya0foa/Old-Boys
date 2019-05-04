"""回调函数
        ---- 把一个函数的返回值作为参数，执行另一个函数(在主进程执行)"""

import os
from multiprocessing import Pool

def func1(n):
    print('In func1 ', os.getpid())

    return n**2

def func2(n):
    print('In func2 ', os.getpid())
    print(n)

if __name__ == '__main__':
    print('主进程:', os.getpid())
    p = Pool(5)
    p.apply_async(func=func1, args=(9, ), callback=func2)
    p.close()
    p.join()