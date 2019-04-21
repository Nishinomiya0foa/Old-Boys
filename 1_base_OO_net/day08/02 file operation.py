# 打开绝对路径文件
# f = open('C:\\Users\Administrator\Desktop\myfavourite.txt', 'r', encoding='utf-8')
# content = f.read()
# print(content)
# f.close()

# 打开相对路径  ----在当前文件夹路径下

# 只读
# bytes -> str
# f2 = open('thisisafile', 'r', encoding='utf-8')
# print(f2.read())
# f2.close()

# 只写 w
# f3 = open('lgo.txt','w', encoding='utf-8')
# f3.write("i'm here! \tyou know \nanother line!")
# f3.close()

# 只写 wb
# f = open('lgo.txt', 'wb', )
# f.write('he呵呵he'.encode('utf-8')) # 将str的unicode类型，转换为utf-8类型
# f.close()

# 追加 a
# f = open('lgo1.txt', 'a', encoding='utf-8')
# f.write('bie啊')
# f.close()

# 追加 ab
# f = open('lgo.txt', 'ab')
# f.write('qusi'.encode('utf-8'))
# print(f.read())
# f.close()

# 读写 r+
# 1.先读后写，文件中的内容被读出，光标移至末尾，再写的话就是从末尾添加
# 2.先写后读，从第0个位置写文件（因为默认光标在0号位置），然后读出原文件写了之后除了被覆盖的其余内容，
#   由于py3使用utf-8编码，一个汉字=3个字节，所以汉字会覆盖3个英文/字符
# ps：原文件中包含中文的情况（使用utf-8编码），如果使用英文字符覆盖，但读写到该中文时，覆盖该中文的应该是3个英文字符，
#     但如果英文字符不够3个，会造成乱码情况
# f = open('lgo.txt', 'r+', encoding='utf-8')
# # print(f.read())
# f.write('aaa')
# print(f.read())
# f.close()

# 写读 w+   先清空文件，再进行写入
# f = open('lgo1.txt', 'w+', encoding='utf-8')
# f.write('aaa')
# # seek(index) 调整光标位置
# print(f.read())
# f.close()

# 写读 a+
# f = open('lgo.txt', 'a+', encoding='utf-8')
# print(f.read())
# f.write('adsf')
# f.seek(3)
# print(f.read())
# f.close()

"""
方法
    f.read(d)  ----读文件内容，默认全部读出，或读出d个字符
    f.seek(d)  ----按字节来定光标位置。对英文无影响，但是utf-8编码下，1个中文=3个字节
    f.tell()  ----返回当前光标所在位置int
    f.readable()  ----返回当前文件是否可读，bool
    f.readline()  ----读出一行,结尾为\n，光标置于下一行起始位置
    f.readlines()  ----读出文件全部内容，每一行当作list的一个元素，添加到list中
    f.truncate(size)  ----1.不指定size的值，文件从起始位置截断至光标所在位置，之后的内容删除
                      ----2.指定size的值，文件从起始位置截断size长度的值，之后的内容删除
    for line in f:  ----遍历打印文件
        new_line = line.strip('\n') #  每一行line的末尾总有一个"\n"，不去除会有额外空行
        print(new_line)
    with open('lgo.txt', 'r+', encoding='utf-8') as f1, open('text1.txt', 'r+', encoding="utf-8") as f2:
                        ----不用close()，文件使用完后会自动close,可同时打开多个文件

"""
# f = open('lgo.txt', 'r+', encoding='utf-8')
# content = f.read(3)

# seek()
# f.seek(17) #  此处是按字节查找，utf-8中，一个中文=三个字节

# tell() 返回光标位置
# print(f.tell())

# tell()应用  ----读文件最后5个字符
# cont = f.tell()
# print(cont)
# f.seek(cont - 5)
# print(f.read())

# truncate(size)  1.不指定size的值，文件从起始位置，截断至光标位置，之后的内容删除
#                 2.指定size的值，文件从起始位置，截断size长度的内容，之后的内容删除
# f.seek(7)
# f.truncate(3)
# content = f.readlines()
# print(content,f.tell())
# print(f.read())
# for line in f:
#     print(line.strip('\n'))
# f.close()

# with
# with open('lgo.txt', 'f+', encoding='utf-8') as f1,open('frame.py', 'f+', encoding='utf-8') as f2:
#     print(f1)

"""
    练习，注册（将账号密码填入一个文件）+3次登录
    要求。用户名不可以重复，密码全为数字。
"""
chosen = int(input('1注册，2登录，其余退出：'))
if chosen == 1:
    """注册"""
    with open('user_info.txt', 'a+', encoding='utf-8') as r_f:
        user_name = input('姓名:')
        r_f.seek(0)
        flag = True
        for name_pwd in r_f:  # name_pwd是str  -> {name:pwd}
            if user_name == name_pwd[0:name_pwd.index(':')]:  # 检查id是否已存在
                flag = False
                break
        if flag:
            user_pwd = input('密码(only digit):')
            user_pwd_again = input('确认密码(only digit):')
            if user_pwd.isdigit() and user_pwd == user_pwd_again:  # 验证密码是否为数字，和两次密码相同
                r_f.write('{}:{}'.format(user_name, user_pwd))
                r_f.write('\n')
            else:
                print("请确保密码为数字且两次输入的密码一致")
        else:
            print('用户已存在！')

elif chosen == 2:
    """登录"""
    chances = 3
    while chances > 0:
        with open('user_info.txt', 'r', encoding='utf-8') as l_f:
            name_input = input('姓名:')
            pwd_input = input('密码:')
            user_info = {}
            flag = False
            for name_pwd_l in l_f:
                dic_name = name_pwd_l[0: name_pwd_l.index(':')]  # 通过切片返回用户名，方法是找到':'的索引，":"前为id，后为'pwd'
                dic_pwd = name_pwd_l[name_pwd_l.index(':')+1:-1]
                user_info[dic_name] = name_pwd_l[name_pwd_l.index(':')+1:-1]
                for key in user_info:
                    if name_input == key and pwd_input == user_info[key]:
                        flag = True
                        break
                    else:
                        flag = False
            if flag:
                print("登录成功")
                chances = -11
            else:
                chances -= 1
                print("登录失败，重试机会为{}".format(chances))

else:
    print('gun')
    pass