from django.db import models
from .department import Department
from .product import Product


class ShopLook(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='shoplook/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Shop Looks"
        verbose_name_plural = "Shop Looks"
        db_table = 'shop_looks'
