from django.shortcuts import render
from .serializers import NewsSerializer, TrendingSerializer, TimeLineDataSerializer, AdSerializer
from .models import News, Trending, TimeLineData, Ad
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class Home(APIView):

    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        news = News.objects.all()
        news_serializer = NewsSerializer(news, many=True)

        trendings = Trending.objects.all()
        trendings_serializer = TrendingSerializer(trendings, many=True)

        timelinedata = TimeLineData.objects.all()
        timelinedata_serializer = TimeLineDataSerializer(timelinedata, many=True)

        ad = Ad.objects.all()
        ad_serializer = AdSerializer(timelinedata, many=True)

        return Response({
            'timeline': timelinedata_serializer.data,
            'trending': trendings_serializer.data,
            'news':     news_serializer.data,
            'ad': ad_serializer.data
        })
