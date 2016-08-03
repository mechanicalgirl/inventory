from django.contrib import admin

from .models import Item
from .models import EtsyItem, SpoonflowerItem

class EtsyItemInline(admin.StackedInline):
    model = EtsyItem
    extra = 1
    max_num = 1

class SpoonflowerItemInline(admin.StackedInline):
    model = SpoonflowerItem
    extra = 1
    max_num = 1

class ItemAdmin(admin.ModelAdmin):
    ordering = ['account__market', 'id']
    list_filter = ('account__market',)
    list_display = ('name', 'id', 'which_market', 'created_date', 'active')
    readonly_fields = ('created_date',)
    inlines = [
        EtsyItemInline,
        SpoonflowerItemInline,
    ]

    def get_formsets_with_inlines(self, request, obj=None):
        for inline in self.get_inline_instances(request, obj):
            # hide/show market-specific inlines based on market name
            if obj and obj.extra_fields_by_market() == inline.__class__.__name__:
                yield inline.get_formset(request, obj), inline

admin.site.register(Item, ItemAdmin)
