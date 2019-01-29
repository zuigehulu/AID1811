create database dict default charset =utf8;

create table user (
    uname varchar(128) Primary KEY,
    pword varchar(128) DEFAULT '000000'
)default charset = utf8;

create table dict(
   id int PRIMARY KEY auto_increment,
   word varchar(32) not NULL,
   annotation varchar(256)
)default charset = utf8;

create table record(
    id int PRIMARY KEY auto_increment,
    uname varchar(128) not null,
    word VARCHAR(32) not null,
    time varchar(64)
)default charset = utf8;
insert into