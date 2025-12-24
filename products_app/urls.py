from django.urls import path
from . import views

urlpatterns = [
    path('top5/', views.top5_products),
    path('time/', views.current_time),
    path('about/', views.about_me),
]
