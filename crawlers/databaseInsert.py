import pymysql


# 使用pymysql库写入数据库
def insertToDatabase(defaultList = []):
    # 建立数据库连接
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='123456789',
        port=3306,
        db='news'
    )
    # 初始化数据库游标
    cur = db.cursor()
    # SQL插入语句
    sql = 'INSERT INTO news values (%s, %s, %s, %s, %s, %s)'
    for item in defaultList:
        if len(item[1])>1 and len(item[4])>1:
            row_counst = cur.execute(sql, item)
    # row_counst = cur.execute(sql, defaultList)
    # 提交更改
    db.commit()
    # 关闭游标
    cur.close()
    # 关闭连接
    db.close()


