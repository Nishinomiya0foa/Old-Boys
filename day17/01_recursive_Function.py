"""递归函数"""

# 在函数中调用自身函数

# 如果递归函数不能结束递归，会报错：超过递归最大深度默认998次，目的保护内存

# 如果递归算法需要递归太多次，那么就不适合用递归了

# 缺点  ---- 占内存
# 优点  ---- 简洁

# 例子
def recu(n):
    if n == 4:
        return 40
    elif n>0 and n<4:
        return recu(n+1) + 2    # 如果n满足这个elif条件，进到return时，只会执行到recu(n+1)，就会继续进行recu()函数的调用了
                                # 而不会执行return，或者后面的+2
                                # 后续，返回时会再依次返回