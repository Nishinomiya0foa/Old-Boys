# 基本数据类型
print(1)
print('\'1')
print("'1")
a = '\'1'
b = "'1"

print(a == b)
print(a + b)

print(a * 5)

a = False
if not a:
    print('a is True')


name = input("请输入你的名字 >")
age = input("请输入你的年龄 >")
print('你的文字是'+name+'，你'+age+'岁了')

num = input('请输入您猜的数字：')

if num == '1':
    print('一起抽烟')
elif num == '2':
    print('一起喝酒')
elif num == '3':
    print('新开了一家，走看看')
else:
    print('你猜错了.....')


line = 0
count = 0
while line <= 100:
    count = count + line
    line+=1
print(count)


num = 0
while num < 30:
    num += 1
    if num == 28:
        continue
    print(num)


# 1、使用while循环输入 1 2 3 4 5 6     8 9 10
num = 0
while num <= 9:
    num += 1
    if num == 7:
        continue
    print(num, end=' ')
# 2、求1-100的所有数的和
#
# 3、输出 1-100 内的所有奇数
#
# 4、输出 1-100 内的所有偶数
#
# 5、求1-2+3-4+5 ... 99的所有数的和
a = -1
num = 1
sum = 0
while num < 100:
    sum = sum + num*(-a) # 0+1+
    num += 1
    a = -a
print(sum)

i = 0
sum1 = 0
sum2 = 0
while i<10:
    i = i + 1
    num1 = i%2
    if num1 == 1:
        sum1 = sum1 + i
    else:
        sum2 = sum2 + i
print(sum1-sum2)
# 6、用户登陆（三次机会重试）

id = "thisisid"
pwd = "thisispwd"
num = 0
while num < 3:
    id_user = input('id:')
    id_pwd = input('pwd:')
    if id_user != id or id_pwd != pwd:
        print("密码错误，重新输入机会为{}".format(2-num))
        num += 1
        continue
    else:
        print('密码正确！')




