dic = {
    'name':['chenwb', 'xiaoming', 'zhanglei'],
    'py9':{
        'time':'1213',
        'learn_money':19800,
        'adress':'CBD',
    },
    'age':21,
}

dic['age'] = 23

# name里新增tiantian
# dic['name'].append('tiantian')
# print(dic)

# xiaoming 大写
dic['name'][1] = dic['name'][1].upper()
print(dic)

# py9对应的字典里新增一对键值对: female:6
dic['py9'].setdefault('female', 6)
# dic['py9']['female'] = 6
print(dic)


# 输入一段 字母+数字 混合， 判断出现了几段数字
user_input = input('>>')
count = 0
for i in user_input:
    if i.isalpha():
        user_input = user_input.replace(i, ' ')
# 这里有点坑  当想把所有的空格 \t \n都split时， split()里什么都不填
# 如果填了split(' ') 返回的列表里会有['', '']这种脏数据
# count_list = user_input.split(' ')
count_list = user_input.split()
print(count_list)
print(len(count_list))

