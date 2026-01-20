from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Бренд")

    def __str__(self):
        return self.name

class ClothesModel(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)  # <- временно
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='clothes/', null=True, blank=True)

    def __str__(self):
        return self.name



