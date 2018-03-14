# mysql

概念:数据库,表,行,字段,E-R模型,三范式
完整性:字段的类型,约束

## 表的相关操作
```
create database students charset=utf8;
show databases;
use table;
show tables;
select database();
create table students(
id int auto_increment primary key not null,
name varchar(10) not null,
birthday datatime,
gender bit default 1,
isDelete bit default 0
);

alter table students add | change | drop 字段 类型;
drop table students;
rename table students to stu;
show create talbe students;
desc 表名;
```

## 表中相关数据操作
```
select * from students;
insert into students values(null, "gqs","1990-01-10", 1, 0 );
insert into students(name, gender, birthday) values ('th', 0, '1910-9-9');
insert into students() values(),()...   ---------> mysql独有
update students set name='',,, where 条件;
delete from students where 条件; -------> 物理删除
update students set idDelete = 1 where 条件; ------>逻辑删除
```
## mysql数据备份与恢复
1. sudo -s
2. cd /var/lib/mysql
3. mysqldump -uroot -p 数据库名 > userDir/bak.sql

1. mysql -uroot -p
2. create database py charset=utf8;
3. mysql -uroot -p py < userDir/bak.sql
