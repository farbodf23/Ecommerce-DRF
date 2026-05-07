from django.contrib import admin
from .models import Category, Product
# Register your models here.


@admin.register(Category)
class TodoAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock',
                    'is_active', 'category', 'created_at']
    list_filter = ['is_active', 'category', 'created_at']  # sidebar filters
    search_fields = ['name', 'description']                 # search bar
    list_editable = ['price', 'stock', 'is_active']        # inline editing
    ordering = ['-created_at']
