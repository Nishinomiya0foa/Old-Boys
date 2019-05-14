"""concurrent.futures 启动并行任务: 同时包括进程和线程,外部接口完全一致
    submit:
    map: 无返回值
    shutdown: 等同与之前的 p.close() + p.join()

    回调函数 callback

"""
import time
from concurrent.futures import ThreadPoolExecutor


def func(n):
    time.sleep(2)
    print(n)
    return n**2


def deal(m):
    print('结果是{}'.format(m.result()))


# t = ThreadPoolExecutor(max_workers=5,)  # 最大不要超过5*cpu个数
# r_list = []
executor = ThreadPoolExecutor(max_workers=5)
for i in range(15):
    # executor.submit(func, i)
    future = executor.submit(func, i).add_done_callback(deal)  # 接收函数名和参数, 不要以元组的形式.
    # r_list.append(future)
    # print(future.result())
executor.shutdown()  # close+join
print('主线程')
# print(len(r_list))