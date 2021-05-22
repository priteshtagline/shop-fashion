from django.db import models
from .product import Product


class SimilarProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    similar_products = models.ManyToManyField(
        Product, related_name="similar_products", verbose_name="Similar Products")

    def __str__(self):
        return self.product.title
    
    class Meta:
        verbose_name = "Similar Products"
        verbose_name_plural = "Similar Products"
        db_table = 'similar_products'

