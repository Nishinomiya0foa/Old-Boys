"""

python全栈9期月考题
—基础知识：（70分）
1. 文件操作有哪些模式？请简述各模式的作用（3分）
    读（文件不存在报错）、写（不存在新建）、追加（不存在新建）
    r:只读，也是默认这个，打开时指针位置默认在0 w：只写，打开清空文件 a：只追加，指针在最后
    r+：读写，打开时指针位置默认在0，写的时候会覆盖 w+:写读，打开清空文件 a+：可读可追加，指针在末尾
    rb wb ab
"""



"""
2. s= ’*：}：hello，world!**’请使用strip方法去掉字符串两端的*号（2分）
"""
# s= '*：}：hello，world!**'
# s = s.strip('*')
# print(s)
"""
3. 用户输入一个任意数字n，求1-n之间所有数字中的奇数,包括n（4分）
"""
# num = input('>')
# if int(num):
#     for i in range(1, int(num)+1):
#         print(i if i % 2 == 1 else '', end=' ')


"""
4. s = ’hskakhlkshfkskjakf’，请去除s字符串中重复的字母（4分）
"""
# # 这样顺序不变
# s = 'hskakhlkshfkskjakfxx'
# n = []
# for i in s:
#     if i not in n:
#         n.append(i)
# print(n)
# s = ''.join(n)
# print(s)

# 顺序会变得
# s = 'hskakhlkshfkskjakfxx'
# n = set(s)
# print(n)
# s = ''.join(n)
# print(s)

"""
5.
a=10
b=20
def test5(x，y):
    print(x, y)
c = test5(b, a)
print(c)
上述代码中，打印出来的值a, b，c分别是什么？为什么？（4分）
c = None   a = 10 b =20 X
20 10
None
"""


"""
6.s ='123.33sdhf3424.34fdg323.324'，计算字符串中所有数字的和（4分)
本题结果应为：123.33+3424.34+323.324
"""
# import re
# s ='123.33sdhf3424.34fdg323.324dfs32fds0.33'
# obj = re.findall('[0-9]+\.?[0-9]*', s)
# print(obj)
# for num in obj:
#     sum += float(num)

# ret = [float(num) for num in obj ]
# print(sum(ret))

"""
7. d={’kl’：’vl’，’k2’ ：[1，2,3]，（ ‘k’，’ 3’）：{1，2，3}} (4分）
请用程序实现：
1) 输出上述字典中value为列表的key (2分）
2) 如果字典中的key是一个元祖，请输出对应的value值。（2分）
3) d[(’k’，’3’）]对应的value是一个什么数据类型（1分）
"""
# d={'kl':'vl','k2':[1,2,3],( 'k',' 3'):{1,2,3}}
# for key in d:
#     print(key if type(d[key]) is list else '', end='')
#     if type(key) is tuple:
#         print(d[key])
# print(type(d[( 'k',' 3')]))

"""
8. 如果不使用©wrapper装饰器，请在a()之前加入一句代码，达到相同的效果（2分)
def wrapper(func):
    def inner(*arg, **kwargs):
        func(*arg, **kwargs)
    return inner

@wrapper
def a(arg):
    print(arg)

a()
"""
# def wrapper(func):
#     def inner(*arg, **kwargs):
#         func(*arg, **kwargs)
#     return inner
#
# # @wrapper
# def a(arg):
#     print(arg)
#
# # a = wrapper(a)
# a()

"""处理文件， 输出所有以T 开头的行"""
# with open('作业.txt') as f1:
#     for line in f1:
#         if line.st:
#             print(line.strip())

"""写出调用顺序及结果"""
# def f1():  # 1
#     print('fun f1')
#
# def f2():  # 2
#     print('fun f2')  # 5
#     return 1  # 6
#
# def f3(func1):  # 3
#     l1 = func1()  # 4
#     print('fun f3')  # 7
#     return l1  #8
#
# print(f3(f2))

"""创建一个闭包函数需要满足哪几点"""
# 嵌套函数
# 函数内调用了外部命名空间中的变量

"""转化为结构化时间和格式化时间"""
# import time
# print(time.strftime('%Y/%m/%d %H:%M:%S'))
#
# t = '2019/03/26 21:13:55'
# p = time.strptime(t, '%Y/%m/%d %H:%M:%S')  # 格式化时间转换为结构化时间
# print(p)

"""用什么模块能知道文件夹存在与否? 怎么获取这个文件夹的大小？"""
# import os
# print(os.path.exists('fsdfsfs'))
# print(os.path.getsize('./')) # 应该去循环这个文件里的所有的文件大小

"""写一个匹配手机号的正则语句"""
import re
s = '13000030000'
obj = re.match(r'1[3578]\d{9}$', s)
if obj:
    print(obj.group())

"""四个数字 1 2 3 4   能组成多少个互不相同且不重复的三位数，各是多少"""
# num = 0
# for i in range(1,5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if i!=j and j!=k and i != k:
#                 print(i,j,k,end='|')
#                 num += 1
#                 if num % 4 == 0:
#                     print('')
# print(num)


# 0 3 5
# n = [0,1]
# for i in range(1):
#     n.append(n[1]*4+1)
# print(n)
# num = []
# for i in n:
#     for j in n:
#         for k in n:
#             for l in n:
#                 if i+j+k+l not in num:
#                     print(i,j,k,l,'--{}'.format(i+j+k+l))
#                     num.append(i+j+k+l)
#                 # else:print('重复的：{},{},{},{}--{}'.format(i,j,k,l,i+j+k+l))
# print(len(num))

# s = [0,1]
# def get_num(n,m=[]):  # 4
#     global s
#     m.append(n)
#     # print(m)
#     # true_n = n - len(dim)  #
#     if n > 2:
#         # print(get_num(n-1)*m[0] + 1)
#         if get_num(n-1)*m[0] + 1 not in s:
#             s.append(get_num(n-1)*m[0] + 1)
#         print(s)
#         return get_num(n-1)*m[0] + 1
#     else:
#         return 1
#
# ss = [0,1]
# ss.append(get_num(5))
#
# print(ss)

"""简述 类 对象 实例化 实例这些名词的含义"""
# 类。 是一个抽象概念，许多对象的共同属性或方法的集合
# 对象与实例： 是类的具体对象，与类的关系是“是”的关系，
# 实例化。 由类创建实例的过程

"""面向对象的三大特性 """
# 封装：面向对象的思想本身就是封装
# 继承：单继承和多继承
# 多态：


"""有个类：
1.初始化10个不同的对象
2.求最高age的对象的name
"""
# import random
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
# name_l = [chr(i) for i in range(97,107)]
# obj_l = []
#
# # 使用max(obj, key=age)
# max_obj = Person('aaa', 0)
# for i in range(10):
#     name_l[i] = Person(name_l[i],random.randint(5,55))
#     obj_l.append(name_l[i])
#     if name_l[i].age >= max_obj.age:
#         max_obj = name_l[i]
# print(max_obj.name,max_obj.age)

"""
 有Police和Terrorist类
 Police：name health weapon gender
 可以攻击Terrorist
 
 Terrorist：name，health weapon gender
 可以攻击Police
 
 1.实例化两个对象，警察攻击匪徒，匪徒掉血
"""
# class People:
#     def __init__(self, name, health, weapon, gender):
#         self.name = name
#         self.health = health
#         self.weapon = weapon
#         self.gender = gender
#
# class Police(People):
#     def punish(self, terrorist):
#         print('{} punished {}'.format(self.name, terrorist.name))
#         terrorist.health -= 10
#
# class Terrorist(People):
#     def punish(self):
#         print('{} punished {}'.format(self.name, Police.name))
#
# a_sir = Police('asir', 100, 'Gun', 'MALE')
# stup = Terrorist('stupid', 100, 'Gun', 'MALE')
#
# print(stup.health)
# a_sir.punish(stup)
# print(stup.health)

"""阅读以下代码， 回答：
1. 面向对象中self指什么
2. 运行结果是？   为什么？
"""
class Base:
    def f1(self):
        self.f2()

    def f2(self):
        print('...')

class Foo(Base):
    def f2(self):
        print('9999')

obj = Foo()
obj.f1()  # 9999


