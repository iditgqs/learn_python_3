# mysql 查询
## distinct ----> 比较所有行

## where 条件:
    =, >, <, >=, <=, != | <> 
    and or not
    like '%%' or '__'
    in 表示在一个非连续的范围内(3,4,5)
    between...and...表示一个连续的范围内3~8
    is null
    is not null
    () ,

## 聚合:统计
count(*)     --------> 总共行
max(列|字段)    
min(列|字段)
sum(列|字段)
avg(列|字段)
 ---与子查询---
    where id = (select max(id) from students)

## 分组:为了聚合---->统计
select 列1|字段1,列2|字段2.... ,聚合 from students group by 列1|字段1,列2|字段2....

having 列1|字段1的条件..聚合... ------>筛选分组的结果集

## 排序
order by 列1|字段2 asc|desc,列2|字段2 asc|desc,....(如果相同就看下一个)

## 分页
limit start,count  ----> limit (n-1)*m,m

## 编写顺序
select discinct ...
from students
where ...
group by ....having...
order by ....
limit start, count

## 执行顺序
from students
where ...
group by ....
select distinct ...
having ...
order by ...
limit start, count
