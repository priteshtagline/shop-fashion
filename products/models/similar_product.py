from django.db import models
from .product_metadata import ProductMetadata


class SimilarProduct(models.Model):
    product = models.ForeignKey(ProductMetadata, on_delete=models.CASCADE)
    similar_product = models.ManyToManyField(
        ProductMetadata, related_name="SimilarProduct", verbose_name="Similar Product")

    def __str__(self):
        return self.product
