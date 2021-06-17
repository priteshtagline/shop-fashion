from django.views.generic import ListView
from products.models.category import Category
from products.models.merchant import Merchant
from products.models.product import Product
from products.models.sub_category import SubCategory
from django.db.models import Q


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
    paginate_by = 36

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

        filter_fields = ('brand', 'store', 'color')
        query_dict = {}
        keyword_filter = Q()
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

        if 'keyword' in self.request.GET:
            keyword = self.request.GET.get('keyword').strip()
            keyword_filter &= (
                Q(title__iexact=keyword) |
                Q(description__iexact=keyword) |
                Q(merchant__name__iexact=keyword) |
                Q(brand__iexact=keyword) |
                Q(department__name__iexact=keyword) |
                Q(category__name__iexact=keyword) |
                Q(subcategory__name__iexact=keyword)
            )

        if not qs.filter(keyword_filter):
            for value in keyword.split(' '):
                keyword_filter |= (
                    Q(title__iexact=value) |
                    Q(merchant__name__iexact=value) |
                    Q(brand__iexact=value) |
                    Q(category__name__iexact=value) |
                    Q(subcategory__name__iexact=value)
                )
        
        if not qs.filter(keyword_filter):
            for value in keyword.split(' '):
                keyword_filter |= (
                    Q(title__icontains=value) |
                    Q(merchant__name__icontains=value) |
                    Q(brand__icontains=value) |
                    Q(category__name__icontains=value) |
                    Q(subcategory__name__icontains=value)
                )
        return qs.filter(keyword_filter).filter(**query_dict)

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
        product_id_list = []
        keyword_filter = Q()
        if 'keyword' in self.request.GET:
            keyword = self.request.GET.get('keyword').strip()
            keyword_filter &= (
                Q(title__iexact=keyword) |
                Q(description__iexact=keyword) |
                Q(merchant__name__iexact=keyword) |
                Q(brand__iexact=keyword) |
                Q(department__name__iexact=keyword) |
                Q(category__name__iexact=keyword) |
                Q(subcategory__name__iexact=keyword)
            )

        if not Product.objects.filter(keyword_filter):
            for value in keyword.split(' '):
                keyword_filter |= (
                    Q(title__iexact=value) |
                    Q(merchant__name__iexact=value) |
                    Q(brand__iexact=value) |
                    Q(category__name__iexact=value) |
                    Q(subcategory__name__iexact=value)
                )

        if not Product.objects.filter(keyword_filter):
            for value in keyword.split(' '):
                keyword_filter |= (
                    Q(title__icontains=value) |
                    Q(merchant__name__icontains=value) |
                    Q(brand__icontains=value) |
                    Q(category__name__icontains=value) |
                    Q(subcategory__name__icontains=value)
                )
        for product in Product.objects.filter(keyword_filter):
            product_id_list.append(product.id)

        filter_brands_list = Product.objects.values_list(
            'brand', flat=True).filter(id__in=product_id_list).distinct()

        filter_brands = set()
        context['filter_brands'] = [x for x in filter_brands_list
                                    if x.lower() not in filter_brands and not filter_brands.add(x.lower())]

        merchant_id_list = Product.objects.values_list(
            'merchant', flat=True).filter(id__in=product_id_list).distinct()

        context['filter_stors'] = Merchant.objects.filter(
            id__in=merchant_id_list)

        color_list = Product.objects.values_list(
            'color', flat=True).filter(id__in=product_id_list).distinct()

        context['filter_colors'] = list(filter(None, color_list))

        return context
