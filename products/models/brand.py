from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=255)
    display_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'brand'
        ordering = ['display_order']
