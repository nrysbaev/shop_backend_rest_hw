from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from . import models
from rest_framework import generics


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductListSerializer

    def list(self, request, *args, **kwargs):
        queryset = models.Product.objects.all()

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = serializers.ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductDetailSerializer
    lookup_field = 'pk'


class ProductReviewsAPIView(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductReviewSerializer


class ProductTagsAPIView(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductTagsSerializer

# @api_view(['GET', 'POST'])
# def products_list_view(request):
#     if request.method == 'GET':
#         products = models.Product.objects.all()
#         data = serializers.ProductListSerializer(products, many=True).data
#         return Response(data=data)
#
#     elif request.method == 'POST':
#         serializer = serializers.ProductCreateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
#                             data={'errors': serializer.errors})
#         print('request.data:', request.data)
#         print('serializer.validated_data: ', serializer.validated_data)
#         # validated data works normally without errors
#         title = serializer.validated_data['title']
#         description = serializer.validated_data.get('description', '')
#         price = serializer.validated_data['price']
#         category = serializer.validated_data['category']
#         tags = serializer.validated_data['tags']
#         # reviews = serializer.initial_data['product_reviews']
#         product = models.Product.objects.create(
#             title=title, description=description, price=price,
#             category_id=category
#         )
#         product.tags.set(tags)
#         # product.product_reviews.create(text=reviews)
#         return Response(data=serializers.ProductDetailSerializer(product).data,
#                         status=status.HTTP_201_CREATED)



# @api_view(['GET', 'PUT', 'DELETE'])
# def products_detail_view(request, id):
#     try:
#         product = models.Product.objects.get(id=id)
#     except models.Product.DoesNotExist:
#         return Response(data={'message': 'NOT FOUND'}, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         data = serializers.ProductDetailSerializer(product).data
#         return Response(data=data)
#
#     elif request.method == 'PUT':
#         serializer = serializers.ProductUpdateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
#                             data={'errors': serializer.errors})
#         product.title = serializer.validated_data.get('title', product.title)
#         product.description = serializer.validated_data.get('description', product.description)
#         product.price = serializer.validated_data.get('price', product.price)
#         product.category_id = serializer.validated_data.get('category', product.category_id)
#         tags = serializer.validated_data.get('tags', [tag for tag in product.tags.all()])
#         product.save()
#         product.tags.set(tags)
#         return Response(data=serializers.ProductDetailSerializer(product).data,
#                         status=status.HTTP_201_CREATED)
#
#     elif request.method == 'DELETE':
#         product.delete()
#         return Response(data={'message': 'Product removed successfully!'})


# @api_view(['GET'])
# def products_reviews_view(request):
#     products = models.Product.objects.all()
#     data = serializers.ProductReviewSerializer(products, many=True).data
#     return Response(data=data)
#
#
# @api_view(['GET'])
# def products_tags_view(request):
#     products = models.Product.objects.all()
#     data = serializers.ProductTagsSerializer(products, many=True).data
#     return Response(data=data)
