# 写出一个登录系统,账号密码在数据库

import pymysql

# 连接数据库
conn = pymysql.connect(host='localhost', user='root', password='123456', database='mytest')  # host user pwd database
# 游标 操作数据
cursor = conn.cursor()

user = '架子'
pwd = '123456'

# 注意防备sql注入
sql = "select * from user where name=%(u)s and  密码=%(p)s"

# cursor.execute(sql,[user,pwd])
cursor.execute(sql,{'u':user,'p':pwd})
#
result = cursor.fetchone()
print(result)

cursor.close()
conn.close()