from codes import courses

# 学校
beida = courses.School('北大', 'Beijing')
shangda = courses.School('上大', 'Shanghai')

# 课程
go = courses.Course('Go', '6 months', 12800, shangda)
linux = courses.Course('Linux', '3 months', 8800, beida)
python = courses.Course('Python', '5 months', 15890, beida)






