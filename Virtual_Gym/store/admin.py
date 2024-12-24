from django.contrib import admin
from .models import Category, ProductList, Cart, Order, OrderProduct

# Register your models here.
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(ProductList)
admin.site.register(Order)
admin.site.register(OrderProduct)