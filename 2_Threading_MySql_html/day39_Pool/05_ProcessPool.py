"""
    进程池: 解决进程的调度问题. 节省进程调度所需的时间(多个进程同时调度,开启,杀死)和空间(内存,堆栈)
    进程池的返回值: 进程池可以拥有返回值.
        # map的时候，所有任务的返回值会统一保存

    创建多个进程时,使用进程池Pool

    pool.map(func, iterable), 默认异步,参数必须可迭代. 自带close() 和 join()功能
    pool.apply(),  同步调用
    pool.appy_async()  异步调用,和主进程完全异步(主进程结束之后主进程就直接关了).需手动close和join

"""
import time
from multiprocessing import Pool

def func(num):
    # print('我打死了 {}'.format(num))
    print(1)

# if __name__ == '__main__':
#     pool = Pool(5)  # 进程池 中间有5个进程.
#     pool.map(func, range(10))
#         # pool.map(func, iterable)  func为子进程要执行的函数, iterable可迭代,其中每个值作为func的参数


# 进程池的返回值
def func2(i):
    time.sleep(1)
    return i*i

if __name__ == '__main__':
    p = Pool(5)
    for i in range(10):
        res = p.apply_async(func2, args=(i, ))  # 异步阻塞， res就是每一个任务的返回值
        print(res.get())  # .get()获取到结果. 会阻塞等待

