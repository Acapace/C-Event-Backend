from django.contrib import admin
from .models import Blog, Vendor, Category, Option, Product, Car


# Register your models here.

admin.site.register(Blog)

admin.site.register(Vendor)

admin.site.register(Category)

admin.site.register(Product)

admin.site.register(Option)

admin.site.register(Car)
