
"""
    创建连接,创建游标
    关闭游标 关闭连接
    execute()  ---- 防止sql注入
    增删改:conn.commit()
    查: 结果
        fetchone()
        fetchall()
    获取自增id
    
    
    作业:权限管理
        有一张权限表:
            订单管理/用户/菜单/权限分配/BUG管理
        新建用户表:
            用户具有1个或多个权限
        用户和权限关系表
        
        python实现,用户登录后,查看自己拥有的权限

            也可以实现一个基于角色的权限管理,为每个员工分配一个角色(普通职工,主管,领导等),同一角色在分配
            权限.
"""

import pymysql

# 基于用户的
conn = pymysql.connect(host='localhost',user='root',password='123456',database='mytest')
cursor = conn.cursor()


# 模拟登录
def login(user,pwd):
    sql = "select name,pwd from user where name=%s and pwd=%s"
    cursor.execute(sql,(user,pwd))
    # 登录成功
    if cursor.fetchone():
        traverse(user)
    else:
        print('登录失败.')


# 查询权限
def traverse(user):
    print('你的权限有:')
    sql = "SELECT `user`.`name`,permission.permission FROM `user` " \
              "LEFT JOIN ownedpermission ON user.id = ownedpermission.user_id " \
              "LEFT JOIN permission ON ownedpermission.permission_id = permission.id where name=%s"
    cursor.execute(sql,(user,))
    result = cursor.fetchall()
    for i in result:
        print(i[1])


if __name__ == '__main__':
    user = input('user:')
    pwd = input('pwd:')
    login(user,pwd)
    cursor.close()
    conn.close()