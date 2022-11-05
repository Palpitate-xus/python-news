from operator import ne
from re import T
import jieba
import jieba.analyse
from collections import Counter
import pymysql
import time

date = time.strftime('%Y%m%d',time.localtime(time.time()))

def count_from_str(content, top_limit=0):
        if top_limit <= 0:
            top_limit = 100
        tags = jieba.analyse.extract_tags(content, topK=100)

        words = jieba.cut(content)
        counter = Counter()
        for word in words:
            if word in tags:
                counter[word] += 1

        return counter.most_common(top_limit)

if __name__ == '__main__':
    db = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="123456789",
        db="news",
        charset="utf8"
    )

    cursor = db.cursor()
    sql = "SELECT * FROM news"
    cursor.execute(sql)
    data = cursor.fetchall()
    result = []
    huanqiu = ""
    netease = ""
    papernews = ""
    peopledaily = ""
    sohu = ""
    Tencent = ""
    for item in data:
        if str(item[3]) == date:
            if item[2] == "People Daily":
                peopledaily+=item[5]
            elif item[2] == "huanqiu":
                huanqiu+=item[5]
            elif item[2] == "Netease":
                netease+=item[5]
            elif item[2] == "sohu":
                sohu+=item[5]
            elif item[2] == "Tencent":
                Tencent+=item[5]
            elif item[2] == "papernews":
                papernews+=item[5]
    pd_result = count_from_str(peopledaily, top_limit=100)
    hq_result = count_from_str(huanqiu, top_limit=100)
    ne_result = count_from_str(netease, top_limit=100)
    sh_result = count_from_str(sohu, top_limit=100)
    tc_result = count_from_str(Tencent, top_limit=100)
    pn_result = count_from_str(papernews, top_limit=100)
    dataList = [
        [date+"1", "peopledaily", date, str(pd_result)],
        [date+"2", "huanqiu", date, str(hq_result)],
        [date+"3", "netease", date, str(ne_result)],
        [date+"4", "sohu", date, str(sh_result)],
        [date+"5", "Tencent", date, str(tc_result)],
        [date+"6", "papernews", date, str(pn_result)],
    ]
    # SQL插入语句
    sql = 'INSERT INTO frequency values (%s, %s, %s, %s)'
    for item in dataList:
        row_counst = cursor.execute(sql, item)
    # row_counst = cur.execute(sql, defaultList)
    # 提交更改
    db.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    db.close()

    print(pd_result, hq_result, ne_result, sh_result, tc_result, pn_result)