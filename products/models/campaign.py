from django.db import models
from .product import Product


class Campaign(models.Model):
    title = models.CharField(max_length=255)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'campaign'
