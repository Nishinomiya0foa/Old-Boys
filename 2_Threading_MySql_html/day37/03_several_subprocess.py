"""
    创建多个子进程
        多个p.start()就好了;

    如果我们希望确保多个子进程都执行完之后,立即同步到主进程,该怎么做?
        1.将所有的子进程id 添加到列表
        2.待所有的进程开启之后,将所有的子进程id,同步
"""
import time
from multiprocessing import Process


def fun(*args):
    print('*'*args[0])
    time.sleep(2)
    print('*'*args[1])



if __name__ == '__main__':
    p_list = []
    for i in range(10):
        p = Process(target=fun, args=(5*i,10*i))
        p_list.append(p)
        p.start()
    # p.join()  # 这种方法只会把 i = 9(最后一次循环执行完之后的p),同步到主进程;而此时,所有的子进程不一定都执行完了
    [p.join() for p in p_list]  # 确保之前的所有进程都必须在这里执行完,才能执行之后的代码
    # for p in p_list:
    #     p.join()
    print('执行完了')