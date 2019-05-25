import pymysql


# 新增
def insert(tup):
    # 创建数据库连接
    db = pymysql.connect("localhost", "root", "a601583400", "testpy")

    # 获取游标对象
    cur = db.cursor()
    sql = "INSERT INTO company (name, job, salary, location) " \
          "VALUES (%s,%s,%s,%s)"
    cur.executemany(sql, tup)
    # 获取响应行数
    num = cur.rowcount
    # 提交
    db.commit()
    if num > 0:
        print("insert success")
    else:
        print("insert error")
