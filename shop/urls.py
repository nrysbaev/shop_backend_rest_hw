from django.urls import path
from shop import views

urlpatterns = [
    path('api/v1/products/', views.ProductListCreateAPIView.as_view()),
    path('api/v1/products/<int:pk>', views.ProductDetailUpdateDeleteAPIView.as_view()),
    path('api/v1/products/reviews/', views.ProductReviewsAPIView.as_view()),
    path('api/v1/products/tags/', views.ProductTagsAPIView.as_view()),

    # path('api/v1/products/', views.products_list_view),
    # path('api/v1/products/<int:id>', views.products_detail_view),
    # path('api/v1/products/reviews/', views.products_reviews_view),
    # path('api/v1/products/tags/', views.products_tags_view),
]
