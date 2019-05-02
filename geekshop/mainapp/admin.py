from django.contrib import admin
from .models import ProductCategory
from .models import Product

admin.site.register(ProductCategory)
admin.site.register(Product)
