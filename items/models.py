from django.db import models
from django.db.models import Sum

class Order(models.Model):
    @property
    def totalprice(self):
        total_price = Item.objects.aggregate(Sum('price'))
        return total_price.get('price__sum')
class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    order = models.ForeignKey(
        Order, 
        on_delete=models.PROTECT, 
        related_name = 'items_in_order', 
        null=True, 
        blank=True,
        default=1)

    def __str__(self):
        return self.name