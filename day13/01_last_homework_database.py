"""
1.默写：带参数的装饰器。需要标注代码的执行步骤。
2.整理作业：函数的知识点以及装饰器相关作业。装饰器作业需要自己写一遍，并给作业加注释。
3.周末大作业：实现员工信息表
文件存储格式如下：
id，name，age，phone，job
1,Alex,22,13651054608,IT
2,Egon,23,13304320533,Teacher
3,NASA,25,1333235322,IT

现在需要对这个员工信息文件进行增删改查。

不允许一次性将文件中的行都读入内存。
基础必做：
a.可以进行查询，支持三种语法：
select 列名1，列名2，… where 列名条件
支持：大于小于等于，还要支持模糊查找。
示例：
select name, age where age>22
select * where job=IT
select * where phone like 133
"""

def do_search_all(split_input):
    """
        查询符合条件的所有完整行。
        split_input: 用户输入的内容，按空格切分之后形成的数组
        judge: split_input数组的后三个元素
        cols_menu: employ_ee文件的列名
        dic_data: employ_ee文件每行的每个元素，按照 列名：值 的键值对存入字典
        ret_data: 符合查询条件的所有行组成的列表
        :return 返回ret_data
    """
    judge = split_input[-3:]
    # print(judge)
    # dic_data = {'id':None, 'name':None, 'age':None, 'phone':None, 'job':None}
    cols_menu = ['id','name','age','phone','job']
    dic_data = {}  # 单行记录增城的字典
    ret_data = []  # 返回的列表
    with open('employee_data', 'r', encoding='utf-8') as f1:
        for line in f1:
            split_data = line.strip('\n').split(',')
            # print(split_data)
            for i in cols_menu:
                dic_data[i] = split_data[cols_menu.index(i)]
            if judge[0] in dic_data:  #
                if judge[1] == '>':  # 处理大于号
                    if int(dic_data[judge[0]]) > int(judge[-1]):  # 大于号前后应该都为数字
                        ret_data.append(line.strip('\n'))
                elif judge[1] == '<':
                    if int(dic_data[judge[0]]) < int(judge[-1]):  #
                        ret_data.append(line.strip('\n'))
                elif judge[1] == '=':
                    if dic_data[judge[0]].lower() == judge[-1]:  # 判断字符串是否相等！
                        ret_data.append(line.strip('\n'))
                else:
                    if judge[-1] in dic_data[judge[0]].lower():  # like 模糊查询
                        ret_data.append(line.strip('\n'))
    return ret_data

from functools import wraps
def split_ret_data(f):  # 装饰器函数
    """select name, age where age>22"""
    @wraps(f)
    def inner(user_input):
        ret = f(user_input)  # 执行被装饰的函数，返回整条数据，以列表形式保存
        user_input_split = user_input.split()  # 用户输入的查询语句被以空格分隔，返回了列表
        user_see = user_input_split[1:user_input_split.index('where')]  # 用户想要select 的 列名 组成的列表
        if user_see != ['*']:  # 判断是不是查询显示整条数据
            cols_menu = ['id', 'name', 'age', 'phone', 'job']  # emplyee_data文件的列名
            dic_data = {}  # 字典  {查询显示的列名：值}
            ret_fin = []  # 列表  放查询显示的值
            for i in ret:
                temp_lis = i.split(',')  # 去除被装饰函数中的每个， 组成一个新列表
                for j in range(5):  # 将所有查询到的数据，放入dic_data
                    dic_data[cols_menu[j]] = temp_lis[j]
                for i in user_see:  # 将user_see中的列名，找出对应的值。用列表保存
                    i = i.strip(',')
                    if i in dic_data:
                        ret_fin.append(dic_data[i])
                ret_fin.append('\n')
            text = ""
            for i in range(int(len(ret_fin) / len(user_see))):  # 把ret_fin 的数据，更好的显示出来
                text = ' '.join(ret_fin[i*(len(user_see)+1):(i+1)*(len(user_see)+1)]) + text
            ret_data = text
            return ret_data
        else:  # 查询 * 的情况
            return '\n'.join(ret)
    return inner


@split_ret_data  # ->choose_search_part = split_ret_data(choose_search_part)
def choose_search_part(s):
    """
    查询函数的跳转
    """
    s = s.lower()
    sigh = ['>','<','=','like']
    split_input = s.split()  # 将输入的按空格切分。放入数组
    if split_input[0] == 'select' and 'where' in split_input:
        where_position = split_input.index('where')  # 'where'的索引
        flag_position = split_input[where_position + 2]  # 处理不够好
        for sign in sigh:
            if sign in flag_position:
                ret_cel = do_search_all(split_input)  # 跳转到查询
                return ret_cel


def add_employee(name='Null',age='Null',phone='Null',job='Null'):
    """employee_data中新增文件记录"""
    with open('employee_data', 'r+', encoding='utf-8') as f1:
        for line in f1:
            lis = line
        id = int(line[:lis.find(',')]) +1  # 新增的id应该是上一条的id+1
        f1.write('{id},{name},{age},{phone},{job}'.format(id=id, name=name, age=age, phone=phone,job=job))
        f1.write('\n')


import os
def del_employee(user_input_search):
    """删除某条记录"""
    user_input = 'select * where ' + user_input_search  # 指引用户输入查询条件
    employee_list = choose_search_part(user_input)  # 调用 查询的函数。 接收其返回值
    if employee_list:
        print('以下为查询结果：')
        print(employee_list)
    else:
        print('没有相关记录')
        return
    del_command = input('输入id以删除用户：')  # 输入想删除的记录的id
    with open('employee_data', 'r+', encoding='utf-8') as f1, open('employee_data.bak', 'w', encoding='utf-8') as f2:
        for line in f1:
            if line[:line.index(',')] == del_command:
                continue
            f2.write(line)  # 除了想删除的哪行，其余行写入到新文件
    os.remove('employee_data')  # 删除旧文件
    os.renames('employee_data.bak','employee_data')  # 新文件改名


def alter_employee(user_input_alter:str):
    """
        修改文件中某条记录
        # set name = xxx where id = 3
    """
    cols_menu = ['id', 'name', 'age', 'phone', 'job']
    user_input_alter = user_input_alter.split(' ')
    user_input_alter_search = ' '.join(user_input_alter[-3:])
    user_input = 'select * where ' + user_input_alter_search  #
    employee_record = choose_search_part(user_input)  # 调用 查询的函数。 接收其返回值
    if employee_record == '':
        print('没有这条数据')
    employee_record = employee_record.split('\n')
    with open('employee_data', 'r', encoding='utf-8') as f1, open('employee_data.bak', 'w', encoding='utf-8') as f2:
        for line in f1:
            for i in employee_record:
                print(i)
                alter_cont = user_input_alter[1:4]  # 想要修改的内容
                line_list = line.strip('\n').split(',')
                if i+'\n' == line:
                    # 进行修改
                    for j in cols_menu:
                        if j == alter_cont[0]:
                            line_list[cols_menu.index(j)] = alter_cont[2]
                    line = ','.join(line_list) + '\n'
            f2.write(line)
    os.remove('employee_data')
    os.renames('employee_data.bak', 'employee_data')
    print('修改完成')


def wrap_login(f):
    def inner():
        flag = False
        while not flag:
            admin_id = input('管理员账号：')
            admin_pwd = input('管理员密码：')
            if admin_id == 'admin' and admin_pwd == '123456':
                flag = True
        f()
    return inner


import time

@wrap_login
def operate():
    while 1:
        print('输入查询，新增，删除，修改，q退出')
        print('选择想要进行的操作：')
        operation = input('>')
        if operation.lower() == 'q':
            print("正在退出系统...")
            time.sleep(0.5)
            break
        elif operation == '查询':
            search_words = input('输入查询语句：')
            print(choose_search_part(search_words))
        elif operation == '新增':
            add_words_name = input('输入姓名：')
            add_words_age = input('输入年龄：')
            add_words_phone = input('输入手机号：')
            add_words_job = input('输入工作：')
            add_employee(add_words_name, add_words_age, add_words_phone, add_words_job)
        elif operation == '删除':
            print('输入想要删除的记录查询：')
            del_words = input('select * where ')
            del_employee(del_words)
        elif operation == '修改':
            alter_words = input('输入修改语句：')
            alter_employee(alter_words)
        else:
            print('不能识别您输入的信息。重新输入或退出')


operate()






"""
进阶选做：
b.可创建新员工记录，id要顺序增加
c.可删除指定员工记录，直接输入员工id即可
d.修改员工信息
语法：set 列名=“新的值” where 条件
#先用where查找对应人的信息，再使用set来修改列名对应的值为“新的值”
# set name = xxx where id = 3

注意：要想操作员工信息表，必须先登录，登陆认证需要用装饰器完成
其他需求尽量用函数实现

作业要求：
1.今天的第2、3个作业一起打包交上来
2.放在作业2文件夹中
需要交整理的函数相关的思维导图
整理的函数知识点的博客
装饰器作业加注释
3.大作业放在3文件夹中
　　文件夹中需要包括：
　　代码
　　流程图（请上交一张png图片。如果没有合适的画图软件，可以用processon画）
　　readme文件（请上交一个txt文件，对作业进行一些简单说明，包括作业的整体思路，如何运行，实现了哪些功能，遇到了哪些问题等。）

"""