from django.contrib import admin
from .models import Product, Review

admin.site.register(Product)
admin.site.register(Review)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')  
    search_fields = ('title',) 

