from django.db.models import Count, Q
from django.db.models.functions import Lower
from django.views.generic import ListView
from products.models.department import Department
from products.models.merchant import Merchant
from products.models.product import Product


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

        filter_fields = ('brand', 'store', 'color')
        query_dict = Q()
        for param in self.request.GET:
            if param in filter_fields and self.request.GET.get(param):
                param_value_list = self.request.GET.get(param).split(',')
                for param_value in param_value_list:
                    print(param_value)
                    if param == 'brand':
                        query_dict |= (Q(brand__iexact=param_value))
                    elif param == 'store':
                        query_dict |= Q(merchant__name__iexact=param_value)
                    elif param == 'color':
                        query_dict |= (Q(color__iexact=param_value))
        
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

        filter_object_list = Product.objects.filter(
            keyword_filter).filter(query_dict)
        if filter_object_list:
            return filter_object_list

        department_list = Department.objects.values_list('name', flat=True)
        department_list_lower = [x.lower() for x in department_list]
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

        filter_object_list = Product.objects.filter(
            keyword_filter).filter(query_dict)
        if filter_object_list:
            return filter_object_list

        keyword_filter = Q()
        for value in keyword.split(' '):
            if value.lower() not in department_list_lower:
                keyword_filter &= (
                    Q(description__iregex=fr"[[:<:]]{value}[[:>:]]")
                )

        return Product.objects.filter(keyword_filter).filter(query_dict)


    def get_queryset2(self):
        """Override django generic listview get_queryset method because
           as per requrments to diaplay product data by department, category and sub category so,
           pass keyword arguments to the url and hear filter by given keywords arguments.

           If user more product filter by brand, store and color then pass in query parameter and
           hear filter product by given querystring parameter.

        Returns:
            [queryset object]: [filter product queryset object data]
        """

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

        filter_object_list = Product.objects.filter(keyword_filter).filter()
        if filter_object_list:
            return filter_object_list

        department_list = Department.objects.values_list('name', flat=True)
        department_list_lower = [x.lower() for x in department_list]
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

        filter_object_list = Product.objects.filter(keyword_filter)
        if filter_object_list:
            return filter_object_list

        keyword_filter = Q()
        for value in keyword.split(' '):
            if value.lower() not in department_list_lower:
                keyword_filter &= (
                    Q(description__iregex=fr"[[:<:]]{value}[[:>:]]")
                )

        return Product.objects.filter(keyword_filter)



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
        product_id_list = [product.id for product in self.get_queryset2()]

        context['filter_brands'] = Product.objects.annotate(brand_name=Lower('brand')).values('brand_name').filter(
            id__in=product_id_list).annotate(product_count=Count('brand_name')).order_by('brand_name')

        context['filter_colors'] = Product.objects.annotate(color_name=Lower('color')).values('color_name').filter(
            id__in=product_id_list).annotate(product_count=Count('color_name')).filter(product_count__gt=1).exclude(color_name__exact='').order_by('color_name')

        context['filter_stors'] = Merchant.objects.annotate(total_product=Count(
            'product', filter=Q(product__id__in=product_id_list))).filter(total_product__gt=1).order_by('name')

        return context
