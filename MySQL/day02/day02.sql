create table acct(
    acct_nu varchar(32),
    acct_name varchar(128)
)default charset=utf8;

create table acct(
    acct_no varchar(32),  -- 账号，字符串　３２字节
    acct_name varchar(128), -- 户名，１２８字节
    cust_no varchar(32),   -- 客户编号
    acct_type int,    -- 账户类型，整数型
    reg_date date, -- 开户日期，日期类型
    status int,      -- 账户状态，整数型
    balance decimal(16,2) -- 数字类型 最长１６位，２位小数    
)default charset=utf8;

selec
insert into acct(acct_name,acct_no) values
('Sesa','622345000007')

作业:
1. 创建库eshop,并制定编码为utf8
2. 创建订单表（orders,utf8编码），包含如下字段：
   Order_id  订单编码，字符串，32字节
   Cust_id   客户编号，字符串，32字节
   Order_date 下单时间，DateTime类型
   Status   订单状态，枚举类型取值范围(‘1’,’2’,’3’,’4’,’5’,’6’,’9’) 1-待付款 2-待发货 3-已发货 4-已收货 5-申请退货 6-已退货 9-已废弃
    Products_num  订单包含的商品数量
    Amt  订单总金额，浮点数，两位小数

create table orders(
    order_id varchar(32),
    cust_id varchar(32),
    order_date datetime,
    status enum('1','2','3','4','5','6','9'),
    products_num int,
    amt decimal(8,2)
)default charset=utf8;
3.至少插入5笔数据（要求数据看上去尽量真实）
insert into orders values
('2018120300001','C00001',str_to_date('2018-12-03 9:55:12','%Y-%m-%d %H:%i:%s'),'1',4,2000),
('2018120300002','C00001',str_to_date('2018-12-03 9:55:12','%Y-%m-%d %H:%i:%s'),'2',4,2000),
('2018120600001','C00003',str_to_date('2018-12-06 9:55:12','%Y-%m-%d %H:%i:%s'),'3',2,1000),
('2018121500001','C00005',str_to_date('2018-12-15 9:55:12','%Y-%m-%d %H:%i:%s'),'4',6,6000),
('2018121600001','C00004',str_to_date('2018-12-16 9:55:12','%Y-%m-%d %H:%i:%s'),'5',4,2000),
('2018121700001','C00004',str_to_date('2018-12-17 9:55:12','%Y-%m-%d %H:%i:%s'),'6',4,2000),
('2018121900001','C00006',str_to_date('2018-12-19 9:55:12','%Y-%m-%d %H:%i:%s'),'9',4,2000),
('2018122000001','C00006',str_to_date('2018-12-20 9:55:12','%Y-%m-%d %H:%i:%s'),'3',4,2000),
('2018123000001','C00007',str_to_date('2018-12-30 9:55:12','%Y-%m-%d %H:%i:%s'),'1',4,2000);

4.编写如下SQLyuju 
   1) 查找所有待付款订单
   select * from orders where status = '1';
   2）查找所有已发货、已收货、申请退货订单 3.4.5
   select * from orders where status = '3' or status = '4' or status = '5';
   select * from orders where status between 3 and 5 order by status desc;
   3）查找某个客户的待发货订单 2
   select status '待发订单' , cust_id '客户名称' from orders 
   group by cust_id,status having status = '2' and cust_id = 'C00001';

   select status,cust_id from orders where cust_id = 'C00001' and status = 2;
   4）根据订单编号，查找订单下单日期、订单状态
   select order_date,status from orders where order_id = '2018120300001';
   5）查找某个客户所有订单，并按照下单时间倒序排序
   select * from orders where cust_id = 'C00004' order by order_date desc;
   6） 统计每种状态的订单数量
   select count(*) ,status from orders group by status;
   7） 查询单笔订单最大值、最小值、平均值，所有订单总金额
   select max(amt),min(amt),avg(amt),sum(amt) from orders;
   8）查询金额最大的前3笔订单
select * from orders order by amt desc limit 3;
   9）在表的最后，添加两个字段：
       Invoice  开票状态 整数
       Invoice_date 开票日期，datetime
    alter table orders add invoice int;
    alter table orders add invoice_date datetime;
   10）修改某个订单状态为’已收货’
   update orders set status = '4' where order_id = '2018122000001'
   11) 删除已废弃的订单  9
   delete from orders where status = '9';

create table account(
    order_no varchar(32) primary key,
    order_id varchar(32),
    constraint foreign key (order_id)
    references comter(order_id)
)default charset=utf8;

insert into comter VALUES
('12345','123456','1234567'),
('23456','234567','2345678');
insert into account values
('123456','12345678');

create table ai_test(
    tset_id int primary key auto_increment,
    tset_name varchar(64)
)default charset=utf8;

insert into ai_test VALUES
(null,'1234'),
(null,'2345');

create table acct_trans_detail(
    trans_sn varchar(32) not null, -- 交易流水号
    trans_date datetime not null,  -- 交易时间
    acct_no varchar(32) not null,  -- 交易账号
    trans_type int,                 -- 交易类型 存款　取款　刷卡　结息
    amt decimal(16,2),              -- 交易金额
    unique(trans_sn),  -- 在trans_sn上创建唯一索引
    index(trans_date)  -- 在trans_date上建立普通索引
);

create table acct_trans_detail(
    trans_sn varchar(32) not null,
    trans_date datetime not null,
    acct_no varchar(32) not null,
    trans_type int,
    amt decimal(16,2),
    unique(trans_sn),
    index(trans_date)
)default charset = utf8;

create table acct_trans_detail1(
    trans_sn varchar(32) not null,
    trans_date datetime not null,
    acct_no varchar(32) not null,
    trans_type int,
    amt decimal(16,2),
    unique liushuihao (trans_sn),
    index jiaoyishijian (trans_date)
)default charset = utf8;

insert into acct_trans_detail1 values
("1234",now(),'qwe',12,30),
("2345",str_to_date("2018-12-14 17:25:20","%Y-%m-%d %H:%i:%s"),'qwer',14,33);

SELECT * FROM xxx FORCE INDEX yyy WHERE zzz,
select * from xxx force index yyy where zzz,
select * from acct_trans_detail1 force index trans_sn where liushuihao = '1234';

select * from acct
into outfile '/var/lib/mysql-files/acct.bak'
fields terminated by ','
lines terminated by '\n';

show variables like'secure_file%';
 /var/lib/mysql-files/

load data infile '/var/lib/mysql-files/acct.bak'
into table acct
fields terminated by ','
lines terminated by '\n';

1.修改order表结构
  1）在order_id列上添加主键约束
  alter table orders modify order_id varchar(32) primary key;
  2）在cust_id,order_date,products_num 字段上添加非空约束
  alter table orders modify cust_id varchar(32) not null;
  alter table orders modify order_date datetime not null;
  alter table orders modify products_num int not null;
  3）在status字段上添加默认值，默认值为1
  alter table orders modify status enum('1','2','3','4','5','6','9') default 1;
  4）在order_date上添加普通索引
  create index order_date on orders(order_date);
  alter table orders add index order_date(order_date);
2.创建客户信息表，包含字段有
  Cust_id   客户编号，字符串，32位，主键
  Cust_tel  客户电话，字符串，32位，非空
  Cust_name 客户姓名，字符串，64位，非空
  Address 送货地址，字符串，128位，非空
  create table customers(
     cust_id varchar(32) primary key,
     cust_tel varchar(32) not NULL,
     cust_name varchar(64) not null,
     address varchar(128) not null
  )default charset=utf8;
3.为customers表添加数据，要求每个orders表中的cust_id都有对应的客户信息
insert into customers VALUES
('C00001','134567892','王磊','北极'),
('C00003','188567892','张鹏','北京'),
('C00004','133567892','韩飞','上海'),
('C00005','130567892','刘洋','东莞'),
('C00006','139567892','戈荣','山东'),
('C00007','189567892','王强','山西');

4.在orders表的cust_id上创建外键约束，参照customers表的cust_id字段
alter table orders add 
constraint foreign key (cust_id)
references customers(cust_id);

constraint foreign key(cust_no)
    references customer(cust_no)

create table ase(
    ased varchar(32)
    );

select * from orders where cust_id in 
(select cust_id from customers);

select * from customers where cust_id in 
(select distinct cust_id from orders);

select * from orders where amt >= 
(select avg(amt) from orders);

select * from orders,customers where orders.cust_id = customers.cust_id;

select * from orders inner join customers on orders.cust_id = customers.cust_id;

select * from orders left join customers on orders.cust_id = customers.cust_id;

select * from orders right join customers on orders.cust_id = customers.cust_id where orders.cust_id = 'C00001';

grent all privilegs on *.*
to 'Tom'@%

start transaction;

select * from customers;
Status   订单状态，枚举类型取值范围(‘1’,’2’,’3’,’4’,’5’,’6’,’9’) 1-待付款 2-待发货 3-已发货 4-已收货 5-申请退货 6-已退货 9-已废弃
Order_id  订单编码，字符串，32字节
   Cust_id   客户编号，字符串，32字节
   Order_date 下单时间，DateTime类型
练习：
使用eshop库，完成如下操作
1.	利用子查询，查询所有订单状态为‘申请退货’的客户名称、电话号码
select cust_name,cust_tel,cust_id from customers where cust_id in 
(select cust_id from orders where status = '5');
2.	利用链接查询，查询‘待发货’订单信息
查询字段包括：订单编号、下单时间、客户编号、客户电话、送货电话
select o.order_id,c.cust_id, c.cust_tel,c.cust_name,o.order_date
from orders o inner join customers c 
on o.cust_id = c.cust_id
where o.status = '2';
3．创建eshop_admin 用户，并授权：
   1）eshop库里的所有表、所有权限
   2）允许任意客户端登录
   3）设置密码
   Grant all privileges on *.*
        To ‘Danie’@’%’
        Identified by ‘123456’
        With grant option;
         [identified by ‘密码’]
        [with grant option]


grant all privileges on eshop.*
to "eshop_admin"@'%'
identified by '123456'
with grant option;
4.创建eshop_user 用户，并授权
   1）eshop库中所有表查询权限
   2）允许任意客户端登录
   3）设置密码
grant select on eshop.*
to 'eshop_user'@'%'
identified by '123456'
with grant option;
