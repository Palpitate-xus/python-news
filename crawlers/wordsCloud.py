import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pymysql
import time
date = time.strftime('%Y%m%d',time.localtime(time.time()))
f = open("./crawlers/stopwords.txt", "r", encoding="UTF-8")
stopword = f.readlines()


def createWordCloud(content):
    # 使用结巴库分词
    text = " ".join(jieba.cut(content[5]))
    # 使用wordcloud库生成词云
    wordcloud = WordCloud(background_color='white',font_path="./crawlers/simsun.ttf", scale=32, mode="RGBA", stopwords=stopword).generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig("./wordclouds/"+str(content[0])+'.png', dpi=500, bbox_inches = 'tight')
    return content[0]

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
            createWordCloud(data_item)
    
