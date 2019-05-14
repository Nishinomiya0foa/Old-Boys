"""条件 Condition
 四个方法:
    acquire
    release
    wait
    notify(n):  唤醒最多n个等待这个条件变量的进程
                需要被acquire和release嵌套之间.
                不会释放锁.

"""


from threading import Thread,Condition


def func(con,i):
    con.acquire()
    con.wait()  # 比锁多的一步, 需等待
    print('在第%s个循环里'%i)
    con.release()


con=Condition()
for i in range(10):
    Thread(target=func,args=(con,i)).start()
while True:
    num=int(input('>>>'))
    # notify必须被acquire和release嵌套
    con.acquire()
    con.notify(num) #造钥匙
    con.release()