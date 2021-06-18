
from django import template

register = template.Library()


@register.filter(is_safe=True)
def render_model_list(app_list):
    """Reorder django admin panel app and model list

    Args:
        app_list (list): [list of install app and his models]

    Returns:
        [list]: [reordered app and model list]
    """
    app_ordering = {"Authentication and Authorization": 1,
                    "Users": 2, "Products": 3}
    app_list = sorted(app_list, key=lambda x: app_ordering[x['name']])

    model_ordering = {
        "Groups": 1,
        "Users": 2,
        "Email subscribes": 3,
        "Merchants": 3,
        "Departments": 3,
        "Categories": 4,
        "Sub Categories": 5,
        "Products": 7,
        "Recommended Products": 8,
        "Similar Products": 9,
        "Vtov Products": 10,
        "Shop Looks": 11,
        "Campaigns": 12,
        "Home Carousels": 13
    }

    for app in app_list:
        app['models'].sort(key=lambda x: model_ordering[x['name']])

    return app_list
