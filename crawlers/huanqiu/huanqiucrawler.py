import re
from bs4 import BeautifulSoup
import requests
from newspaper import Article
import sys
import time
#模块所在目录加入到搜索目录中
sys.path.append('./crawlers')
from databaseInsert import *

# 获取当前日期
date = time.strftime('%Y%m%d',time.localtime(time.time()))

def purified(psg):
    otc=psg.replace(r'\n','')
    punc='[~ ` + - * / # $ % ^ \' " ； 、 。 ， ？ ！ ! ? , . ; : ： ( ) （ ） — - _ 《 》]'
    otc=re.sub(punc,"",otc)
    otc=re.sub("<.*?>","",otc)
    return otc     

findlink=re.compile(r'<a.*?href="(.*?)"')


def getdata(url):
    datalist=[]
    soup=BeautifulSoup(askurl(url),'html.parser')
    i = 0
    for list in soup.find_all('div',class_="centerThr"):
        for link in re.findall(findlink,str(list)):
            if(len(link)>32):
                article=Article("https:"+link,language='zh')
                article.download()
                article.parse()
                datalist.append([str(int(date)*1000+100+i), article.title, "huanqiu", date, article.text, purified(article.text)])
                i+=1
    return datalist


def askurl(url):
    head={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
    html=requests.get(url,headers=head).text
    return html

baseurl="https://www.huanqiu.com/"
data = getdata(baseurl)
insertToDatabase(data)
print("Success!")