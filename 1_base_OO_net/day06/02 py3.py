"""
区别 py3 and  py2
    py3         py2区别
    utf-8       unicode
    print(obj)  print obj
    range()     xrange() ----生成器
    input()     raw_input()
"""

"""
区别 =    ==              is                      id(obj)
    赋值  比较值是否相等  比较内存地址是否相等     打印内存id 
"""
#
# lis1 = [1,2,3]
# lis2 = [1,2,3]
# print(lis1 == lis2)
# print(id(lis1), id(lis2))

"""
内存地址：
    数字  字符串     小数据池概念：如果创建的数字or字符串在小数据池内，则共用一个内存
                                         数字的范围：   -5 -- 256
                                         字符串的范围（无明确范围）：1.无特殊字符； 2.s*20以内都是同一个地址，s*21以后就不是同一个内存地址了
    其他类型：list set等 无小数据池概念。
"""


"""
    
"""