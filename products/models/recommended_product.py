from django.db import models
from .product import Product


class RecommendedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    recommended_products = models.ManyToManyField(
        Product, related_name="recommended_products", verbose_name="Recommended Products")
    display_order = models.PositiveIntegerField(
        default=0, blank=False, null=False)

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = "Recommended Products"
        verbose_name_plural = "Recommended Products"
        db_table = 'recommended_products'
        ordering = ['display_order']
