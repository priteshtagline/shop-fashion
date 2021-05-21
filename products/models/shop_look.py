from django.db import models
from .department import Department
from .product_metadata import ProductMetadata


class ShopLook(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    product_metadata = models.ManyToManyField(ProductMetadata)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='shoplook/')

    def __str__(self):
        return self.title
