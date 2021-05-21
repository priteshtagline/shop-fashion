from django.db import models
from .product_metadata import ProductMetadata


class Campaign(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="campaign/")
    button_text = models.CharField(max_length=255)
    product_metadata = models.ManyToManyField(ProductMetadata)

    def __str__(self):
        return self.title
