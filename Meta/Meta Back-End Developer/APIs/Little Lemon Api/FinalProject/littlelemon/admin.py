from django.contrib import admin
from .models import Category, Order, OrderItem, MenuItem, Cart

# Register your models here
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(MenuItem)
admin.site.register(Cart)