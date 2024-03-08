from django.contrib import admin
from .models import Commodity, SupplyRequest

class CommodityInline(admin.TabularInline):  # or StackedInline
    model = SupplyRequest.commodities.through
    readonly_fields = ['commodity']
    extra = 1

@admin.register(SupplyRequest)
class SupplyRequestAdmin(admin.ModelAdmin):
    list_display = ['supplier', 'status', 'created', 'updated']
    list_filter = ['supplier', 'status', 'created']
    date_hierarchy = 'created'
    readonly_fields = ['supplier', 'created', 'updated', 'commodities']
    inlines = [CommodityInline]
