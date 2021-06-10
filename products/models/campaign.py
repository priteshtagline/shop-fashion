from django.db import models
from .product import Product


class Campaign(models.Model):
    """Campaign model

    Args:
        models (method): [django model method]

    Returns:
        [string]: [campaign title]
    """
    title = models.CharField(max_length=255)
    products = models.ManyToManyField(Product)
    display_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'campaign'
        ordering = ['display_order']
