# -*- coding:utf-8 -*-

from MySQLdb import *
from hashlib import sha1
from MysqlHelper import MysqlHelper


def main():
    name = raw_input("please input youer user name:")
    passwd = raw_input("please input youer password:")

    mysql = MysqlHelper("localhost", 3306, "python3", "root", "gqs123")
    mysql.open()

    # 判断用户名是否存在
    select_sql = "select * from users where name = %s"
    select_params = [name]
    result = mysql.all(select_sql, select_params)

    # 如是空元组
    if len(result) == 0:
        sql = "insert into users(name, passwd) values(%s, %s)"
        jm = sha1()
        jm.update(passwd)
        passwd = jm.hexdigest()
        params = [name, passwd]
        mysql.cud(sql, params)
    else:
        print("用户名已存在...")

    mysql.close()


if __name__ == "__main__":
    print("______________________-")
    main()

