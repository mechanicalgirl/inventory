from django.contrib import admin

from .models import Supply
from inventory.models import ItemSupply


class ItemSupplyInline(admin.TabularInline):
    model = ItemSupply
    extra = 1

class SupplyAdmin(admin.ModelAdmin):
    ordering = ['name', 'maker_name', 'seller_name']
    list_filter = ('maker_name', 'seller_name')
    list_display = ('name', 'id', 'price', 'maker_name', 'seller_name')
    inlines = [
        ItemSupplyInline,
    ]

admin.site.register(Supply, SupplyAdmin)
