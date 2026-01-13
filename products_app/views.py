from django.shortcuts import render, get_object_or_404, redirect

from .models import Product, Review


def home(request):
    """Главная страница"""
    products = Product.objects.all()[:5]

    return render(request, 'products_app/home.html', {
        'products': products,
        'title': 'Главная'
    })


def product_list(request):
    """Список всех продуктов"""
    products = Product.objects.all()

    return render(request, 'products_app/products_list.html', {
        'products': products,
        'title': 'Все продукты'
    })


def product_detail(request, product_id):
    """Детальная страница продукта с комментариями"""
    product = get_object_or_404(Product, id=product_id)
    reviews = Review.objects.filter(product=product)

    return render(request, 'products_app/products_detail.html', {
        'product': product,
        'reviews': reviews
    })


def add_review(request, product_id):
    """Добавление комментария к продукту (без авторизации)"""
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        author_name = request.POST.get('author_name')
        text = request.POST.get('text')
        rating = request.POST.get('rating')

        Review.objects.create(
            product=product,
            author_name=author_name,
            text=text,
            rating=rating
        )

        return redirect('product_detail', product_id=product.id)

    return render(request, 'products_app/add_review.html', {
        'product': product
    })


def blog(request):
    """Блог"""
    return render(request, 'products_app/blog.html', {
        'title': 'Блог'
    })


def about(request):
    """О нас"""
    return render(request, 'products_app/about.html', {
        'title': 'О нас'
    })


def basket(request):
    """Корзина"""
    return render(request, 'products_app/basket.html', {
        'title': 'Корзина'
    })


def hashtags(request):
    """Хештеги"""
    return render(request, 'products_app/hashtags.html', {
        'title': 'Hashtags'
    })
