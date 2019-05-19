"""MySql操作补充
            ---- 增删改查

查看设计表
    desc t1;
查看表的创建
    show create table t1;
删除表
    drop table t1;



增:
    增添一条数据:
        insert into t1(name,age) values('花瓶儿', 35);
    增添多条数据:
        insert into t1(name,age) values('香蕉',18),('架子',22);
    将一张表的数据复制到另一张表:
        insert into t1(name,age) select name,age from t2;

删:
    删除整表
        delete from t2;
    条件语句
        delete from t2 where name='花瓶儿' and age=35;

改:
    update t1 set age=33,name='仕女' where id > 33;

查:
    给列名取别名
        select name as '名字',age as '年龄' from t1 where id=7(条件)
    列名处可添加int
        select name,age,11 from t1;
修改:
    添加列:
        alter table 表名 add 列名 类型
    删除列:
        alter table 表名 drop column 列名
    修改列:
        修改类型 alter table 表名 modify column 列名 类型
        修改列名 alter table 表名 原列名 新列名 类型
    添加主键:
        alter table 表名 add primary key(列名)
    删除主键:
        alter table 表名 drop primary key
    添加外键:
        alter table 从表 add constraint 外键名 foreign key 从表(列名) references 主表(主键)
    删除外键:
        alter table 表名 drop foreign key 外键名

其他:
    不等于
        !=  或者 <>    ----两种写法
    区间  in/between
        select * from t1 where id in (1,5,3);  ---- 取id为1,3,5的
        select * from t1 where id in (select id from t2);  ---- 查t2表中的id在t1表中的数据
        select * from t1 where id not in (1,5,3);  ---- 取id不为1,3,5的
        select * from t1 where id between 1 and 5;  ---- 取1到5的值 [1,5]

    通配符 %|_
        where name like 'chen%'  ---- 以chen开头的全部字符
        where name like 'chen_'  ---- 仅匹配chen开头的,后面紧跟一个字符
    限制  limit
        select * from t1 limit 5;  ---- 仅查询前5条
        select * from t1 limit 2,5  ---- 取从第2条开始的后面5条
    排序  order by
        select * from t1 order by id desc;  ---- 按照id从大到小   desc(递减)|asc(递增)
        select * from t1 order by id desc, name asc;  ---- 按照id降序,有重复则按照name升序
            select * from t1 order by id desc limit 10;  ---- 倒序之后再取前10个,即后10条数据
             # 与limit合用时需先排序,在limit,否则报错.
    分组  group by
        select part_id,max(id) from t1 group by part_id;  ---- 按part_id分组显示,有重复的则取id最大的那个
        select part_id,count(id) from t1 group by part_id;  ---- 按part_id分组显示,count(id)显示出id数量,即人数
        count|max|min|sum|avg
            # 对于聚合函数的结果进行二次筛选时,必须使用having
            select part_id,count(id) as count from t1 group by part_id having count(id) > 10;
                ---- 再统计id数量>10的
        select count(*) from t1;  ---- 统计一共有多少条数据
    **连表**
        select * from course, teacher where course.teacher_id = teacher.teacher_id;
            ---- 两张表一起显示
        # left join  ---- left表左边数据全部显示;right则相反
            select * from course left join teacher on course.teacher_id = teacher.teacher_id;
                ---- 效果一样. 推荐使用这种
        # inner join
            ---- 将null的行 隐藏

"""