from django.db import models
from colorfield.fields import ColorField


class Color(models.Model):
    name = models.CharField(max_length=255)
    color_code = ColorField(format='hexa')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'color'
