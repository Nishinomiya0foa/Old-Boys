
"""
1、常用字符串格式化有哪些？并说明他们的区别（6）
    答: %s -- 普通字符串  
        %d -- 数组
        %r -- 不进行转译
        或者 format()
            按顺序填写/按编号填写/命名
2、请写出【元祖，列表，字典，集合】的定义方法、新增方法、更改方法、删除方法（4）
    元组:  t = () / t = tuple()
            元组没有新增方法.
            元组不提供更改方法,可以转为数组,使用数组的replace(old, new)之后,转回元组
            删除元组 del t; 元组不提供删除里面元素的方法,同样可以使用数组的remove(obj), 或pop(index)方法
    列表:  l = [] / l = list[]
    字典:  d = {}
            d[key] = value
            d[key] = newvalue
            del d[key]/ d.pop(key)/ del d
    集合:  s = set()
            s.add()
            s.remove()
    
3、利用python打印前一天的本地时间，格式为‘2018-01-30’（面试题）（5）

4、python中search（）和match（）的区别（面试题）（5）
    re 模块
        search: 不从头匹配,中间仍有可能匹配到结果
        match:从头匹配,开头不一致则一定无法匹配到结果
5、什么是1ambda函数，有什么好处（2）
    匿名函数,不用给函数命名,可以完成一些简单的事情,简洁
6、说明_init和_new_的作用（2）
    __init__初始化函数, 是类被实例之后就会直接调用的函数
7、简述反射是怎么回事？（3）
    由字符串类型,反射为其本身的类型
8、解释python中深拷贝和浅拷贝的区别（3）
    deepcopy: 拷贝内存地址
    copy: 拷贝值
9、用最简洁的方式生成这样一个列表【4，16，32，64，128】（3）
    a = [2**i for i in range(2,8)]
10、python中如何实现随机数并打印，默认的随机数范围是多少？（2）
    random模块
    (0,1)
    print(random.random())
11、新式类和金典类（旧式类）的区别（一种一分）（2）
    新式类默认继承object;
    super
12、装饰器什么时候被执行的（3）

13、什么是”并发“？什么是”并行“？（2）
    并发是cpu层面的,是每个任务都能很快被执行,执行时间也很短,所以可以多个任务看起来像在同时执行,成为并发
    并行是宏观的,是同时执行的任务数<cpu数量. 可以被同时执行
14、以个人理解描述Event的执行原理（2）
    Event是进程间通信的, 具有两种状态. True?False, 可以根据状态的改变来传递信号.
    创建之初是False, 阻塞; 等待状态被set后,变为True,不阻塞
15、什么是粘包，如何避免？（3）
    只有TCP会出现粘包. send时由于nagle算法,多个较小的包会统一发送
                      recv时 没有一次性从缓冲区取出所有的包, 下一次取包时,取出的是上次的遗留数据
16、什么是进程？（2）
    是cpu执行任务的最小单位
17、什么是线程？（2）
    是CPU调度的最小单位
18、简述你对管道、队列的理解；（3）
    管道Pipe:
    队列Queue: fifo/
19、编程题；写一个装饰器实现功能：打印程序的运行时间（5）
"""
import time
import random

# def cal_time(f):  # 1
#     def inner(*args, **kwargs):  # 4
#         t1 = time.time()
#         f(*args, **kwargs)
#         t2 = time.time()
#         print(t2-t1)
#     return inner
#
#
# def func():  # 2
#     print('程序开始执行.')
#     time.sleep(random.randint(0,4))
#     print('程序执行结束.')
#
# func = cal_time(func)  # 3 右边
#
# func()
"""
20、读以下代码，写出答案并简述原因（面试题建议不是电脑）（5）
下面代码会输出什么：
def f(x，1=[])：
    for i in range(x)：
        1.append(i*i)
    print 1

f(2)
f(3,[3,2,1])
f(3)

21、使用python简单实现打印九九乘法表（3）
"""
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,'*',i,'=', j*i, end='    ')
#     print('')

# [print(j,'*',i,'=', j*i, end='    ') for i in range(1,10) for j in range(1,i+1)]

"""
22、简述python GIL的概念，以及它对python多线程的影响？（2）
    在多线程中,多个cpu中的缓存数据同步时,可能引发数据不安全.所以引入了全局排他锁的方法
    导致了Cpython编译器中不能实现真正意义上的多线程,降低了效率.
23、写一个单例模式（4）
24、编程题：将以下1ist3的格式转换成list4格式（8）
list3=[
    {"name"："alex"，"hobby"："抽烟}，
    {"name"："alex"，"hobby"："喝酒"}，
    {"name"："alex"，"hobby"："烫头"}，
    {"name"："alex"，"hobby"："Massage"}，
    {"name"："egon"，"hobby"："喊麦}，
    {"name"："egon"，"hobby"："街舞}，
]
list4=[
    {"name"："alex"，"hobby_list"：["抽烟"，"喝酒"，”烫头"，"Massage"]}，
    {"name"："egon"，"hobby_list"：["喊麦”，“街舞"]}，
]

25、编程题（7）
一：定义一个学生类。有下面的类属性：
    1姓名
    2年龄
    3成绩（语文，数学，英语）[每课成绩的类型为整数]
类方法：
    1获取学生的姓名：get_name（）返回类型：str
    2获取学生的年龄：get_age（）返回类型：int
    3返回3门科目中最高的分数。get_course（）返回类型：int
写好类以后，可以定义2个同学测试下：
    zm=Student'zhangming'，20，[69，88，100]）
返回结果：
    zhangming
    20
    100

26、写一个socket客户端和服务端兵进行通讯（4）
27、什么是异步，什么是异步阻塞？（2）
    #在同一时间可以同时做两件事情
28、写一个程序，包含十个线程，子线程必须等待主线程sleep10秒钟之后才执行，并打印当前时间（5）
"""
from concurrent.futures import thread


def print_time():
    print(time.strftime('%H:%M:%S'))


"""
29、你所了解的锁都有哪些？（2）
30、threading.RLock和threading.Lock的区别
"""
