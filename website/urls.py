from django.urls import path
from django.views.generic.base import TemplateView

from website.views.browse import BrowseListView
from website.views.home import HomeView
from website.views.product import ProductDeatilView

app_name = 'website'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('privacy_policy', TemplateView.as_view(
        template_name='privacy_policy.html'), name='privacy_policy'),
    path('terms_conditions', TemplateView.as_view(
        template_name='terms_conditions.html'), name='terms_conditions'),
    path('product/<slug:slug>/<int:pk>',
         ProductDeatilView.as_view(), name='product'),
    path('browse/<department>/<category>/<subcategory>/',
         BrowseListView.as_view(), name='browse'),
    path('browse/<department>/<category>/',
         BrowseListView.as_view(), name='browse_category'),
    path('browse/<department>/',
         BrowseListView.as_view(), name='browse_department'),
]
