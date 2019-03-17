""" random  ---- 随机数 """

import random

# 随机整数
print(random.randint(5, 5))  # randint(a, b) 返回a-b之间的随机整数，包含a和b；a必小于等于b
print(random.randrange(1,5,2))  # randrange(a,b,sep) 返回a-b之间的随机整数，包含a，不包含b，步长sep

# choice(iterable)  ---- 接收iterable，返回其中任意1个元素
print(random.choice([3,2,1,0]))

# sample(iterable, count)  ---- 接收iterable，返回其中任意count个元素的组合;不重复
print(random.sample([3,2,1,0,-1,-3], 3))

# shuffle(list)  ---- 接受列表,返回该对象被打乱后的状态。 必须为可变数据类型
l = [1,2,3,4,5]
b = (1,2,3,4,5)
s = '12345'
random.shuffle(l)
print(l)

# 验证码

# chr() 可以返回数字对应的ASCII码
print(chr(122))  # 65 - 90   97 - 122
                    # 0-9
l = []
for i in range(65, 91):
    l.append(chr(i))
for i in range(97,123):
    l.append(chr(i))
l.extend(range(10))
print(random.sample(l, 4))

