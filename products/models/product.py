from django.db import models
from colorfield.fields import ColorField
from .brand import Brand
from .category import Category
from .department import Department


class Product(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(
        Brand, blank=True, null=True, on_delete=models.SET_NULL)
    store = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    redirect_url = models.URLField()
    price = models.FloatField(blank=True, null=True,)
    color = ColorField(format='hexa')
    description = models.TextField()
    image1 = models.ImageField(upload_to='product/')
    image2 = models.ImageField(upload_to='product/')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'product'

