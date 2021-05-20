from django.contrib import admin
from .models import Color


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('color_name', 'color_code')

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}

        color = Color.objects.all()
        color_disply = Color.objects.all()

        extra_context.update({
            "colors": color,
            "color_disply": color_disply,
        })
        return super().changelist_view(request, extra_context=extra_context)
