from django.urls import path
from . import views

urlpatterns = [
    path('', views.basket_list, name='basket_list'),
    path('add/<int:product_id>/', views.add_to_basket, name='add_to_basket'),
    path('edit/<int:item_id>/', views.edit_basket_item, name='edit_basket_item'),
    path('delete/<int:item_id>/', views.remove_from_basket, name='remove_from_basket'),
    path('order/place', views.place_order, name='place_order'),
]