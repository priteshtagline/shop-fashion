from django import template
from products.models.department import Department

register = template.Library()


@register.inclusion_tag('header.html')
def header(user, request):
    """Custome templet tag for header menu.

    Args:
        user (object): [header html page extend in all page and this page data is pass by templet tag.
                        so, user data pass and display user name in header.]

    Returns:
        [json objects]: [return user information and all departments object]
    """
    keyword_earch = "" if not 'keyword' in request.GET else request.GET['keyword']
    return {'user': user, 'search_keyword': keyword_earch, 'departments': Department.objects.all()}


@register.filter_function
def order_by(queryset, args):
    args = [x.strip() for x in args.split(',')]
    return queryset.order_by(*args)
