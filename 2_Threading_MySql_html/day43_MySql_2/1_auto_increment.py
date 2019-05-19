"""
desc t1;    查看列属性
show create t1;  查看表设计
自增列
    起始值
        alter table t1 auto_increment=2;
        修改
    步长
        基于会话级别(session),就像每次用户登录
            查看全局变量
                show session variable like 'auto_inc%';
            设置会话步长
                set session auto_increment_increment=2;
        基于全局级别(尽量少用)
            查看全局变量
                show global variable like 'auto_inc%';
            设置会话步长
                set global auto_increment_increment=2;
"""