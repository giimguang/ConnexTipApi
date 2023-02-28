from django.shortcuts import render
from .models import Tag
from .serializers import TagSerializer
from rest_framework import generics

# Create your views here.

class TagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagCreate(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagUpdate(generics.UpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDelete(generics.DestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer