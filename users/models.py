from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, verbose_name="Номер телефона")
    age = models.PositiveIntegerField(null=True, blank=True, verbose_name="Возраст")
    city = models.CharField(max_length=100, verbose_name="Город")
    english_level = models.CharField(max_length=50, verbose_name="Уровень английского")
    description = models.TextField(verbose_name="Описание о себе")
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    github = models.URLField(blank=True, verbose_name="GitHub")
    experience = models.PositiveIntegerField(verbose_name="Опыт работы (лет)")
    your_photo = models.ImageField(upload_to='users/', null=True, blank=True, verbose_name="Фото")

    def __str__(self):
        return self.username


class HorseTour(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} - {self.location}"


class TourRegistration(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    tour = models.ForeignKey(
        HorseTour,
        on_delete=models.CASCADE
    )
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} → {self.tour}"


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ClothesModel(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='clothes/', null=True, blank=True)
    
    def __str__(self):
        return self.name



