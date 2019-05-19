import pymysql


conn = pymysql.connect(host='localhost', user='root', password='123456', database='mytest')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 参数 cursor=pymysql.cursors.DictCursor, 则fetch返回值为字典
sql = "select * from user;"

# 有返回值, 为受影响的函数
r = cursor.execute(sql)
print(r)

# 执行多句;
# cursor.executemany(sql,[(),(),()])

# cursor.lastrowid  # 返回刚刚插入的一条数据的自增id

# 提交更改,当涉及修改其中的值的时候; 增/删/改
# conn.commit()

# 查
# 如果在建立游标时,指定参数cursor=pymysql.cursors.DictCursor,则返回的结果为字典类型或 多个结果时列表中嵌套了多个字典
# result = cursor.fetchone()  # 获取一条结果,元组类型
# result = cursor.fetchmany(num)  # 获取n条结果,用的比较少,n被控制在sql语句中了
result = cursor.fetchall()  # 获取全部结果,元组类型,嵌套元组

# fetch时可调整游标指针位置,类似文件里的seek()
# cursor.scroll(1,mode='relative')  # 相对当前位置移动
# cursor.scroll(2,mode='absolute') # 相对绝对位置移动

print(result)
cursor.close()
conn.close()