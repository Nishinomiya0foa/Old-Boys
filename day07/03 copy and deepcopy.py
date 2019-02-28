# _*_ coding:utf-8 _*_
__author__ = 'brian'
__date__ = '2019/2/28 0028 23:17'


# 赋值运算中
# lis1 = [1,2,3,['i','love','you'], 'bazinga']
# lis2 = lis1  # 把lis2也指向lis1的内存地址，所以lis2的值与lis1的值会相等

"""
 浅拷贝 copy 
    对于浅拷贝而言，只是在内存中新创建了一个空间存放新列表，但新老列表中的所有元素是公共的；这意味着所有内部元素的
    内存地址是一样的，是同一个元素
"""
# lis1 = [1,2,3,['i','love','you'], 'bazinga']
# lis2 = lis1.copy()
# print(id(lis1), id(lis2))       # lis1与lis2的内存地址是不同的
# print(id(lis1[3]), id(lis2[3])) # 但其内部所有元素的内存地址仍相同

"""
深拷贝 copy.deepcopy(lis1)
    与浅拷贝的区别：
        内部的可变数据类型的元素的内存地址拷贝前后是不同的，这意味着内存新开辟了存储空间；其余与浅拷贝一样
"""
import copy
lis1 = [1,2,3,['i','love','you'], 'bazinga']
lis2 = copy.deepcopy(lis1)
print(id(lis1), id(lis2))   # 深拷贝两个列表的内存地址是不同的，这与浅拷贝一样
print(id(lis1[1]), id(lis2[1])) # 其中不可变数据的内存地址仍相同，这与浅拷贝一样
print(id(lis1[3]), id(lis2[3])) # 但其中可变数据的内存地址是不同的，这是与浅拷贝的区别





