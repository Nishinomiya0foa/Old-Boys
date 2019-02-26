"""
不可变数据类型： tuple, bool, str, int    ----可哈希
  可变数据类型： list，dict， set

dict：无序的-没有索引
    1. key必须为不可变数据类型
    2. value没有数据类型限制

    优点：
        1.二分查找查询
        2.大量关系型数据

dict：增删改查
    增：
        1. dict['key'] = value  如果key不存在，则新增；
                                如果key已存在，则覆盖
        2. dict.setdefault('key', d)    如果key不存在，则新增 value=d
                                        如果key已存在，则没有作用，不报错
    删：
        1. dict.pop(key, d) 删除key对应的键值，有返回值，返回值为value值。
                            key不存在则返回d，默认为None
        2. dict.popitem()   随机删除一对键值；有返回值，为被删除的2-tuple
        3. del dict['key']  删除key对应的键值，也可以删除整个字典
                            key不存在则报错
        4. dict.clear()     清空字典
    改：
        1. dict['key'] = value  如果key不存在，则新增；
                                如果key已存在，则覆盖
        2. old_dict.update(new_dict)    用new_dict更新old_dict,有重复的key或old_dict中不存在的key，则更新为new_dict中的键值
    查：
        1. dict.get('key', d)   返回value, 如果这个key不存在，则返回d，d的默认值为None
        2. dict.keys()  dict.values()   dict.items()
              key           value      ('key', 'value')

            for key, value in dict.items():   -> 遍历字典键值
"""

dic = {
    'name': 'web',
    'age': 22,
    'gender': 'male',
}

"""
    增
"""
# 如果dict['key'],key为dict中已存在的key，则新的value会覆盖
dic['height'] = 179
print(dic)

dic['age'] = 25
print(dic)

# setdefault(key, value) value默认值为None；key已存在则不覆盖，不存在则新增
dic.setdefault('age',144)
print(dic)

"""
    删除
"""
# pop(key) 删除key对应的键值对，返回key对应的value
# pop(key, d) 如果没有这个key,返回d
print(dic.pop('age'), 'pop')  # 删除k

# popitem() 随机删除一对键值对（python3.6以后的版本随机删除)
# 返回 2-tuple(二元元组）
dic.popitem()
print(dic.popitem())

# clear() 清空字典

# del dict[key]   可删除字典或字典中的键值对


"""
    改
"""
# dict['key'] = value 该键值对已存在则覆盖，即改动

# old_dict.update(new_dict) 把new_dict中的所有键值，更新到old_dict中。key相同则覆盖，不同则新增
dic = {
    'name':'web',
    'age':22,
    'gender':'male',
    }

dic2 = {
    'name':'cwb',
    'hobby':'coding',
    'iq':100,
}
dic.update(dic2)
print(dic)

"""
    查
"""
dict3 = {'name': 'cwb', 'age': 22, 'gender': 'male', 'hobby': 'coding', 'iq': 100}
# 打印所有键
print(dict3.keys())
# 打印所有值
print(dict3.values())
# 打印所有键值。 tuple
print(dict3.items())

for key, value in dict3.items():
    print(key, value)

# dict['key'] 如果key不存在 则报错

# dict.get('key', d)  返回'key'对应的value，key不存在则返回d，d默认为None


# a = 1, b = 2 一行代码互换a，b的值
a = 1
b = 2
a, b = b, a
print(a, b)

#
a, b = [1, 2]
print(a, b)

print(dict3.get('name1','fxxk'))