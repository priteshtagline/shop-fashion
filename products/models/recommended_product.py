from django.db import models
from .product import Product


class RecommendedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    recommended_products = models.ManyToManyField(
        Product, related_name="RecommendedProduct", verbose_name="Recommended Product")

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = "Recommended Products"
        verbose_name_plural = "Recommended Products"
        db_table = 'recommended_products'
