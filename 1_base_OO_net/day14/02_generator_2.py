"""生成器进阶"""
# 惰性运算

# def generator():
#     print(123)
#     words = yield 1
#     print(words)
#     print(456)
#     yield 2
#     print(789)
#
# g = generator()
# ret = g.__next__()
# print(ret)
# # 新的获取值得方式
# ret = g.send('Hello')  # seng()，在获取下一个yield值（效果等同__next__())时，传递一个值给上一个yield的位置
# print(ret)

# send()的注意事项
# send()使用前，需要__next__获取下一个值，因为他需要给上一个yield位置传值
# 最后一个yield不能使用send()，或者可以最后一个yield不进行传值


# 例子 利用生成器的send()方法 完成运动员射击比赛每轮的平均环数计算

# def average_shoot():
#     sum = 0
#     shoots = 0
#     avg = 0
#     while 1:
#         num = yield avg
#         sum += num
#         shoots += 1
#         avg = sum / shoots
#
#
# g = average_shoot()
# g.__next__()
# print(g.send(10))
# print(g.send(20))


# 利用生成器，输出斐波那契数列
# [0,1,1,2,3,5,8...]

def feb_g():
    febn = [0, 1]
    i = 0
    while 1:
        febn.append(febn[i]+febn[i+1])
        i += 1
        yield febn[i+1]


feb = feb_g()
num = 0
# for i in feb:
#     if num <5:
#         print(i)
#         num += 1
lis = []
for i in range(10):
    lis.append(feb.__next__())

print(lis)
