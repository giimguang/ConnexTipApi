from django.db import models
from tags.models import Tag
import random

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    banner = models.ImageField(upload_to='banners/', null=True, blank=True)
    slug = models.CharField(max_length=20, unique=True, null=True)
    viewer = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag, related_name="tagged")
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category_articles', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            strs = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789"
            ran_slug = ""
            for _ in range(7):
                ran_slug += random.choice(strs)
            self.slug = ran_slug
        super(Article, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ['-created_date']

class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title