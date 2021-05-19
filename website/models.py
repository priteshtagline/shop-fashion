from django.db import models

# Create your models here.
class Color(models.Model):
    color_name = models.CharField(max_length=255, unique=True)
    color_code = models.TextField(max_length=7, unique=True)
    order = models.PositiveSmallIntegerField(default=0, blank=False, null=False)
    
    def __str__(self):
        return self.color_name
    
    class Meta:
        ordering = ('order',)
