import pickle

from Student_Manage.core import course, classes, school, student
from Student_Manage.conf import conf

class Teacher:
    def __init__(self, name, pwd, identity, course, classes, school):
        self.name = name
        self.pwd = pwd
        self.identity = identity
        self.course = course
        self.classes = classes
        self.school = school


teacher_wang = Teacher('王老师', 123123, '老师', course.python, classes.class1, school.beida)
teacher_chen = Teacher('陈老师', 123123, '老师', course.python, classes.class1, school.beida)


if __name__ == '__main__':
    print(teacher_chen.identity)
    # with open(conf.users_file, 'ab') as f1:
    #     pickle.dump({teacher_wang.name: teacher_wang}, f1)
    #     pickle.dump({teacher_chen.name: teacher_chen}, f1)
    with open(conf.users_file, 'rb') as f1:
        print(pickle.load(f1))