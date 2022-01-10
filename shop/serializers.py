from rest_framework import serializers
from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['name']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = ['name']


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['id', 'title']


class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = models.Product
        fields = ['title', 'description', 'price', 'category', 'tags']
