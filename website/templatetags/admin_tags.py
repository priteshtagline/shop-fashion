from django import template
from products.models.department import Department

register = template.Library()


@register.inclusion_tag('header.html')
def header(user):
    """Custome templet tag for header menu.

    Args:
        user (object): [header html page extend in all page and this page data is pass by templet tag.
                        so, user data pass and display user name in header.]

    Returns:
        [json objects]: [return user information and all departments object]
    """
    return {'user': user, 'departments': Department.objects.all()}
