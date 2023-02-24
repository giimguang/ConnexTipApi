from django.shortcuts import render
from .models import Tags
from .serializers import TagSerializer
from rest_framework import generics

# Create your views here.

class TagList(generics.ListAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer

class TagCreate(generics.CreateAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer

class TagUpdate(generics.UpdateAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer

class TagDelete(generics.DestroyAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer