from django.contrib import admin

from .models import SellerAccount

class SellerAccountAdmin(admin.ModelAdmin):
    list_display = ['username', 'market']
    ordering = ['market', 'username']

admin.site.register(SellerAccount, SellerAccountAdmin)
