from django.urls import path
from .views import (
    ProductListView, ProductDetailView,
    ProductCreateView, ProductUpdateView, ProductDeleteView
)

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),  # Home page
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('admin/products/add/', ProductCreateView.as_view(), name='product_add'),
    path('admin/products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('admin/products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]
