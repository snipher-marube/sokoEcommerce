from django.contrib import admin

from .models import Payment, Order, OrderProduct

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'payment_id', 'payment_method', 'amount_paid', 'status', 'created_at']
    list_filter = ['status', 'created_at']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'full_name', 'phone', 'email', 'city', 'order_total', 'tax', 'status', 'is_ordered', 'created_at']
    list_filter = ['status', 'is_ordered', 'created_at']
    list_per_page = 20
    search_fields = ['order_number', 'first_name', 'last_name', 'phone', 'email']
    
    def full_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'
    
    full_name.short_description = 'Name'

@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'order', 'payment', 'product', 'variations', 'quantity', 'product_price', 'ordered']
    list_filter = ['ordered']
    list_per_page = 20
    search_fields = ['order__order_number', 'product__product_name']

    
