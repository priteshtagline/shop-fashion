from django.db import models
from .product import Product


class VtovProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    vtov_products = models.ManyToManyField(
        Product, related_name="VtovProduct", verbose_name="Vtov Product")

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = "Vtov Products"
        verbose_name_plural = "Vtov Products"
        db_table = 'vtov_products'
