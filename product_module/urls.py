from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='product_index'),
    path('create/', views.create_product, name='product_create'),
    path('<int:pk>/edit/', views.edit_product, name='product_edit'),
    path('<int:pk>/delete/', views.delete_product, name='product_delete'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
]
