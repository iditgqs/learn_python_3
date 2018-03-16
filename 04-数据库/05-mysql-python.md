## 安装引入模块
	. 安装mysql模块
	sodo apt-get install python-mysqldb
	. 在python中引用模块
	import MySQLdb

## 连接基本结构
	1. from MySQLdb import *
	2. conn = connect(host, port, db, user, passwd, charset)
	3. cursor = conn.cursor()
	4. sql = ""
	5. cursor.execute(sql)
	6. conn.commit()|conn.rollback()
	7. cursor.close() & conn.close()

## sql参数化---->同java的预编译
	params = [name]
	execute(sql, params):sql中用%s点位

## 数据加密 ---> hashlib
	md5
	sha1...
