# -*- coding:utf-8 -*-

from MySQLdb import *
from hashlib import sha1
from MysqlHelper import MysqlHelper


def main():
    name = raw_input("please input youer name:")
    password = raw_input("please input youer password:")

    mysql = MysqlHelper("localhost", 3306, "python3", "root", "gqs123")
    mysql.open()

    # 判断用户是否存在
    sql = "select passwd from users where name = %s"
    params = [name]
    result = mysql.all(sql, params)
    if len(result) == 0:
        print("用户不存在...")
    else:
        # sha1加密
        jm = sha1()
        jm.update(password)
        if result[0][0] == jm.hexdigest():
            print("登录成功...")
        else:
            print("密码错误...")

    mysql.close()


if __name__ == "__main__":
    print("_______________________-")

    main()