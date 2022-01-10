from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products/', views.products_list_view),
    path('api/v1/products/<int:id>', views.products_detail_view),
]
