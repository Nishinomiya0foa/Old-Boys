"""
    字符串索引及切片 [i,j),前闭后开：
        1.str[i:j] 返回str从第i到第j个元素组成的新str。
        2.str[i:]  返回str从第i开始的全部元素组成的新str
        3.str[i:-1] -1值最后一个元素，仍然前闭后开
        4.str[i:j:k] k指步长，即间隔
        5.str1[:] 即str1，一样的str
    字符串的常用方法：
        1.capitalize() 首字母大写,其余小写
        2.upper() 全部大写 lower 全部小写
        3.swapcase() 大小写翻转
        4.title() 每个被隔开的单词首字母大写,其余小写
        5.center(width, obj) 将str居中，总长度width，用obj填满，obj默认为空格
        6.split(obj) 以obj元素将str分割，返回列表，不包含该obj元素
        7.find(obj, start, end) 找从start至end索引下的obj元素，返回索引。没有该元素返回-1
        7.1. index(obj) 通过元素找索引，返回索引。找不到则报错
        8.strip(obj) 去除str中左右的obj,obj默认空格；迭代删除  lstrip,rstrip
        9.count(obj) 返回str中obj的个数
        10.replace(old, new, count) 用new替换str中的old， 替换的总数为count，默认全部
        11.isalnum() 判断str是否为纯字母+数字；isdigit isalpha
        12.startswith(obj, start, end) 判断str的从start到end索引的str1，是否以obj开头
            endswith()
    公共方法：
        1.len() 返回str的长度
    格式化： format：
        1.'我叫{},今年{}，我叫{}'.format('web',23,'web')   #普通
        2.'我叫{0},今年{1}，我叫{0}'.format('web',23)   # 重复的格式化
        3.'我叫{name},今年{age}，我叫{name}'.format(name='web',age=24)   # 带变量名
"""
test_words = '+86618644444444+'
print(test_words[0::2])


useless_words = 'ABCdandef@GHori11J_Chen'
# str[i:j:k] -> [开始位置（包含）:结束位置(不包含)：步长]
print(useless_words[1:6:1])

# capitalize() 首字母大写，其余小写
print(useless_words.capitalize())

# upper() 全部变为大写; lower 全部变为小写
print(useless_words.upper())
print(useless_words.lower())

#  验证码的应用
# pwd_code = 'AceG'
# user_input = 'aceg'
# if pwd_code.upper() == user_input.upper():
#     print(True)

# swapcase() 大小写翻转
print(useless_words.swapcase())

# title() 每个隔开的单词首字母大写,其余小写
useless_words = 'ABCdandef@GHori11J_ChEn'
print('title()用法：', useless_words.title())

# center(width, obj)  居中：将str放在width宽度的中间，两边以obj填充
print(useless_words.center(44, '-'))

""" 公共方法 """
# str() 返回str的长度
print(len(useless_words))


useless_words = '1ABCdandefGHori11JChen1'
# find() 找到返回索引下标；否则返回-1
if useless_words.find('e', 0, 5):
    print(useless_words.find('e', 0, 5))
else:
    print(False)
print(useless_words[0:5])
print(useless_words[0:5].find('v'))

# 位运算符&
print(12&123)

# strip('x') lstrip() rstrip() 去除左右'x',默认空格;迭代删除
print(useless_words.strip('1 A'))

# count('a') 返回str中'a'的个数
print(useless_words.count('A'))

# split('x') 以‘x’为分隔符，分割str。返回列表
# 字符串->列表
print(useless_words.split(' '))

# format
"""
    format 格式化输出,3种用法 
        1.'我叫{}，今年{}'.format('web',25)
        2.'我叫{0}，今年{1},我真的叫{0}'.format('web',25)
        3.'我叫{name},今年{age},我真的叫{name}'.format(age=24,name='web')
"""
print('我叫{}，今年{}'.format('web',25))
print('我叫{0}，今年{1},我真的叫{0}'.format('web',25))
print('我叫{name},今年{age},我真的叫{name}'.format(age=24,name='web'))

# replace(old, new, count) 替换,count指替换的数量，默认全部
print(useless_words.replace('ABC', 'XYZ'))

"""
    isalnum:判断是否由字母+数字组成
    isalpha:纯字母
    isdigit:纯数字
"""
print(useless_words.isalnum())

