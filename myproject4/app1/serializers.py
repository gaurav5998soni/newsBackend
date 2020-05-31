from rest_framework import serializers
from .models import News, TimeLineData, Trending


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'description', 'time', 'video_url', 'image','image_url']

class TimeLineDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'description', 'time', 'video_url', 'image','image_url']

class TrendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'description', 'time', 'video_url', 'image','image_url']

class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['image_url']