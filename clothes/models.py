from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class ClothesModel(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='clothes/', null=True, blank=True)
    brands = models.ManyToManyField(Brand, related_name='clothes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
