import re
import requests
import sys
import time
# 使用newspaper库爬取新闻
from newspaper import Article
#模块所在目录加入到搜索目录中
sys.path.append('./crawlers')
from databaseInsert import *
from purified import *
# 获取当前日期
date = time.strftime('%Y%m%d',time.localtime(time.time()))
# 使用新闻接口获取新闻url列表
def get_page(page):
    url_temp = 'http://temp.163.com/special/00804KVA/cm_guonei_0{}.js'
    return_list = []
    for i in range(2, page):
        url = url_temp.format(i)
        response = requests.get(url)
        if response.status_code != 200:
            continue
        # 获取响应正文
        content = response.text
        # 使用正则表达式获取链接
        pattern = re.compile(r'"docurl":"https://([\w-]+\.)+[\w-]+(/[./?%&=\w-]*)?"')
        urls = pattern.findall(content)
        for url in urls:
            # 补全链接
            return_list.append("https://www.163.com"+url[1])
    return return_list
result = []
i = 0
for article_url in get_page(8):
    # 使用获取到的链接列表爬取新闻
    try:
        article= Article(article_url, language='zh') #Chinese
        article.download()
        article.parse()
        if (len(article.title) >= 4):
            result.append([str(int(date)*1000+i),article.title, "Netease", date, article.text, purified(article.text)])
            i+=1
    except:
        print("\n\n====error====\n\n")
        continue
# 将结果存入数据库
insertToDatabase(result)