# _*_ coding:utf-8 _*_
__author__ = 'brian'
__date__ = '2019/3/2 0002 20:23'

"""
    默认参数的陷阱:
        1.如果默认参数的值是一个可变数据类型,那么每一次调用的时候,如果不进行传值,那么会共用这个参数
"""
def func(l=[]):
    l.append(1)
    print(l)
func()
func()
func()