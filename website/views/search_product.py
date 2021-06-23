from django.views.generic import ListView
from products.models.merchant import Merchant
from products.models.product import Product
from products.models.department import Department
from collections import Counter
from django.db.models import Count, Q


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
    paginate_by = 80

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
        department_list = Department.objects.values_list('name', flat=True)
        department_list_lower = [x.lower() for x in department_list]

        if Product.objects.filter(keyword_filter):
            return qs.filter(keyword_filter).filter(**query_dict)
        else:
            keyword_filter = Q()
            for value in keyword.split(' '):
                if value.lower() not in department_list_lower:
                    keyword_filter &= (
                        Q(title__iregex=fr"[[:<:]]{value}[[:>:]]") |
                        Q(merchant__name__iexact=value) |
                        Q(brand__iexact=value) |
                        Q(category__name__iexact=value) |
                        Q(subcategory__name__iexact=value)
                    )

        if Product.objects.filter(keyword_filter):
            return qs.filter(keyword_filter).filter(**query_dict)
        else:
            keyword_filter = Q()
            for value in keyword.split(' '):
                if value.lower() not in department_list_lower:
                    keyword_filter &= (
                        Q(description__iregex=fr"[[:<:]]{value}[[:>:]]")
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
        
        for product in self.get_queryset():
            product_id_list.append(product.id)

        filter_brands_list = Product.objects.values_list(
            'brand', flat=True).filter(id__in=product_id_list).order_by('brand')
        context['filter_brands'] = dict(
            Counter(x.lower() for x in filter_brands_list))

        filter_color_list = Product.objects.values_list(
            'color', flat=True).filter(id__in=product_id_list).order_by('color')
        context['filter_colors'] = dict(
            Counter(x.lower() for x in list(filter(None, filter_color_list))))

        context['filter_stors'] = Merchant.objects.annotate(total_product=Count(
            'product', filter=Q(product__id__in=product_id_list))).filter(total_product__gt=1).order_by('name')

        return context
