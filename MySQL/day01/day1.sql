-- day1.sql
-- MySQL 第一天使用的SQL语句
-- 创建表acct(账户)
create table acct1(
    acct_nu varchar(32) key ,
    acct_name varchar(128)
)default charset=utf8;

create table acct(
    acct_no varchar(32)  key, default = 'kong',
    acct_name varchar(128)
)default charset=utf8;

-- 重新创建
create table acct1(
    acct_no varchar(32),  -- 账号，字符串　３２字节
    acct_name varchar(128), -- 户名，１２８字节
    cust_no varchar(32),  -- 客户编号
    acct_type int,    -- 账户类型，整数型
    reg_date date, -- 开户日期，日期类型
    status int,      -- 账户状态，整数型
    balance decimal(16,2) -- 数字类型　最长１６位，２位小数 
)default charset=utf8;

-- 插入
insert into acct
values('622345000001','Jerry','C0001',
        1,now(),1,1000.00);

-- 插入多笔数据
insert into acct values
('622345000002','Tom','C0002',1,now(),1,2000.00),
('622345000003','Dekie','C0003',1,now(),1,3000.00),
('622345000004','Bob','C0004',1,now(),1,5000.00),
('622345000005','Jos','C0005',1,now(),1,4000.00);

--指定字段插入
insert into acct(acct_no,acct_name)
values('622345000006','Emma');
-- 查询
select * from acct;
-- 指定查询
select acct_no,acct_name,balance from acct;

-- 查询指定字段，并且位字段起别名
select acct_no "账号",
       acct_name "户名",
       balance as "余额"
from acct;

--
-- 查询时，利用字段值进行计算
select acct_no "账号",
       acct_name "户名",
       balance/10000 as "余额(万元)"
from acct;

-- 带条件的查询
select * from acct where acct_no = '622345000002'
-- 带两个条件的查询，两个条件同时满足
select * from acct where 
acct_no = '622345000002'
and acct_name = 'Bob';

-- 带两个条件的查询，两个条件满足一个
select * from acct where 
acct_no = '622345000002'
or acct_name = 'Bob';

create table tmp(
    acct_no char(10),
    acct_name varchar(32)
);

insert into tmp values
('0001','Jerry'),
('0002','Lucky'),
('0003','Tom');

-- enum,set类型
create table enum_test(
    name varchar(32),
    sex enum('boy','girl'),  -- 从二者选一
    course set('music','dance','paint') 
);
-- 在枚举范围内，可以插入
insert into enum_test
values('Jerry','girl','music,dance');

-- 在枚举范围之外，插入报错
insert into enum_test
values('Jerry','girl','music,dance，football');
