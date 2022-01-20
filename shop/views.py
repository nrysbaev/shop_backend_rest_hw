from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from . import models


@api_view(['GET', 'POST'])
def products_list_view(request):
    if request.method == 'GET':
        products = models.Product.objects.all()
        data = serializers.ProductListSerializer(products, many=True).data
        return Response(data=data)

    elif request.method == 'POST':
        serializer = serializers.ProductCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors': serializer.errors})
        title = serializer.initial_data['title']
        description = serializer.initial_data.get('description', '')
        price = serializer.initial_data['price']
        category = serializer.initial_data['category']
        tags = serializer.initial_data['tags']
        # reviews = serializer.initial_data['product_reviews']
        product = models.Product.objects.create(
            title=title, description=description, price=price,
            category_id=category
        )
        product.tags.set(tags)
        # product.product_reviews.create(text=reviews)
        return Response(data=serializers.ProductDetailSerializer(product).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def products_detail_view(request, id):
    try:
        product = models.Product.objects.get(id=id)
    except models.Product.DoesNotExist:
        return Response(data={'message': 'NOT FOUND'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = serializers.ProductDetailSerializer(product).data
        return Response(data=data)

    elif request.method == 'PUT':
        serializer = serializers.ProductUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors': serializer.errors})
        product.title = serializer.validated_data.get('title', product.title)
        product.description = serializer.validated_data.get('description', product.description)
        product.price = serializer.validated_data.get('price', product.price)
        product.category_id = serializer.validated_data.get('category', product.category_id)
        tags = serializer.validated_data.get('tags', [tag for tag in product.tags.all()])
        product.save()
        product.tags.set(tags)
        return Response(data=serializers.ProductDetailSerializer(product).data,
                        status=status.HTTP_201_CREATED)

    elif request.method == 'DELETE':
        product.delete()
        return Response(data={'message': 'Product removed successfully!'})


@api_view(['GET'])
def products_reviews_view(request):
    products = models.Product.objects.all()
    data = serializers.ProductReviewSerializer(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def products_tags_view(request):
    products = models.Product.objects.all()
    data = serializers.ProductTagsSerializer(products, many=True).data
    return Response(data=data)
