from django.contrib import admin

from .models import Commodity, SupplyRequest

@admin.register(Commodity)
class CommodityAdmin(admin.ModelAdmin):
    list_display = ['name', 'available_amount', 'price']

@admin.register(SupplyRequest)
class SupplyRequestAdmin(admin.ModelAdmin):
    list_display = ['supplier', 'status', 'created', 'updated']
    list_filter = ['supplier', 'commodity', 'created']
    date_hierarchy = 'created'

    
