"""
1,继续整理函数相关知识点，写博客。
"""

"""
2,写函数，接收n个数字，求这些参数数字的和。（动态传参）
"""
# def get_sum(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
# print(get_sum(1,3,2,5,6,0,-1))

"""
3,读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？
    a=10
    b=20
    def test5(a,b):
             print(a,b)
    c = test5(b,a)
    print(c)
    
"""
# 20 10
# None 这是因为函数没有返回值
# 因为 c = test5(b ,a)  其中的b=20， a=10；   采用位置传参，将20传给了a，10传给了b；打印a，b

""""
4,读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？
    a=10
    b=20
    def test5(a,b):
        a=3
        b=5
        print(a,b)
    c = test5(b,a)
    print(c)    
"""
# a = 10
# b = 20
# def test5(a, b):
#     a = 3
#     b = 5
#     print(a, b)
#
# c = test5(b, a)
# print(c)
# 3 5  因为 函数内部的3， 5    传入的值实际并没有用到；
# None  因为test5函数没有返回值


"""
5,写函数,传入函数中多个实参(均为可迭代对象如字符串,列表,元祖,集合等),将每个实参的每个元素依次添加到函数的动态参数args里面.
例如 传入函数两个参数[1,2,3] (22,33)最终args为(1,2,3,22,33)
"""
# def get_obj(*args):
#     temp_args = []
#     for i in args:
#         for k in i:
#             temp_args.append(k)
#     args = tuple(temp_args)
#     return args
# print(get_obj([1,2,3],(22,33)))


"""
6,写函数,传入函数中多个实参(实参均为字典),将每个实参的键值对依次添加到函数的动态参数kwargs里面.
例如 传入函数两个参数{‘name’:’alex’} {‘age’:1000}最终kwargs为{‘name’:’alex’ ,‘age’:1000}
"""
# def get_dic(**kwargs):
#     temp_dic = {}
#     for i in kwargs:
#         for key,value in i.items():
#             temp_dic.setdefault(key)
#     return temp_dic
# print(get_dic({'a':1}, {'b',2}))


"""
7, 下面代码成立么?如果不成立为什么报错?怎么解决?
7.1
    a = 2
    def wrapper():
            print(a)
    wrapper()
"""
# 成立啊


"""

7.2
    a = 2
    def wrapper():
            a += 1
        print(a)
    wrapper()
"""
# 报错。  局部函数里改动了全局变量，应对该变量进行全局声明


"""    
7.3
def wrapper():
    a = 1
    def inner():
        print(a)
    inner()
wrapper()
"""
# 正常


"""        
7.4
def wrapper():
    a = 1
    def inner():
        a += 1
        print(a)
    inner()
wrapper()
"""
# 报错。  内部函数影响了外部函数中定义的变量。应对该变量进行nonlocal声明


"""
8，写函数,接收两个数字参数,将较小的数字返回.
"""
# def get_min(a,b):
#     return min(a,b)
# print(get_min(3,-3))

"""
9，写函数,接收一个参数(此参数类型必须是可迭代对象),将可迭代对象的每个元素以’_’相连接,形成新的字符串,并返回.
例如 传入的可迭代对象为[1,'老男孩','武sir']返回的结果为’1_老男孩_武sir’
"""
# 包含数字，无法直接 ''.join(a)
# a = [1,'老男孩','武sir']
# print('_'.join('{}'.format(i) for i in a))

"""
1，写函数，传入n个数，返回字典{‘max’:最大值,’min’:最小值}
"""
# def get_max_and_min(*args):
#     max_num = max(args)
#     min_num = min(args)
#     return {'max_num':max_num, 'min_num':min_num}
#
# dic = get_max_and_min(1,2,321,5412,5,431,12,31,31,-3)
# print(dic)

"""
2，写函数，传入一个参数n，返回n的阶乘
"""
# 递归
# def get_factorial(n):
#     if n > 1:
#         return n*get_factorial(n-1)
#     else:
#         return 1  # 结束条件
# print(get_factorial(5))

# 不递归
# def get_factorial(n):
#     count = 1
#     while n > 0:
#         count *= n
#         n -= 1
#     return count
# print(get_factorial(5))


"""
3，写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组
"""
# 黑桃 红桃 草花 方块
# A 2 3 4。。。 J Q K
# def get_puke():
#     puke = []
#     for i in range(4):
#         for k in ['A', 2,3,4,5,6,7,8,9,10,'J', 'Q', 'K']:
#             if i == 0:
#                 puke.append(('黑桃{}'.format(k)))
#             elif i == 1:
#                 puke.append(('红桃{}'.format(k)))
#             elif i == 2:
#                 puke.append(('草花{}'.format(k)))
#             else:
#                 puke.append(('方块{}'.format(k)))
#     return puke
# puke = get_puke()
# print(puke)

"""
4.有如下函数:
    def wrapper():
        def inner():
            print(666)
    wrapper()
    你可以任意添加代码,用两种或以上的方法,执行inner函数.
"""
# def wrapper():
#     def inner():
#         print(666)
#     return inner  # 方法2
#     # inner()  # 方法1
#
# aaa = wrapper()
# aaa()

"""
5.先纸上写
5.1，有函数定义如下：
    def calc(a,b,c,d=1,e=2):
        return (a+b)*(c-d)+e
    请分别写出下列标号代码的输出结果，如果出错请写出Error。
    print(calc(1,2,3,4,5))
    print(calc(1,2))
    print(calc(e=4,c=5,a=2,b=3))
    print(calc(1,2,3))
    print(calc(1,2,3,e=4))
    print(calc(1,2,3,d=5,4))
5.2
    def extendList(val,list=[]):
        list.append(val)
        return list
        
    list1 = extendList(10)
    list2 = extendList(123,[])
    list3 = extendList('a')
    print('list1=%s'%list1)  # PS:注意这里输出的也是[10, 'a'], 因为后面又使用了一次默认参数。他们使用了同一个默认参数
    print('list2=%s'%list2)
    print('list3=%s'%list3)
5.3
    写代码完成99乘法表.(升级题)
"""

# def get_mult():
#     for i in range(9):
#         for j in range(i+1):
#             print('{} * {} = {}'.format((i+1), (j+1), (i+1)*(j+1)), end=' ')
#         print()
# get_mult()

"""
1，整理函数相关知识点,写博客。

2，写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
"""
# for循环
# def get_odd_nums(b):
#     ret = []
#     for i in range(len(b)):
#         if i % 2 == 1:
#             ret.append(b[i])
#     return ret
# print(get_odd_nums([3,123,14,215,435,12]))

# 切片 有位置规律时，比较好用
# def get_odd_index(b):
#     return b[1::2]
# print(get_odd_index([3,123,14,215,435,12]))

"""
3，写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
"""
# def judge_length(l):
#     return len(l) > 5  # f
# print(judge_length('ge'))


"""
4，写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
"""
# def check_length(l):
#     return l[:2] if len(l) > 2 else None
# print(check_length(['213',213]))

"""
5，写函数，计算传入函数的字符串中,[数字]、[字母]、[空格] 以及 [其他]的个数，并返回结果。
"""
# def get_category(str1):
#     category = {'digit_num': 0, 'alpha_num': 0, 'space_num': 0, 'others_num': 0}
#     for i in str1:
#         if i.isdigit():
#             category['digit_num']+=1
#         elif i.isalpha():
#             category['alpha_num']+=1
#         elif i.isspace():  # 判断是否空格
#             category['space_num'] +=1
#         else:
#             category['others_num']+=1
#     return category
# print(get_category(' 2zxc ##2 '))

"""写函数，检查对象（字符串 列表 元组）中是否有元素为空"""
# def check_null(s):
#     for i in s:
#         if i== '':
#             return True
# print(check_null(' 32'))

"""
6，写函数，接收两个数字参数，返回比较大的那个数字。
PS：三元运算
    返回1 if 条件 else 返回2  ----条件为True，返回1；否则返回2
"""
# def get_bigger_num(a,b):
#     return b if b>=a else a  # 三元运算
# print(get_bigger_num(8,8))


"""
7，写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
    dic = {"k1": "v1v1", "k2": [11,22,33,44]}
    PS:字典中的value只能是字符串或列表
    PS:不要轻易的去遍历字典的value。 数据可能太大
"""
# def check_length_dict(a):
#     for key, value in a.items():
#         if len(value) > 2:
#             a[key] = value[:2]
#     return a
# print(check_length_dict({"k1": "v1v1", "k2": [11,22,33,44]}))


"""
8，写函数，此函数只接收一个参数且此参数必须是列表数据类型，此函数完成的功能是返回给调用者一个字典，
    此字典的键值对为此列表的索引及对应的元素。例如传入的列表为：[11,22,33] 返回的字典为 {0:11,1:22,2:33}。
"""
# def get_dic_from_list(a):
#     dic = {}
#     for i in range(len(a)):
#         dic.setdefault(i,a[i])
#     return dic
# print(get_dic_from_list([11,22,33]))

"""
9，写函数，函数接收四个参数分别是：姓名，性别，年龄，学历。用户通过输入这四个内容，
    然后将这四个内容传入到函数中，此函数接收到这四个内容，将内容追加到一个student_msg文件中。
"""
# def fill_info(name,gender,age,quali):
#     with open('student_msg.txt', 'a',encoding='utf-8') as f1:
#         f1.write('{}{}{}{}'.format(name,gender,age,quali))
# fill_info('chen','male','24','benke')

"""
10，对第9题升级：支持用户持续输入，Q或者q退出，性别默认为男，如果遇到女学生，则把性别输入女。
"""
# def fill_info(name,age,quali,gender='male'):
#     with open('student_msg.txt', 'a',encoding='utf-8') as f1:
#         f1.write('{} {} {} {}\n'.format(name,gender,age,quali))
#
# while 1:
#     user_inp = input('>输入姓名 年龄 学历 性别。空格隔开。输入q退出')
#     if user_inp.upper() != 'Q':
#         a = user_inp.split()
#         name, age, quali, gender = a
#         fill_info(name, age, quali, gender)
#     else:
#         break

"""
11，写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作（升级题）。
"""
import os
def alter_file(filename, old, new):
    with open(filename, 'r', encoding='utf-8') as f1,\
        open('after.bak','w',encoding='utf-8') as f2:
        for line in f1:
            if old in line:
                line = line.replace(old, new)
            f2.write(line)

alter_file('before', '123', 'zxc')

os.remove('before')
os.renames('after.bak', 'before')

"""
12，写一个函数完成三次登陆功能：(升级题,两天做完)
(1)用户的用户名密码从一个文件register中取出。
(2)register文件包含多个用户名，密码，用户名密码通过|隔开，每个人的用户名密码占用文件中一行。
(3)完成三次验证，三次验证不成功则登录失败，登录失败返回False。
(4)登陆成功返回True。
"""


"""
13，再写一个函数完成注册功能：(升级题,两天做完)
(1)用户输入用户名密码注册。
(2)注册时要验证（文件regsiter中）用户名是否存在，如果存在则让其重新输入用户名，如果不存在，则注册成功。
(3)注册成功后，将注册成功的用户名，密码写入regsiter文件，并以 | 隔开。
(4)注册成功后，返回True,否则返回False。
"""


# def register(user_name,user_pwd,user_pwd_again):
#     """注册"""
#     with open('user_info.txt', 'a+', encoding='utf-8') as r_f:
#         r_f.seek(0)
#         flag = True
#         for name_pwd in r_f:  # name_pwd是str  -> {name:pwd}
#             if user_name == name_pwd[0:name_pwd.index(':')]:  # 检查id是否已存在
#                 flag = False
#                 break
#         if flag:
#             if user_pwd.isdigit() and user_pwd == user_pwd_again:  # 验证密码是否为数字，和两次密码相同
#                 r_f.write('{}:{}'.format(user_name, user_pwd))
#                 r_f.write('\n')
#             else:
#                 print("请确保密码为数字且两次输入的密码一致")
#         else:
#             print('用户已存在！')
#
#
# def login(name_input,pwd_input):
#     """登录"""
#     with open('user_info.txt', 'r', encoding='utf-8') as l_f:
#         user_info = {}
#         for name_pwd_l in l_f:
#             dic_name = name_pwd_l[0: name_pwd_l.index(':')]  # 通过切片返回用户名，方法是找到':'的索引，":"前为id，后为'pwd'
#             dic_pwd = name_pwd_l[name_pwd_l.index(':')+1:-1]
#             user_info[dic_name] = dic_pwd
#             for key in user_info:
#                 if name_input == key and pwd_input == user_info[key]:
#                     return True
#                 else:
#                     return False
#
#
# chosen = int(input('1注册，0登录，其余退出：'))
# if chosen == 1 or chosen == 0:
#     if chosen:
#         name_input = input('姓名:')
#         pwd_input = input('密码:')
#         user_pwd_again = input('确认密码(only digit):')
#         register(name_input, pwd_input, user_pwd_again)
#     else:
#         num = 0
#         while num < 3:
#             name_input = input('姓名:')
#             pwd_input = input('密码:')
#             flag = login(name_input, pwd_input)
#             if flag:
#                 print('登录成功！')
#                 break
#             else:
#                 num +=1
#                 print('账号或密码有误，还有{}次输入机会。'.format(3-num))

