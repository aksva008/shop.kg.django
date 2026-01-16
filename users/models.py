from django.contrib.auth.models import AbstractUser
from django.db import models 

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
