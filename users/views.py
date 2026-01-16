from django.shortcuts import render, redirect
from django.contrib.auth import login, logout 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from users.forms import CustomUserCreationForm, LoginForm
from users.models import CustomUser

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
        form = AuthenticationForm(request.POST)
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
