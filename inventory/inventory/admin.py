from django.contrib import admin

from .models import Item, ItemSupply
from .models import EtsyItem, SpoonflowerItem


class EtsyItemInline(admin.StackedInline):
    model = EtsyItem
    extra = 1
    max_num = 1

class SpoonflowerItemInline(admin.StackedInline):
    model = SpoonflowerItem
    extra = 1
    max_num = 1

class ItemSupplyInline(admin.TabularInline):
    model = ItemSupply
    extra = 1 
    readonly_fields = ('get_cost', )
    fields = ('item', 'supply', 'quantity', 'get_cost')

    def get_cost(self, obj):
        obj.cost = obj.supply.price * obj.quantity
        obj.save()
        return obj.cost
    get_cost.short_description = 'Cost'

class ItemAdmin(admin.ModelAdmin):
    ordering = ['account__market', 'id']
    list_filter = ('account__market',)
    list_display = ('name', 'id', 'which_market', 'created_date', 'active', 'min_cost',)
    readonly_fields = ('created_date', 'min_cost',)
    inlines = [
        EtsyItemInline,
        SpoonflowerItemInline,
        ItemSupplyInline,
    ]

    def get_formsets_with_inlines(self, request, obj=None):
        for inline in self.get_inline_instances(request, obj):
            # hide/show market-specific inlines based on market name
            if obj and (obj.extra_fields_by_market() == inline.__class__.__name__) or (inline.__class__.__name__ == 'ItemSupplyInline'):
                yield inline.get_formset(request, obj), inline

    def response_add(self, request, new_object):
        obj = self.calculate_inlines(new_object)
        return super(ItemAdmin, self).response_add(request, obj)

    def response_change(self, request, obj):
        obj = self.calculate_inlines(obj)
        return super(ItemAdmin, self).response_change(request, obj)

    def calculate_inlines(self, obj):
        supplies = ItemSupply.objects.filter(item_id=obj.pk)
        obj.min_cost = 0
        for supply in supplies:
            supply_cost = supply.quantity * supply.supply.price
            obj.min_cost = obj.min_cost + supply_cost
        obj.save()
        return obj


admin.site.register(Item, ItemAdmin)
