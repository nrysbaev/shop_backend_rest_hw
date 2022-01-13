from rest_framework import serializers
from .models import Category, Tag, Review, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text']


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title']


class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'category', 'tags', 'reviews']


class ProductReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'reviews']


class ProductTagsSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = 'id title tags'.split()

    def get_tags(self, product):
        active_tags = product.tags.filter(is_active=True)
        data = TagSerializer(active_tags, many=True).data
        return data
