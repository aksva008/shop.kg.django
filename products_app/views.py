from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render
from .models import Product


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

from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Review

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = product.reviews.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        text = request.POST.get('text')

        Review.objects.create(
            product=product,
            name=name,
            text=text
        )
        return redirect('product_detail', pk=pk)

    return render(request, 'product_detail.html', {
        'product': product,
        'reviews': reviews
    })
