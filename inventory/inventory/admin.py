from django.contrib import admin

from .models import Category, Item, ItemCategory

class ItemCategoryInline(admin.TabularInline):
    model = ItemCategory
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    ordering = ['name']

class ItemAdmin(admin.ModelAdmin):
    ordering = ['account__shop_name', 'title']
    list_filter = ('account__shop_name',)
    list_display = ('title', 'id', 'created_date', 'active')
    inlines = [
        ItemCategoryInline,
    ]

admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
