"""
    函数名  ----本质上也只是存在内存地址中的一个变量

    闭包  ----嵌套函数，且内部函数调用外部函数的变量
        ：内部函数包含对外部作用域而非全局作用域名字的引用，该内部函数称为闭包函数

    闭包的调用  ----可以在全局使用一个内部的函数，方法是把这个内部函数的函数名返回
a = 1
def outer():
    a = 2
    def inner():
        nonlocal a
        a = 3
    print(inner.__closure__)  # 如果内部函数的__closure__方法打印了有cell，则该内部函数必为闭包
    print(a)
    return inner  # 返回了内部函数名。外部就可用这个内部函数。任何时候都可用
inn = outer()
inn()

    闭包的好处  ----延长函数内变量等的生存周期

"""
# a = 1
# def outer():
#     a = 2
#     def inner():
#         nonlocal a
#         a = 3
#     print(inner.__closure__)  # 如果内部函数的__closure__方法打印了有cell，则该内部函数必为闭包
#     print(a)
#     return inner  # 返回了内部函数名。外部就可用这个内部函数。任何时候都可用
#
# inn = outer()
# inn()

# import urllib
# from urllib.request import urlopen
# def get_url():
#     url = 'https://www.bilibili.com/'
#     def get_url_inner():
#         ret = urlopen(url).read()
#         ret = ret.decode('utf-8')
#         print(ret)
#     return get_url_inner
#
# get_url_inner = get_url()
# get_url_inner()