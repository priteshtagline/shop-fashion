from django.db.models import Count, Q
from django.db.models.functions import Lower
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

        kwargs_filters = {
            'department__name__iexact': self.kwargs['department'],
        }

        if 'category' in self.kwargs:
            kwargs_filters['category__name__iexact'] = self.kwargs['category']

        if 'subcategory' in self.kwargs:
            kwargs_filters['subcategory__name__iexact'] = self.kwargs['subcategory']

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
                        
        return Product.objects.filter(**kwargs_filters).filter(query_dict)

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
            context['categories_list'] = Category.objects.annotate(
                total_product=Count('product', distinct=True)).filter(**kwargs_filters).order_by('name')

        if 'subcategory' in self.kwargs:
            kwargs_filters['subcategory__name__iexact'] = self.kwargs['subcategory']
        else:
            context['subcategories_list'] = SubCategory.objects.annotate(total_product=Count(
                'product', distinct=True)).filter(**kwargs_filters).order_by('name')

        product_ids = [
            product.id for product in Product.objects.filter(**kwargs_filters)]

        context['filter_brands'] = Product.objects.annotate(brand_name=Lower('brand')).values('brand_name').filter(
            id__in=product_ids).annotate(product_count=Count('brand_name')).order_by('brand_name')

        context['filter_colors'] = Product.objects.annotate(color_name=Lower('color')).values('color_name').filter(
            id__in=product_ids).annotate(product_count=Count('color_name')).filter(product_count__gt=1).exclude(color_name__exact='').order_by('color_name')

        context['filter_stors'] = Merchant.objects.annotate(total_product=Count(
            'product', filter=Q(product__id__in=product_ids))).filter(total_product__gt=1).order_by('name')

        return context
