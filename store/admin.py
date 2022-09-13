from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image', 'is_hidden', 'is_trending', 'created_at']
    list_editable = ('is_hidden', 'is_trending')
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image', 'category', 'is_hidden', 'is_trending', 'created_at']
    list_editable = ('is_hidden', 'is_trending')
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}