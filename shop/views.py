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
        title = request.data['title']
        description = request.data.get('description', '')
        price = request.data['price']
        category = request.data['category']
        tags = request.data['tags']
        product = models.Product.objects.create(
            title=title, description=description, price=price, category_id=category
        )
        product.tags.set(tags)
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
        product.title = request.data.get('title', f'{product.title}')
        product.description = request.data.get('description', f'{product.description}')
        product.price = request.data.get('price', f'{product.price}')
        product.category_id = request.data.get('category', f'{product.category_id}')
        tags = request.data.get('tags', [tag for tag in product.tags.all()])
        product.tags.set(tags)
        product.save()
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
