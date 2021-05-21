from django.db import models
from .department import Department
from .category import Category
from .store import Store
from .brand import Brand


class ProductMetadata(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    brand = models.ForeignKey(
        Brand, blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    description = models.TextField()
    redirect_url = models.URLField()
    price = models.FloatField(blank=True, null=True,)
    thumbnail_image = models.ImageField(upload_to='product_thumbnail')
    main_image = models.ImageField(upload_to='product_mainimage')
    publish_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
