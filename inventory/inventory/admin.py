from django.contrib import admin

from .models import Category, Item, ItemCategory, EtsyItem

class ItemCategoryInline(admin.TabularInline):
    model = ItemCategory
    extra = 1
    max_num = 1

class EtsyItemInline(admin.StackedInline):
    model = EtsyItem
    extra = 1
    max_num = 1

class CategoryAdmin(admin.ModelAdmin):
    ordering = ['name']

class ItemAdmin(admin.ModelAdmin):
    ordering = ['account__market', 'id']
    list_filter = ('account__market',)
    list_display = ('title', 'id', 'account', 'which_market', 'created_date', 'active')
    readonly_fields = ('created_date',)
    inlines = [
        ItemCategoryInline,
        EtsyItemInline,
    ]

    def get_formsets_with_inlines(self, request, obj=None):
        for inline in self.get_inline_instances(request, obj):
            # hide/show market-specific inlines based on market name
            if obj and obj.extra_fields_by_market() == 'EtsyItemInline':
                yield inline.get_formset(request, obj), inline

admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
