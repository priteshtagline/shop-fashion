from django.db import models
from .merchant import Merchant
from .category import Category
from .sub_category import SubCategory
from .department import Department


class Product(models.Model):
    """Product model

    Args:
        models (method): [django model method]

    Returns:
        [string]: [product title]
    """
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    label = models.CharField(max_length=255, null=True, blank=True)
    merchant = models.ForeignKey(
        Merchant, blank=True, null=True, on_delete=models.SET_NULL)
    brand = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    redirect_url = models.URLField(max_length=2000)
    price = models.FloatField(blank=True, null=True,)
    color = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    image1 = models.ImageField(upload_to='product/')
    image2 = models.ImageField(upload_to='product/', null=True, blank=True)
    display_order = models.PositiveIntegerField(
        default=0, blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'product'
        ordering = ['display_order']
