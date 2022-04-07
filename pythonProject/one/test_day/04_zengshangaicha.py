import pymysql
import utils

# 查询方法
def query():
    conn, cursor = utils.get_conn()
    sql = 'select * from admin'
    cursor.execute(sql)
    content = cursor.fetchall()
    print(content)
    # 释放资源
    utils.close(conn,cursor)
# 插入数据
def insert():
    conn, cursor = utils.get_conn()
    sql = 'insert into admin values(7,"22","22","22","22","22",1,13,13);'
    cursor.execute(sql)
    # 提交事务
    conn.commit()
    utils.close(conn, cursor)

# 更新数据
def update():
    conn, cursor = utils.get_conn()
    sql = 'update admin set name="L" where aid=6'
    cursor.execute(sql)
    conn.commit()
    utils.close(conn,cursor)
# 删除
def delete():
    conn, cursor = utils.get_conn()
    sql = 'delete from admin where aid=7'
    cursor.execute(sql)
    conn.commit()
    utils.close(conn,cursor)

if __name__ == "__main__":
    # query()
    # insert()
    # update()
    # delete()
    query()


