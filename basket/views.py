from django.shortcuts import render, get_object_or_404, redirect
from .models import BasketItem, Order, OrderItem
from .forms import BasketForm, OrderForm
from products_app.models import Product


def basket_list(request):
    items = BasketItem.objects.all()
    return render(request, 'basket/basket_list.html', {'items': items})


def add_to_basket(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = BasketForm(request.POST)
        if form.is_valid():
            basket_item = form.save(commit=False)
            basket_item.product = product  
            basket_item.save()
            return redirect('basket_list')
    else:
        form = BasketForm(initial={'quantity': 1})

    return render(request, 'basket/add_to_basket.html', {'form': form, 'product': product})


def edit_basket_item(request, item_id):
    item = get_object_or_404(BasketItem, id=item_id)

    if request.method == 'POST':
        form = BasketForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('basket_list')
    else:
        form = BasketForm(instance=item)

    return render(request, 'basket/edit_basket_item.html', {'form': form, 'item': item})


def remove_from_basket(request, item_id):
    item = get_object_or_404(BasketItem, id=item_id)
    item.delete()
    return redirect('basket_list')


def place_order(request):
    items = BasketItem.objects.all()
    if not items.exists():
        return redirect('product_list') 

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity
                )

            items.delete()

            return render(request, 'basket/order_success.html', {'order': order})
    else:
        form = OrderForm()

    return render(request, 'basket/place_order.html', {'form': form, 'items': items})
