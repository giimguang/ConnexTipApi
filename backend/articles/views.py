from django.shortcuts import render
from .models import Article
from tags.models import Tags

from rest_framework import generics
from .serializers import ArticleSerializer


# Create your views here.

class ArticleList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleTrending(generics.ListAPIView):
    queryset = Article.objects.order_by("-viewer")
    serializer_class = ArticleSerializer

class ArticleTag(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        tag = self.kwargs['tag']
        return Article.objects.filter(tags__name__in=[tag])

class ArticleCreate(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(generics.RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = "slug"

    def get_object(self):
        instance = super(ArticleDetail, self).get_object()
        instance.viewer = instance.viewer + 1
        instance.save()
        return instance

class ArticleUpdate(generics.UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = "slug"

class ArticleDelete(generics.DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = "slug"