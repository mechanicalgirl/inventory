from django.db import models

class Market(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return "%s" % (self.name)

class SellerAccount(models.Model):
    market = models.ForeignKey(Market)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50, blank=True, null=True)  # optional
    shop_name = models.CharField(max_length=50, blank=True, null=True)
    shop_url = models.CharField(max_length=200)
    active = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return "SellerAccount: %s - %s" % (self.market.name, self.username)

