from django import template
from products.models.department import Department

register = template.Library()


@register.simple_tag
def show_departments():
    departments = Department.objects.all()
    # return departments
    return {'departments': departments}
