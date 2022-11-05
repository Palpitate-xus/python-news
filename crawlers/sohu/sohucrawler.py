import re
from bs4 import BeautifulSoup
import urllib.request,urllib.error
import time
import re
import sys
#模块所在目录加入到搜索目录中
sys.path.append('./crawlers')
from databaseInsert import *
# from purified import *
# 获取当前日期
date = time.strftime('%Y%m%d',time.localtime(time.time()))
findlink=re.compile(r'a.*com/a/(.*?)"')
findart=re.compile(r'<p.*?>(.*?)<')
findtitle=re.compile(r'<h1>.*\n.* (.*)')
findtitle2=re.compile(r'<h1>(.*?)<span')
findorgt=re.compile(r'>(.*?)<')


def purified(psg):
    otc=psg.replace(r'\n','')
    punc='[~ ` + - * / # $ % ^ \' " ； 、 。 ， ？ ！ ! ? , . ; : ： ( ) （ ） — - _ 《 》]'
    otc=re.sub(punc,"",otc)
    otc=re.sub("<.*?>","",otc)
    return otc


def getdata(baseurl):
    datalist=[]
    html=askurl(baseurl)
    soup=BeautifulSoup(html,"html.parser")
    i = 0
    for list in soup.find_all('div',class_="list16"):
        for link in re.findall(findlink,str(list)):
            data=[str(int(date)*10000+1000+i), "", "sohu", date, "", ""]
            link='http://www.sohu.com/a/'+link
            html=askurl(link)
            soup=BeautifulSoup(html,"html.parser")
            if(len(soup.find_all('div',class_="content-info"))):
                continue
            title0=re.findall(findtitle,str(soup.find_all('div',class_="text-title")))
            title1=re.findall(findorgt,str(soup.find_all('span',class_="title-info-title")))
            title2=re.findall(findtitle2,str(soup.find_all('div',class_="text-title")))
            if(len(title1)):
                data[1]=title1[0]
            elif(len(title0)):
                data[1]=title0[0]
            elif(len(title2)):
                data[1]=title2[0]
            if(len(data[0]) and data[0][0]==' '):
                data[0]=data[0].replace(' ','',19);
            for psg in re.findall(findart,str(soup.find_all('article',class_="article"))):
                data[4]+="\n"+psg
            data[5] = purified(data[4])
            i=i+1
            datalist.append(data)
    return datalist
def askurl(url):
    head={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
    request=urllib.request.Request(url,headers=head)
    html=""
    try:
        response=urllib.request.urlopen(request)
        html=response.read()#.decode("UTF-8")
    except urllib.error.URLError as e:
        if(hasattr(e,"code")):
            print(e.code)
        if(hasattr(e,"reason")):
            print(e.reason)
    return html

baseurl="http://news.sohu.com/"
datalist=getdata(baseurl)
insertToDatabase(datalist)
print("Success!")