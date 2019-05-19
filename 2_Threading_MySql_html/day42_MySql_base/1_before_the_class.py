"""
MySQL：是用于管理文件的一个软件
-服务端软件
    -socket服务端
    -本地文件操作
    -解析指令【so语句】
-客户端软件（各种各样）
    -socket客户端
    -发送指令
    -解析指令【sQL语句】
PS：
    -DBMS数据库管理系统
    -sQl语句
技能：
    -安装服务端和客户端
    -连接
    -学习sQL语句规则；指示服务端做任意操作

    非关系型: redis, mongodb



连接:
    默认: root 123456
    创建用户:
        create user 'xiaochen'@'localhost' identified by '123456'
    授权:
        grant 权限  给人
        grant select,insert,update on mytest.* to 'xiaochen'@'localhost'
        grant all privileges(除grant之外的所有权限) on mytest.* to 'xiaochen'@'localhost'

"""