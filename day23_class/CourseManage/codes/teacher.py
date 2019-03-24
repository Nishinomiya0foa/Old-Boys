class Classes:
    def __init__(self, school, subject, name):
        self.name = name  # 班级名， 例如    初二2班
        self.school = school  # 学校
        self.subject = subject  # 科目
        self.student = ['student_obj']

class Course:
    def __init__(self, name, period, price):
        self.name = name  # 课程名
        self.period = period  # 课程周期
        self.price = price  # 课程价格

class Teacher:
    def __init__(self, name, classes, course):
        self.classes = classes
        self.course = course
        self.name = name
        self.classes = ['classes_obj']
        self.course = Course  # 组合