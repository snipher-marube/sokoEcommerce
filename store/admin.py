from django.contrib import admin
from django.utils.html import format_html

from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.image.url))
    
    list_display = ['thumbnail', 'product_name', 'price', 'stock', 'category', 'created_date', 'modified_date', 'is_available']
    prepopulated_fields = {'slug': ('product_name',)}
    list_display_links = ['thumbnail', 'product_name']
