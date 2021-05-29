from django.views.generic import ListView, DetailView
from products.models.campaign import Campaign
from products.models.product import Product

class IndexView(ListView):
    context_object_name = 'campaigns'
    template_name = 'home.html'
    queryset = Campaign.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['campaigns'] = Campaign.objects.all()
        return context
    

class ProductDeatilView(DetailView):
    model = Product
    template_name = 'product.html'
