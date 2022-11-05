import pymysql

conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="123456789",
    db="news",
    charset="utf8"
)

cursor = conn.cursor()
sql = "SELECT * FROM news"
cursor.execute(sql)
data = cursor.fetchall()
result = []
for item in data:
    element = [item[0], item[1], item[2], item[3], item[4], item[5]]
    result.append(element)
print(result[200][5])
