from django.contrib import admin
from .models import Item, Order
# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'totalprice',)
