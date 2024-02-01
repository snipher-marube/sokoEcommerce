from django.contrib import admin
from django.http.request import HttpRequest

from .models import ProductRequest

@admin.register(ProductRequest)
class ProductRequestAdmin(admin.ModelAdmin):
    list_display = ( 'vendor', 'product_name', 'product_price', 'product_quantity', 'status', 'date_created')
    list_filter = ('status', 'date_created')
    search_fields = ('product_name', 'vendor__username')
    list_per_page = 20
    actions = ('approve', 'reject')
    
    def approve(self, request, queryset):
        queryset.update(status='Approved')
        
    def reject(self, request, queryset):
        queryset.update(status='Rejected')
    
    