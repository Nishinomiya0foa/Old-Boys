from Student_Manage.core import course,classes

class School:
    def __init__(self, name, place, course, classes):
        self.name = name
        self.place = place
        self.course = course
        self.classes = classes


beida = School('北京大学', '北京', course.python, classes.class1)

