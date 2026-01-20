from django.urls import path
from .views import BasketListView, BasketAddView, BasketDeleteView

app_name = 'basket'

urlpatterns = [
    path('', BasketListView.as_view(), name='basket_list'),
    path('add/', BasketAddView.as_view(), name='basket_add'),
    path('delete/<int:pk>/', BasketDeleteView.as_view(), name='basket_delete'),
]
