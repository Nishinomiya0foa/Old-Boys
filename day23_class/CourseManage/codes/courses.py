class User():
    def __init__(self, id, pwd):
        self.id = id
        self.pwd = pwd

    def login(self):
        pass



class School:
    def __init__(self, name='北大', place='Beijing'):
        self.name = name
        self.place = place


class Student(User):
    def __init__(self, id, pwd, name, school, grade):
        super().__init__(id, pwd)
        self.name = name
        self.school = school
        self.grade = grade

    def watch_courses(self):
        print(self.grade.course)


class Course:
    def __init__(self, name, time, price, school):
        self.name = name
        self.time = time
        self.price = price
        self.school = school


class Teacher(User):
    def __init__(self, id, pwd, name, school):
        super().__init__(id, pwd)
        self.pwd = pwd
        self.name = name
        self.school = school


class Grade:
    def __init__(self, course, teacher):
        self.course = course
        self.teacher = teacher


class Admin(User):
    """创建老师，年级，课程"""
    def __init__(self, id, pwd, name):
        super().__init__(id, pwd)
        self.name = name

    def create_teacher(self):
        print('正在创建老师...\n', '请依次输入老师的school，pwd，name信息')
        print('学校请选择\n1.北大\n2.上大')
        school = input('school:')
        id = input('id:')
        pwd = input('pwd:')
        name = input('name:')



if __name__ == '__main__':
    # 学校
    beida = School('北大', 'Beijing')
    shangda = School('上大', 'Shanghai')

    # 课程
    go = Course('Go', '6 months', 12800, shangda)
    linux = Course('Linux', '3 months', 8800, beida)
    python = Course('Python', '5 months', 15890, beida)

    # 教师
    xiaoming = Teacher(10001, 123123, '小明', beida)
    xiaodong = Teacher(10002, 123123, '小东', shangda)

    # 班级
    erban = Grade(go, xiaodong)
    sanban = Grade(python, xiaoming)

    # 学生
    shubiao = Student(1001, 123123, '鼠标', beida, sanban)
    jianpan = Student(1002, 123123, '键盘', beida, sanban)
    fengshan = Student(2001, 123123, '风扇', shangda, erban)

    # 管理员
    admin1 = Admin(101, 123123, '管理员1')

    print(admin1.name)
    admin1.create_teacher()
