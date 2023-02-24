from rest_framework import serializers
from .models import Article
from tags.serializers import TagSerializer
from tags.models import Tags

class ArticleSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = "__all__"

    def create(self, validated_data):
        tags_data = self.context['request'].data.get('tags')
        tags_split = tags_data.split(",")
        tags_name = [t.strip().lower() for t in tags_split]
        tags = Tags.objects.filter(name__in=tags_name)
        article = Article.objects.create(**validated_data)
        article.tags.set(tags)
        article.save()
        return article
    
    def update(self, instance, validated_data):
        tags_data = self.context['request'].data.get('tags')
        tags_split = tags_data.split(",")
        tags_name = [t.strip().lower() for t in tags_split]
        tags = Tags.objects.filter(name__in=tags_name)
        instance.tags.set(tags)
        instance.save()
        return instance