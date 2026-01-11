from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('add-review/', views.add_review, name='add_review'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('hashtags/', views.hashtags, name='hashtags'),
    path('basket/', views.basket, name='basket'),
]