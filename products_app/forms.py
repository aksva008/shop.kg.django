from django import forms
from products_app.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"