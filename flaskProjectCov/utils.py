import time
import pymysql
#获取系统时间
def get_sys_time():
    #当前时间
    dt = time.strftime("%Y-%m-%d %X")
    return dt

# 获取数据库连接
def get_coon():
    conn = pymysql.connect(
        host='127.0.0.1',port=3306,
        user='root',password='123456',
        database='cov',charset='utf8'
    )
    cursor = conn.cursor()
    return conn,cursor

# 查询数据库数据
def query(sql,*args):
    conn,cursor = get_coon()
    cursor.execute(sql,args)
    res = cursor.fetchall()
    return res

# 释放数据库
def close(conn,cursor):
    cursor.close()
    conn.close()


# 获取center1
def get_center1():
    # 查询详情表
    sql = "SELECT SUM(confirm)," \
          "(SELECT suspect FROM history ORDER BY ds DESC LIMIT 1)," \
          "SUM(heal)," \
          "SUM(dead)" \
          " FROM details " \
          "WHERE update_time=(SELECT update_time FROM details ORDER BY update_time DESC LIMIT 1);"
    res = query(sql)
    # print(res)
    return res[0]

# 获取center2
def get_center2():
    sql = "SELECT province," \
          "SUM(confirm) " \
          "FROM details " \
          "WHERE update_time=(SELECT update_time FROM details ORDER BY update_time DESC LIMIT 1) " \
          "GROUP BY province "
    res = query(sql)
    # print(res)
    return res

def get_left1():
    sql = 'SELECT ds,confirm,suspect,heal,deal FROM history;' # deal 为数据库中dead，误写
    res = query(sql)
    # print(res)
    return res

def get_left2():
    sql = "SELECT ds,confirm_add,suspect_add From history"
    res = query(sql)
    # print(res)
    return res

def get_right1():
    sql = 'SELECT city,confirm FROM ' \
          '(SELECT city,confirm FROM details ' \
          'WHERE update_time=(SELECT update_time FROM details ORDER BY update_time DESC LIMIT 1) ' \
          'AND province NOT IN ("湖北","北京","上海","天津","重庆") ' \
          'UNION ALL ' \
          'SELECT province AS city, SUM(confirm) AS confirm FROM details ' \
          'WHERE update_time=(SELECT update_time FROM details ORDER BY update_time DESC LIMIT 1) ' \
          'AND province IN ("北京","上海","天津","重庆") GROUP BY province) AS a ' \
          'ORDER BY confirm DESC LIMIT 5'
    res = query(sql)
    # print(res)
    return res

def get_right2():
    sql = "SELECT content From hotsearch ORDER BY id desc"
    res = query(sql)
    print(res)
    return res


if __name__ == "__main__":
    # get_center1()
    # get_center2()
    # get_left1()
    # get_left2()
    # get_right1()
    get_right2()