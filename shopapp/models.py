from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    """
    Модель для представления Товара, который можно продавать в интернет-магазине
    Заказы: :model:'shopapp.Order'
    """
    
    class Meta:
        ordering = ['name', 'price']
        # db_table = 'new_products'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    name = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    discount = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)
    archived = models.BooleanField(default=False)
    author = models.ForeignKey(to=User, on_delete=models.SET_NULL, blank=True, null=True, related_name='author')

    def __str__(self):
        return f'Товар {self.name},  pk={self.pk}'
    
    @property
    def description_short(self):
        if len(self.description) < 50:
            return self.description
        return self.description[:50] + '...'


class Order(models.Model):
    adress = models.TextField(null=True, blank=True)
    promo = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, related_name='orders')


