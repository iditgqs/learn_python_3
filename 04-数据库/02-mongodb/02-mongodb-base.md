## mongodb数据库操作
    db
    show dbs
    use database
    db.dropDatabase()
    db.createCollection(name, options) --->optons:{capped:true, size:10...}
    show collections
    db.stu.drop() -->删除stu集合
## mongodb类型
    Object ID
    String
    Boolean
    Integer
    Double
    Arrays
    Object
    Null
    Timestamp
    Date
### 插入
    db.stu.insert({name:'gqs', gendger:true})

### 简单查询
    db.stu.find()

### 更新
    db.stu.update(
        <query>,
        <update>,
        {multi: <boolean>}
    )
    db.stu.update({}, {$set:{}}, {multi:true})

### 保存
    db.stu.save(document)
    db.stu.save({_id:xxxxxx, name:'gqs', gender:1})

### 删除
    db.stu.remove(
        <query>,
        {
            justOne:<boolean>  ----->是否删除所有
        }
    )
