"""部分练习"""

name = "aleX leNb"
# 移除name变量对应的值两边的空格，并输出处理结果
print(name.strip())

# 移除name变量左边的’al’并输出处理结果
print(name.lstrip('al'))

# 移除name变量右而的’Nb’，并输出处理结果
print(name.rstrip('Nb'))

# 移除name变量开头的a’与最后的’b’，并输出处理结果
print(name.strip('ab'))

# 判断name变量足否以"al”开头，并输出结果
print(name.startswith('al'))

# 判断name变虽是否以”Nb”结尾，并输出结果
print(name.endswith('Nb'))

# 将name变量对应的值中的所有的'l'替换为“p”，并输出
print(name.replace('l', 'p'))

# 将name变量对应的值中的第一个'l'替换为“p”，并输出
print(name.replace('l', 'p', 1))

# 将name变量对应的值根据所有的'l'分割,并输山结果
print(name.split('l'))

# 将name变量对应的值根据第一个'l'分割,并输山结果
print(name.split('l', 1))

# 将name变量全部大写/小写
print(name.upper())
print(name.lower())

# 将name变量对应的值首字母‘a’大写，其余小写
print(name.capitalize())

# 判断name变量对应的值字母'l'出现几次，并输出结
print(name.count('l'))

# 输出name中e所在的索引位置
print(name.find('e'))

str1 = '132a4b5c'
# 切片输出s3  '1245'
print(str1[::2])

"""
    返回用户输入的数据中有几个整数
"""
user_input = input('>>')
count = 0
for word in user_input:
    if word.isdigit():
        count+=1
print(count)


"""
    用户输入四则计算器  ：  1+8等
    无法计算负数
"""
calculate_plus = input('>>')
if '+' in calculate_plus:
    correct_form = calculate_plus.split('+')
    sum = int(correct_form[0])+int(correct_form[1])
    print(sum)
elif '-' in calculate_plus:
    correct_form = calculate_plus.split('-')
    sum = int(correct_form[0])-int(correct_form[1])
    print(sum)
elif '*' in calculate_plus:
    correct_form = calculate_plus.split('*')
    sum = int(correct_form[0]) * int(correct_form[1])
    print(sum)
elif '/' in calculate_plus:
    correct_form = calculate_plus.split('/')
    sum = int(correct_form[0]) / int(correct_form[1])
    print(sum)


"""
    while for 循环输出 str 中的每一字符
"""
words_be_count = input('>>')
# for i in words_be_count:
#     print(i)
count = 0
while count < len(words_be_count):
    print(words_be_count[count])
    count+=1


