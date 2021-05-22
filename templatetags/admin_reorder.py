from django.contrib.admin import site
from django.apps import apps
from django import template
from django.utils.text import capfirst
from django.contrib.auth.models import User


register = template.Library()


@register.filter(is_safe=True)
def render_model_list(app_list):
    app_ordering = {"Authentication and Authorization": 1,
                    "Users": 2, "Products": 3}
    app_list = sorted(app_list, key=lambda x: app_ordering[x['name']])

    model_ordering = {
        "Groups": 1,
        "Users": 2,
        "Departments": 3,
        "Categories": 4,
        "Brands": 5,
        "Products": 6,
        "Recommended Products": 7,
        "Similar Products": 8,
        "Vtov Products": 9,
        "Shop Looks": 10,
        "Campaigns": 11,
    }

    for app in app_list:
        app['models'].sort(key=lambda x: model_ordering[x['name']])

    return app_list
