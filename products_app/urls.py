from django.urls import path
from .views import (
    HomeView,
    ProductListView,
    ProductDetailView,
    ReviewCreateView,
    SearchView,
    BlogView,
    AboutView,
    BasketView,
    HashtagsView,
    ContactView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:product_id>/review/', ReviewCreateView.as_view(), name='add_review'),
    path('search/', SearchView.as_view(), name='search'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('about/', AboutView.as_view(), name='about'),
    path('basket/', BasketView.as_view(), name='basket'),
    path('hashtags/', HashtagsView.as_view(), name='hashtags'),
    path('contact/', ContactView.as_view(), name='contact'),
]
