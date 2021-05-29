from django import template
from products.models.department import Department

register = template.Library()


@register.inclusion_tag('header.html')
def header():
    return {'departments': Department.objects.all()}
