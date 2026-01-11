from django.shortcuts import render
from .models import Product, Review
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

def home(request):
    """Главная страница"""
    products = Product.objects.all()[:5]  
    

    if not products:
        Product.objects.create(
            name="Кимпаб",
            korean_name="김밥",
            price=350,
            description="Корейские роллы с овощами, яйцом и мясом"
        )
        Product.objects.create(
            name="Токпоки", 
            korean_name="떡볶이",
            price=450,
            description="Острые рисовые палочки в соусе"
        )
        products = Product.objects.all()
    
    return render(request, 'products_app/home.html', {
        'products': products,
        'title': 'Главная страница'
    })

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products_app/product_list.html', {
        'products': products,
        'title': 'Все продукты'
    })

@login_required
def add_review(request):
    if request.method == 'POST':
        product_id = request.POST.get('product')
        text = request.POST.get('text')
        rating = request.POST.get('rating')
        
        try:
            product = Product.objects.get(id=product_id)
            Review.objects.create(
                product=product,
                user=request.user,
                text=text,
                rating=rating,
                is_published=True
            )
            return redirect('product_list')
        except Product.DoesNotExist:
            pass
    
    products = Product.objects.all()
    return render(request, 'products_app/add_review.html', {
        'products': products
    })

def blog(request):
    return render(request, 'products_app/blog.html', {
        'title': 'Блог'
    })

def about(request):
    return render(request, 'products_app/about.html', {
        'title': 'О нас'
    })

def hashtags(request):
    return render(request, 'products_app/hashtags.html', {
        'title': 'Хештеги'
    })

def basket(request):
    return render(request, 'products_app/basket.html', {
        'title': 'Корзина'
    })