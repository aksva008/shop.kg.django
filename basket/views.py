from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import BasketItem
from clothes.models import ClothesModel


class BasketListView(ListView):
    model = BasketItem
    template_name = 'basket/basket_list.html'
    context_object_name = 'basket'

    def get_queryset(self):
        return BasketItem.objects.filter(user=self.request.user)


class BasketAddView(CreateView):
    model = BasketItem
    template_name = 'basket/basket_add.html'
    fields = ['item', 'quantity']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('basket:basket_list')


class BasketDeleteView(DeleteView):
    model = BasketItem
    template_name = 'basket/basket_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('basket:basket_list')
