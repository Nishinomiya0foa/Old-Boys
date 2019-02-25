"""
    int 的方法：
        1.bit_length() 表达该数字的二进制最短位数
    bool： True/False
    int bool str 互相转换：
        int -> str: str(int)
        str -> int: int(str)  # 该str由纯数字组成
        int -> bool: bool(int)  # 非0为True，否则False
        bool -> int: int(bool)  # True->1,False->0
        str -> bool: bool(str) # str空，则False；否则为True


    PS: while True效率小于 while 1
"""

num = 0
print(num.bit_length())

a = True
print(type(a))
print(str(a))
print(type(str(a)))

name = ''
if name:
    pass
else:
    print('{name}为空'.format(name=name))