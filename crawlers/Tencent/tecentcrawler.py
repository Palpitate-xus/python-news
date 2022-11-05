import requests
import json
from newspaper import Article
import re
import sys
import time
#模块所在目录加入到搜索目录中
sys.path.append('./crawlers')
from databaseInsert import *

# 获取当前日期
date = time.strftime("%Y%m%d",time.localtime(time.time()))


headers={
    'referer': 'https://news.qq.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}


def purified(psg):
    otc=psg.replace(r'\n','')
    punc='[~ ` + - * / # $ % ^ \' " ； 、 。 ， ？ ！ ! ? , . ; : ： ( ) （ ） — - _ 《 》]'
    otc=re.sub(punc,"",otc)
    otc=re.sub("<.*?>","",otc)
    return otc


def getdata():
    linklist=[]
    datalist=[]
    today_news_url='https://i.news.qq.com/trpc.qqnews_web.pc_base_srv.base_http_proxy/NinjaPageContentSync?pull_urls=news_top_2018'
    infolist=getPage(today_news_url)
    for info in infolist["data"]:
        linklist.append(info["url"])
    for i in range(4):
        hot_news_url ='https://i.news.qq.com/trpc.qqnews_web.kv_srv.kv_srv_http_proxy/list?sub_srv_id=24hours&srv_id=pc&offset=' + str(
        i*20) + '&limit=20&strategy=1&ext={%22pool%22:[%22top%22],%22is_filter%22:7,%22check_type%22:true}'
        for info in getPage(hot_news_url)["data"]["list"]:
            linklist.append(info["url"])
    i = 0
    for link in linklist:
        article=Article(link,language='zh')
        article.download()
        article.parse()
        if len(article.text) >= 1 and len(article.title) >= 1:
            datalist.append([str(int(date)*10000+400+i), article.title, "Tencent", date, article.text, purified(article.text)])
            i+=1
    return datalist
def getPage(url):
    try:
        re=requests.get(url,headers=headers)
        re.encoding=re.apparent_encoding
        return json.loads(re.text)
    except:
        print(re.status_code)

data = getdata()
insertToDatabase(data)
print("Success!")