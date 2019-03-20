from codes import set, courses
# 教师
xiaoming = courses.Teacher(10001, 123123, '小明', set.beida)
xiaodong = courses.Teacher(10002, 123123, '小东', set.shangda)

# 班级
erban = courses.Grade(set.go, xiaodong)
sanban = courses.Grade(set.python, xiaoming)

# 学生
shubiao = courses.Student(1001, 123123, '鼠标', set.beida, sanban)
jianpan = courses.Student(1002, 123123, '键盘', set.beida, sanban)
fengshan = courses.Student(2001, 123123, '风扇', set.shangda, erban)

dic = {}
dic.setdefault('shubiao', [shubiao.id, shubiao.pwd, shubiao.name])
dic.setdefault('xiaoming', [xiaoming.id, xiaoming.pwd, xiaoming.name])
print(dic)

def add_teacher(id, pwd, name, school):
    return courses.Teacher(id, pwd, name, school)

xiaobei = add_teacher(10003, 123123, '小北', set.shangda)
print(xiaobei.school.name)

