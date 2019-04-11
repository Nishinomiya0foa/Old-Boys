import pickle


from Student_Manage.conf import conf
from Student_Manage.core import student


def login():
    print("""
    学生管理系统：
    请依次输入用户名和密码：
    """)
    # uid = input('用户名：')
    # pwd = input('密码：')
    with open(conf.users_file, 'rb') as f1:
        users = []
        try:
            while True:
                users.append(pickle.load(f1))
        except EOFError:
            pass
    print(users)

    # users [{'小明': <Student_Manage.core.student.Student object at 0x0000000002882B38>}]
    # for i in range(len(users)):
    #     if uid in users[i] and pwd == str(users[i][uid].pwd):
    #         print("登录成功！欢迎您，{}:{}".format(users[i][uid].identity, users[i][uid].name))
    #         print('以下是您可以进行的操作：')
    #         print('*'*25)
    #         this_user = users[i][uid]
    #         if this_user.identity == '学生':
    #             while True:
    #                 for key in student.Student.dic:
    #                     print(key)
    #                 print('*' * 25)
    #                 operation = input('选择您要进行的操作：')
    #                 getattr(this_user, student.Student.dic[operation])()
    #
    #         elif this_user.identity == '老师':
    #             print(11111111111111)
    #         break


def main():
    login()


if __name__ == '__main__':
    main()
