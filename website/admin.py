from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from django.utils.html import format_html
from .models import Color
from .forms import ColorForm


class ColorAdmin(SortableAdminMixin, admin.ModelAdmin):
    """
    ColorAdmin override with SortableAdminMixin and admin.ModelAdmin.
    SortableAdminMixin is define display of color order in admin and user side.
    Display Django admin color name, and color code.
    """
    form = ColorForm
    list_display = ('color_name', 'color_code_display',)

    def color_code_display(self, obj):
        return format_html('<b style="color:{0};">{0}</b>'.format(obj.color_code))

    color_code_display.short_description = 'Color Code'

admin.site.register(Color, ColorAdmin)
