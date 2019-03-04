# _*_ coding:utf-8 _*_
__author__ = 'brian'
__date__ = '2019/3/2 0002 22:37'

"""函数嵌套和作用域链"""

"""
函数嵌套调用：
def func1():
    pass
def func2():
    func1()
func2()
    
    第一类对象：  ----函数属于此类
        1.可在运行时创建
        2.可作为函数的参数或返回值
        3.可作为变量的实体
    
函数可以嵌套定义
def outer():
    def inner():
        pass
    
    内部函数可以使用外部函数中的变量，仅使用离他最近的一个外部变量。
    内部函数定义之后，只能在定义他的直接外部函数中调用
    nonlocal 关键字 ----仅声明一个离他最近的上层的局部变量，用法及功能类似小global。仅局部变量
    
def outer():    # 定义外部函数outer()
    a = 1   # 声明外部函数中的变量a=1
    b = 1   # 声明外部函数中的变量b=1
    def inner():    # 第一层内部函数inner()
        print('我现在进入了 inner()') # 打印字符串，证明进入了inner()函数
        print('我在inner()中使用了外部函数outer()中的变量a：'a)    # 打印a的值，这里打印的是outer()中的变量a的值
        b=3.1414    # 在内部函数inner()中，声明b=3.1414。这里的b不是outer()中的b
        def inner2():   # 定义第二层内部函数inner2()，他的直接外部函数为inner()，最外层函数为outer()
            nonlocal b  # 对变量b进行，nonlocal声明。这里的声明会影响到外部函数中的b，
                        # 如果直接外部函数中没有这个变量。会再在更外层
            b =3    # 修改b的值
            print('我现在进入了 inner2')  # 打印字符串，证明进入了inner2函数
            print('我对变量b进行了nonlocal声明。')
            print('我改变了b的值，现在b=',b)  # 打印此时inner2中b的值
        inner2()  # 执行inner2()
        print('inner中的b为{}，这是因为我再inner2()中声明了nonlocal，且修改了他的值'.format(b)) # 打印inner中的b的值。 这里的b被inner2()中修改了
                               # 嵌套的函数inner2中由于声明了nonlocal，会影响到这一层
    inner() # 执行inner()
    print('outer中的b为{}，这是因为nonlocal没有影响到这一层'.format(b))  # inner2()中的nonlocal声明不会影响到这一层
outer() # 执行inner()
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

# def func():
#     print(123)
# func2 = func
# func2()     # 函数名也是一个普通的变量，可以赋值给其他变量
#
# l = [func, func2]  # 函数名可以作为容器类型的元素
# for i in l:
#     i()
#
# def my_func(f):  # 函数名可以参数
#     f()
#     return f
#
# fun3 = my_func(func)  # 函数名可以作为返回值
# fun3()

# def outer():    # 定义外部函数outer()
#     a = 1   # 声明外部函数中的变量a=1
#     b = 1   # 声明外部函数中的变量b=1
#     def inner():    # 第一层内部函数inner()
#         print('我现在进入了 inner()') # 打印字符串，证明进入了inner()函数
#         print('我在inner()中使用了外部函数outer()中的变量a：',a)    # 打印a的值，这里打印的是outer()中的变量a的值
#         b=3.1414    # 在内部函数inner()中，声明b=3.1414。这里的b不是outer()中的b
#
#         def inner2():   # 定义第二层内部函数inner2()，他的直接外部函数为inner()，最外层函数为outer()
#             nonlocal b  # 对变量b进行，nonlocal声明。这里的声明会影响到外部函数中的b，
#                         # 如果直接外部函数中没有这个变量。会再在更外层
#             b =3    # 修改b的值
#             print('我现在进入了 inner2')  # 打印字符串，证明进入了inner2函数
#             print('我对变量b进行了nonlocal声明。')
#             print('我改变了b的值，现在b=',b)  # 打印此时inner2中b的值
#         inner2()  # 执行inner2()
#         print('inner中的b为{}，这是因为我再inner2()中声明了nonlocal，且修改了他的值'.format(b)) # 打印inner中的b的值。 这里的b被inner2()中修改了
#                                # 嵌套的函数inner2中由于声明了nonlocal，会影响到这一层
#     inner() # 执行inner()
#     print('outer中的b',b)  # inner2()中的nonlocal声明不会影响到这一层
# outer() # 执行inner()