from django.db import models

class Supply(models.Model):
    """
    """
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=15, decimal_places=2, help_text="Cost per unit")
    description = models.TextField(blank=True, null=True)
    maker_name = models.CharField(max_length=50, blank=True, null=True)
    seller_name = models.CharField(max_length=50, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = 'Supply'
        verbose_name_plural = 'Supplies'

    def __str__(self):
        return "%s" % (self.name)
