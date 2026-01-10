from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_list, name='home'),  
    path('categories/', views.categories_list, name='categories_list'),  
    path('products/', views.products_list, name='products_list'),      
    path('categories/<int:category_id>/', views.category_products, name='category_products'),
    path('top5/', views.top5_products, name='top5_products'),           
]