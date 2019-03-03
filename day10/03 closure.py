"""
    闭包  ----嵌套函数，且内部函数调用外部函数的变量
	
	看到了 闭包4分钟
"""
a = 1
def outer():
    a = 2
    def inner():
        nonlocal a
        a = 3

    print(inner.__closure__)  # 如果内部函数的__closure__方法打印了有cell，则该内部函数必为闭包
    inner()
    print(a)
outer()
