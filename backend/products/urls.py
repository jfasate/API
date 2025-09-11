from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.ProductDetailAPIView.as_view(), name='product-detail'),
    path('create/', views.ProductCreateAPIView.as_view(), name='product-create'),
    path('', views.ProductListAPIView.as_view(), name='product-list'),
    path('list-create/', views.ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('<int:pk>/delete/', views.ProductDeleteAPIView.as_view(), name='product-delete'),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view(), name='product-update'),
]