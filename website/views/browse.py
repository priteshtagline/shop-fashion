from django.views.generic import ListView
from products.models.merchant import Merchant
from products.models.product import Product


class BrowseListView(ListView):
    model = Product
    template_name = 'browse.html'
    context_object_name = 'products'
    # paginate_by = 40

    def get_queryset(self):
        qs = super(BrowseListView, self).get_queryset()
        kwargs_filters = {
            'department__name__iexact': self.kwargs['department'],
            'category__name__iexact': self.kwargs['category'],
        }
        if 'subcategory' in self.kwargs:
            kwargs_filters['subcategory__name__iexact'] = self.kwargs['subcategory']

        filter_fields = ('brand', 'store', 'color')
        query_dict = {}
        for param in self.request.GET:
            if param in filter_fields and self.request.GET.get(param):
                param_value_list = self.request.GET.get(param).split(',')
                if param == 'brand':
                    query_dict['brand__iregex'] = r'(' + '|'.join(param_value_list) + ')'
                elif param == 'store':
                    query_dict['merchant__name__in'] = param_value_list
                elif param == 'color':
                    query_dict['color__iregex'] = r'(' + '|'.join(param_value_list) + ')'

        return qs.filter(**kwargs_filters, **query_dict)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        kwargs_filters = {
            'department__name__iexact': self.kwargs['department'],
            'category__name__iexact': self.kwargs['category'],
        }
        if 'subcategory' in self.kwargs:
            kwargs_filters['subcategory__name__iexact'] = self.kwargs['subcategory']

        context['filter_brands'] = Product.objects.values_list(
            'brand', flat=True).filter(**kwargs_filters).distinct()

        merchant_id_list = Product.objects.values_list(
            'merchant', flat=True).filter(**kwargs_filters).distinct()

        context['filter_stors'] = Merchant.objects.filter(
            id__in=merchant_id_list)
        context['filter_colors'] = Product.objects.values_list(
            'color', flat=True).filter(**kwargs_filters).distinct()

        return context
