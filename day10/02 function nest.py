# _*_ coding:utf-8 _*_
__author__ = 'brian'
__date__ = '2019/3/2 0002 22:37'

"""
    函数嵌套
    
    第一类对象：  ----函数属于此类
        1.可在运行时创建
        2.可作为函数的参数或返回值
        3.可作为变量的实体
"""

# 利用函数嵌套，求3个数的最大值
# def max_of_2(a, b):
#     return max(a, b)
# def max_of_3(x,y,z):
#     c = max_of_2(x,y)  # 一个函数中调用其他函数
#     return max_of_2(c, z)
# print(max_of_3(3,2,6))

# 函数的嵌套定义
# 内部函数可以使用外部函数中的变量
# 内部函数定义之后，只能在定义他的直接外部函数中调用
# nonlocal 关键字 ----仅声明一个离他最近的上层的局部变量，用法及功能类似小global。仅局部变量

# def outer():
#     a = 1
#     b = 1
#     def inner():
#         print(a)
#         b=3.1414
#         print('here inner')
#         def inner2():
#             nonlocal b
#             b =3
#             print('here inner2')
#             print('inner2中的b',b)
#         inner2()
#         print('inner中的b', b) # 嵌套的函数inner2中由于声明了nonlocal，会影响到这一层
#     inner()
#     print('outer中的b',b)  # inner2()中的nonlocal声明不会影响到这一层
# outer()

def func():
    print(123)
func2 = func
func2()     # 函数名也是一个普通的变量，可以赋值给其他变量

l = [func, func2]  # 函数名可以作为容器类型的元素
for i in l:
    i()

def my_func(f):  # 函数名可以参数
    f()
    return f

fun3 = my_func(func)  # 函数名可以作为返回值
fun3()