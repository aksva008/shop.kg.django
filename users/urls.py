from django.urls import path
from .views import (
    register_view,
    login_view,
    all_users,
    register_tour,
    tour_success,
    clothes_list,
)

app_name = 'users'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('users/', all_users, name='all_users'),
    path('tour/', register_tour, name='register_tour'),
    path('tour/success/', tour_success, name='tour_success'),
    path('clothes/', clothes_list, name='clothes_list'),
]
