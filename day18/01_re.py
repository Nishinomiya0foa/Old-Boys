# _*_ coding:utf-8 _*_
__author__ = 'brian'
__date__ = '2019/3/13 0013 22:03'

"""
正则表达式  ----字符串匹配、贪婪匹配：匹配尽可能长的字符串 回溯算法
re模块
量词后+上问号  如：{1,6}?  +?  ----非贪婪匹配即惰性匹配
r''  ---- 取消转义

# .*?
"""
# re.search(obj,s,flag)  ---- obj为正则表达式，s为所要进行正则匹配的字符串，flag为
# flags： 常用的3个
# re.I  ---- 忽略大小

import re

# a = '李杰和李莲英李二棍子'
#
# obj_s = re.findall('李[杰莲英二棍子]+', a)
# if obj_s:
#     print(obj_s)


# 分组 （）  ----需要对整体进行量词约束时
# 分组可以用group读取。 第一个分组里的匹配到的值，可以用group(1)，以此类推

# 模式
# findall()  ---- 匹配所有。有分组优先原则，返回值只是分组内匹配到的值；避免分组优先 可以在括号内开头位置加上？：
# ret = re.findall('我真的(123|ojbk)愿意', '我真的ojbk愿意xzfzxcxz')  # 返回值只有ojbk,这就是因为分组优先
# print(ret)
# ret2 = re.findall('我真的(?:123|ojbk)愿意', '我真的ojbk愿意xzfzxcxz')  # 括号内加上?:   取消了分组优先
# print(ret2)
# search()  ---- 从前往后，找寻到一个结果即返回，返回值需调用其group()方法；没找到返回None，None没有group()方法
# match()  ---- 用法同search()，从头开始匹配，匹配到返回；匹配不到返回None

# sub(old, new, obj, num)  ----把obj字符串中的old元素用new元素替换，old可以是正则表达式，替换次数为num，num默认全部
# subn(old, new, obj, num)  ----除了拥有sub()的功能外，还会返回替换的次数。组成2-tuple
# compile()  ----编译正则规则,后续可多次调用
# obj = re.compile('[\d]{3}x')
# ret = obj.findall('123x532xgsdg2zxc21')
# print(ret)

# finditer()  ---- 返回迭代器，其中每个元素都需调用其group()方法


# 匹配字符串a中的所有整数
# a = '1-2*(60+(-40.35/5)-(-4*3))'
# ret = re.findall('-?\d+\.\d+|-?\d+',a)
# print(ret)

#  匹配邮箱 http://blog.csdn.net/make164492212/article/details/51656638
a = '3ax_x_f3f@sina.com'
ret = re.match('[A-Za-z0-9][A-Za-z0-9_]+@[A-Za-z0-9]+.com',a)
if ret:
    print(ret.group())