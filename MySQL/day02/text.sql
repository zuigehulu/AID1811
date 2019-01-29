create database users default charset = utf8;

create table user_table (
    user_id int primary key auto_increment,
    user_name varchar(128),
    user_pd varchar(128),
    user_status enum('1','2','3')
)default charset = utf8;

insert into user_table values
(null,'pansen','p12345','1'),
(null,'manwang','p123456','2'),
(null,'zhaoxin','1234567','3');
