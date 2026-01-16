from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from users.forms import CustomUserCreationForm
from users.models import (
    CustomUser,
    HorseTour,
    TourRegistration,
    ClothesModel,
)



def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})



def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('users:all_users')
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})



def all_users(request):
    users = CustomUser.objects.all()
    return render(request, 'users/all_users.html', {'users': users})



@login_required
def register_tour(request):
    user = request.user

    if TourRegistration.objects.filter(user=user).exists():
        messages.warning(request, "Вы уже зарегистрированы на тур!")
        return redirect('users:tour_success')

    tours = HorseTour.objects.all()

    if request.method == 'POST':
        tour_id = request.POST.get('tour')
        selected_tour = HorseTour.objects.get(id=tour_id)

        TourRegistration.objects.create(user=user, tour=selected_tour)
        messages.success(
            request,
            f"Вы успешно зарегистрировались на тур: {selected_tour.title}"
        )
        return redirect('users:tour_success')

    return render(request, 'users/register_tour.html', {'tours': tours})



@login_required
def tour_success(request):
    registration = TourRegistration.objects.filter(
        user=request.user
    ).first()

    return render(request, 'users/tour_success.html', {
        'registration': registration
    })



def clothes_list(request):
    clothes = ClothesModel.objects.all()
    return render(request, 'users/clothes_list.html', {
        'clothes': clothes
    })
