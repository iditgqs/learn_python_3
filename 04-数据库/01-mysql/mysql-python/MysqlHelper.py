# -*- coding:utf-8 -*-

from MySQLdb import *

class MysqlHelper(object):

    def __init__(self, host, port, db, user, passwd, charset="utf8"):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset

    def open(self):
        self.conn = connect(host=self.host, port=self.port, db=self.db, user=self.user, passwd=self.passwd,charset=self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def cud(self, sql, params=[]):
        try:
            # self.open()
            self.cursor.execute(sql, params)
            self.conn.commit()
            # self.close()
            print("OK")
        except Exception,e:
            print(e.message)

    def all(self, sql, params=[]):
        try:
            # self.open()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchall()
            # self.close()
            return result
        except Exception,e:
            print(e.message)


if __name__ == "__main__":
    mysql = MysqlHelper("localhost", 3306, "python3", "root", "gqs123")
    mysql.open()

    # name = raw_input("input student name:")
    # id = raw_input("input studend id:")

    # sql = "update students set name = %s where id = %s"
    # params = [name, id]
    # mysql.cud(sql, params)

    select_sql = "select * from students"
    result = mysql.all(select_sql)
    for stu in result:
        print(stu)

    mysql.close()