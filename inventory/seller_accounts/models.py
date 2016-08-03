from django.db import models

class SellerAccount(models.Model):
    MARKET_NAME_CHOICES = (
        ('Etsy', 'Etsy'),
        ('Artfire', 'ArtFire'),
        ('Handmadeatamazon', 'Handmade at Amazon'),
        ('Spoonflower', 'Spoonflower'),
    )
    market = models.CharField(
        max_length=200,
        choices=MARKET_NAME_CHOICES,
        default='Etsy',
    )
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50, blank=True, null=True)  # optional
    shop_name = models.CharField(max_length=50, blank=True, null=True)
    shop_url = models.CharField(max_length=200)
    active = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return "%s : %s" % (self.market, self.username)

