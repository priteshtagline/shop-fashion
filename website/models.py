from django.db import models
from colorfield.fields import ColorField


# Create your models here.


class Color(models.Model):
    color_name = models.CharField(max_length=255, unique=True)
    color_code = ColorField(default='#FF0000', format='hexa')

    def __str__(self):
        return self.color_name
