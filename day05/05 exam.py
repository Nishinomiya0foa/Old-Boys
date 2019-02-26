# 1. 简述变量命名规范（3分）
"""
    1.常量全大写 PI
    2.普通变量用小写单词或小写单词加下划线 student_age
    3.普通私有变量，以_开头，如_private_name
"""


# 2. 字节和位的关系。（2分）
"""
    1.1bytes（字节 = 8bit（位
"""
# 3.’太白’使用utf-8编码时，占的位数和字节数，是多少？使用gbk编码时，占的位数和字节数，是多少。（2分）
"""
    32 4
    24 3
"""
# 4.默写字符串的十二个功能，并描述其作用。（12分）
"""
    1.upper() 全部大写
    2.lower() 全部小写
    3.caplize() 首字母大写，其余小写
    4.swapcase() 大小写翻转
    5.split(obj, num) 以obj切分字符串，最多前num个，默认全部。返回数组，该obj不保存
    6.format()  a. '{}{}'.format('', '')
                b. '{0}{1}{0}'.format('','')
                c. '{name}{age}'.format(name='',age='')
    7.切片
    8.count(obj) 统计obj出现的次数
    9.startswith(obj) endswith(obj) 检查是否以obj开头结尾，返回T/F
    10.title() 被分割开的词，首字母大写，其余小写
    11.strip(obj) 去除str左右的obj，默认为空格
"""
# 5.数字，字符串，列表，元祖，字典对应的布尔值的False分别是什么？（5分）
"""
    1.数字    非零为True，0为False
    2.字符串  非空为True，空为False
    3.列表    非空为True，空为False
    4.元组    非空为True，空为False
    5.字典    非空为True，空为False
"""
# 6. 书写Python2与python3中的三个不同。（3分）
"""
    1.编码。 python2默认unicode；python3默认utf-8
    2.print     python2为print xxx   python3为print(xxx)
    3.
"""
# 7. 写代码，有如下列表，利用切片实现每一个功能（每题一分，共计4分）
li = [1, 3, 2, 'a', 4, 'b', 5, 'c']
#     (1)通过对li列表的切片形成新的列表l3,l3 = [1,2,4,5]
li3 = li[::2]
print(li3)
#     (2)通过对li列表的切片形成新的列表l4,l4 = [3,’a’,’b’]
li4 = li[1:6:2]
print(li4)
#     (3)通过对li列表的切片形成新的列表l5,l5 = [‘c’]
l5 = []
a = li[-1]
l5.append(a)
print(l5)
#     (4)通过对li列表的切片形成新的列表l6,l6 = [‘b’,’a’,3]
l6 = li[5:0:-2]
print(l6)
"""
    8. 组合嵌套题。
     a. 写代码，有如下列表，按照要求实现每一个功能（每题3分，写出一种方法得1分，写出两种方法的3分。此题共9分）
     （每个都是一行代码实现）
"""
lis = ['k', ['qwe', 20, {'k1':['tt', 3, '1']}, 89], 'ab']

#     (1) 将列表lis中的’tt’变成大写（用两种方式）。
# lis[1][2]['k1'][0] = lis[1][2]['k1'][0].upper()
# lis = ['k', ['qwe', 20, {'k1':['TT', 3, '1']}, 89], 'ab']
# print(lis)

#     (2) 将列表中的数字3变成字符串’100’（用两种方式）。
# lis[1][2]['k1'][1] = '100'
# print(lis)


#     (3) 将列表中的字符串’1’变成数字101（用两种方式）。
lis[1][2]['k1'][2] = 101
print(lis)


#
"""
    b. 写代码，有如下字典，按照要求实现每一个功能(5分)
"""
dic = {'k1':'v1', 'k2':['alex', 'sb'], (1, 2, 3, 4, 5):{'k3':['2', 100, 'wer']}}
#     (1) 将’k2’对应的值的最后面添加一个元素’23’。
# dic['k2'].append('23')

#     (2) 将’k2’对应的值的第一个位置插入一个元素’a’。
# dic['k2'].insert(0, 'a')
# print(dic)

#     (3) 将(1,2,3,4,5)对应的值添加一个键值对’k4’,’v4’。
# dic[(1,2,3,4,5)]['k4'] = 'v4'
# print(dic)

#     (4) 将(1,2,3,4,5)对应的值添加一个键值对(1,2,3),’ok’。
# dic[(1,2,3,4,5)][(1,2,3)] = 'ok'
# print(dic)

#     (5) 将’k3’对应的值的’wer’更改为’qq’。
dic[(1,2,3,4,5)]['k3'][2] = 'qq'
print(dic)

#
# 9. 转化题（4分）
#     (1) Int与str之间如何转化，转换的结果是什么？有没有条件？
"""
    int->str: str(int),返回str类型，无条件
    str->int: int(str),返回int类型，需要该str里全是数字
"""
#     (2) Int与bool之间如何转化，转换的结果是什么？有没有条件?
"""
    int->bool: bool(int),非零为True，否则为False
    bool->int: int(bool), False->0,True->1
    无条件
"""
#     (3) str与bool之间如何转化，转换的结果是什么？有没有条件?
"""
    str->bool: bool(str),非空为True，否则False
    bool->str: True->'1',False->''
"""
#     (4) str与list能否转化？如何转化？
"""
    str->list: obj.split(str),把str用obj分隔，转换为list，list中没有该obj元素
    list->str: obj.join(list),把list用obj连接，转换为str，返回字符串str类型
"""
#
# 10. 实现下列结果（5分）
#     (1)有列表li = [‘alex’,’wusir’,’rain’]通过操作该列表构造一个字符串s=’alexwusirrain’
li = ['alex','wusir','rain']
# print(''.join(li))

#     (2)有列表li = [‘alex’,’wusir’,’rain’]通过操作该列表构造一个字符串s=’alex*wusir*rain’
# li = ['alex','wusir','rain']
# print('❥'.join(li))

#     (3)有字符串s = ‘alexwusirlex’,通过操作该字符串构造一个列表li = [‘a’,’exwusirlex’]
s = 'alexwusirlex'
li = s.split('l', 1)
print(li)

#     (4)有字符串s = ‘alex wusir’,通过操作该字符串构造一个列表li = [‘alex’,’wusir’]
s1 = 'alex wusir'
li2 = s1.split(' ')
print(li2)

#     (5)有字符串s = ‘alex’通过操作该字符串构造一个字符串s1 = ‘a_l_e_x’
s2 = 'alex'
s3 = '_'.join(s2)
print(s3)

#
# 11. 分别使用while循环，和for循环打印1-2+3-4+5.......+99的结果。（10分）
# while
flag = -1
num = 0
sum = 0
while num<100:
    sum = sum + (num + 1) * (flag)
    num += 1
    flag = -flag
print(sum)

# for
sum = 0
for i in range(1, 100):
    if i % 2 == 0:
        i = -i
    sum = sum + i
    if i == 99:
        print(sum)

print(sum)



#
# 12. 使用range打印100,99,98，....1,0(2分)
for i in range(100,-1, -1):
    print(i, end=' ')
    print()

#
# # 13. 计算用户输入内容中索引为奇数并且对应的元素为数字的个数（没有则个数为零）（6分）
# user_input = input('>>')
# n = 0
# for i in range(len(user_input)):
#     if i % 2 != 0 and user_input[i].isdigit():
#         n+=1
#         # print(user_input[i])
# print(n)




#
# 14. 补充代码(从已有的代码下面继续写)：（6分）
#     有如下值li= [11,22,33,44,55,77,88,99,90]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
li = [11,22,33,44,55,77,88,99,90]
lib = []
lis = []
result = {}
for row in li:
    if row >= 66:
        lib.append(row)
    else:
        lis.append(row)
result['bigger'] = lib
result['smaller'] = lis
print(result)

# 15. 查找列表li中的元素，移除每个元素的空格，并找出以’A’或者’a’开头，并以’c’结尾的所有元素，
#     并添加到一个新列表中,最后循环打印这个新列表。（3分）
li = ['taibai ', 'alexC', 'AbC ', 'egon', ' Ritian', ' Wusir', ' aqc']
li_new = []
for index in range(len(li)):
    li[index] = li[index].strip(' ')
    if (li[index].startswith('a') or li[index].startswith('A')) and li[index].endswith('c'):
        li_new.append(li[index])
print(li_new)

#
# 16. 实现一个整数加法计算器：（3分）
#     如：content = input(‘请输入内容:’) # 如用户输入：5+8+7....(最少输入两个数相加)，然后进行分割再进行计算，
#     将最后的计算结果添加到此字典中(替换None)：
#     dic={‘最终计算结果’:None}。
content = input('请输入内容:')
cal_list = content.split('+')
sum = 0
for i in cal_list:
    sum += int(i)
dic = {'结果':sum}
print(dic)


#
# 17. 按要求完成下列转化（如果按照索引去做，只能得4分）。(6分)
#     list3 = [
#     {"name": "alex", "hobby": "抽烟"},
#     {"name": "alex", "hobby": "喝酒"},
#     {"name": "alex", "hobby": "烫头"},
#     {"name": "alex", "hobby": "Massage"},
#     {"name": "wusir", "hobby": "喊麦"},
#     {"name": "wusir", "hobby": "街舞"},
#     ]
#     如何把上面的列表转换成下方的列表？
#     list4 = [
#     {"name": "alex", "hobby_list": ["抽烟", "喝酒", "烫头", "Massage"]},
#     {"name": "wusir", "hobby_list": ["喊麦", "街舞"]},
#     ]
list3 = [
    {"name": "alex", "hobby": "抽烟"},
    {"name": "alex", "hobby": "喝酒"},
    {"name": "alex", "hobby": "烫头"},
    {"name": "alex", "hobby": "Massage"},

    {"name": "wusir", "hobby": "喊麦"},
    {"name": "wusir", "hobby": "街舞"},
]







#
# 18. 写程序：模拟公司HR录入员工账号密码的程序。（10分）
#
# (1) 员工的账号密码存储在这种数据类型中：
#     user_list = [
#     {'username':'barry','password':'1234'},
#     {'username':'alex','password':'asdf'},
#     .........
#     ]
# (2) 非法字符模板：board = ['张三','李小四','王二麻子']
# (3) HR输入用户名，密码（可持续输入，如果想终止程序，那就在输入用户名时输入Q或者q退出程序），在Hr输入用户名时，
#     检测此用户名是否有board里面的非法字符，如果有非法字符，则将非法字符替换成同数量的*（如王二麻子替换成****），
#     然后添加到user_list中，如果没有非法字符，则直接添加到user_list中，每次添加成功后，打印出刚添加的用户名，密码。
board = ['张三','李小四','王二麻子']
user_list = [
    {'username': 'barry', 'password': '1234'},
    {'username': 'alex', 'password': 'asdf'},
]

while 1:
    username = input('name(press Q to exit):')
    temp_dic = {}
    if username in board:
        this_username = '*' * len(username)
        this_userpwd = '*' * len(username)
        temp_dic[this_username] = this_userpwd
    elif username.upper() != 'Q':
        userpwd = input('pwd:')
        temp_dic[username] = userpwd
        print(temp_dic)
    else:break
    user_list.append(temp_dic)
print(user_list)




