from django.db import models
from django.conf import settings  
from clothes.models import ClothesModel

class BasketItem(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    item = models.ForeignKey(
        ClothesModel,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        item_name = self.item.name if self.item else "No item"
        username = self.user.username if self.user else "Anonymous"
        return f"{item_name} x {self.quantity} ({username})"

    def total_price(self):
        return self.item.price * self.quantity if self.item else 0

