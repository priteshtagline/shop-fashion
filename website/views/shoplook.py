from django.views.generic import ListView, DetailView
from products.models.shop_look import ShopLook


class ShopLookListView(ListView):
    """Website shop look list page

    Args:
        ListView ([Django Method]): [Extend by django generic listview]

    Returns:
        [html/text]: [return render html for shop look page]
    """
    model = ShopLook
    template_name = 'shoplook.html'
    context_object_name = 'shoplooks'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


class ShopLookDetailView(DetailView):
    """Website product detail page

    Args:
        DetailView ([Django Method]): [Extend by django generic]

    Returns:
        [html/text]: [return render html for product detail page]
    """
    model = ShopLook
    template_name = 'shoplook_detail.html'

