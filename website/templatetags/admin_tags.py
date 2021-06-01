from django import template
from products.models.department import Department

register = template.Library()


@register.inclusion_tag('header.html')
def header(user):
    return {'user':user, 'departments': Department.objects.all()}
