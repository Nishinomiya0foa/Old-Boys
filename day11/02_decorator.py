# _*_ coding:utf-8 _*_
__author__ = 'brian'
__date__ = '2019/3/4 0004 23:19'

"""decorator 装饰器"""
# 装饰器形成的过程
#    ----从无参无返回值，到任意参数，有返回值的
#    ----装饰器一般 命名 wrapper()
# 装饰器的作用
#   给函数添加功能，但不影响本身函数的内部结构
# 原则:开放封闭原则。保护程序的稳定性
#    ----开放：对扩展开放
#    ----封闭：对修改封闭
# 装饰器的固定模式
# def wrapper(f):  # 装饰器函数，需定义在被装饰器函数之前；f是形参，接受传入的被装饰的函数的函数名
#     def inner(*args,**kwargs):
#         """此处添加被装饰函数执行前执行的程序"""
#         ret = f(*args,**kwargs)  # 执行被装饰的函数。把它的返回值赋值给变量ret
#         """此处添加被装饰函数执行后执行的程序"""
#         return ret  # inner（）函数返回ret，ret也是被装饰器函数的返回值
#     return inner    # 直接返回inner函数的函数名，注意不加括号。否则会直接执行 inner（）
#
# @wrapper  # 调用装饰器函数
# def be_wrappered(a,b=3):  # 被装饰器函数
#     print(a ** b)
#
# be_wrappered(3,1)  # 假装直接调用被装饰器函数；实际调用了inner函数




"""
time 模块
time.time()  # 获取当前时间 
            #1551713495.179004   小数点前的数字为1970.01.01距今的秒数
time.sleep(n) # 程序执行到这儿，停n秒
"""


# 不修改函数的调用过程，在函数的前后增加功能
# 以下的timmer（）就是一个装饰器函数，只是对一个函数，起装饰作用

# # 标注出以下程序每一行的执行顺序
#
# import time
# def func():  # 一 定义函数func（）
#             # 十二 进入func（）函数， 执行内部逻辑
#     """被装饰的函数"""
#     time.sleep(0.01)  # 十三 执行休眠代码，也是工作代码
#     print("123123123123123")  # 十四 工作代码
#
# def timmer(f):  # 二 定义函数timmer（）
#                 # 四 进入timmer（）函数，执行内部逻辑，实参为第三步的参数func，及第一步中定义的函数名
#     """装饰器函数"""
#
#     def inner():  # 五 定义内部函数 inner（）
#                 # 九 进入inner（）函数，执行内部逻辑
#         start = time.time()  # 十 当前时间赋值给变量start
#         f()  # 十一 调用函数f（），f为外面函数的参数 func。所有这形成了闭包
#                 # 被装饰的函数
#         end = time.time()  # 十五 当前时间赋值给变量end
#         print(end-start)   #十六 输出工作代码的执行时长
#     return inner  # 六 将内部函数inner（）的函数名返回
#
# func = timmer(func)  # 三 执行函数timmer（），参数为函数func（）的函数名--func
#                     # 七 将等号右边的值 赋值给func， 即func=inner
# func()  # 八 由于func = inner，所以这一步执行了inner（）函数




# 写一个函数，返回一个数字的平方。
# 使用装饰器模式，在他的前后行加上说明和结束语句

def decor_explain(f):
    def inner(*args, **kwargs):
        print("现在开始计算：")
        f(*args, **kwargs)
        print("计算结束")
        return f(*args, **kwargs)
    return inner

@decor_explain  # 语法糖
def get_pow(num):  # 被装饰的函数
    pows = num ** 2
    return pows

@decor_explain # 语法糖
def get_pow_2(num1,num2):
    pows = num1 ** num2
    return pows

# get_pow = decor_explain(get_pow)

print(get_pow(12))
print(get_pow_2(3,num2=3))
