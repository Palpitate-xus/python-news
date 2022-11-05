from django.shortcuts import render
from django.shortcuts import HttpResponse
import json
from news.models import News
from news.models import TopNews
from news.models import Frequency
import time
date = time.strftime('%Y%m%d', time.localtime(time.time()))
# Create your views here.


def test(request):
    response = {'code': 200, 'msg': 'success'}
    return HttpResponse(json.dumps(response))


def get_news(request):
    if request.method == 'POST':
        sql = "select * from news.news"
        result = News.objects.raw(sql)
        data = []
        for i in result:
            if i.timeStamp == int(date):
                news_item = {
                    'id': i.id,
                    'title': i.title,
                    'author': i.author,
                    'timeStamp': i.timeStamp,
                    'content': i.content,
                }
                data.append(news_item)
        response = {"code": 200, "data": data}
        return HttpResponse(json.dumps(response))
    else:
        response = {'code': 0, 'msg': 'success'}
        return HttpResponse(json.dumps(response))


def get_specific_news(request):
    if request.method == 'POST':
        received_data = json.loads(request.body.decode())
        this_author = received_data.get('author')
        sql = "select * from news.news"
        result = News.objects.raw(sql)
        data = []
        for i in result:
            if i.timeStamp == int(date) and i.author == this_author:
                news_item = {
                    'id': i.id,
                    'title': i.title,
                    'author': i.author,
                    'timeStamp': i.timeStamp,
                    'content': i.content,
                }
                data.append(news_item)
        response = {"code": 200, "data": data}
        return HttpResponse(json.dumps(response))
    else:
        response = {'code': 0, 'msg': 'success'}
        return HttpResponse(json.dumps(response))


def get_top_news(request):
    if request.method == 'POST':
        sql = "select * from news.top_news"
        result = TopNews.objects.raw(sql)
        data = []
        for i in result:
            if i.timeStamp == int(date):
                news_item = {
                    'id': i.id,
                    'title': i.title,
                    'author': i.author,
                    'timeStamp': i.timeStamp,
                    'content': i.content,
                }
                data.append(news_item)
        print(data)
        response = {"code": 200, "data": data}
        return HttpResponse(json.dumps(response))
    else:
        response = {'code': 0, 'msg': 'success'}
        return HttpResponse(json.dumps(response))


def delete_news(request):
    if request.method == 'POST':
        received_data = json.loads(request.body.decode())
        news_id = received_data.get('id')
        news = News.objects.get(id=news_id)
        news.delete()
        response = {"code": 200, "msg": 'success'}
        return HttpResponse(json.dumps(response))
    else:
        response = {'code': 0, 'msg': 'success'}
        return HttpResponse(json.dumps(response))


def delete_top_news(request):
    if request.method == 'POST':
        received_data = json.loads(request.body.decode())
        news_id = received_data.get('id')
        news = TopNews.objects.get(id=news_id)
        news.delete()
        response = {"code": 200, "msg": 'success'}
        return HttpResponse(json.dumps(response))
    else:
        response = {'code': 0, 'msg': 'success'}
        return HttpResponse(json.dumps(response))


def get_digest(request):
    if request.method == 'POST':
        sql = "select * from news.frequency"
        result = Frequency.objects.raw(sql)
        data = []
        for i in result:
            if i.timeStamp == date:
                digiest_item = {
                    'id': i.id,
                    'author': i.author,
                    'timeStamp': i.timeStamp,
                    'words': i.words,
                }
                data.append(digiest_item)
        print(data)
        response = {"code": 200, "data": data}
        return HttpResponse(json.dumps(response))
    else:
        response = {'code': 0, 'msg': 'success'}
        return HttpResponse(json.dumps(response))