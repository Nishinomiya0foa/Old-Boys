import pickle

from codes import set
from codes import courses

user = {}
user['id'] = ['']

with open('F:\oldboys_code\Old-Boys\day23_class\CourseManage\db\info', 'wb') as f1:
    bbb = pickle.dumps(set.shubiao)
    f1.write(bbb)

with open('F:\oldboys_code\Old-Boys\day23_class\CourseManage\db\id_pwd', 'w', encoding='utf-8') as f1:
    pass

# for i in courses.Student.grade:
#     print(i)


user_id = 1001
user_pwd = 123123

# if user_id ==

