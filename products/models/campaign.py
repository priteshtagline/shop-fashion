from django.db import models
from .product import Product


class Campaign(models.Model):
    title = models.CharField(max_length=255)
    products = models.ManyToManyField(Product)
    display_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'campaign'
        ordering = ['display_order']
