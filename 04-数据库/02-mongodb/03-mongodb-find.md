## mongodb 查询
    find({条件}, {投影:要显示的字段1 or 0})  ----->括号中是查询条件和投影
    findOne()
    find().pretty() --->格式化

#### 查询条件
##### 比较运算符

    默认就是等于
    $lt     --->小于
    $gt     --->大于
    $lte    --->小于等于
    $gte    --->大于等于
    $ne     --->不等于
    
    {count:{$gt:5}} ---->count大于5的

##### 逻辑运算符

    默认是逻辑与
    db.stu.find({age:{$gte:18},gender:1}) -->age大于等于18 and gender等于1
    $or -->$or:[{k:v,k:v}]  -->数组中的json就是or

##### 范围运算符
    $in -->{age:{$in[18,29]}} :18or29
    $nin

##### 正则表达式
    // or $regex
    db.stu.find({name:/^黄/})
    db.stu.find({name:{$regex:'^黄'}}})

##### 自定义查询
    db.stu.find({$where:function(){return this.age>20}})

##### limit skip
	db.stu.find().skip(num).limit(num)  ---->start,count

##### 投影
	find({},{name:1, age:0})  ---> name显示,age不显示

##### 排序
	db.stu.find().sort({age:1, gender:-1})  --->1升序,-1降序

##### 统计个数
	db.stu.find().count() or db.stu.count({条件})

##### 消除重复
	db.stu.distinct('字段',{条件})