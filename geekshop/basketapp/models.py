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

    @property
    def product_cost(self):
        """return cost of all products"""
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        """return total quantity for user"""
        _items = BasketSlot.objects.filter(user=self.user)
        _totalquantity = sum(list(map(lambda x: x.quantity, _items)))
        return _totalquantity

    @property
    def total_cost(self):
        """return total cost for user"""
        _items = BasketSlot.objects.filter(user=self.user)
        _totalcost = sum(list(map(lambda x: x.product_cost, _items)))
        return _totalcost
