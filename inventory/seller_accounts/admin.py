from django.contrib import admin

from .models import Market, SellerAccount

class MarketAdmin(admin.ModelAdmin):
    ordering = ['name']

class SellerAccountAdmin(admin.ModelAdmin):
    ordering = ['market__name', 'username']

admin.site.register(Market, MarketAdmin)
admin.site.register(SellerAccount, SellerAccountAdmin)
