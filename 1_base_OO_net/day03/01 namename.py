"""
    变量命名规范：
        1.单词之间用_分开  add_num()
        2.全局变量，大写   PI,NUMBER()
        3.实例变量，以_开头     _example()
        4.私有实例变量    __private()
        5.普通函数，_动词+名词   _get_name(),_add_age()
        6.普通私有函数， __动词+名词   __get_name()
        7.类名，首字母大写单词串    MyClass
        8.函数&方法，函数名应该为小写，可以用下划线风格单词以增加可读性  myfunction,my_function
"""


# 6 or 2>1   6
# 3 or 2>1   3
# 0 or 5<4   F
# 5<4 or 3   3


# 2>1 or 6   T
print(2>1 or 6 )

# 3 and 2>1  T
print( 3 and 2>1)

# 0 and 3>1  0

# 2>1 and 3  3
print(2>1 and 3)

# 3>1 and 0  0
print(3>1 and 0)

# 3>1 and 2 or 2<3 and 3 and 4 or 3>2
# 2 or 4 or T
print(2 or 4 or True)
print(3>1 and 2 or 2<3 and 3 and 4 or 3>2)


# 5、求1-2+3-4+5 ... 99的所有数的和, 除了88
a = -1
num = 1
sum = 0
while num < 100:
    if num != 88:
        sum = sum + num*(-a) # 0+1+
        num += 1
        a = -a
    else:
        num += 1
        a = -a  # 这行如果注释掉，那将会变成  ..+87-89+90...99
print(sum)


# 5、求1-2+3-4+5 ...-89+90...99的所有数的和, 除了88
a = -1
num = 1
sum = 0
while num < 100:
    if num < 88:
        sum = sum + num*(-a) # 0+1+
        num += 1
        a = -a
    elif num == 88:
        num += 1
        continue
    elif num > 88:
        sum = sum + num*(-a) # 0+1+
        num += 1
        a = -a
print(sum)

# 4<7 and 8==8
print(4<7 and 8==8 or 1>2)

# 检测是否存在敏感词 "葫芦"
illegal_words = [
    '葫芦','小白'
]
# illegal_word = "葫芦小白"
user_input = input(">")
for illegal_word in illegal_words:
    while illegal_word in user_input:
        print("你输入的文字中包含{}，重新输入".format(illegal_word))
        user_input = input(">")

