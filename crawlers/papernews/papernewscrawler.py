from selenium import webdriver
from newspaper import Article
import time
import re
import sys
#模块所在目录加入到搜索目录中
sys.path.append('./crawlers')
from databaseInsert import *
# from purified import *
# 获取当前日期
date = time.strftime('%Y%m%d',time.localtime(time.time()))
findlink=re.compile(r'<a href="(.*?)"')

def purified(psg):
    otc=psg.replace(r'\n','')
    punc='[~ ` + - * / # $ % ^ \' " ； 、 。 ， ？ ！ ! ? , . ; : ： ( ) （ ） — - _ 《 》]'
    otc=re.sub(punc,"",otc)
    otc=re.sub("<.*?>","",otc)
    return otc


def getdata(url):
    datalist=[]
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    time.sleep(5)
    driver.execute_script('scrollTo(0,{})'.format(2000))
    for i in range(10):
        driver.execute_script('scrollTo(0,{})'.format(2000+i*1000))
        time.sleep(2)
    i = 0
    for item in driver.find_elements_by_class_name("news_tu"):
        article=Article("https://www.thepaper.cn/"+re.findall(findlink,item.get_attribute("innerHTML"))[0],language='zh')
        article.download()
        article.parse()
        datalist.append([str(int(date)*1000+200+i), article.title, "papernews", date, article.text, purified(article.text)])
        i+=1
    return datalist
    driver.quit()

baseurl="https://www.thepaper.cn/"
data = getdata(baseurl)
insertToDatabase(data)
print("Success!")