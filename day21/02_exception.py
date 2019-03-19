"""
异常处理

错误分为语法错误和逻辑错误。 错误异常针对逻辑错误

程序一旦发生错误，就从错误的位置停下，不再执行后续内容。
异常处理可以使我们能够处理了这个异常，并接着执行后续程序。

结构：  ---- 捕捉到一个异常后,try中的代码就不会接着执行了
        ---- 尽量对小段完整逻辑的代码进行异常捕捉

try:
    code    ---- 可能会有异常的代码
except ERROR_TYPE1 as E1:  ---- ERROR_TYPE为错误类型，需要被捕捉; 对捕捉到的错误进行命名E1，后续可以打印E1，或进行其他操作
    do_sth
except ERROR_TYPE2:  ---- 捕捉ERROR_TYPE2
    do_other
else:       ---- 如果try中无异常，则会执行else中代码
    do_one_thing
finally:    ---- 无论try中有无异常，都会执行finally，做收尾工作
            ---- 存放无论如何都要执行的重要代码
            ---- 即使try中return了，finally中的代码依然会执行！多用在函数里
    do_last_thing

except Exception  ---- 万能异常捕捉.啥异常都捕捉
                    ----  如果需要多个分支捕捉异常,Exception应该是最后一个分支
即使有万能异常捕捉,也需要特定的异常类型捕捉,这样方便调试.


"""
# user_input_num = int(input('>'))  # 如果此时输入的不是数字，程序报错 exit(1)
# print(user_input_num*'*')

try:    # 关键字，开始执行一段程序
    user_input_num = int(input('>'))
    print(user_input_num * '*')
except ValueError:      # 捕捉异常。 这里捕捉的是ValueError异常。 如果有ValueError，才会执行其中的代码
    print('请输入一个数字')
except IndexError:
    print('索引错误')
else:
    print("No Error")
finally:
    print('关闭文件')
print('Hello World')