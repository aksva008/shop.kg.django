from django.contrib import admin
from .models import Brand, ClothesModel


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(ClothesModel)
class ClothesModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'photo')
