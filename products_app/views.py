from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

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

