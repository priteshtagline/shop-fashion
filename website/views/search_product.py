from django.views.generic import ListView
from products.models.category import Category
from products.models.merchant import Merchant
from products.models.product import Product
from products.models.sub_category import SubCategory


class SearchListView(ListView):
    """Website browse product list page

    Args:
        ListView ([Django Method]): [Extend by django generic listview]

    Returns:
        [html/text]: [return render html for browse product page]
    """
    model = Product
    template_name = 'search_product.html'
    context_object_name = 'products'
    paginate_by = 100

    def get_queryset(self):
        """Override django generic listview get_queryset method because
           as per requrments to diaplay product data by department, category and sub category so,
           pass keyword arguments to the url and hear filter by given keywords arguments.

           If user more product filter by brand, store and color then pass in query parameter and
           hear filter product by given querystring parameter.

        Returns:
            [queryset object]: [filter product queryset object data]
        """
        qs = super(SearchListView, self).get_queryset()

        filter_fields = ('keyword', 'department', 'category', 'subcategory', 'store', 'color')
        query_dict = {}
        for param in self.request.GET:
            if param in filter_fields and self.request.GET.get(param):
                param_value_list = self.request.GET.get(param).split(',')
                if param == 'brand':
                    query_dict['brand__iregex'] = r'(' + \
                        '|'.join(param_value_list) + ')'
                elif param == 'store':
                    query_dict['merchant__name__in'] = param_value_list
                elif param == 'color':
                    query_dict['color__iregex'] = r'(' + \
                        '|'.join(param_value_list) + ')'
                elif param == 'keyword':
                    query_dict['title__icontains'] = param_value_list[0]

        return qs.filter(**query_dict)

    def get_context_data(self, **kwargs):
        """Override django generic listview get_context_data method because
           as per requrments to diaplay product data by department, category and sub category so,
           pass keyword arguments to the url and hear filter by given keywords arguments.

           Hear context product data with pass dyanamiclly filter data as per select 
           deparametn, category and sub category wise set filter data.

        Returns:
            [json object]: [product and his filter object data]
        """
        context = super().get_context_data(**kwargs)
        print(self.request.GET.get('keyword'))
        return context
