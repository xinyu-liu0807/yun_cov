import pymysql

conn = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="123456",database="books",charset="utf8")

if conn == None:
    print("connection fail")
else:
    print("connection success")

# 查询数据 使用cursor 游标
cursor = conn.cursor()
sql = 'select * from admin'
print(cursor.execute(sql))
# 查询具体内容 （元组形式）
content = cursor.fetchall()
print(content)


