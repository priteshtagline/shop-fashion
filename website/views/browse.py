from django.views.generic import ListView
from products.models.category import Category
from products.models.merchant import Merchant
from products.models.product import Product
from products.models.sub_category import SubCategory


class BrowseListView(ListView):
    """Website browse product list page

    Args:
        ListView ([Django Method]): [Extend by django generic listview]

    Returns:
        [html/text]: [return render html for browse product page]
    """
    model = Product
    template_name = 'browse.html'
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
        qs = super(BrowseListView, self).get_queryset()

        kwargs_filters = {
            'department__name__iexact': self.kwargs['department'],
        }

        if 'category' in self.kwargs:
            kwargs_filters['category__name__iexact'] = self.kwargs['category']
        
        if 'subcategory' in self.kwargs:
            kwargs_filters['subcategory__name__iexact'] = self.kwargs['subcategory']
       

        filter_fields = ('brand', 'store', 'color')
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

        return qs.filter(**kwargs_filters, **query_dict)

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
        kwargs_filters = {
            'department__name__iexact': self.kwargs['department'],
        }

        if 'category' in self.kwargs:
            kwargs_filters['category__name__iexact'] = self.kwargs['category']
        else:
            context['categories_list'] = Category.objects.values_list(
                'name', flat=True).filter(**kwargs_filters)

        if 'subcategory' in self.kwargs:
            kwargs_filters['subcategory__name__iexact'] = self.kwargs['subcategory']
        else:
            context['subcategories_list'] = SubCategory.objects.values_list(
                'name', flat=True).filter(**kwargs_filters)

        filter_brands_list = Product.objects.values_list(
            'brand', flat=True).filter(**kwargs_filters).distinct()

        filter_brands = set()
        context['filter_brands'] = [x for x in filter_brands_list
                                    if x.lower() not in filter_brands and not filter_brands.add(x.lower())]

        merchant_id_list = Product.objects.values_list(
            'merchant', flat=True).filter(**kwargs_filters).distinct()

        context['filter_stors'] = Merchant.objects.filter(
            id__in=merchant_id_list)

        color_list = Product.objects.values_list(
            'color', flat=True).filter(**kwargs_filters).distinct()

        context['filter_colors'] = list(filter(None, color_list))

        return context
