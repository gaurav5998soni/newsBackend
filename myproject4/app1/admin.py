from django.contrib import admin
from .models import News, TimeLineData, Trending, Ad
# Register your models here.
admin.site.register(News)
admin.site.register(Trending)
admin.site.register(TimeLineData)
admin.site.register(Ad)