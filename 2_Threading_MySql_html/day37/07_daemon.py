"""
守护进程: 是子进程转换成的
    ---- 守护进程会随着主进程的代码执行结束而结束*; 即即使有其他的子进程还活着,守护进程也会结束.
p.daemon = True 设置为守护进程
p.name  # 进程名
terminate()  # 关闭子进程; 不会立即生效,操作系统会有一个极短的响应时间.
is_alive()  # 返回进程是否存活
"""
import time
import random
from multiprocessing import Process


class TryDaemon(Process):
    def run(self):
        while True:
            words = random.choice(['我还活着','我在呢','一直守护你'])
            time.sleep(0.5)
            print(words)


if __name__ == '__main__':
    p = TryDaemon()
    # 设置为守护进程
    p.daemon = True
    p.start()
    time.sleep(5)
    print('Main Process END!')