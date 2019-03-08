"""生成器的表达式"""
#生成器：没执行__next__和其他获取生成器的值得方法时，生成器的内部不执行 


# 列表推导式
# 简易生成  把每一个for循环得到的值返回给前面
# egg_list = ['蛋蛋{}'.format(i) for i in range(10)]  # 返回列表
# print(egg_list)


# 生成器表达式
# 只能生成简易的生成器
# g = (i for i in range(10))  # 返回生成器。可使用生成器的方法去访问；几乎不占用内存
# for i in g:
#     print(i)


# 例子 生成器表达式
g_egg = ('鸡蛋{}'.format(i) for i in range(10))
print(g_egg.__next__())
num = 0
for i in g_egg:
    if num < 5:
        print(i)
        num+=1

# 计算10以内的正整数的平方和
print(sum(x ** 2 for x in range(10)))

# 输出 10以内所有的正整数的平方
sq_g = (x ** 2 for x in range(1, 10))
for i in sq_g:
    print(i)