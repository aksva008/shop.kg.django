from django.urls import path
from .views import ClothesListView, ClothesDetailView, ClothesCreateView

app_name = 'clothes'

urlpatterns = [
    path('', ClothesListView.as_view(), name='clothes_list'),
    path('add/', ClothesCreateView.as_view(), name='clothes_add'),
    path('<int:clothes_id>/', ClothesDetailView.as_view(), name='clothes_detail'),
]
