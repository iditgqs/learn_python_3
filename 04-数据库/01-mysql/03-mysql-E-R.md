# 关系(E-R)
#### 引用主键:第三范式
A 对 B 是一对多,关系字段存在于B表中
1. 外键约束:保证关系的正确性,有效性
```
foreign key(当前表的字段) references students(id)
外键的级联操作:删除外键对应的数据
restrict 不让删除,报错
cascade	一并删除
set null 添加null
no action 什么都不做

# 添加外键
alter table scores add constraint stu_score foreign key(sutid) references students(id)
```
2. 连接查询:join on
```
inner join on	:内连接		---->所有都匹配的才会出现不会前后
left join on	:左连接		---->只要left join 前有就有
right join on	:右连接		---->只要right join 后有就有,但都有inner join 的部分
```
3. 最终编写顺序
```
select distinct ...
from table1 inner|left|right join table2 on 关系(主外)
where 条件...
group by ...
having 条件...
order by ... asc|desc
limit start,count
```
