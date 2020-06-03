from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    """docstring for ProductAdmin."""
    list_display = ['__str__', 'slug']
    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
