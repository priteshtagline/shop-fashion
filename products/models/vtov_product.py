from django.db import models
from .product_metadata import ProductMetadata
from users.models import User


class VtovProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductMetadata, on_delete=models.CASCADE)

    def __str__(self):
        return self.user
