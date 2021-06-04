from django.views.generic import DetailView
from products.models.product import Product
from products.models.similar_product import SimilarProduct


class ProductDeatilView(DetailView):
    model = Product
    template_name = 'product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # pd = Product.objects.get(id=504).prefetch_related('similar_products')
        # smp = SimilarProduct.objects.filter(product=504)
        # for sm in smp:
        #     print(sm.prefetch_related('similar_products'))

        # context['similar_products'] = smp
        pd = SimilarProduct.objects.prefetch_related('product__similar_products')
        print(pd)
        return context
