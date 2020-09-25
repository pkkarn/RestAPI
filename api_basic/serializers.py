from rest_framework import serializers
from .models import Article
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'author', ]
