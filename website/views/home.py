from django.views.generic import ListView
from products.models.campaign import Campaign


class HomeView(ListView):
    context_object_name = 'campaigns'
    template_name = 'home.html'
    queryset = Campaign.objects.all()

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['campaigns'] = Campaign.objects.all()
        return context
