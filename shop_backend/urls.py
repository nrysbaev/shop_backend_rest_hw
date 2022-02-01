from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products/', views.products_list_view),
    path('api/v1/products/<int:id>', views.products_detail_view),
    path('api/v1/products/reviews/', views.products_reviews_view),
    path('api/v1/products/tags/', views.products_tags_view),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
