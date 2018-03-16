# -*- coding:utf-8 -*-

from MySQLdb import *

try:
    # name = raw_input("input student name:")

    conn = connect(host="localhost", port=3306, db="python3", user="root", passwd="gqs123", charset="utf8")
    cursor_1 = conn.cursor()

    # sql = "insert into students(name) values('python2')"
    # sql = "insert into students(name) values(%s)"
    sql = "select * from students"
    cursor_1.execute(sql)
    lists = cursor_1.fetchall()
    for student in lists:
            print(student)

    conn.commit()

    cursor_1.close()
    conn.close()

except Exception, e:

    print(e.message)