from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.PositiveIntegerField(verbose_name="Цена")
    image = models.ImageField(upload_to='products/', blank=True, null=True)


    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


    def __str__(self):
        return self.title
    