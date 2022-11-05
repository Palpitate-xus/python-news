import requests
import bs4
import time
import datetime
import sys
import re
#模块所在目录加入到搜索目录中
sys.path.append('./crawlers')
from databaseInsert import *

# 获取当前日期
now_date = time.strftime('%Y%m%d',time.localtime(time.time()))


def purified(psg):
    otc=psg.replace(r'\n','')
    punc='[~ ` + - * / # $ % ^ \' " ； 、 。 ， ？ ！ ! ? , . ; : ： ( ) （ ） — - _ 《 》]'
    otc=re.sub(punc,"",otc)
    otc=re.sub("<.*?>","",otc)
    return otc

# 获取链接列表
def getUrl(url):
    # 网络请求头
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
    }
    # 发送request请求，获取网页内容
    rec = requests.get(url, headers=headers)
    rec.raise_for_status()
    rec.encoding = rec.apparent_encoding
    return rec.text

# 获取内容列表
def getPageList(year, month, day):
    url = 'http://paper.people.com.cn/rmrb/html/' + year + '-' + month + '/' + day + '/nbs.D110000renmrb_01.htm'
    html = getUrl(url)
    # 使用靓汤库获取并解析网页
    bsobj = bs4.BeautifulSoup(html,'html.parser')
    temp = bsobj.find('div', attrs = {'id': 'pageList'})
    if temp:
        pageList = temp.ul.find_all('div', attrs = {'class': 'right_title-name'})
    else:
        pageList = bsobj.find('div', attrs = {'class': 'swiper-container'}).find_all('div', attrs = {'class': 'swiper-slide'})
    linkList = []
    
    for page in pageList:
        link = page.a["href"]
        url = 'http://paper.people.com.cn/rmrb/html/'  + year + '-' + month + '/' + day + '/' + link
        linkList.append(url)
    return linkList

def getTitleList(year, month, day, pageUrl):

    # 功能：获取报纸某一版面的文章链接列表
    # 参数：年，月，日，该版面的链接

    html = getUrl(pageUrl)
    bsobj = bs4.BeautifulSoup(html,'html.parser')
    temp = bsobj.find('div', attrs = {'id': 'titleList'})
    if temp:
        titleList = temp.ul.find_all('li')
    else:
        titleList = bsobj.find('ul', attrs = {'class': 'news-list'}).find_all('li')
    linkList = []
    
    for title in titleList:
        tempList = title.find_all('a')
        for temp in tempList:
            link = temp["href"]
            if 'nw.D110000renmrb' in link:
                url = 'http://paper.people.com.cn/rmrb/html/'  + year + '-' + month + '/' + day + '/' + link
                linkList.append(url)
    
    return linkList

def getContent(html):

    # 功能：解析 HTML 网页，获取新闻的文章内容
    # 参数：html 网页内容
   
    bsobj = bs4.BeautifulSoup(html,'html.parser')
    
    # 获取文章 标题
    title = bsobj.h3.text + '\n' + bsobj.h1.text + '\n' + bsobj.h2.text + '\n'
    #print(title)
    
    # 获取文章 内容
    pList = bsobj.find('div', attrs = {'id': 'ozoom'}).find_all('p')
    content = ''
    for p in pList:
        content += p.text + '\n'      
    #print(content)
    
    # 返回结果 标题+内容
    resp = title + content
    title = title.replace("\n", "")
    content = content.replace("\n", "")
    return [title, content]


def download_rmrb(year, month, day):

    # 功能：爬取《人民日报》网站 某年 某月 某日 的新闻内容，并保存在数据库中
    # 参数：年，月，日

    data = []
    date = int(year+month+day)
    i = 0
    pageList = getPageList(year, month, day)
    for page in pageList:
        titleList = getTitleList(year, month, day, page)
        for url in titleList:
            # 获取新闻文章内容
            html = getUrl(url)
            content = getContent(html)
            if len(content[0]) <= 4:
                continue
            data_item = [str(date*100+i), content[0], "People Daily", now_date, content[1], purified(content[1])]
            data.append(data_item)
            i+=1
    insertToDatabase(data)
            
           
if __name__ == '__main__':
    # 主函数：程序入口
    # 爬取指定日期的新闻
    # newsDate = input('请输入要爬取的日期（格式如 20190502 ）:')
    # 获取当前年月日
    year=(datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y')
    month=(datetime.date.today() - datetime.timedelta(days=1)).strftime('%m')
    day=(datetime.date.today() - datetime.timedelta(days=1)).strftime('%d')
    # year = newsDate[0:4]
    # month = newsDate[4:6]
    # day = newsDate[6:8]
    date = time.strftime('%Y%m%d',time.localtime(time.time()))
    download_rmrb(year, month, day)
    print("爬取完成：" + year + month + day)

    