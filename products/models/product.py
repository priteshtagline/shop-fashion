from django.db import models
from colorfield.fields import ColorField
from .merchant import Merchant
from .category import Category
from .sub_category import SubCategory
from .department import Department


class Product(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    merchant = models.ForeignKey(
        Merchant, blank=True, null=True, on_delete=models.SET_NULL)
    brand = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    redirect_url = models.URLField()
    price = models.FloatField(blank=True, null=True,)
    color = ColorField(format='hexa')
    description = models.TextField()
    image1 = models.ImageField(upload_to='product/')
    image2 = models.ImageField(upload_to='product/')
    display_order = models.PositiveIntegerField(
        default=0, blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'product'
        ordering = ['display_order']

