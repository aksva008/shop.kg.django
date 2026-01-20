from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager

GENRE_CHOICES = [
    ('action', 'Action'),
    ('comedy', 'Comedy'),
    ('drama', 'Drama'),
    ('horror', 'Horror'),
    ('sci-fi', 'Sci-Fi'),
]

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()

    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)
    

    rating = models.FloatField(default=0.0, verbose_name="Рейтинг")

    image = models.ImageField(upload_to='movies/', null=True, blank=True, verbose_name="Постер")

    def __str__(self):
        return self.title