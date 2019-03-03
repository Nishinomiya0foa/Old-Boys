# _*_ coding:utf-8 _*_
__author__ = 'brian'
__date__ = '2019/3/2 0002 22:37'

"""
    函数嵌套
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
# nonlocal 关键字 ----生命一个上层的局部变量，功能类似小global。仅局部变量
def outer():
    a = 1
    def inner():
        print(a)
        print('here inner')
        def inner2():
            print('here inner2')
        inner2()
    inner()
outer()
