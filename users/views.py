from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .models import CustomUser


class HomeView(TemplateView):
    template_name = 'users/home.html'


class UserRegisterView(CreateView):
    model = CustomUser
    template_name = 'users/register.html'
    fields = [
        'username',
        'password',
        'phone',
        'age',
        'city',
        'english_level',
        'description',
        'date_of_birth',
        'github',
        'experience',
        'your_photo',
    ]
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'users/login.html'


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')
