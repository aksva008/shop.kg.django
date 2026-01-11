from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    korean_name = models.CharField(max_length=100, verbose_name="Корейское название")
    price = models.IntegerField(verbose_name="Цена")
    description = models.TextField(verbose_name="Описание")
    
    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    text = models.TextField(verbose_name="Текст отзыва")
    rating = models.IntegerField(verbose_name="Оценка")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
    
    def __str__(self):
        return f"Отзыв от {self.user} на {self.product}"