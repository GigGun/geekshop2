from django.db import models
from django.conf import settings
from mainapp.models import Product
from authapp.models import ShopUser


class BasketSlot(models.Model):
    class Meta:
        verbose_name = 'корзина'
        verbose_name_plural = 'корзины'

    user = models.ForeignKey(ShopUser, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    created = models.DateTimeField(verbose_name='время', auto_now_add=True)

    def __str__(self):
        return self.user.username + ' - ' + self.product.name
