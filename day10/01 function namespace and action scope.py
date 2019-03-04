# _*_ coding:utf-8 _*_
__author__ = 'brian'
__date__ = '2019/3/2 0002 21:33'

"""命名空间和作用域"""


"""
命名空间 三种：
    内置命名空间：python解释器
                ----python解释器中已经存在的。如：print(), input();
                      内部命名在启动解释器的时候被加载进内存
    全局命名空间：我所定义的除函数内部的命名
                ----放置了我所定义的所有变量和函数名（除函数内部变量和函数名）。如：my_func(),my_name
                      命名是在程序从上而下被执行的过程中被加载进内存的            
    局部命名空间：函数内部
                  ----函数内部定义的名字
                  ----调用该函数时，创建这个命名空间，函数执行结束时，命名空间回收
                  ----各函数的局部命名空间相互独立，不共享
                                 
在局部：可使用全局、内置命名空间的名字
在全局：可以使用内置命名空间的文字。不能使用局部命名空间中的命名  ----上层依赖于底层
命名冲突时的优先级：
    定义了与内置名重名的名字，自己定义的名字优先级更高。
    PS：不建议命名与内置名重名的名字！

作用域：
    全局作用域  ----作用在全局：包含内置和全局命名空间中的名字。
                    globals()方法可以查看全局作用域中的命名
                    全局命名可以在局部或全局中使用，对于不可变数据类型，局部无法做直接修改
                    但是如果在局部里对变量进行global声明，那么局部内做的改动在全局有效
        例如：
        a = 1
        def func():
            global a  # 对变量a进行全局声明
            a += 1
            return a
        print(func())  # 不建议使用global关键字，不安全
        
        可以使用：
        a = 1
        def func():
            a += 1
            return a
        a = func(a)
        print(a)  # 这种方法比较安全，建议使用
                    
    局部作用域  ----作用在局部：局部空间中的名字。局部命名只能在局部使用
                    locals()方法可以查看




"""

#
#
# a = 1
# def func():
#     global a
#     a += 1
#     return a
# print(func())
# print(globals())




# a = 1
# def func():
#     print(a)
# func()

# def func(a):
#     return a
#
# a = 2
# print(func)


"""作用域链"""
#
# def f1():
#     a = 1
#     def f2():
#         a = 2
#     f2()
#     print('a in f1 : ',a)
#
# f1()

# 内部可使用上层的变量
# def f1():
#     a = 1
#     def f2():
#         def f3():
#             print(a)
#         f3()
#     f2()
#
# f1()