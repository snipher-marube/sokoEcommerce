from django.contrib import admin
from django.utils.html import format_html
import admin_thumbnails 

from .models import Product, Variation, ReviewRating, ProductGallery

@admin_thumbnails.thumbnail('image')
class ProductGalleryAdmin(admin.TabularInline):
    model = ProductGallery
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.image.url))
    
    list_display = ['thumbnail', 'product_name', 'price', 'stock', 'category', 'created_date', 'modified_date', 'is_available']
    prepopulated_fields = {'slug': ('product_name',)}
    list_display_links = ['thumbnail', 'product_name']

    inlines = [ProductGalleryAdmin]

@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    list_display = ['product', 'variation_category', 'variation_value', 'is_active', 'created_date']
    list_editable = ['is_active']
    list_filter = ['product', 'variation_category', 'variation_value', 'is_active', 'created_date']
    list_display_links = ['product', 'variation_value']

@admin.register(ReviewRating)
class ReviewRatingAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'subject', 'rating', 'status', 'created_at']
    list_filter = ['product', 'user', 'rating', 'status', 'created_at']
    list_editable = ['status']
    list_display_links = ['product', 'user', 'subject']



@admin.register(ProductGallery)
class ProductGalleryAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.image.url))
    
    list_display = ['thumbnail', 'product']
    list_display_links = ['thumbnail', 'product']

    
