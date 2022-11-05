from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    timeStamp = models.IntegerField()
    content = models.TextField()
    splitWords = models.TextField()

    class Meta:
        db_table = "news"


class TopNews(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    timeStamp = models.IntegerField()
    content = models.TextField()
    splitWords = models.TextField()
    repeat = models.IntegerField()

    class Meta:
        db_table = "top_news"


class Frequency(models.Model):
    author = models.CharField(max_length=255)
    timeStamp = models.CharField(max_length=255)
    words = models.TextField()

    class Meta:
        db_table = 'frequency'


