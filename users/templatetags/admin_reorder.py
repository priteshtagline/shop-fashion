from django import template


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
        "Sub Categories": 5,
        "Brands": 6,
        "Products": 7,
        "Recommended Products": 8,
        "Similar Products": 9,
        "Vtov Products": 10,
        "Shop Looks": 11,
        "Campaigns": 12,
    }

    for app in app_list:
        app['models'].sort(key=lambda x: model_ordering[x['name']])

    return app_list
