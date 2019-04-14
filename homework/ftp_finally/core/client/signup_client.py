def signup_client():
    print('请输入账号ID，仅支持字母和数字：')
    user = input('>')
    if user.isalnum():
        pass
    else:
        print('用户名不合法')
        exit(-1)
    print('请输入密码，仅支持字母和数字：')
    pwd = input('>')
    if pwd.isalnum():
        pass
    else:
        print('密码不合法')
        exit(-1)
    return user,pwd