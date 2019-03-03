"""
python 常用数据结构有哪些？请简要介绍一下。
"""
# int:纯数字 str：字符串 bool：bool类型 True/False tuple:元组，不变列表  ----不可变数据类型
# list：列表，存储大量数据 dict：字典。键值对。键是唯一的。无序。key必须为不可变数据类型 set：可变数据类型。不重复。无序  ----可变数据类型

"""
简要描述 Python 中单引号、双引号、三引号的区别。
"""
# '':字符串需要引号包裹
# "":除了包裹字符串。也能在其内部加单引号
# """ """:注释。或是大段文字，会保存字符串里的格式

"""
如何在一个 function 里面设置一个全局的变量？
"""
# 对该变量进行global声明


"""
Python 里面如何拷贝一个对象？（赋值、浅拷贝、深拷贝的区别）

浅拷贝：lis2 = lis1.copy
    把lis1的值拷贝给lis2，lis1和lis2的内存地址不一样，但其内部的各个元素的内存地址都一样。但新开辟了一个空间，内部元素是公用的
    
深拷贝：
import copy
lis1 = ['asdf', 'aaa',{'aaa':1}]
lis2 = copy.deepcopy(lis1)
    lis1的值拷贝给了lis2。lis1与lis2的内存地址是不同的。其内部的不可变数据类型的内存地址是相同的，但可变数据类型的内存地址是不同的。
"""

"""
如果 custname 字符串的内容为 utf-8 的字符，如何将 custname 的内容转为 gb18030 的字符串？
"""
custname = 'xzzxcz123'
custname.encode('gb18030')



"""


请写出一段 Python 代码实现删除一个 list 里面的重复元素。

这两个参数是什么意思：args，*kwargs？

统计如下 list 单词及其出现次数。

a=['apple', 'banana', 'apple', 'tomato', 'orange', 'apple', 'banana', 'watermeton']

给列表中的字典排序：假设有如下 list 对象
alist=[{"name":"a", "age":20}, {"name":"b", "age":30}, {"name":"c", "age":25}]

将 alist 中的元素按照 age 从大到小排序。

写出下列代码的运行结果
a = 1
def fun(a):
  a = 2
fun(a)
print(a)
a = []
def fun(a):
  a.append(1)
fun(a)
print(a)
class Person:
    name = 'Lily'
 
p1 = Person()
p2 = Person()
p1.name = 'Bob'
print(p1.name)
print(p2.name)
print(Person.name)
假设有如下两个 list：a = ['a', 'b', 'c', 'd', 'e']，b = [1, 2, 3, 4, 5]，将 a 中的元素作为 key，b 中元素作为 value，将 a，b 合并为字典。

使用 python 已有的数据结构，简单的实现一个栈结构。

"""