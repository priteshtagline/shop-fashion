from django.db import models


class Merchant(models.Model):
    """Merchant model

    Args:
        models (method): [django model method]

    Returns:
        [string]: [merchant name]
    """
    name = models.CharField(max_length=255)
    website = models.URLField()
    display_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'merchant'
        ordering = ['display_order']
