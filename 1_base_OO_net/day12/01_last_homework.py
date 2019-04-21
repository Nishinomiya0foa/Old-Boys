"""
    编写装饰器 为多个函数加上认证的功能（用户的账号密码来源于文件
    登录成功一次后，后续的函数都无序再输入用户名和密码
"""
# 账号密码保存在文件
# 需登录后，才可调用之后的函数；否则登录死循环

# 没使用装饰器。 辣鸡辣鸡
# def login(input_id, input_pwd):
#     with open('id_pwd', 'r', encoding='utf-8') as f1:
#         id_pwd = f1.readlines()
#         flag = 0
#         if input_id == id_pwd[0].strip('\n') and \
#                 input_pwd == id_pwd[1].strip('\n'):
#             flag = 1
#         return flag
# def reset_pwd():
#     print('pwd has been reset!')
# def scan_vlogs():
#     print('you are scanning vlogs!')
# flag = 0
# while not flag:
#     input_id = input('name:')
#     input_pwd = input('pwd:')
#     flag = login(input_id, input_pwd)
# reset_pwd()
# scan_vlogs()
# reset_pwd()

# FLAG = False  # 没办法 ， 使用全局变量
# def login_wrap(f):
#     def inner():
#         global FLAG
#         if FLAG:
#             ret = f()
#             return ret
#
#         while not FLAG:
#             input_id = input('id:')
#             input_pwd = input('pwd:')
#             with open('id_pwd', 'r', encoding='utf-8') as f1:
#                 id_pwd = f1.readlines()
#
#                 if input_id == id_pwd[0].strip('\n') and input_pwd == id_pwd[1].strip('\n'):
#                     FLAG = True
#                     print('登录成功！')
#                     ret = f()
#                     return ret
#     return inner
#
# @login_wrap
# def reset_pwd():
#     print('pwd has been reset!')
# @login_wrap
# def scan_vlogs():
#     print('you are scanning vlogs!')
#
# reset_pwd()
# scan_vlogs()
# reset_pwd()


"""
    编写装饰器，为多个函数加上记录调用功能。
    要求每次调用函数都将被调用的函数名写入文件
"""
# import time
# def wrap_record(f):
#     def inner():
#         f()
#         struct_time = time.localtime()
#         timesession = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)
#         with open('used_func', 'a', encoding='utf-8') as f1:
#             f1.write('{}\t-{}\n'.format(f.__name__,timesession))  # func.__name__ 返回函数名
#     return inner
#
#
# @wrap_record
# def reset_pwd():
#     print('pwd has been reset!')
#
#
# @wrap_record
# def scan_vlogs():
#     print('you are scanning vlogs!')
#
# reset_pwd()
# scan_vlogs()
# reset_pwd()

"""
    1.编写下载网页内容的函数。用户传入一个url，函数返回下载页面的结果
    2.为上述函数添加装饰器。实现缓存网页的功能：
        下载的页面存入文件。如果文件不为空，则从文件中读取内容。否则下载并存入文件
"""
# import os
# os.path.getsize(filename)  # 获取文件大小
# from urllib.request import urlopen
#
# def wrap_url(f):
#     def inner(url):
#         with open('cache_page', 'r+', encoding='utf-8') as f1:
#             for line in f1:
#                 if line:  # os.path.getsize(filename)  # 获取文件大小   也可以使用这招
#                     return ''.join(f1.readlines())  # readlines读出的是一个列表。将其转换为字符串
#             cont_page = f(url)
#             f1.write(cont_page)
#         return cont_page
#     return inner
#
#
# @wrap_url
# def down_page(url):
#     resp = urlopen(url).read()
#     resp = resp.decode('utf-8')  # 不可变数据类型str 所以需要重新赋值
#     return resp
#
# print(down_page('http://www.cnblogs.com/pilgrim-acc/'))
