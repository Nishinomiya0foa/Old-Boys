""" 序列化  ---- 将原本的字典，数组等转化为字符串的过程，称为序列化
            ---- 从字符串转回之前的数据类型的过程，称为反序列化
json
pickle
shelve
"""

"""json 模块！  ---- 数字，字符串，列表，字典，元组支持序列化；其中元组是被当作字典处理的！
    # 非常重要
    # json是通用的序列化格式
    # 只有小部分数据类型能通过json转化为字符串：数字，字符串，列表，字典，元组
    # json内部只有双引号， 单引号在外部
    
"""
import json
# dic = {'k1':'请大家发'}
# # dumps， loads方法    ---- 操作内存中的数据
# str_dic = json.dumps(dic)  # dumps(obj) 对obj进行序列化操作，使obj转化为str类型，返回值为这个str
# print(type(str_dic), str_dic)
# dic_dic = json.loads(str_dic)  #loads(str)  对str进行反序列化，使其恢复之前的数据类型，有返回值
# print(type(dic_dic), dic_dic)

# dump, load方法  ---- 用于文件的操作,一次性写入，一次性读出来
# dic = {'k1':'请大家发'}
# with open('json_test', 'w', encoding='utf-8') as f1:
#     json.dump(dic, f1, ensure_ascii=False)  # 先对dic进行序列化，在写入句柄f1中;
#                                             # ensure_ascii=False,不以ascii码的形式写入，保证文件中能写入中文bytes
# with open('json_test', 'r', encoding='utf-8') as f1:
#     res = json.load(f1)  # 从文件中读取内容，并将其进行反序列化
#     print(type(res), res)


"""重要的pickle模块 
    # 所有的python中的数据类型都能转化为字符串
    # pickle序列化的内容只有python能解
    # 反序列化依赖代码
    # 可分步dump、load，这是与json不同
"""
import pickle
# 序列化的结果是一个二进制字符串
# 同样拥有dumps、loads 和 dump、load方法。和json同样的用法。在dump和load时，文件打开类型必须为二进制。
#


"""shelve  ---- 
    # 序列化句柄，
    # 使用句柄直接操作，方便
"""
# shelve
# import shelve
# with shelve.open('aaa', writeback=True) as f1:  # 直接shelve.open(file)打开文件返回句柄，接下来可以直接进行各种数据类型的读写
#                             ---- writeback参数= True;这是由于shelve不会保存所作修改。所以进行修改时，需要将此参数设置为True
# #     f1['key'] = {'k22':'v222'}
#     obj = f1['key']     # 读句柄内的文件，操作等同于原数据类型
# print(obj)