import jieba
import math
import re
import pymysql
import time

date = time.strftime('%Y%m%d',time.localtime(time.time()))
def purify(psg):
    otc=""
    otc=psg.replace(r'\n','')
    punc='[… { } ’ ‘ | ” “ ~ ` + - * / # $ % & ^ \' " ； 、 。 ， ？ ！ ! ? , . ; : ： ( ) （ ） — - 《 》_ 【 】\[ \]]'
    otc=re.sub(punc,"",otc)
    otc=re.sub("<.*?>","",otc)
    return otc
def rept(s0,s1):
    vec={}
    len0=len1=dotp=0
    for word in jieba.cut(s0):
        if(word in vec):
            vec[word][0]+=1
        else:
            vec[word]=[1,0]
    for word in jieba.cut(s1):
        if(word in vec):
            vec[word][1]+=1
        else:
            vec[word]=[0,1]
    for dim in vec:
        dotp+=vec[dim][1]*vec[dim][0]
        len0+=vec[dim][0]**2
        len1+=vec[dim][1]**2
    return math.acos(dotp/(math.sqrt(len0*len1)))*180/math.pi
def lookup(newslist):
    zeros=0
    for i in range(len(newslist)):
        newslist[i].append(0)
    for i in range(len(newslist)-1):
        print(i)
        if(newslist[i]):
            for j in range(i+1,len(newslist)):
                if(not newslist[j]):continue
                if(newslist[i][2]!=newslist[j][2] and rept(newslist[i][5],newslist[j][5])<=50):
                    newslist[i][6]+=1
                    newslist[j]=0
                    zeros+=1
    for i in range(zeros):
        newslist.remove(0)
    newslist.sort(key=lambda k:k[6],reverse=True)
    topnews=[]
    for i in range(min(10,len(newslist))):
        topnews.append(newslist[i])
    return topnews
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
    dataList = []
    for item in data:
        if str(item[3]) == date:  
            data_item = [item[0], item[1], item[2], item[3], item[4], item[5]]
            dataList.append(data_item)
    sql = 'INSERT INTO top_news values (%s, %s, %s, %s, %s, %s, %s)'
    for item in lookup(dataList):
        row_counst = cursor.execute(sql, item)
        # 提交更改
    db.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    db.close()

