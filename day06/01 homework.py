# _*_ coding:utf-8 _*_
__author__ = 'brian'
__date__ = '2019/2/27 0027 21:59'

"""
    1
"""
tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
# a. 讲述元祖的特性
"""内部元素无法修改， 只读数组。 但内部如果嵌套了其他如数组，字典，则被嵌套的这些可以进行修改"""
# b. 请问tu变量中的第一个元素 "alex" 是否可被修改？
"""No"""
# c. 请问tu变量中的"k2"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素 "Seven"
"""数组"""
tu[1][2]['k2'].append('Seven')

# d. 请问tu变量中的"k3"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素 "Seven"
""" 元组  不能新增元素'Seven' """


"""
    2
"""
# dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}

# a.请循环输出所有的key
# for key in dic.keys():
#     print(key)

# b.请循环输出所有的value

# c.请循环输出所有的key和value
# for key, value in dic.items():
#     print(key, value)

# d.请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
# dic['k4'] = 'v4'
# print(dic)

# e.请修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
# dic['k1'] = 'alex'
# print(dic)

# f.请在k3对应的值中追加一个元素 44，输出修改后的字典
# dic['k3'].append(44)
# print(dic)

# g.请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
# dic['k3'].insert(0, 18)
# print(dic)


"""
    3
"""
av_catalog = {
    "欧美":{
        "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
        "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "x-art.com":["质量很高,真的很高","全部收费,屌丝请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}

# a,给此 ["很多免费的,世界最大的","质量一般"]列表第二个位置插入一个  元素：'量很大'。
# av_catalog['欧美']["www.youporn.com"].insert(1, '量很大')
# print(av_catalog)

# b,将此 ["质量很高,真的很高","全部收费,屌丝请绕过"]列表的 "全部收费,屌丝请绕过" 删除。
# av_catalog['欧美']["x-art.com"].pop(1)
# print(av_catalog)

# c,将此["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]列表的 "verygood"全部变成大写。
# av_catalog['日韩']["tokyo-hot"][1] = av_catalog['日韩']["tokyo-hot"][1].upper()
# print(av_catalog)

# d,给 '大陆' 对应的字典添加一个键值对 '1048' :['一天就封了']
# av_catalog['大陆'].setdefault('1048', ['一天就疯了'])
# print(av_catalog)

# e,删除此"letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"]键值对。
# av_catalog['欧美'].pop('letmedothistoyou.com')
# print(av_catalog)

# f,给此["全部免费,真好,好人一生平安","服务器在国外,慢"]列表的第一个元素，加上一句话：'可以爬下来'
# av_catalog['大陆']['1024'][0] = av_catalog['大陆']['1024'][0]+', 可以爬下来'
# print(av_catalog)
# av_catalog['大陆']['1024'].insert(0, '可以爬下来')
# print(av_catalog)

"""
    4
"""
# 有字符串"k:1|k1:2|k2:3|k3:4" 处理成字典 {'k':1,'k1':2....}
dirty_str = "k:1|k1:2|k2:3|k3:4"
clean_dic = {}
be_worked_dirty_str = dirty_str.split('|')
for i in be_worked_dirty_str:
    temp_list = i.split(':')
    clean_dic.setdefault(temp_list[0], int(temp_list[1]))
print(clean_dic)

"""
    5
    有如下值li= [11,22,33,44,55,77,88,99,90]，将所有大于 66 的值保存至字典的第一个key中，
    将小于 66 的值保存至第二个key的值中。
    即： {'k1': 大于66的所有值列表, 'k2': 小于66的所有值列表}
"""
li= [11,22,33,44,55,77,88,99,90]
list_s = []
list_b = []
for i in li:
    if i >= 66:
        list_b.append(i)
    else:
        list_s.append(i)
dic = {}
dic.setdefault('k1', list_b)
dic.setdefault('k2', list_s)
print(dic)


"""
    6
    输出商品列表，用户输入序号，显示用户选中的商品
    商品列表：
         goods = [{"name": "电脑", "price": 1999},
             {"name": "鼠标", "price": 10},
             {"name": "游艇", "price": 20},
             {"name": "美女", "price": 998}, ]
    要求:
    1：页面显示 序号 + 商品名称 + 商品价格，如：
                  1 电脑 1999 
                   2 鼠标 10
                 …
    2：用户输入选择的商品序号，然后打印商品名称及商品价格
    3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
    4：用户输入Q或者q，退出程序。
"""
goods = [{"name": "电脑", "price": 1999},
         {"name": "鼠标", "price": 10},
         {"name": "游艇", "price": 20},
         {"name": "美女", "price": 998}, ]
id = 0
for i in goods:
    print('第 {id} 个商品为 {name} ，价格为 {price}'.format(id=id+1,
                                                   name=goods[id]['name'], price=goods[id]['price']))
    id += 1
while 1:
    customer_chosen = input('输入商品序号：')
    if customer_chosen.upper() == 'Q':
        break
    id = int(customer_chosen)
    if 0 < id <= len(goods):
        print('你选择的是{}, 价格为{}'.format(goods[id-1]['name'], goods[id-1]['price']))
        break
    else:
        print('无此商品，重新输入')

# 默写 字典的增删改查
# 默写大妈 过滤敏感字符 l = ['小三','后宫如云']， 用相同数量的*代替