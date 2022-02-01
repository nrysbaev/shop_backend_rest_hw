from django.urls import path
from users import views

urlpatterns = [
    path('api/v1/register/', views.RegisterAPIView.as_view()),
    path('api/v1/login/', views.LoginAPIView.as_view()),
    path('api/v1/activate/<int:id>/', views.ActivateAPIView.as_view()),

    # path('api/v1/register/', views.register),
    # path('api/v1/login/', views.login),
    # path('api/v1/activate/<int:id>/', views.activate),
]
