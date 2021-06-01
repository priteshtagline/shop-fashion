from django.urls import include, path
from django.views.generic.base import TemplateView

from . import views

app_name = 'website'
urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('privacy_policy', TemplateView.as_view(
        template_name='privacy_policy.html'), name='privacy_policy'),
    path('terms_conditions', TemplateView.as_view(
        template_name='terms_conditions.html'), name='terms_conditions'),
    path('product/<pk>', views.ProductDeatilView.as_view(), name='product'),
    path('browse/<department>/<category>/<subcategory>', views.BrowseLiseView.as_view(), name='browse'),
]
