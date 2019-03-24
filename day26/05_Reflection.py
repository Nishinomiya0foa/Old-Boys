"""反射机制"""
# hasattr  判断是否有
# getattr  没有则报错
# delattr
class Teacher:
    dic = {'查看学生信息': 'show_teacher', '查看课程信息': 'show_course'}

    def show_teacher(self):
        print('show_teacher')

    def show_course(self):
        print('show_course')

    @classmethod
    def cls_func(cls):
        print('cls_func')

# 类.属性
# ret = getattr(Teacher, 'dic')  # getattr(cls, obj)  将cls类中的obj属性取出， 赋值给ret
# print(ret)
#
# chen = Teacher()
# print(getattr(chen, 'dic'))  # 实例也可以有getattr
#
# # 类.方法
# ret2 = getattr(Teacher, 'cls_func')  # getattr(cls, func) 将cls类中的func方法取出，赋值给ret2
# ret2()

# 作业可以用到反射。
chen = Teacher()
for key in Teacher.dic:
    print(key)

operation = input('输入操作:')
if hasattr(chen, Teacher.dic[operation]):
    getattr(chen, Teacher.dic[operation])()
