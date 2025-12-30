from django.urls import path
from . import views
from django.urls import path
from .views import product_list

urlpatterns = [
    path('top5/', views.top5_products),
    path('time/', views.current_time),
    path('about/', views.about_me),
    path('', product_list, name='product_list'),
    path('', product_list, name='product_list'),
]
