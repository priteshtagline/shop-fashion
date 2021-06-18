from django.views.generic import ListView
from products.models.campaign import Campaign
from products.models.home_carousel import HomeCarousel


class HomeView(ListView):
    context_object_name = 'campaigns'
    template_name = 'home.html'
    model = Campaign

    def get_queryset(self):
        """Override django generic listview get_queryset method because
           as per requrments to diaplay campaigns product data for first campaigns products.

        Returns:
            [queryset object]: [filter first campaigns queryset object data]
        """
        qs = super(HomeView, self).get_queryset()

        return qs[:1]

    def get_context_data(self, **kwargs):
        """Override django generic listview get_context_data method because
           as per requrments to diaplay campaigns product data with home carousel display.

        Returns:
            [json object]: [campaign product and home carousels object data]
        """
        context = super().get_context_data(**kwargs)

        context['home_carousels'] = HomeCarousel.objects.all()

        return context
