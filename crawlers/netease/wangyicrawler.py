from bs4 import BeautifulSoup
import re
import sys
import time
import urllib.request,urllib.error
#模块所在目录加入到搜索目录中
sys.path.append('./crawlers')
from databaseInsert import *

# 获取当前日期
date = time.strftime('%Y%m%d',time.localtime(time.time()))
findlink=re.compile(r'<a.*href="(.*?)"')
findtitle=re.compile(r'>(.*?)<')
findpsg=re.compile(r'<p.*?>(.*?)</p>')


def purified(psg):
    otc=psg.replace(r'\n','')
    punc='[~ ` + - * / # $ % ^ \' " ； 、 。 ， ？ ！ ! ? , . ; : ： ( ) （ ） — - _ 《 》]'
    otc=re.sub(punc,"",otc)
    otc=re.sub("<.*?>","",otc)
    return otc


def getdata(baseurl):
    datalist=[]
    soup=BeautifulSoup(askurl(baseurl),"html.parser")
    link=re.findall(findlink,str(soup.find_all('div',class_="yaowen_news")))
    for i in range(0,len(link)//2):
        data=["","","","","",""]
        soup=BeautifulSoup(askurl(link[i]),"html.parser")
        data[1]=re.findall(findtitle,str(soup.find_all('h1',class_="post_title")))[0]
        for psg in re.findall(findpsg,str(soup.find_all('div',class_="post_body"))):
            data[4]+='\n'+psg
        data[0] = str(int(date)*10000+i)
        data[2] = "Netease"
        data[3] = date
        data[5] = purified(data[4])
        datalist.append(data)
    return datalist
def askurl(url):
    head={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
    request=urllib.request.Request(url,headers=head)
    html=""
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode("UTF-8")
    except urllib.error.URLError as e:
        if(hasattr(e,"code")):
            print(e.code)
        if(hasattr(e,"reason")):
            print(e.reason)
    return html

baseurl="http://163.com/"
datalist=getdata(baseurl)
insertToDatabase(datalist)
print("Success!")