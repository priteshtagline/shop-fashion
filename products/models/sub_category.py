from django.db import models

from .department import Department
from .category import Category


class SubCategory(models.Model):
    """SubCategory model

    Args:
        models (method): [django model method]

    Returns:
        [string]: [sub category title]
    """
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    display_order = models.PositiveIntegerField(
        default=0, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sub Category"
        verbose_name_plural = "Sub Categories"
        db_table = 'sub_category'
        unique_together = ('category', 'name')
        ordering = ['display_order']
