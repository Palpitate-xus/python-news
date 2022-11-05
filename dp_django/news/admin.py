from django.contrib import admin
from news import models
# Register your models here.


admin.site.register(models.News)
admin.site.register(models.TopNews)
admin.site.register(models.Frequency)
