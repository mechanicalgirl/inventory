from django.db import models

from seller_accounts.models import SellerAccount

class Item(models.Model):
    account = models.ForeignKey(SellerAccount)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    quantity = models.IntegerField()
    description = models.TextField()
    tags = models.TextField(help_text="Comma-separated words or phrases")
    date_listed = models.DateTimeField(blank=True, null=True)
    final_url = models.CharField(max_length=200, blank=True, null=True)
    active = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Item: %s" % (self.name)

    def which_market(self):
        return self.account.market

    def extra_fields_by_market(self):
        extra_inline_model = ''
        if self.account.market:
            extra_inline_model = str(self.account.market)+'ItemInline'
        return extra_inline_model

class EtsyItem(models.Model):
    """
    Fields required when the item is listed
    on the market 'Etsy'
    """

    ETSY_WHO_MADE_IT_CHOICES = (
        ('i_did', 'I did'),
        ('collective', 'A member of my shop'),
        ('someone_else', 'Another company/person'),
    )

    PRODUCT = 0
    SUPPLY = 1
    ETSY_WHAT_IS_IT_CHOICES = (
        (PRODUCT, 'A finished product'),
        (SUPPLY, 'A supply or tool to make things'),
    )

    ETSY_WHEN_WAS_IT_MADE_CHOICES = (
        ('made_to_order', 'Made To Order'),
        ('2010_2016', '2010 - 2016'),
        ('2000_2009', '2000s'),
        ('1997_1999', '1997 - 1999'),
        ('before_1997', 'Before 1997'),
        ('1990_1996', '1990 - 1996'),
        ('1980s', '1980s'),
        ('1970s', '1970s'),
        ('1960s', '1960s'),
        ('1950s', '1950s'),
        ('1940s', '1940s'),
        ('1930s', '1930s'),
        ('1920s', '1920s'),
        ('1910s', '1910s'),
        ('1900s', '1900 - 1909'),
    )

    item = models.ForeignKey(Item)
    materials = models.TextField(help_text="Comma-separated words or phrases")
    etsy_who_made_it = models.CharField(
        max_length=12,
        choices=ETSY_WHO_MADE_IT_CHOICES,
        default='i_did',
    )

    etsy_what_is_it = models.IntegerField(
        choices=ETSY_WHAT_IS_IT_CHOICES,
        default=0,
    )
    etsy_when_was_it_made = models.CharField(
        max_length=14,
        choices=ETSY_WHEN_WAS_IT_MADE_CHOICES,
        default='2010_2016'
    )
    category_name = models.CharField(max_length=60, blank=True, null=True, help_text='Your store category')

    """
    These additional Etsy fields will be needed if we're going
    to use this app to post items using the API.

    etsy_category/sub-categories
    etsy type
    etsy_occasion =
    etsy_style =
    """

    class Meta:
        verbose_name = 'Etsy Data'
        verbose_name_plural = 'Etsy Data'
    
    def __str__(self):
        return "Item %s" % (self.item.id)


class SpoonflowerItem(models.Model):
    """
    Fields required when the item is listed
    on the market 'Spoonflower'
    """
    item = models.ForeignKey(Item)
    base_image_name = models.CharField(max_length=200)

    SPOONFLOWER_MATERIAL_CHOICES = (
        ('fabric', 'Fabric'),
        ('wallpaper', 'Wallpaper'),
        ('giftwrap', 'Gift Wrap'),
    )
    material_type = models.CharField(
        max_length=10,
        choices=SPOONFLOWER_MATERIAL_CHOICES,
        default='fabric',
    )

    SPOONFLOWER_REPEAT_CHOICES = (
        ('basic', 'Basic'),
        ('halfdrop', 'Half-Drop'),    # not available for wallpaper
        ('halfbrick', 'Half-Brick'),  # not available for wallpaper
        ('center', 'Center'),         # not available for wallpaper
        ('mirror', 'Mirror'),         # not available for wallpaper
    )
    repeat_type = models.CharField(
        max_length=10,
        choices=SPOONFLOWER_REPEAT_CHOICES,
        default='basic',
        help_text="'Basic' is the only option available for wallpaper."
    )

    design_width = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, help_text="In inches")
    design_height = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, help_text="In inches")
    dpi = models.IntegerField(blank=True, null=True, default=150)
    additional_details = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Spoonflower Data'
        verbose_name_plural = 'Spoonflower Data'

    def __str__(self):
        return "Item %s" % (self.item.id)
