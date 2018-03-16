# mysql高级部分

1. 查询时的过程
	1. 找出想要的条件，结果
	2. 判断相关关系
	3. 判断是否有分组(出现聚合---->考虑分组,只有聚合不用分组,部分信息考虑分组)

2. 自关联   mysql> source xxx.sql--->导入sql
	1. 自己有自己的外键连接关系

3. 视图----> 对于复杂的查询,不利于维护:解决方法--->定义视图
	
	#### create|alter|drop view xxx as ...

	注意重复字段问题:id...	

```
	# 没有使用视图view
	select * from scores
	inner join students on students.id = scores.stuid
	inner join subjects on subjects.id = scores.subid;

	# 添加到视图view
	create view v_stu_sub_score as
	# select * from scores
	select scores.*,students.name,subjects.title from scores
        inner join students on students.id = scores.stuid
        inner join subjects on subjects.id = scores.subid;
```

4. 事务(ACID)
  1. 原子性

  2. 一致性

  3. 隔离性

  4. 持久性

    当数据被更改时:考虑事务(insert, update, delete)
  ```
  开启	begin;
  提交	commit;
  回滚	rollback;
  ```

5. 索引(index)
  show index from students;

  主键和唯一都是索引
  尽量列为避免null
  where后等值的写在范围前(能不用or别用)

  ```
  create index indexName on students(name(len));
  drop index indexName on students;

  show profiles;  ----> 性能监测工具
  set profiling = 1 --->开启性能监测
  ```

  ​