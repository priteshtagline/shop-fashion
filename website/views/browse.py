from django.db.models import Count, Q
from django.db.models.functions import Lower
from django.views.generic import ListView
from products.models.category import Category
from products.models.department import Department
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
    browse_filter_data = {}
    department_id = category_id = subcategory__id = ''

    def get_queryset(self):
        """Override django generic listview get_queryset method because
           as per requrments to diaplay product data by department, category and sub category so,
           pass keyword arguments to the url and hear filter by given keywords arguments.

           If user more product filter by brand, store and color then pass in query parameter and
           hear filter product by given querystring parameter.

        Returns:
            [queryset object]: [filter product queryset object data]
        """
        self.department_id = Department.objects.filter(
            name__iexact=self.kwargs['department']).first().id

        kwargs_filters = {
            'department__id': self.department_id
        }

        if 'category' in self.kwargs:
            self.category_id = Category.objects.filter(
                name__iexact=self.kwargs['category']).first().id
            kwargs_filters['category__id'] = self.category_id

        if 'subcategory' in self.kwargs:
            self.subcategory_id = SubCategory.objects.filter(
                name__iexact=self.kwargs['subcategory']).first().id
            kwargs_filters['subcategory__id'] = self.subcategory_id

        self.browse_filter_data = Product.objects.filter(**kwargs_filters)

        filter_fields = ('brand', 'store', 'color')
        query_dict = Q()
        for param in self.request.GET:
            if param in filter_fields and self.request.GET.get(param):
                param_value_list = self.request.GET.get(param).split(',')
                for param_value in param_value_list:
                    if param == 'brand':
                        query_dict |= (Q(brand__iexact=param_value))
                    elif param == 'store':
                        query_dict |= Q(merchant__name__iexact=param_value)
                    elif param == 'color':
                        query_dict |= (Q(color__iexact=param_value))
        if query_dict:
            return self.browse_filter_data.filter(query_dict)
        else:
            return self.browse_filter_data

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
            'department__id': self.department_id
        }

        if 'category' in self.kwargs:
            kwargs_filters['category__id'] = self.category_id
        else:
            context['categories_list'] = Category.objects.values('name').annotate(
                total_product=Count('product', distinct=True)).filter(**kwargs_filters).order_by('name')

        if not 'subcategory' in self.kwargs:
            context['subcategories_list'] = SubCategory.objects.values('name').annotate(total_product=Count(
                'product', distinct=True)).filter(**kwargs_filters).order_by('name')

        context['filter_brands'] = self.browse_filter_data.annotate(brand_name=Lower(
            'brand')).values('brand_name').annotate(product_count=Count('brand_name')).order_by('brand_name')

        context['filter_colors'] = self.browse_filter_data.values(
            'color').annotate(color_name=Lower('color')).annotate(product_count=Count('color_name')).filter(product_count__gt=1).exclude(color_name__exact='').order_by('color_name')

        context['filter_stors'] = self.browse_filter_data.annotate(merchant_name=Lower(
            'merchant__name')).values('merchant__name').annotate(product_count=Count('merchant__name')).order_by('merchant__name')

        return context
