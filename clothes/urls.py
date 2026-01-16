from django.urls import path
from .views import clothes_list

urlpatterns = [
    path('', clothes_list, name='clothes'),
]