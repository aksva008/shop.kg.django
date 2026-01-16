from django import forms
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    captcha = CaptchaField()

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'phone', 'age', 'city',
                  'english_level', 'email', 'description', 'date_of_birth',
                  'github', 'experience', 'your_photo'] 

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = CaptchaField()
