# _*_ coding:utf-8 _*_
__author__ = 'brian'
__date__ = '2019/3/2 0002 11:49'


"""
函数（方法） def my_function() 定义了之后可以多次调用
    函数中不能用break跳出函数
    
return 返回值：  ----
    # 一旦函数中执行了return，其后的代码就不再执行
    1.没有返回值  ---- 返回值为None
        # 1.无return，就无返回值；2.只写了return；3.return None
    2.返回一个值
        # 1.可以返回任意数据类型; 
    3.返回多个值
        # 1. 返回的数据类型是元组,为一个变量（这是py内部做的工作）
        # 2. 元组a = (1,2)   x,y = a     ->  x = 1, y = 2  ----列表、字典也有此特性
        
参数：
    1.所有形参都必须有唯一的实参传递进来，否则报错
    2.动态函数 *args  ----可以接收按照位置传参的任意多个参数,组成元组，参数名习惯*args
               **kwargs  ----可以接收按照关键字传参的任意多个值，组成字典,参数名习惯**kwargs
    3.形参：定义函数时括号里的参数
    4.实参：调用函数时，传递进来的参数
    5.参数个数：
        1,没有参数
            # 定义和调用函数时，func()括号内没有任何东西
        2.一个参数
            # 传什么就是什么
        3.多个参数
            # 按位置传数
            # 按关键字传参  ----位置传参和关键字传参可以混着用，必须先按照位置传参，再按照关键字传参
                                不能给同一个变量传多个值
    6.参数定义：
        1.顺序：
            位置参数，*args，默认参数，**kwargs
        
"""

"""
函数的定义
函数的调用
函数的返回值
函数的参数
    形参
        位置参数
        *args
        关键字参数
        **kwargs
    实参
"""

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

# 函数的注释
def func():
    """
    函数的功能
    参数1
    参数2
    :return:返回值
    """
    pass
