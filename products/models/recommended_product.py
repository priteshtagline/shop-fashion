from django.db import models
from .product_metadata import ProductMetadata


class RecommendedProduct(models.Model):
    product = models.ForeignKey(ProductMetadata, on_delete=models.CASCADE)
    recommended_product = models.ManyToManyField(
        ProductMetadata, related_name="RecommendedProduct", verbose_name="Recommended Product")

    def __str__(self):
        return self.product
