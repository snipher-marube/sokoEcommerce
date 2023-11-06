from django.contrib import admin
from django.utils.html import format_html

from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # category thumbnail
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.cat_image.url))
    
    list_display = ('category_name', 'thumbnail', 'slug', 'description')
    prepopulated_fields = {'slug': ('category_name',)}
