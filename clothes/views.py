from django.shortcuts import render
from .models import ClothesModel, Brand

def clothes_list(request):
    clothes = ClothesModel.objects.all()
    brands = Brand.objects.all()

    
    brand_id = request.GET.get('brand')
    if brand_id:
        clothes = clothes.filter(brands__id=brand_id)

    
    sort = request.GET.get('sort')
    if sort == 'title':
        clothes = clothes.order_by('title')
    elif sort == 'date':
        clothes = clothes.order_by('-created_at')

    return render(request, 'clothes/clothes.html', {
        'clothes': clothes,
        'brands': brands,
    })
