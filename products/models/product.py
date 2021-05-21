from django.db import models
from .department import Department
from .category import Category
from .brand import Brand
from .color import Color


class Product(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(
        Brand, blank=True, null=True, on_delete=models.SET_NULL)
    store = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    redirect_url = models.URLField()
    price = models.FloatField(blank=True, null=True,)
    color = models.ForeignKey(
        Color, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField()
    image1 = models.ImageField(upload_to='product/')
    image2 = models.ImageField(upload_to='product/')
    publish_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'product'
