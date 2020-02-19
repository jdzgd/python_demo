# coding=utf-8
import pymysql as mdb
import pymysql.cursors

try:
    # cursor(): 创建游标对象
    # fetchone(): 得到结果集的下一行
    # fetchmany([size = cursor.arraysize]):得到结果集的下几行
    # fetchall(): 得到结果集中剩下的所有行
    # excute(sql[, args]): 执行一个数据库查询或命令
    # executemany(sql, args): 执行多个数据库查询或命令

    con = mdb.connect(user="root", passwd="123456", db="fish", host="127.0.0.1", charset="utf8mb4")
    cur = con.cursor()
    count = cur.execute("select * from f_user;")
    print('计算总条数:', count)

    row = cur.fetchone()
    print('单行数据: ', row)

    i = 1
    for row in cur.fetchall():
        print('遍历获取数据,序号: ', i, row)
        i = i + 1

    cur.close()
    con.close()
except mdb.err as e:
    print("Error %d: %s" % (e.args[0], e.args[1]))
