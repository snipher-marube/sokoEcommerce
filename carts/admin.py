from django.contrib import admin

from .models import Cart, CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'date_added')
    list_filter = ('cart_id', 'date_added')
    search_fields = ('cart_id', 'date_added')
    ordering = ['date_added']
    list_per_page = 10
    
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'cart', 'quantity', 'is_active')
    list_filter = ('product', 'cart', 'quantity', 'is_active')
    search_fields = ('product', 'cart', 'quantity')
    ordering = ['product']
    list_per_page = 10

