from django import forms
from .models import BasketItem, Order

class BasketForm(forms.ModelForm):
    class Meta:
        model = BasketItem
        fields = ['customer_name', 'phone', 'email', 'address', 'quantity']  # product добавляем вручную

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'phone', 'email', 'address']
