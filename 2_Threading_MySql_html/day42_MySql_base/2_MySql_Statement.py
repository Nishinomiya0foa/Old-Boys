"""MySql语句规则

数据库
    创建数据库
        create database <name> default charset utf8;
    删除数据库
        drop database <name>;

数据表
    新建数据表
        create table <table name>(
            列名1 类型 null/not null default <值> ,
                       *是否允许为空    默认值
            列名2 类型 auto_increment primary key
                          自动递增    主键,不能重复且不能为空
        ) engine=innodb default charset utf8;
        支持事务(出错回滚)    设置默认编码
    查看所有表
        show tables;
    清空数据表

        truncate table t1;  # 仅保留列名, 不保留递增
    删除数据表
        drop table t1;

表中内容,增删改查
    查看表中内容
        select <条件> from <表明>;
    删除
        delete from t1 where id<6;   # 保留列名及递增记录
    修改:
        update t1 set age=18;  # 将所有age列改为18
        update t1 set age=18 where name='alex'  # 加上了条件
    新增数据
        insert into <表名>(列名1, 列名2, 列名4) values(value1, value2, value4);

"""

# 外键(一对多)  与另一张表建立的约束关系
#     create table userinfo(
#     uid bigint auto_increment primary key,
#       name varchar(32),
#       department_id int,
#       constraint fk_user_depart foreign key (department_id) references department(id)
#           # 建立外键约束fk_user_depart, 在department_id列   和 department 表中的id列
#     )engine=innodb default charset=utf8;  # 第一张表

#    create table department(
#    id bigint auto_increment primary key,
#    title char(15)
#    )engine=innodb default charset=utf8;  # 第二张表

# 需建立第一张表和第二张表的外键练习

"""

    # 数据类型
        枚举类型
            gender ENUM('male', 'female'),  # 从里边选一个
        集合类型
            score SET('a','b', 'c','d'),  # 从里边选一些.
            例如插入数据时:   insert into t1(score) values('a,c')
        数字:
            整数
            小数
                float
                double
                decimal(总位数, 小数点后位数)
        字符串:
            # sql优化时, 把定长的列放在前面. 变长的放后面
            # 图片 视频等,以文件的形式存好,地址存到服务器
            char(长度,max=255): 自动补位,补满10位(速度快)
            varchar(长度,max=255): 实际数据是多少就占多少位(节省空间,)
            test(max=65535)
        时间类型:
            DATETIME
"""