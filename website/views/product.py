from django.views.generic import DetailView
from products.models.product import Product
from products.models.similar_product import SimilarProduct
from products.models.recommended_product import RecommendedProduct
from products.models.vtov_product import VtovProduct


class ProductDeatilView(DetailView):
    """Website product detail page

    Args:
        DetailView ([Django Method]): [Extend by django generic]

    Returns:
        [html/text]: [return render html for product detail page]
    """
    model = Product
    template_name = 'product.html'

    def get_context_data(self, **kwargs):
        """Override django generic detailview get_context_data method because
           as per requrments to diaplay product detail with similar, recommended
           and vtov product list carsole.

        Returns:
            [json object]: [product detail with similar, recommended and vtov product list]
        """
        context = super().get_context_data(**kwargs)
        product_id = context['product'].id

        similer_product_id_list = SimilarProduct.objects.values_list('similar_products', flat=True).filter(
            product__id=product_id)
        context['similer_products'] = Product.objects.filter(
            id__in=similer_product_id_list)

        recommended_product_id_list = RecommendedProduct.objects.values_list('recommended_products', flat=True).filter(
            product__id=product_id)
        context['recommended_products'] = Product.objects.filter(
            id__in=recommended_product_id_list)

        vtov_product_id_list = VtovProduct.objects.values_list('vtov_products', flat=True).filter(
            product__id=product_id)
        context['vtov_products'] = Product.objects.filter(
            id__in=vtov_product_id_list)

        return context
