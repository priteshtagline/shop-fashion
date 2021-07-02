from django.db import models


class HomeCarousel(models.Model):
    """Home Carousel model

    Args:
        models (method): [django model method]

    Returns:
        [string]: [carousel name]
    """
    title = models.CharField(max_length=255)
    browse_url = models.URLField(max_length=2000)
    image = models.ImageField(upload_to='carousel/')
    text_color = models.CharField(max_length=255, default='black')
    display_order = models.PositiveIntegerField(
        default=0, blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Home Carousels"
        verbose_name_plural = "Home Carousels"
        db_table = 'home_carousel'
        ordering = ['display_order']
