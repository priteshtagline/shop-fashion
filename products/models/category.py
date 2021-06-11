from django.db import models

from .department import Department


class Category(models.Model):
    """Category model

    Args:
        models (method): [django model method]

    Returns:
        [string]: [category name]
    """
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    display_order = models.PositiveIntegerField(
        default=0, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        db_table = 'category'
        unique_together = ('department', 'name')
        ordering = ['display_order']

    
