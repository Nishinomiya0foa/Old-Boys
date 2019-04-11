# _*_ coding:utf-8 _*_
__author__ = 'brian'
__date__ = '2019/3/2 0002 11:49'


"""
函数：
　　1.可读性强；2.复用性强
函数的定义
　　def func()  ----定义了一个无参函数，函数名为func()
函数的调用
　　实例化：f1 = func()
    print(func)  ----直接打印函数名，会打印该函数的内存地址
函数的返回值 默认return None  ----函数中至多只允许出现一个return，return之后的内容不会再执行
　　无返回值  ----函数仅执行，不需要执行的结果。返回值为None
　　　　　　# 1.没有return，自然就没有返回值；2.只写了return，没写return的内容；3.return None
　　一个返回值  ----可以是任意数据类型
　　多个返回值  ----1.多个返回值组成一个元组，返回值的结果其实是一个元组
　　　　　　　  PS：元组/字典/列表的一个特性： a = (1,2)  x,y=a -> x=1, y=2
函数的参数
　　默认参数 ----func(a,b,c=5)，如果实参中没有对c进行传c，则c为5；如果有对c进行传参，则值覆盖5
　　　　　　　　　　　默认参数的陷阱: 1.如果默认参数的值是一个可变数据类型,那么每一次调用的时候,如果不进行传值,那么会共用这个参数

    形参  ----1.定义函数里，func(a)括号内的参数
        位置参数  ----按位置进行传值，有几个位置参数的形参，实参就要传递几个值
        *args  ----可以接收按位置传参的任意多个参数，组成元组，参数名习惯*args
        默认参数  ----可以使用变量名赋值的方式进行传参，也可以不进行传参
        **kwargs  ----可以接收按关键字传参的任意多个参数，组成字典，参数名习惯**kwargs
    实参  ----1.调用函数时，实际传递进来的参数
　　
　　参数个数
　　　　0  ----定义和调用函数时，括号内没有任何东西
　　　　1个  ----传什么就是什么
　　　　多个  ----注意参数顺序，形参有几个，实参就得传几个
　　
　　参数的顺序  ----位置参数、*args、关键字参数、**kwargs

动态传参的另一种形式：
1.实参是一个可迭代对象，给他加上*，即(*lis1)，是指将他迭代之后，按顺序赋值给形参；形参*args会再将他们组成元组
def func(*args):
    pass
lis1 = [1,2,3,4,5,6]
try_func = func(*lis1)  #
"""
# 函数的注释
# def func():
#     """
#     函数的功能
#     参数1
#     参数2
#     :return:返回值
#     """
#     pass



# def get_length(l):  # 声明函数/定义函数
#     count = 0
#     for i in l:
#         count += 1
#     return count  # 返回值
#
# print(type(get_length('my love')))  # 调用函数

# def my_func():
#     return 1,2
# a, b = my_func()
# print(a)

# 参数
# def my_func(num):  # 接收参数，形参
#     a = 1 + num
#     return a
#
# num = 3
# my_func(num)  # 传参，实参

# # 多个参数
# def my_sum(a, b):
#     return a+b
# # sum = my_sum(1,4)  # 按位置传参
# sum = my_sum(b=1, a=4)  # 按关键字传参
# print(sum)

# 默认参数 gender='male', 如果没有实参传入，gender='male'
#                         如果有实参传入，gender=实参值
# def get_classmate(name, gender='male'):
#     print('姓名：{}，性别：{}'.format(name, gender))
# get_classmate('陈文波')
# get_classmate('七仙女','female')

# 动态参数 *args，形参个数不定
# def sum(*a):
#     sum = 0
#     for i in a:
#         sum = i + sum
#     print(sum)
#
#
# sum(1,2,3,4)
# sum(1,2)
# sum()


# **kwargs
# def func(**kwargs):
#     print(kwargs)
#
# func(a = 2, b = 'huai')
# func(c = 4, cc = 3, act = False)


# *args + **kwargs
# 先按位置传， 再按关键字传。   **kwargs必须在最后
# def func(*args, studyid=22, **kwargs):
#     print(args, kwargs, sep='||||||')
#     print(studyid)
#
# func(1,2,3,4,5,6, name='xiaobai', weight='144',studyid=33)


# 动态参数的另一种传参形式
# def func(*args):
#     print(args)
#
# l = [1,2,3,4,5,6,7]
# d = {'dd':1, 'cc':2}
# num = '125'
# # func(*l)
# # func(*d)  # 给一个可迭代对象加上*，是指将他迭代之后，按顺序赋值给形参; 形参*args会再将它们组成元组
# func(*num)

# def func(**kwargs):
#     print(kwargs)
#
# # func(a=1,b=2)
#
# d = {'dd':1, 'cc':2}  # 同 *args, 只是可以传键值对
# func(**d)


