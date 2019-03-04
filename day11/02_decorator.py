# _*_ coding:utf-8 _*_
__author__ = 'brian'
__date__ = '2019/3/4 0004 23:19'

# 装饰器形成的过程
# 装饰器的作用
# 原则:开放封闭原则
# 装饰器的固定模式



"""
time 模块
time.time()  # 获取当前时间 
            #1551713495.179004   小数点前的数字为1970.01.01距今的秒数
time.sleep(n) # 程序执行到这儿，停n秒
"""
import time


# 标注出以下程序每一行的执行顺序
def func():  # 一 定义函数func（）
            # 十二 进入func（）函数， 执行内部逻辑
    """工作实际要用的函数"""
    time.sleep(0.01)  # 十三 执行休眠代码
    print("123123123123123")  # 十四 工作代码

def timmer(f):  # 二 定义函数timmer（）
                # 四 进入timmer（）函数，执行内部逻辑，实参为第三步的参数func，及第一步中定义的函数名
    """统计工作函数运行时间的函数"""
    def inner():  # 五 定义内部函数 inner（）
                # 九 进入inner（）函数，执行内部逻辑
        start = time.time()  # 十 当前时间赋值给变量start
        f()  # 十一 调用函数f（），f为外面函数的参数 func。所有这形成了闭包
        end = time.time()  # 十五 当前时间赋值给变量end
        print(end-start)   #十六 输出工作代码的执行时长
    return inner  # 六 将内部函数inner（）的函数名返回

func = timmer(func)  # 三 执行函数timmer（），参数为函数func（）的函数名--func
                    # 七 将等号右边的值 赋值给func， 即func=inner
func()  # 八 由于func = inner，所以这一步执行了inner（）函数