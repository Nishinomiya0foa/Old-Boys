"""生成器进阶"""

def generator():
    print(123)
    words = yield 1
    print(words)
    print(456)
    yield 2
    print(789)

g = generator()
ret = g.__next__()
print(ret)
# 新的获取值得方式
ret = g.send('Hello')  # seng()，在获取下一个yield值（效果等同__next__())时，传递一个值给上一个yield的位置
print(ret)

# send()的注意事项
# send()使用前，需要__next__获取下一个值，因为他需要给上一个yield位置传值
# 最后一个yield不能使用send()，或者可以最后一个yield不进行传值
