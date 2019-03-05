"""
1.带参数的装饰器
2.多个装饰器控制同一个函数
    1.表现
    2.原理
"""
# 带参数的装饰器

# 多个函数调用装饰器时，为了便于控制装饰器。可以这样做
# import time
#
# FLAG = True  # 一 定义了全局变量FLAG
# def timmer_out(flag):  # 二 定义timmer_out()函数。接受一个参数
#     def timmer(f):  # 七 定义内部函数timmer() 接受一个参数
#         def inner(*args, **kwargs):
#             if flag:
#                 start = time.time()
#                 ret = f(*args, **kwargs)
#                 end = time.time()
#                 print(end - start)
#             else:
#                 ret = f(*args, **kwargs)
#             return ret
#         return inner
#     return timmer  # 八 返回timmer函数名
#
# @timmer_out(FLAG)  # 这里如果有参数，意思是先调用timmer_out()函数 参数为FLAG。return了timmer，然后就和无参数的装饰器一样了
#                 #  六 执行函数timmer_out()。 实参FLAG
#                 #  九 这里的作用等同于 @timmer   之后就与不带参数的装饰器执行步骤相同
# def work():  # 三 定义函数 work()
#     print('123123123')
#     time.sleep(0.1)
#
# @timmer_out(FLAG)
# def work1():  # 四 定义函数work1
#     print("working!")
#     time.sleep(1)
# work()  # 五 执行函数work
# work1()


# def wraper1(f):  # f -> func
#     def inner1():
#         print('wrap1 before')
#         f()
#         print('wrap1 after')
#     return inner1
#
# def wraper2(f):  # f -> inner1
#     def inner2():
#         print('wrap2 before')
#         print('wrap2 before')
#         f()
#         print('wrap2 after')
#         print('wrap2 after')
#     return inner2
#
# @wraper2  # func = wraper2(func) 此时的func 已经被 @ wraper1变成了inner1 所以：  func = wraper2(inner1) -》 func = inner2
# @wraper1  # func = wraper1(func)  -> func =  inner1
# def func():
#     print('in func now')
#
# func()  # 由于装饰器的原因  这里本质上执行的是 inner2()


""""""
import time

FLAG = False  # 增加标志位， 作为装饰器的开关
def timmer_out(flag):  # 装饰器外面再套上一层函数。形参为标志位
    def timmer(f):
        def inner(*args, **kwargs):
            if flag:
                start = time.time()
                ret = f(*args, **kwargs)
                end = time.time()
                print(end - start)
            else:
                ret = f(*args, **kwargs)
            return ret
        return inner
    return timmer

@timmer_out(FLAG)
def func1():
    print('this is func1')
    time.sleep(0.1)

@timmer_out(FLAG)
def func2():
    print('this is func2')
    time.sleep(0.2)

func1()
func2()