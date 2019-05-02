"""事件
    ---- 通过一个信号来控制多个进程, 是他们同时执行或阻塞

    事件被创建之后,默认是阻塞状态
    e = Event()  # 创建一个事件;状态默认为False

    .set()  # 修改事件状态为True
    .clear()  # 重置事件状态为False;

    .is_set()  # 查看事件的状态
    .wait()  # 根据事件状态来决定是否阻塞.  True -> 不阻塞; False -> 阻塞

    """
import time
import random
from multiprocessing import Event, Process
# e = Event()  # 创建了一个事件
# print(e.is_set())  # 查看这个事件的状态,默认为阻塞
# e.set()  # 把这个事件的状态改为True, 非阻塞
# e.wait() # 根据e.is_set()的值来决定是否阻塞
# e.clear()  # 重置事件状态, 默认为阻塞
#
# print(e.is_set())


# 红绿灯事件
class PassCar(Process):
    def __init__(self, e, car_num):
        super().__init__()
        self.e = e
        self.car_num = car_num
    def run(self):
        if not self.e.is_set():  # 红灯
            print('\033[0;31;40m car{} 在等待通行\033[0m'.format(self.car_num))
            self.e.wait()
        print('\033[0;32;40m car{} 在已经通过\033[0m'.format(self.car_num))



class TrafficLight(Process):
    def __init__(self, e):
        super().__init__()
        self.e = e

    def run(self):
        while True:
            if not self.e.is_set():  # 不是默认值(即not e的状态为false)  这是not false -> True
                # 设置信号量为True, 绿灯亮3秒
                self.e.set()
                print('\033[32m绿灯亮\033[0m')
                time.sleep(3)
            else:
                # 设置信号量为False,红灯亮3秒
                self.e.clear()
                print('\033[31m红灯亮\033[0m')
                time.sleep(3)


if __name__ == '__main__':
    e = Event()
    traffic = TrafficLight(e)
    traffic.start()

    for i in range(30):
        time.sleep(random.random())
        car = PassCar(e, i)
        car.start()
