from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import Product, Category

def top5_products(request):
    products = [
        "Kimchi",
        "Bulgogi",
        "Bibimbap",
        "Tteokbokki",
        "Samgyeopsal"
    ]
    return HttpResponse("<br>".join(products))

def current_time(request):
    now = timezone.now()
    return HttpResponse(f"Текущая дата и время: {now}")

def about_me(request):
    return HttpResponse("""
        <h2>Обо мне</h2>
        <img src="https://linguacats.com/media/zoo/images/Korea_557b98c6da7d269ce2357efaceac8303.jpg">
        <p>Меня зовут Акылай, я учу Django 😊</p>
    """)

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def products_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'category_products.html', {
        'category': category,
        'products': products
    })