from django.db import models
from .department import Department
from .product import Product


class ShopLook(models.Model):
    """ShopLook model

    Args:
        models (method): [django model method]

    Returns:
        [string]: [shoplook title]
    """
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='shoplook/')
    display_order = models.PositiveIntegerField(
        default=0, blank=False, null=False)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Shop Looks"
        verbose_name_plural = "Shop Looks"
        db_table = 'shop_looks'
        ordering = ['display_order']
