from django.db import models
from .product import Product


class VtovProduct(models.Model):
    """VtovProduct model

    Args:
        models (method): [django model method]

    Returns:
        [string]: [product title]
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    vtov_products = models.ManyToManyField(
        Product, related_name="vtov_products", verbose_name="Vtov Products")
    display_order = models.PositiveIntegerField(
        default=0, blank=False, null=False)

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = "Vtov Products"
        verbose_name_plural = "Vtov Products"
        db_table = 'vtov_products'
        ordering = ['display_order']
