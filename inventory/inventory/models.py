from django.db import models

from seller_accounts.models import SellerAccount

class Category(models.Model):
    """
    Seller's shop categories (as opposed to market's item type categories)
    """
    name = models.CharField(max_length=60)
    active = models.BooleanField(default=True)

    def __str__(self):
        return u"%s" % self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "categories"

class Item(models.Model):
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

    account = models.ForeignKey(SellerAccount)
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    quantity = models.IntegerField()
    description = models.TextField()
    dimensions = models.TextField()
    tags = models.TextField(help_text="Comma-separated words")
    materials = models.TextField(help_text="Comma-separated words")
    final_url = models.CharField(max_length=200, blank=True, null=True)
    active = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now = True)

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

    """
    All the Etsy fields will be needed if we're going
    to use this app to post items using the API.

    etsy_category/sub-categories
    etsy type
    etsy_occasion =
    etsy_style =
    """

    def __str__(self):
        return "Item: %s" % (self.title)

class ItemCategory(models.Model):
    item = models.ForeignKey(Item)
    category = models.ForeignKey(Category)

    class Meta:
        verbose_name_plural = "item categories"
