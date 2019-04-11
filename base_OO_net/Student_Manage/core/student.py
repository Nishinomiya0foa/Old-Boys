import pickle

from Student_Manage.core import school,classes,course
from Student_Manage.conf import conf

class Student:
    """登录后可以查看课程和班级"""
    dic = {
        '查看课程': 'show_course',
        '查看班级': 'show_classes',
    }

    def __init__(self, name, pwd, identity, school, classes, course):
        self.name = name
        self.pwd = pwd
        self.identity = identity
        self.school = school
        self.classes = classes
        self.course = course

    def show_course(self):
        print('您的课程是：{}'.format(self.course.name))

    def show_classes(self):
        print('您的班级是：{}'.format(self.classes.name))


xiaoming = Student('小明', 123123, '学生', school.beida, classes.class1, course.python)
xiaohong = Student('小红', 123123, '学生', school.beida, classes.class1, course.python)



if __name__ == '__main__':
    xiaoming.show_classes()
    # with open(conf.users_file, 'wb') as f1:
    #     pickle.dump({xiaoming.name:xiaoming}, f1)
    #     pickle.dump({xiaohong.name:xiaohong}, f1)
    with open(conf.users_file, 'rb') as f1:
        print(pickle.load(f1))
        print(pickle.load(f1))
        print(pickle.load(f1))


