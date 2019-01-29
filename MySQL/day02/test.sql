create table class(
    cid int primary KEY,
    caption varchar(64)
)default charset = utf8;

insert into class VALUES
(1,'三年级二班'),
(2,'一年级二班'),
(3,'三年级一班');

create table students(
    sid int PRIMARY KEY,
    sname varchar(64),
    gender enum('男','女'),
    class_id int,
    constraint foreign key(class_id)
    references class (cid)
)default charset = utf8;

insert into students VALUES
(1,'段誉','男',1),
(2,'鸠摩智','男',1),
(3,'阿朱','女',2),
(4,'王语嫣','女',3);

create table teacher(
    tid int primary KEY,
    tname varchar(64)
)default charset=utf8;

insert into teacher VALUES
(1,'酒剑仙'),
(2,'李逍遥'),
(3,'赵灵儿'),
(4,'林月如');

create table coures(
    cid int PRIMARY KEY,
    cname VARCHAR(64),
    tearch_id int
)default charset = utf8;

insert into coures VALUES
(1,'御剑术',1),
(2,'醉仙望月步',1),
(3,'飞龙探云手',2),
(4,'天仙下凡',3); 

create table scores(
    sid int,
    student_id INT,
    course_id INT,
    number int,
    constraint foreign key(course_id)
    references coures (cid),
    constraint foreign key(sid)
    references students (sid)
)default charset = utf8;

insert into scores VALUES
(1,1,1,60),
(2,1,2,90),
(3,2,2,59),
(1,2,3,59),
(2,2,1,98),
(4,4,4,100);

2、查询 御剑术比飞龙探云手成绩高的同学的所有学号；
select sid,course_id from scores where number >
(select number from scores where course_id = 3) and course_id = 1;
3、查询 学了御剑术的同学，还学了哪些课程；
select * from coures inner join scores 
on coures.cid =scores.course_id 
where coures.cid = 1;
4、查询平均成绩大于60分的同学的学号；
select * from scores inner join students
on scores.sid = students.sid
where scores.number > 60;
5、查询所有同学的学号、姓名、选课数、总成绩；
select scores.sid,students.sname,sum(scores.number),count(course_id)
from scores inner join students 
on scores.sid  = students.sid
group by scores.sid ;

6、查询姓“李”的老师的个数；
select count(tname) from teacher
where tname like '李%';

7、查询学过“1”并且也学过编号“2”课程的同学的学号、姓名；
select students.sid,students.sname
from students inner join scores
on students.sid = scores.sid
where scores.course_id = 1 or  scores.course_id =2;
8、查询有课程成绩小于60分的同学的学号、姓名；
select students.sid,students.sname
from students inner join scores
on students.sid = scores.sid
where scores.number >60;
9、查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；
select course_id, max(number),min(number)
from scores
group by course_id;
10、查询酒剑仙的所有学生；
select * from teacher inner join coures
on teacher.tid = coures.tearch_id
inner join scores on coures.cid = scores.course_id
inner join students on scores.sid = students.sid
where teacher.tid = 1;

11、检索至少选修两门课程的学生学号；
select sid,count(course_id) '修炼课程数' from scores 
group by sid
having count(course_id) >=2;
12、查询每门课程被选修的学生数；
select count(sid),course_id from scores
group by course_id;
13、查询出只选修了一门课程的全部学生的学号和姓名；st.sname 
select sid,sname from students 
where sid 
in (select sid from scores group by sid having count(course_id)=1);