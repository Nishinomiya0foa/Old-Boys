num = 0
while num < 3:
    id_user = input('id:')
    id_pwd = input('pwd:')
    if id_user != "thisisid" or id_pwd != "thisispwd":
        print("密码错误，重新输入机会为{}".format(2-num))
        num += 1
        continue
    else:
        print('密码正确！')
        break
