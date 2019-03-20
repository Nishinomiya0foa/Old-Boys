class School:
    def __init__(self, name, place):
        self.name = name
        self.place = place


class Student:
    def __init__(self, id, pwd, name, school, grade):
        self.id = id
        self.pwd = pwd
        self.name = name
        self.school = school
        self.grade = grade


class Course:
    def __init__(self, name, time, price, school):
        self.name = name
        self.time = time
        self.price = price
        self.school = school


class Teacher:
    def __init__(self, id, pwd, name, school):
        self.id = id
        self.pwd = pwd
        self.name = name
        self.school = school


class Grade:
    def __init__(self, course, teacher):
        self.course = course
        self.teacher = teacher
