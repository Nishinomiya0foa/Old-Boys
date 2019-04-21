# _*_ coding:utf-8 _*_
__author__ = 'brian'
__date__ = '2019/2/27 0027 21:45'

dic = {'name':'web'}
dic2 = {}
"""
dict: dic = {'name':'web'}
增：
    dic['age'] = 21     没有就增加，有了就覆盖
    dic.setdefault('age', 21)   没有就增加，有了不做改动
删除:
    dic.pop(key，d)    删除key对应的键值，返回值默认为value或d
    dic.popitem()   随机删除一对键值，py3中是删除最后一对;返回值是该键值组成的2-tuple
    dic.clear()     清空字典，字典为空：dic={}
    del dic         删除字典
    del dic[key]    删除key对应的键值
改：
    dic.update(dic2)    用dic2中的键值更新dic，无返回值
    dic[key] = value
查：
    dic.keys()      所有的key
    dic.values()    所有的value
    dic.items()     所有的(key, value)
    
    for key,value in dic.items()
        print(key,value)        输出字符串key,value
        
    dic.get(key, d) 返回key对应的value。key不存在则返回d，d默认为None
    
"""

