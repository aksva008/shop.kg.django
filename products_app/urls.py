from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_review/<int:product_id>/', views.add_review, name='add_review'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('hashtags/', views.hashtags, name='hashtags'),
    path('contact/', views.contact, name='contact'),
    path('basket/', views.basket, name='basket'),
]
