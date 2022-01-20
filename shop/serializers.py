from rest_framework import serializers
from rest_framework.exceptions import ValidationError

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
    product_reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'category', 'tags', 'product_reviews']


class ProductReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'product_reviews']


class ProductTagsSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = 'id title tags'.split()

    def get_tags(self, product):
        active_tags = product.tags.filter(is_active=True)
        data = TagSerializer(active_tags, many=True).data
        return data


class ProductCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=20)
    description = serializers.CharField(required=False)
    price = serializers.IntegerField(default=0)
    category = serializers.IntegerField()
    tags = serializers.ListSerializer(child=serializers.IntegerField())

    def validate_title(self, title):
        product = Product.objects.filter(title=title)
        if product:
            raise ValidationError('This Product already exists!')
        return title


class ProductUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=20, required=False)
    description = serializers.CharField(required=False)
    price = serializers.IntegerField(required=False)
    category = serializers.IntegerField(required=False)
    tags = serializers.ListSerializer(required=False, child=serializers.IntegerField())
