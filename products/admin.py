from django.contrib import admin
from .models import (Category,
                     Product,
                     Image)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    fields = ('name', 'slug', 'parent', 'is_active')
    prepopulated_fields = {'slug': ('name', )}


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_filter = ('category', 'is_active', 'timestamp')

    fields = ['main_image',
              'video',
              'owner',
              'name',
              'category',
              'price',
              'overview',
              'discount',
              'is_active',
              'timestamp']
    list_display = ('name',
                    'category',
                    'price',
                    'is_active')
    inlines = [ImageInline, ]
