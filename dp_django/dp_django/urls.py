"""dp_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from news.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    url('^api/test', test),
    url('^api/get_news', get_news),
    url('^api/delete_news', delete_news),
    url('^api/delete_top_news', delete_top_news),
    url('^api/get_top_news', get_top_news),
    url('^api/get_specific_news', get_specific_news),
    url('^api/get_digest', get_digest),
]
