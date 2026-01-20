from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Brand, ClothesModel

class ClothesListView(ListView):
    model = ClothesModel
    template_name = 'clothes/clothes_list.html'
    context_object_name = 'clothes'

class ClothesDetailView(DetailView):
    model = ClothesModel
    template_name = 'clothes/clothes_detail.html'
    context_object_name = 'clothes'
    pk_url_kwarg = 'clothes_id'

class ClothesCreateView(CreateView):
    model = ClothesModel
    template_name = 'clothes/clothes_create.html'
    fields = ['name', 'brand', 'price', 'photo']
    success_url = reverse_lazy('clothes:clothes_list')

