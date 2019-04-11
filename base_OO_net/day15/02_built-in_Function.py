"""
内置函数，总共68个，分为：
    1.作用域相关
    2.迭代器/生成器相关
    3.其他
"""
# 作用域相关
# print(locals())  # 返回局部作用域中所有命名
# print(globals())  # 返回全局作用域中的所有命名

# 迭代器/生成器相关
# print(next([1,2,3].__iter__()))  # next(迭代器) 等同于 迭代器.__next__()方法
# print(iter([1,2,3]))  # 等同于 可迭代对象.__iter__()
# print([i for i in range(1,11,2)])  # range() 不是迭代器


"""其他内置函数"""
# dir()
# print(dir([]))  # 查看一个对象拥有的所有方法,常用的查询，辅助

# callable()
# print(callable(print))  # 返回一个对象是否能被调用，是否为方法

# help()
# def f():print(1)
# help(f)  # 返回对象相关的所有方法，用法

# import
# import os  # 导入一个模块

# open()
# open('homework') as f1: # 打开一个文件句柄为f1

# id()
# print(id([1]))  # 返回对象的内存地址

# hash()  # 返回对象的哈希结果,不可哈希会报错
        # int str bool tuple 是可哈希的
        # 对于相同可哈希的值，在一次哈希的过程中，总是不变的

# print()  # 输出 end指定结束符默认为换行符；sep指定多个值之间的分隔符，默认为逗号;file指定输出的位置，默认为屏幕上
# for i in range(5):
#     print(123,213, sep='*',end='%%')

# 打印进度条
# import time
# for i in range(0,101,2):
#      time.sleep(0.1)
#      char_num = i//2      #打印多少个'*'
#      per_str = '\r%s%% : %s\n' % (i, '*' * char_num) if i == 100 else '\r%s%% : %s'%(i,'*'*char_num)
#      print(per_str,end='', flush=True)
#小越越  ： \r 可以把光标移动到行首但不换行*

# input()
# input()  # 返回用户输入的信息

# exec
# exec('print(123)')  # 执行字符串类型，其中为代码；无返回值

# eval
# print(eval('1+2+3+4'))  # 执行字符串类型，其中为代码;有返回值。不安全！

# compile  # 编译字符串类型的代码

"""基础数据类型相关"""
# complex  复数 ----实部+虚部 如： 1+2i

# float  浮点数  ----有限小数及无限循环小数；小数点后很长时，会不准，这是由于二进制小数转换时

# 进制转化
# print(bin(9))  # 将十进制转换为二进制
# print(oct(9))  # 将十进制转换为二进制
# print(hex(9))  # 将十进制转换为十六进制

# abs()  绝对值

# divmod(a, b)  ---- 返回a/b的商和余数组成的元组
#           除余方法;div除法；mod取余;  返回
# print(divmod(10,3))

# round(float, a)  ---- 精确小数位数
# print(round(3.17237, 4))

# pow(a,b)  ----返回a的b次幂
# pow(a,b,c)  ----返回a的b次幂对c取余的值

# sum(iterable, obj)  ---- 返回iterable的迭代值，再加上obj
# print(sum([1,2,3],6))

# min max  key可以指定按照何种方法来找
# print(min(1,2,3,-4, key=abs))
# print(1 or True)

